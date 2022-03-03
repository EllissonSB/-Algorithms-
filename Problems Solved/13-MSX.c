#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

struct frases{
    char frase[100];
}registros[44];

void maiuscula(char *textao){
    int j = 0;
    char ch;
    
    while (textao[j]) {
        ch = textao[j]; 
        putchar(toupper(ch));
        j++; 
    }
    printf("\n");
}

int main() {
    
int cont = 0;

while('True'){ 
    
    gets(registros[cont].frase);
    
    if(strcmp(registros[cont].frase,"the end!")==0){
        break;
    }else{
        maiuscula(registros[cont].frase);
        cont++;
        }
}
    
    return 0;
};