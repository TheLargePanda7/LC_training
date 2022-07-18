from heapq import heappush,heappop,heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        """
        We will use a max-heap to store the key pair values (frequency and number) where the root node of the max heap will always store a highest frequency of a number. Once a max root node is removed from max heap, the next maximum element will become a root node. 
        By constructing the max heap, we will pop the element from the max heap k times and append elements to the result array since we want the top k most frequent numbers.        
        """
        # First create a dictionary 
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        # Construct max heap
        heap = []
        heapify(heap)
        for key in dict:
            # We only have min-heap, but to create max heap, we multiple the value by -1
            heappush(heap,(-dict[key],key))
        res = []
        while k > 0:
            frequency,numb = heappop(heap)
            print(frequency * -1,numb)
            res.append(numb)
            k-=1  
        
            
        # Return the top k most frequent elements
        return res
        
        
        
        
