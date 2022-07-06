# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        n = 4
        
        0 -> 1 -> 2 -> 3
        
        0 is twin of 3
        1 is twin of 2
        
        i = 0 -> its twin == 4 - 1 - i = 3
        i = 1 -> its twin == 4 - 1 -1 = 2
    
        Goal:
        Collect pairs of twin of nodes and sum them up 
        Return the possible maximum sum value of twin pair
        
        Initial thought:
        Find the middle element of linked list
        Traverse through entire linked list and append node values to array
        Iterate through array from i = 0 -> i = middle and find its twin for each element
        Compute currSum and take max(currSum,res)
        
        return res
    
        Run-time Complexity: O(n) -> Need to construct the array from traversing linked list
        Space Complexity: O(n) -> Need to create an array to hold values of each node
        
        Optimization:
        Use fast-slow pointers technique to find the middle node of the linked list
        Divide the linked list into half (left half and right half)
        Reverse the right half linked list (now they should be pair by pair)
        Have one pointer to head of left half and one to head of right half linked list
        Move two pointers forward at the same time and add the pair values together
        Use temp variable to keep track of currMax and return temp variable
        
        Run-time Complexity: O(n) -> Need to traverse linked list to get a pointer to the middle node
        Space Complexity: O(1) -> no data structure is created
        
        """
        arr = []
        curr_node = head
        while curr_node:
            arr.append(curr_node.val)
            curr_node = curr_node.next
        # Edge case
        if len(arr) == 2:
            return arr[0] + arr[1]
        #print(arr)
        #print(len(arr))
        L = 0
        n = len(arr)
        R = n - 1
        res = 0
        middle = (R + L) // 2
        #print(middle)
        for i in range(0,middle+1):
            twin = n - 1 - i
            print(arr[i],arr[twin])
            currSum = arr[i] + arr[twin]
            res = max(currSum,res)
        return res
            
