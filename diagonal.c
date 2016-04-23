#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);
    int a[n][n];
    int prim_diag = 0;
    int sec_diag = 0;
    int difference;
    int mid = 0;
    int i,j;

    if(n % 2 == 0)
    	mid = n/2;
    else
    	mid = (n/2)+1;

    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){
          
          scanf("%d",&a[a_i][a_j]);
       }
    }

    printf("\n");

    for(i = 0; i <= n-1; i++){
    	prim_diag += a[i][i];
    }

    for(i = n-1; i >=0; i--){
    		sec_diag += a[i][(n-1)-i];
    	}
    	
    difference = abs(prim_diag - sec_diag);

    printf("%d\n", difference);
    return 0;
}
