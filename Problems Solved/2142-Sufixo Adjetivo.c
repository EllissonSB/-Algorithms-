#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() {
  char c[50],*p_c=c;
  int d,e;
  scanf("%s",c);
  d=strlen(c);
  c[d-1]='\0';
  c[d-2]='\0';
  c[d-3]='\0';
  e=strlen(c);
  printf("Aquilo que ");
  for (int i=0;i<e;i++){
    printf("%c",p_c[i]);
  }
  printf(".");
	return 0;
}