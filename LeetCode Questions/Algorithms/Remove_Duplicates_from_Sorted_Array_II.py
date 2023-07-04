class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Thoughts about the solution:
        # We use 2 pointers to go through the array
        # the first to go through all numbers in the current array.
        # For the other one, we assume we have another invisible empty array, and that pointer is used to point at the last place of that 'invisible array'. If this number pointed by the first array needs to be put in the new 'invisible array', we put it in
        i = 0
        
        for n in nums:
            if (i<2) or (n!=nums[i-2]): 
                # so the first 2 numbers will be included
                # and if a number is included more than 2 times
                # it will not be included
                nums[i] = n
                i += 1
        
        # Why returns i?
        # Because the question asks for k == ExpectedNums.length, then use for loop to loop through first 'i' numbers
        # So we do not need to clear all numbers after the i_th number
        return i  

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    solution_instance = Solution()
    length = solution_instance.removeDuplicates(nums)

    print(length)

    print("[", end="")
    for i in range(length):
        print(nums[i], end="")
        if i!=length-1:
            print(", ", end="")
    print("]")
