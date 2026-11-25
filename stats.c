//add some code please related to stats
#include <stdio.h>

int main() {
    // Example statistics calculation
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += numbers[i];
    }
    double average = (double)sum / size;
    printf("Sum: %d\n", sum);
    printf("Average: %.2f\n", average);
    return 0;
}

