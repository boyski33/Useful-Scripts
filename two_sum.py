## find the indexes of a pair of integers in a list that add up to a certain number
## a unique pair, and guaranteed to be in the list

nums = [4, 2, 11, 7, 32, 11]
target = 22

cost_map = {}
for i in range(len(nums)):
    a = nums[i] 
    b = target - a ## basically, the number you're looking for in the array (that adds up to the target sum)
    if b in cost_map.keys():
        print(cost_map[b], i)
    else:
        cost_map[a] = i ## put the values you pass and their respective indexes in the dictionary
        
