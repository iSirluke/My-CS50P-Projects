#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int x;
    do
    {
        x = get_int("Start population size: ");
    }
    while (x < 9);

    // TODO: Prompt for end size
    int y;
    do
    {
        y = get_int("End population size: ");
    }
    while (y < x);

    // TODO: Calculate number of years until we reach threshold
    int start_size = x;
    int years = 0;
    while (start_size < y)
    {
        start_size = start_size + start_size/3 - start_size/4;
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
