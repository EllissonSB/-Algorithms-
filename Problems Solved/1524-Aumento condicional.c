#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
  float sala,aumento,aumento_s;
  scanf("%f",&sala);
  if (sala<=280){
    aumento=sala*1.20;
    aumento_s=aumento-sala;
    printf("%.2f\n",sala);
    printf("20\n");
    printf("%.2f\n",aumento_s);
    printf("%.2f",aumento);
  }
  else
    if (sala>280 & sala<=700){
      aumento=sala*1.15;
      aumento_s=aumento-sala;
      printf("%.2f\n",sala);
      printf("15\n");
      printf("%.2f\n",aumento_s);
      printf("%.2f",aumento);
    }
    else
    if (sala>700 & sala<1500){
      aumento=sala*1.10;
      aumento_s=aumento-sala;
      printf("%.2f\n",sala);
      printf("10\n");
      printf("%.2f\n",aumento_s);
      printf("%.2f",aumento);
    }
    else
    if (sala>=1500){
      aumento=sala*1.05;
      aumento_s=aumento-sala;
      printf("%.2f\n",sala);
      printf("5\n");
      printf("%.2f\n",aumento_s);
      printf("%.2f",aumento);
    }
  return 0;
}