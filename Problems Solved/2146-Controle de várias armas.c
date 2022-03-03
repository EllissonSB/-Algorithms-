#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
  while (1){
  char nacionalidade,prof;
  int calibre,quantidade,ret;
  scanf("%s",&nacionalidade);
  ret=strlen(&nacionalidade);
  if (ret>1){
    printf("Fim");
    break;
  }
  if (nacionalidade=='B'){
    scanf("%s",&prof);
    scanf("%i",&quantidade);
    scanf("%i",&calibre);
    if (prof=='M'){
      printf("Liberado\n");
    }
    else if (prof=='T'|| prof=='O'){
      if (quantidade>1){
        printf("Barrado\n");
      }
      else if (quantidade<=1 & calibre<=22){
        printf("Liberado\n");
      }
      else if (calibre>22){
        printf("Barrado\n");
      }
    }
    else if (prof=='C'){
      if (quantidade<=2 & calibre<=38){
        printf("Liberado\n");
      }
      else printf("Barrado\n");
    }}
    else if (nacionalidade=='E'){
      scanf("%s",&prof);
      scanf("%i",&quantidade);
      scanf("%i",&calibre);
      if (quantidade==0){printf("Liberado\n");}
      else {printf("Barrado\n");}
    }
  
  else{
    printf("Fim");
    break;
  }
  }
	return 0;}