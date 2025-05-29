#include "seamcarving.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// #include "c_img.c" // remove this line before putting into gradescope

int compare (const void *p_a, const void *p_b) {
    double *p_a_i = (double *)p_a;
    double *p_b_i = (double *)p_b;
    return *p_a_i-*p_b_i;
}
void calc_energy(struct rgb_img *im, struct rgb_img **grad) {
    // create grad
    *grad = (struct rgb_img *)malloc(sizeof(struct rgb_img));
    (*grad)->height = im->height;
    (*grad)->width = im->width;
    (*grad)->raster = (uint8_t *)malloc(3 * im->height * im->width);

    int rows = im->height;
    int cols = im->width;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            int i_a, i_b, j_b, j_a;
            // calculate r_x, g_x, b_x
            j_a = j+1==cols ? 0:j+1;
            j_b = j-1<0 ? cols-1 : j-1;
            int rgbx[3];
            rgbx[0] = get_pixel(im, i, j_a, 0) - get_pixel(im, i, j_b, 0);
            rgbx[1] = get_pixel(im, i, j_a, 1) - get_pixel(im, i, j_b, 1);
            rgbx[2] = get_pixel(im, i, j_a, 2) - get_pixel(im, i, j_b, 2);

            // calculate r_y, g_y, b_y
            i_a = i+1==rows ? 0:i+1;
            i_b = i-1<0 ? rows-1 : i-1;
            int rgby[3];
            rgby[0] = get_pixel(im, i_a, j, 0) - get_pixel(im, i_b, j, 0);
            rgby[1] = get_pixel(im, i_a, j, 1) - get_pixel(im, i_b, j, 1);
            rgby[2] = get_pixel(im, i_a, j, 2) - get_pixel(im, i_b, j, 2);

            double gsx = (rgbx[0]*rgbx[0] + rgbx[1]*rgbx[1] + rgbx[2]*rgbx[2]);
            double gsy = (rgby[0]*rgby[0] + rgby[1]*rgby[1] + rgby[2]*rgby[2]);

            uint8_t temp = sqrt(gsx + gsy)/10;
            set_pixel(*grad, i, j, temp, 0, 0); // use this because of how print_grad is defined
        }
    }
}

void dynamic_seam(struct rgb_img *grad, double **best_arr) {
    // NOTE: make everything negative so we can do easy comparisons 
    // initalize size of *best_arr
    *best_arr = malloc(sizeof(double)*(grad->height*grad->width));
    // populate first row 
    for (int i = 0; i < grad->width; ++i) {
        (*best_arr)[i] = (double) get_pixel(grad,0,i,0);
    }
    // O(rows x cols) time complexity
    // check max 3 parent pixels
    for (int i = 1; i < grad->height; ++i) {
        for (int j = 0; j < grad->width; ++j) {
            int ic, j1, j2,j3;
            ic = i-1;
            j1 = j; // we always have this one
            j2 = (j-1>=0) ? j-1 : j;
            j3 = (j+1 < grad->width) ? j+1 : j;
            
            // populate costs
            double costs[3];
            costs[0] = (*best_arr)[ic*grad->width+j1];
            costs[1] = (*best_arr)[ic*grad->width+j2];
            costs[2] = (*best_arr)[ic*grad->width+j3];

            // stuffs
            qsort(costs, 3, sizeof(costs[0]), compare);
            // set min value to array
            (*best_arr)[i*grad->width+j] = costs[0]+ (double) get_pixel(grad, i, j, 0); // may be last value
        }
    }
}

void recover_path(double *best, int height, int width, int **path) {
    (*path) = (int *)malloc(sizeof(int)*height);
    // get lowest in final row first
    int minIndex = 0;
    double minVal = best[(height-1)*width];
    for (int j = 0; j < width; ++j) {
        if (minVal > best[j+(height-1)*width]) {
            minVal = best[j+(height-1)*width];
            minIndex = j;
        }
    }
    (*path)[height-1] = minIndex;
    for (int i = height-2; i >= 0; --i) {
        int j = (*path)[i+1];
        int j1,j2,j3;
        j1 = j; // we always have this one
        j2 = (j-1>=0) ? j-1 : j;
        j3 = (j+1 < width) ? j+1 : j;

        double costs[3];
        costs[0] = best[i*width+j1];
        costs[1] = best[i*width+j2];
        costs[2] = best[i*width+j3];

        int minCost = costs[0];
        int minniIndex = 0;
        for (int l = 0; l < 3; ++l) {
            if (costs[l] < minCost) {
                minCost = costs[l];
                minniIndex = l;
            }
        }
        int tmp;
        switch (minniIndex)
        {
        case 0:
            tmp = j1;
            break;
        case 1:
            tmp = j2;
            break;
        case 2:
            tmp = j3;
            break;
        default:
            break;
        }
        (*path)[i] = tmp;

    }
    }
void remove_seam(struct rgb_img *src, struct rgb_img **dest, int *path){
    create_img(dest, src->height, src->width-1);
    // remove one pixel from every row
    for (int i = 0; i < src->height; ++i) {
        int counter = 0;
        for (int j = 0; j < src->width; ++j) {
            if (j != path[i]) { // write it to dest
                // read pixel values
                int r = get_pixel(src, i, j, 0);
                int g = get_pixel(src, i, j, 1);
                int b = get_pixel(src, i, j, 2);
                // write pixel values
                set_pixel(*dest, i, counter, r, g, b);
                ++counter;
            }
        }
    }
}

// int main (void){
    // struct rgb_img *im;
    // struct rgb_img *cur_im;
    // struct rgb_img *grad;
    // double *best;
    // int *path;

    // read_in_img(&im, "HJoceanSmall.bin");

    
    // im->height = 4;
    // im->width = 3;
    // uint8_t testcase[] = {
    // 255, 101,  51,   255, 101,153,   255, 101,255,
    // 255, 153,  51,   255, 153,153,   255, 153,255,
    // 255, 203,  51,   255, 204,153,   255, 205,255,
    // 255, 255,  51,   255, 255,153,   255, 255,255
    // };
    // im->raster = testcase;

    // calc_energy(im, &grad);
    // print_grad(grad);
   // grad = (struct rgb_img *)malloc(sizeof(struct rgb_img));
   // grad->height = 5;
   // grad->width = 6;
   // grad->raster = (uint8_t[]){
        // 24, 24, 24,  22, 22, 22,  30, 30, 30,  15, 15, 15,  18, 18, 18,  19, 19, 19,
        // 12, 12, 12,  23, 23, 23,  15, 15, 15,  23, 23, 23,  10, 10, 10,  15, 15, 15,
        // 11, 11, 11,  13, 13, 13,  22, 22, 22,  13, 13, 13,  21, 21, 21,  14, 14, 14,
        // 13, 13, 13,  15, 15, 15,  17, 17, 17,  28, 28, 28,  19, 19, 19,  21, 21, 21,
        // 17, 17, 17,  17, 17, 17,   7,  7,  7,  27, 27, 27,  20, 20, 20,  19, 19, 19
    // };
    // print_grad(grad);
    // dynamic_seam(grad, &best);
    // for (int i = 0; i < grad->height; ++i) {
        // for (int j = 0; j < grad->width; ++j) {
            // printf("%f ", best[i*grad->width+j]);
        // }
        // printf("\n");
    // }
    // printf("\n\n");
    // recover_path(best, grad->height, grad->width, &path);
     // for (int i = 0; i < grad->height; ++i) {
         // printf("%d ", path[i]);
     // }
// }

    
     // for(int i = 0; i < 550; i++){
         // printf("i = %d\n", i);
         // calc_energy(im,  &grad);
         // dynamic_seam(grad, &best);
         // recover_path(best, grad->height, grad->width, &path);
         // remove_seam(im, &cur_im, path);

         // char filename[200];
         // sprintf(filename, "img%d.bin", i);
         // write_img(cur_im, filename);


         // destroy_image(im);
         // destroy_image(grad);
         // free(best);
         // free(path);
         // im = cur_im;
     // }
 // return 0;
 // }
    // write_img(im, "testingtesting.bin");
    // destroy_image(im);
//}

//int main (void){
    //struct rgb_img *im;
    //struct rgb_img *cur_im;
    //struct rgb_img *grad;
    //double *best;
    //int *path;
    //read_in_img(&im, "HJoceanSmall.bin");

    //for(int i = 0; i < 150; i++){
        //printf("i = %d\n", i);
        //calc_energy(im,  &grad);
        //dynamic_seam(grad, &best);
        //recover_path(best, grad->height, grad->width, &path);
        //remove_seam(im, &cur_im, path);

        //char filename[200];
        //sprintf(filename, "img%d.bin", i);
        //write_img(cur_im, filename);


        //destroy_image(im);
        //destroy_image(grad);
        //free(best);
        //free(path);
        //im = cur_im;
    //}
//}


