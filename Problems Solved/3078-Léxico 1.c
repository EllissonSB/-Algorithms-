#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int caractere(char ch) {
  int cont=0;
  char arr[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
  for (int i=0;i<26;i++) {
    if (arr[i]==ch){
      cont= i+1;
    }
  }
  return cont;
}
int valor (char str[],int cont) {
  cont++;
    if (strlen(str)==cont) return 0;
    return caractere(str[cont]) + valor(str,cont);
}
int maior (int somas,int somas2){
  if (somas<somas2){
    return 2;
  }
  else return 1;
}
int main() {
  int cont=-1,soma1,soma2,result;
  char palavra[20],palavra2[20];
  scanf("%s\n%s", palavra, palavra2);
  soma1=valor(palavra,cont);
  soma2=valor(palavra2,cont);
 
  result=maior(soma1, soma2);
  
  if (result==1)printf("%s", palavra);
  else if (result==2) printf("%s", palavra2);
return 0;
}