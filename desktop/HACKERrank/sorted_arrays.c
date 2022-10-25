#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    if ((int) *a > (int) *b) {
        // printf("\nTrue\n");
        return 1;
    }
    else {
        return 0;
    }
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    if ((int) *a < (int) *b) {
        // printf("\nTrue\n");
        return 1;
    }
    else {
        return 0;
    }
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int value = 0;
    int value2 = 0;
    for (int i = 0; i < strlen(a) - 1; i++) {
        if (a[i] != a[i+1]) {
            value +=1;
        }
    }

    for (int i = 0; i < strlen(b) - 1; i++) {
        if (b[i] != b[i+1]) {
            value2 +=1;
        }
    }

    if (value > value2) {
        return 1;
    } else if (value > value2) {
        return lexicographic_sort(a, b);
    } else {
        return 0;
    }
}

int sort_by_length(const char* a, const char* b) {
    if (strlen(a) > strlen(b)) {
        return 1;
    } else if (strlen(a) == strlen(b)) {
        return lexicographic_sort(a, b);
    } else {
        return 0;
    }
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    int sum = 0;
    if (cmp_func == lexicographic_sort) 
    {
        for (int i=0; i < len - 1; i++) 
        {
            for (int j=0; j < len - 1; j++) 
            {
                int valor = lexicographic_sort(arr[j], arr[j+1]);
                if (valor) {
                    char *temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    if (cmp_func == lexicographic_sort_reverse) 
    {
        for (int i=0; i < len - 1; i++) 
        {
            for (int j=0; j < len - 1; j++) 
            {
                int valor = lexicographic_sort_reverse(arr[j], arr[j+1]);
                if (valor) {
                    char *temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    if (cmp_func == sort_by_length) 
    {
        for (int i=0; i < len - 1; i++)  {
           for (int j=0; j < len - 1; j++) 
            {
                int valor = sort_by_length(arr[j], arr[j+1]);
                if (valor) {
                    char *temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    if (cmp_func == sort_by_number_of_distinct_characters) 
    {
        for (int i=0; i < len - 1; i++)  {
           for (int j=0; j < len - 1; j++) 
            {
                int valor = sort_by_number_of_distinct_characters(arr[j], arr[j+1]);
                if (valor) {
                    char *temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }

    printf("Primeira: \n\n");
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    printf("Segunda: \n\n");
    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    printf("Terceira: \n\n");
    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    printf("Quarta: \n\n");
    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}