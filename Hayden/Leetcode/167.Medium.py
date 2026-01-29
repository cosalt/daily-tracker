class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        output = [0, 0]

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target: 
                output[0], output[1] = left+1, right+1
                break
            elif sum > target: right -= 1
            elif sum < target: left += 1
            
        return output
