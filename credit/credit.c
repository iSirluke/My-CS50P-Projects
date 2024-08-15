#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get credit card number
    long validcc = get_long("Credit card number: ");

    int i = 0;
    long ccard = validcc;
    while (ccard > 0)

    {
        ccard = ccard / 10;
        i++;
    }
    // Check the length of the card
    if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n");
        return 0;
    }
    // calculate checksum
    int sum1 = 0, sum2 = 0;
    long x = validcc;
    int total = 0;
    int mod1, mod2;
    int double1, double2;

    do
    {
        // Remove last digit and add to sum1
        mod1 = x % 10;
        x = x / 10;
        sum1 = sum1 + mod1;

        // Remove second last digit
        mod2 = x % 10;
        x = x / 10;

        // Double second last digit and add digits to sum2
        mod2 = mod2 * 2;
        double1 = mod2 % 10;
        double2 = mod2 / 10;
        sum2 = sum2 + double1 + double2;

    }
    while (x > 0);
    total = sum1 + sum2;

    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    // Get first digits
    long start = validcc;

    do
    {
        start = start / 10;
    }
    while (start > 100);
    // Check first digits for card type
    if ((start / 10 == 5) && (0 < start % 10 && start % 10 < 6))
    {
        printf("MASTERCARD\n");
    }

    else if ((start / 10 == 3) && (start % 10 == 4 || start % 10 == 7))
    {
        printf("AMEX\n");
    }

    else if (start / 10 == 4)
    {
        printf("VISA\n");
    }

    else
    {
        printf("INVALID\n");
    }


}
