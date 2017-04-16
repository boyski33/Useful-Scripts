def quicksort(arr, left, right):
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    index = partition(arr, left, right, pivot) ## the actual magic
    quicksort(arr, left, index-1)
    quicksort(arr, index, right)

## until the two pointers cross, we check if an element on the left side is larger than the current pivot,
## and if an element of the right side is less and then we swap them
def partition(arr, left, right, pivot):
    while left <= right :
        while arr[left] < pivot: ## move the pointer to the right until you reach the element
            left += 1
        while arr[right] > pivot: ## same for the right side
            right -= 1
        if left <= right: ## <= because in case left == right the pointers will never cross, causing an infinite loop
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left
