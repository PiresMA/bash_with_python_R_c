// goto.c
// https://docs.microsoft.com/pt-br/cpp/c-language/goto-and-labeled-statements-c?view=msvc-160
#include <stdio.h>

int main()
{
    int i, j;

    for ( i = 0; i < 5; i++ )
    {
        printf( "Outer loop executing. i = %d\n", i );
        for ( j = 0; j < 2; j++ )
        {
            printf( " Inner loop executing. j = %d\n", j );
            if ( i == 3 )
                goto stop;
        }
    }

    /* This message does not print: */
    printf( "Loop exited. i = %d\n", i );

    stop: printf( "----------------------> Jumped to stop. i = %d\n", i );
}
