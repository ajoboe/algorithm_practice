#include <stdlib.h>
#include <stdio.h>
#include "insertion_sort.h"

int main() {
	int l[]={9,4,3,7,1,2,0,6,5,8};

	int j;
	printf("\nUNsorted\n");
	for(j=0;j<10;j++) printf("%i",l[j]);
	is(l,10);	
	printf("\nsorted\n");
	for(j=0;j<10;j++) printf("%i",l[j]);
	printf("\n\n");
		
	return 0;
}
