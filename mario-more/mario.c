#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get number from user
    int h, i, row, column;
    do
    {
        h = get_int("Height: ");
    }
    //Check if input is between 1 and 8
    while (h < 1 || h > 8);

    for (i = 0; i < h; i++)
    {
        // Checking for columnc
        for (column = 1; column < (h - i); column++)
        {
            printf(" ");
        }
        // Checking for row on the left
        for (row = 0; row <= i; row++)
        {
            printf("#");
        }
        printf("  ");
        //. Checking for row on the right
        for (row = 0; row <= i; row++)
        {
            printf("#");
        }
        printf("\n");
    }

}
