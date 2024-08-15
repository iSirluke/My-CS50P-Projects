#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Get a name from the user
    string answer = get_string("What is your name?: ");

    //Print hello and the user's name
    printf("hello, %s\n", answer);
}