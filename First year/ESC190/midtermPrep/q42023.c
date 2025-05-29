#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct student{
    char s_number[11];
    int marks[10];
}student;

void read_line_by_line(student *s1, char *line){
    FILE *fileptr = fopen("file.txt", "r");
    char line[200];
    if (fileptr == NULL) {
        printf("error: check file");
    }
    int student_count = 0;
    while (fgets(line, sizeof(line), fileptr)){
        // populate student
        populate_student(s1, line);
    }
    fclose(fileptr);
}
void populate_student(student *s1, char *line){
    // first read in the student number
    int j = 0; 
    while (line[j] != ' ') {
        s1->s_number[j] = line[j];
    }
    s1->s_number[++j] = NULL;
    // read in the marks
    j += 1;
    int counter2 = 0;
    int markCounter = 0;
    while (line[j] != '\n') { // each line terminates with a newline
        char num[4];
        if (line[j] == ' ') {
            counter2 = 0;
            int tmp = atoi(num);
            s1->marks[markCounter] = tmp;
            ++markCounter;
            num[0] = '\0'; // reset string
        }
        num[counter2] = line[j];
        ++j; 
        ++counter2;
    }
    // determine avg mark 
    int max_mark = 0;
    int avg = calculate_average(s1, markCounter+1);
    if (avg > max_mark) {
        avg = max_mark;
    }
    // find out who ever has the max mark
}
int calculate_average(student *s1, int markCount) {

    // stuff here
}
