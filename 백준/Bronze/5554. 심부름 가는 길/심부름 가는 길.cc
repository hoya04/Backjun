#include <stdio.h>

int main() {
int x,y,h,s,p,a;
scanf("%d", &h);
scanf("%d",&s);
scanf("%d",&p);
scanf("%d",&a);

x = (h+s+p+a) / 60;
y = (h+s+p+a) % 60;

printf("%d\n",x);
printf("%d\n", y);




return 0;
}