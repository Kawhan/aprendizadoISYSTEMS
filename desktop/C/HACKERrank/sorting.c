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

double calculo_triangulo (triangle t) {
	int a = t.a;
	int b = t.b;
	int c = t.c;
	double p = (a + b + c)/2.0;
	double s = sqrt(p * (p - a) * (p - b) * (p - c));
	return s;
}

void sort_by_area(triangle* tr, int n) {
	triangle temp2; 
	
	for (int i = 0; i < n; i++) {     
        for (int j = 0; j < n -1; j++) {
			if ((calculo_triangulo(tr[j])) > calculo_triangulo(tr[j+1])) {
				temp2 = tr[j];
				tr[j] = tr[j+1];
				tr[j+1] = temp2;
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