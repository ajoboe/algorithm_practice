#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int binary_search(int l[], int key, size_t n);
int binary_search_helper(int l[], int key, size_t n, int first, int last);
void bubble_sort(int l[], size_t n);


/*
    MAIN
*/
int main() {
  // generate a sorted list of random numbers
  // under 100 and print it
  int n = 20;
  int list[n];
  srand(time(0));
  for(int i=0; i<n; i++) {
    list[i] = rand()  % 100;
  }
  bubble_sort(list, n);
  printf("SORTED LIST:\n");
  for(int i=0; i<n; i++) {
    printf("%d\n", list[i]);
  }

  // pick a search key from the list
  // then find and print it
  int key = list[rand() % n];
  printf("\nGonna look for %d...\n", key);
  int result = binary_search(list, key, n);
  printf("\n\nI just found %d!\n\n", result);

  return 0;
}


/*
    BINARY SEARCH
*/
int binary_search(int l[], int key, size_t n) {
  return binary_search_helper(l, key, n, 0, n-1);
}

int binary_search_helper(int l[], int key, size_t n, int first, int last) {
  int size = last - first + 1;
  if(size <= 0) {
    printf("\nsize is %d. returning -1", size);
    return -1;
  }
  int mid = first + size / 2;
  printf("\nkey is %d and mid is %d", key, l[mid]);
  if(key == l[mid]) {
    printf("\nfound it: %d", l[mid]);
    return l[mid];
  }
  if(key < l[mid]) {
    printf("\ngoing left");
    return binary_search_helper(l, key, n, first, mid-1);
  }
  if(key > l[mid]) {
    printf("\ngoing right");
    return binary_search_helper(l, key, n, mid+1, last);
  }
}


/*
    BUBBLE SORT
*/
void bubble_sort(int l[], size_t n) {
  if(n < 2) return;
  for(int i=0; i<n; i++) {
    for(int j=1; j<n; j++) {
      if(l[j] < l[j-1]) {
        int tmp = l[j];
        l[j] = l[j-1];
        l[j-1] = tmp;
      }
    }
  }
}
