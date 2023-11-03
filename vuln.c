#include <stdio.h> 
#include <string.h> 

int main(){
    char buf[256];
    printf("Welcome!\n");
    printf("What's your name, kind stranger?");
    scanf("%s", buf);
    printf("Hello, %s\n", buf);
}