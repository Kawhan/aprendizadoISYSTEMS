#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return -strcmp(a, b);
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int valor1[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    int valor2[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    int value = strlen(a);
    int value2 = strlen(b);
    for (int i = 0; i < strlen(a); i++) {
        for (int j = 0; j < strlen(a); j++) {
            int base = (int) a[j] - (int) 'a';
            valor1[base] += 1;
            if (valor1[base] >= 2) {
                value -= 1;
            }
        }
        break;
    }
    
    // jbbkk = 3
    // 

    for (int i = 0; i < strlen(b); i++) {
        for (int j = 0; j < strlen(b); j++) {
            int base = (int) b[j] - (int) 'a';
            valor2[base] += 1;
            if (valor2[base] >= 2) {
                value2 -= 1;
            }
        }
        break;
    }

    if (value > value2) {
        return 1;
    } else if (value == value2) {
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
    char *temp;

    for (int i=0; i < len ; i++) 
    {
        for (int j=0; j < len - 1; j++) 
        {
            int valor = (*cmp_func)(arr[j], arr[j+1]);
            if (valor > 0) {
               temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
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

    printf("\n\nPrimeira: \n\n");

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