def binary_search(ls, num):
    lower = 0
    upper = len(ls)
    while lower < upper:
        mid = (lower + upper) // 2
        if num == ls[mid]:
            return mid
        elif num > ls[mid]:
            if lower == mid: ## in the case where you search for A in [A, B]
                return mid+1
            lower = mid
        elif num < ls[mid]:
            upper = mid
            
## would return len(ls) is num not in ls and more than the largest number or None if smaller than the smallest
