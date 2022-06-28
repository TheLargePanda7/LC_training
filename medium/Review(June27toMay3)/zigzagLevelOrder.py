Problem: 103. Binary Tree Zigzag Level Order Traversal
Level: Medium
Topic:
	Tree, DFS, Queue
Note:
	For this problem, it is important to review Level Order Traversal problem as it is similar. As we see, we need to BFS search the tree nodes as we visit nodes level by level except we need to alternate the direction as we go
	Once we know that we need BFS, this is a great time of using queue. However, the way we append the nodes to the queue changes based on level i. For example, if level is even, we append from left to right. Otherwise, we append from right to left. To implement this, we declare a level variable to keep track of current level and use it as a key to index to hash map that stores queues. Based on the current level, we will do FIFO if level is even and FILO if level is odd. 

		
Code: 
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            queue = deque()
            queue.append(root)
            dict = defaultdict(deque)
            level = 0
            while queue:
                n = len(queue)
                for i in range(n):
                    pop_element = queue.popleft()
                    if pop_element:
                        if level % 2 == 0:
                            dict[level].append(pop_element.val)
                        elif level % 2 != 0:
                            dict[level].appendleft(pop_element.val)
                        queue.append(pop_element.left)
                        queue.append(pop_element.right)
                
                level += 1


            return dict.values()
					
			
			
