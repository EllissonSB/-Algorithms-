#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
char t[20],t2[20],f[]="ndo";
int a,d,c;
scanf("%s",t);
a=strlen(t);
for (int i=0;i<a-1;i++){
  t2[i]=t[i];
}
c=strlen(t2);
for (int i=0;i<c;i++){
  printf("%c",t2[i]);
}
printf(" ");
strcat(t2,f);
d=strlen(t2);
for (int i=0;i<d;i++){
  printf("%c",t2[i]);
}
  return 0;
}