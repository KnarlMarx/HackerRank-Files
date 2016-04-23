#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n,i;
    int pos_num_sum = 0;
    int neg_num_sum = 0; 
    int zero_num_sum = 0;
    float pos_num_ratio = 0;
    float neg_num_ratio = 0;
    float zero_num_ratio = 0; 
   
    scanf("%d",&n);
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }

    for(i = 0; i < n; i++) {
    	if(arr[i] < 0) {
    		neg_num_sum += 1;
    	}	
    	else if(arr[i] == 0) {
    		zero_num_sum += 1;
    	}
    		
    	else if(arr[i] > 0) {
    		pos_num_sum += 1;

    	}
    		
    }

    neg_num_ratio = (neg_num_sum/(float) n);
    zero_num_ratio = (zero_num_sum/(float)n);
    pos_num_ratio = (pos_num_sum/(float)n);

    printf("%f\n", pos_num_ratio);
    printf("%f\n", neg_num_ratio);
    printf("%f\n", zero_num_ratio);

    return 0;
}
