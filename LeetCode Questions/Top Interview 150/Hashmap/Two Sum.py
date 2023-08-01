class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        find = False # Flag to indicate if a pair of numbers with the target sum is found
        output = []  # List to store the indices of the two numbers found

        # Use nested loops to iterate through each pair of numbers in the array and try to find the sum equal to the target
        for i in range(len(nums)-1):
            number1 = nums[i] # Get the first number
            for j in range(i+1, len(nums)):
                number2 = nums[j] # Get the second number
                sum_of_two_nums = number1 + number2 # Calculate the sum of the two numbers

                # If a pair of numbers with the target sum is found
                if (sum_of_two_nums == target):
                    find = True # Set the flag to indicate a match is found
                    output.append(i) # Add the index of the first number to the output list
                    output.append(j) # Add the index of the second number to the output list
                    break # Exit the inner loop since a match is found
                    
            if (find): # If a match is found, exit the outer loop as well
                break

        return output

if __name__ == "__main__":
    # Test example
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # It should output [0, 1] since nums[0] + nums[1] == 9, which satisfies the requirement.