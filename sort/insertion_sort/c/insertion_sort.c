#include "insertion_sort.h"

void is(int* l, int n) {
	int i,j,size;
	for(size=0;size<n;size++){
		int item = l[n-1];
		for(i=0;i<size;i++) if(l[n-1]<l[i]) break;
		for(j=n-1;j>i;j--) l[j]=l[j-1];
		l[i]=item;
	}
/*
take last item
insert into correct place in new list
do n times

take last item
insert into first section
	scan for correct spot, index (0 thru <size)
	starting at n-2 --> n-1, skootch each item right
	stop after index+1 = index
	insert item at index
incr sec size

*/
}

void insert(int it, int* l, int n) {
	int i,j,m[n+1];
	for(i=0;i<n;i++) if(it<l[i]) break;
	for(j=n-1;j>i;j--) l[j]=l[j-1];
	l[i]=it;
}

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}
