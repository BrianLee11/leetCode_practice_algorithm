class MyQueue(object):

    def __init__(self):
        # Use two stacks: one for input, one for output
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Push the element onto the input stack
        self.input_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # If the output stack is empty, transfer all elements from the input stack
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        # Pop the top element from the output stack
        return self.output_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        # If the output stack is empty, transfer all elements from the input stack
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        # Peek the top element from the output stack
        return self.output_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # The queue is empty if both stacks are empty
        return not self.input_stack and not self.output_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
