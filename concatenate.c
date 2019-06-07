#include<stdio.h>
int main()
{
    char a[50],b[50];
    int i,j,n,k;
    printf("\n");
    scanf("%s",a);
    printf("\n ");
    scanf("%s",b);
    for(i=0,k=0;a[i]!='\0';i++)
        k++;
    for(j=0,n=0;b[j]!='\0';j++)
        n++;
    for(i=k,j=0;i<=n+k;i++,j++)
            a[i]=b[j];
    printf("\n %s",a);
    return 0;
}
