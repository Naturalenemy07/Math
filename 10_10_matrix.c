#include <string.h>

#define ROWS 10
#define COLUMNS 10

int matrix[ROWS][COLUMNS];

int main(void)
{
    for(int i = 0; i < ROWS; i++)
    {
        for(int j = 0; j < COLUMNS; j++)
        {
            matrix[i][j] = i + j;
            printf("%i ", matrix[i][j]);
        }
        printf("\n");
    }    
}
