struct mapa {
    char** matriz;
    int linhas;
    int colunas; 
};
typedef struct mapa MAPA;

struct posicao
{
    int x;
    int y;
};
typedef struct posicao POSICAO;


void libera_mapa(MAPA* m);
void aloca_mapa(MAPA* m);
void lermapa(MAPA* m);
void imprime_mapa(MAPA* m);
void encontra_mapa(MAPA* m, POSICAO* p, char c);
int ehvalida(MAPA* m, int x, int y);
int ehvazia(MAPA* m, int x, int y);
void andando_mapa(MAPA* m, int xorigem, int yorigem, int xdestino, int ydestino);