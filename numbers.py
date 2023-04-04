nums = [1, 2, 3,4]

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i]= nums[i-1] + nums[i]
    return nums
print(runningSum([1, 2, 3,4]))


numbers = [1, 2, 3,4]
suma = 0
for number in range(len(numbers)):
    suma = suma + numbers[number]
    numbers[number] = suma
