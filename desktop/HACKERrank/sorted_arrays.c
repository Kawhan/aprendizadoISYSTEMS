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

}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    
}

int sort_by_length(const char* a, const char* b) {

}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
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
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}