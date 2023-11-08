#include <stdio.h> 
#include <string.h> 

int main(int argc, char **argv){
    /* initializing 256-byte buffer */
    char buf[256];
    printf("What's your name, kind stranger?\n");
    /* writes unsanitized user input to buffer */
    /* note - no length check! */
    scanf("%s", buf);
    printf("Hello, %s\n", buf);
    return 0;
}
