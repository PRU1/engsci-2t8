#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdint.h>

#include "seamcarving.h"
#include "c_img.c"
void calc_energy(struct rgb_img *im, struct rgb_img **grad){
    size_t height = im->height;
    size_t width = im-> width;
    create_img(grad, height, width);
    for(size_t i = 0; i < height; i++){
        for(size_t j = 0; j < width; j++){
            
            size_t y_top = (i==0? (height-1): (i-1));
            size_t y_bottom = (i== height -1? 0: (i+1));
            size_t x_left = (j==0? (width-1): (j-1));
            size_t x_right = (j== width -1? 0: (j+1));
            int deltaxred = get_pixel(im, i, x_right, 0) - get_pixel(im, i, x_left, 0);
            int deltaxgreen = get_pixel(im, i, x_right, 1) - get_pixel(im, i, x_left, 1);
            int deltaxblue = get_pixel(im, i, x_right, 2) - get_pixel(im, i, x_left, 2);
            int deltayred = get_pixel(im, y_top, j, 0) - get_pixel(im, y_bottom, j, 0);
            int deltaygreen = get_pixel(im, y_top, j, 1) - get_pixel(im, y_bottom, j, 1);
            int deltayblue = get_pixel(im, y_top, j, 2) - get_pixel(im, y_bottom, j, 2);
            int deltaxtotal = deltaxred*deltaxred + deltaxgreen*deltaxgreen + deltaxblue*deltaxblue;
            int deltaytotal = deltayred*deltayred + deltaygreen*deltaygreen + deltayblue*deltayblue;
            double deltafinal = sqrt(deltaxtotal + deltaytotal);
            
            uint8_t energy_value = (uint8_t)(deltafinal / 10.0);
            set_pixel(*grad, i, j, energy_value, energy_value, energy_value);
        }
    }
}
void dynamic_seam(struct rgb_img *grad, double **best_arr){
    size_t height = grad->height;
    size_t width = grad->width;
    int left = 0;
    int right = 0;
    for(int i = 0; i < width; i++){
        best_arr[0][i] =  get_pixel(grad, 0, i, 1);
            for(int j = 1; j < height; j++){
                int temp = get_pixel(grad, j, i, 1);
                left = (i==0?1:0);
                right = (i==width -1?1:0);
                if(left){
                    best_arr[j][i] = fminf(best_arr[j-1][i],best_arr[j-1][i+1]) + temp; 
                }
                else if(right){
                    best_arr[j][i] = fminf(best_arr[j-1][i],best_arr[j-1][i-1]) + temp; 
                }
                else {
                    best_arr[j][i] =fminf(best_arr[j-1][i], fmin(best_arr[j-1][i+1], best_arr[j-1][i-1])) + temp; 
                }
            }

    }
}
void recover_path(double *best, int height, int width, int **path){
    *path = (int *)malloc(height * sizeof(int));
    if (*path == NULL) {
        printf("Can't malloc");
        exit(1);
    }
    int min_index = 0;
    double min_val = best[(height - 1) * width + 0];
    for (int j = 1; j < width; j++) {
        double curr_val = best[(height - 1) * width + j];
        if (curr_val < min_val) {
            min_val = curr_val;
            min_index = j;
        }
    }
    (*path)[height - 1] = min_index;
    for (int i = height - 2; i >= 0; i--) {
        int prev_index = (*path)[i + 1];
        int best_index = prev_index;
        double best_cost = best[i * width + prev_index];
        
        if (prev_index > 0) {
            double left_cost = best[i * width + (prev_index - 1)];
            if (left_cost < best_cost) {
                best_cost = left_cost;
                best_index = prev_index - 1;
            }
        }
        if (prev_index < width - 1) {
            double right_cost = best[i * width + (prev_index + 1)];
            if (right_cost < best_cost) {
                best_cost = right_cost;
                best_index = prev_index + 1;
            }
        }
        (*path)[i] = best_index;
    }

}
void remove_seam(struct rgb_img *src, struct rgb_img **dest, int *path){
    create_img(dest, src->height, src->width - 1);
    for (int i = 0; i < src->height; i++) {
        int seam_col = path[i];
        int new_col = 0;
        for (int j = 0; j < src->width; j++) {
            if (j == seam_col)
                continue;
            uint8_t r = get_pixel(src, i, j, 0);
            uint8_t g = get_pixel(src, i, j, 1);
            uint8_t b = get_pixel(src, i, j, 2);
            set_pixel(*dest, i, new_col, r, g, b);
            new_col++;
}
}
}

int main (void){
    struct rgb_img *im;
    struct rgb_img *cur_im;
    struct rgb_img *grad;
    double *best;
    int *path;

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
    grad = (struct rgb_img *)malloc(sizeof(struct rgb_img));
    grad->height = 5;
    grad->width = 6;
    grad->raster = (uint8_t[]){
         24, 24, 24,  22, 22, 22,  30, 30, 30,  15, 15, 15,  18, 18, 18,  19, 19, 19,
         12, 12, 12,  23, 23, 23,  15, 15, 15,  23, 23, 23,  10, 10, 10,  15, 15, 15,
         11, 11, 11,  13, 13, 13,  22, 22, 22,  13, 13, 13,  21, 21, 21,  14, 14, 14,
         13, 13, 13,  15, 15, 15,  17, 17, 17,  28, 28, 28,  19, 19, 19,  21, 21, 21,
         17, 17, 17,  17, 17, 17,   7,  7,  7,  27, 27, 27,  20, 20, 20,  19, 19, 19
     };
     print_grad(grad);
     dynamic_seam(grad, &best);
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
    // read_in_img(&im, "HJoceanSmall.bin");

    //for(int i = 0; i < 150; i++){
        //printf("i = %d\n", i);
        //calc_energy(im,  &grad);
        ////dynamic_seam(grad, &best);
        ////recover_path(best, grad->height, grad->width, &path);
        ////remove_seam(im, &cur_im, path);

        //char filename[200];
        //sprintf(filename, "img%d.bin", i);
        //write_img(cur_im, filename);


        //destroy_image(im);
        //destroy_image(grad);
        //free(best);
        //free(path);
        //im = cur_im;
    //}
}