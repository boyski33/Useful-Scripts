private static void binarySearch(int[] numbers, int searchNum) {
    int[] sortedNumbers = ArraysProblem4.bubbleSort(numbers);
    int lower = 0;
    int upper = numbers.length-1;

    while (lower <= upper) {
        int mid = (lower + upper) / 2;
        if (searchNum < sortedNumbers[mid]) {
            upper = mid - 1;
        } else if (searchNum > sortedNumbers[mid]) {
            lower = mid + 1;
        } else {
            System.out.println(mid);
            return;
        }
    }

    System.out.println("No such number.");
}
