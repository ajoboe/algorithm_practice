#include <stdio.h>
#include <stdlib.h>
#include "fib.h"

int main() {
	printf("hello, world!\n");

	int i;
	for(i=0;i<9;i++)
		printf("%i\n", fib(i));

	return 0;
}
