#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int a,b,c,p, vida=1, ataque, inimigo=1, defesa, vida_original, controle=0;
    float vt;
    char ch[2];
    
    scanf("%d %d %d %d\n%s\n", &a, &b, &c, &p,ch);
    
    vida_original=p;
    vt=vida_original*0.3;
    
    if (strcmp(ch,"C")==0) ataque=40, defesa=15;
    else if (strcmp(ch,"V")==0) ataque=50, defesa=20;
    
    
    do {
        if (p<=vt & controle==0) defesa=defesa*2,controle+=1;
        
        if (inimigo==1) {
            a=a-ataque;
            p=p-defesa;
            if (a<=0) {
                inimigo+=1;
            }
            if ((p<=0)) {
                vida=0;
                break;
            }
        }
        else if (inimigo==2) {
            b=b-ataque;
            p=p-defesa;
            if ((b<=0)) {
                inimigo+=1;
            }
            
            if ((p<=0)) {
                vida=0;
                break;
            }
            
        }    
            
        else if (inimigo==3) {
            c=c-ataque;
            p=p-defesa;
            if ((c<=0)) {
                inimigo+=1;
                vida+=1;
            }
            
            if ((p<=0)) {
                vida=0;
                break;
            }
            
        }
    
    } while (vida==1);
    if (vida>=1) printf("Eba! Pedro sobreviveu");
    else printf("Que pena... Era um jovem tao promissor");
	return 0;
}