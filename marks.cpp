#include<stdio.h>

//grades of students according to their marks.
int main(){
    float marks;
    
    printf("enter marks \n");
    scanf("%f",&marks);

    if(marks>=90) {
        printf("A \n");
    }

    else if(marks>=80 && marks <90){
        printf("B \n");
    }

    else if(marks>=60 && marks<80){
    printf("C \n");
}

   else if (marks>=45 && marks <60){
    printf("D \n");
   }

   else{
    printf("E \n");
   }
}
