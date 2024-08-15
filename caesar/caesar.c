#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // Check one command-line arguement
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if input is a digit
    string key = argv[1];

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Get text from user and convert to integer
    string message = get_string("Type your message: ");

    int k = atoi(key);
    printf("Ciphertext: ");

    // Get Ciphertext
    for (int i = 0; i < strlen(message); i++)
    {
        // Handle uppercases
        if (isupper(message[i]))
        {
            printf("%c", (((message[i] - 65) + k) % 26) + 65);
        }

        // Handles lowercases
        else if (islower(message[i]))
        {
            printf("%c", (((message[i] - 97) + k) % 26) + 97);
        }

        else
        {
            printf("%c", message[i]);
        }
    }
    printf("\n");

}