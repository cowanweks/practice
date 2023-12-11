#include <stdio.h>

/*
    Arrays in C contain only one type of elements.
    Arrays in C are in the form

    (type) (arrayname)[arraysize]

        (OR)

    (type) (arrayname)[arraysize] = { element1, element2, element3}

    For example having an array of fruits would be

    char* fruits[3]

    (OR)

    char* fruits[3] = { "Mangoes", "Oranges", "Bananas"}

*/

int main()
{

    char *fruits[4] = {"Mangoes",
                       "Oranges",
                       "Avocados",
                       "Bananas"};

    int marks[5] = {40, 80, 50, 65, 20};

    // Adding or updating arrays
    marks[3] = 90;
    fruits[1] = "Strawberrys";

    printf("The marks at marks[3] is %d and the fruit at fruits[1] is %s\n", marks[3], fruits[1]);

    for (int i = 0; i < (sizeof(marks) / sizeof(int)); i++)
    {
        printf("The marks at marks[%d] is %d\n", i, marks[i]);
    }

    for (int i = 0; i < (sizeof(fruits) / sizeof(char *)); i++)
    {
        printf("The fruit at fruits[%d] is %s\n", i, fruits[i]);
    }
}