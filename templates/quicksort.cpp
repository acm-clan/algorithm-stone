#include <stdio.h>

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high)
{
    int anchor = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= anchor) {
            // 永恒经典，一次遍历搞定绕着锚点分大小
            swap(&arr[++i], &arr[j]);
        }
    }
    // 最后把锚点放到中间来
    swap(&arr[i + 1], &arr[high]);
    //返回锚点的位置
    return i + 1;
}

void quick_sort(int arr[], int low, int high)
{
    if (low < high) {
        int anchor = partition(arr, low, high);
        quick_sort(arr, low, anchor - 1);
        quick_sort(arr, anchor + 1, high);
    }
}

void print_array(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int arr[] = { 13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11 };
    int n = sizeof(arr) / sizeof(arr[0]);
    quick_sort(arr, 0, n - 1);
    printf("Sorted array: \n");
    print_array(arr, n);
    return 0;
}