#include <stdio.h>
#include <math.h>

int binarysearch_int(int target, int arr[], int length);

int main(int argc, char* argv[]){
    int arr[] = {1, 4, 6, 9, 10, 14, 28, 34, 36, 45, 55, 120, 203, 404, 501, 502, 503, 504, 506};
    printf("A posição é: %d\n", binarysearch(506, arr, 19));
}

int binarysearch_int(int target, int arr[], int length) {
    int up = length -1;
    int bottom = 0;
    
    while (up >= bottom) {
        int c = bottom + (up - bottom)/2; // Explained in the readme.

        if (arr[c] > target) {
            up = c - 1;
        } else if (arr[c] < target){
            bottom = c + 1;
        } else {
            return c;
        }
    }
    return -1; // i.e no match found.
}