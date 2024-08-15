#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    // User input text
    string text = get_string("Type your text: ");

    // Number of letters in the text
    int ls = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            ls++;

        }

    }

    // Number of words in text
    int w = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            w++;

        }

    }

    // Number of sentences typed
    int ss = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            ss++;
            
        }

    }

    // The Coleman-Liau formula
    float calculation = (0.0588 * ls / w * 100) - (0.296 * ss / w * 100) - 15.8;
    int index  = round(calculation);

    // Determine grade
    if (index < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    else
    {
        printf("Grade %i\n", index);
    }

}