#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

void sort_by_area(triangle* tr, int n) {
	triangle *tr2 = tr;
	triangle temp2;
	int aux[n];
	int temp = 0;    
	/**
	* Sort an array a of the length n
	*/
	for (int i = 0; i < n; i++)
	{
		int p = (tr[i].a + tr[i].b + tr[i].c)/2;
		int s = sqrt(p * (p - tr[i].a) * (p - tr[i].b) * (p - tr[i].c));
		aux[i] = s;
	}


	for (int i = 0; i < n; i++) {     
        for (int j = i+1; j < n; j++) {     
           if(aux[i] > aux[j]) {    
               temp = aux[i];    
               aux[i] = aux[j];    
               aux[j] = temp;    
           }     
        }     
    }    
	
	for (int i = 0; i < n; i++) {     
		int p = (tr[i].a + tr[i].b + tr[i].c)/2;
		int s = sqrt(p * (p - tr[i].a) * (p - tr[i].b) * (p - tr[i].c));
        for (int j = 0; j < n; j++) {
			if (s == aux[j]) {
				temp2 = tr[i];
				tr[i] = tr2[j];
				tr[j] = temp2;
			}
		}
    } 
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}