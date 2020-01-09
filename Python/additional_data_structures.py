class Stack:
    def __init__(self):
        self.vars = []

    def put(self, num):
        self.vars.append(num)

    def pop(self):
        if len(self.vars) == 0:
            raise Exception("Empty stack.")
        else:
            num = self.vars[len(self.vars)-1]
            self.vars.pop(len(self.vars) - 1)
            return num

    def height(self):
        return len(self.vars)

    def show(self):
        return self.vars

    def __str__(self):
        return self.__class__.__name__

# Using Stack -
#
# 1. create an instance
#     stack = Stack()
# 2. insert elements
#     stack.put(1)
# 3. Pop an element
#     stack.pop()
# 4. height of stack
#     stack.height()
# 5. Get all values in a stack
#     stack.show()


class Queue:
    def __init__(self):
        self.vars = []

    def put(self, num):
        self.vars.append(num)

    def out(self):
        if len(self.vars) == 0:
            raise Exception("Empty queue.")
        else:
            num = self.vars[0]
            self.vars.pop(0)
            return num

    def show(self):
        return self.vars

    def length(self):
        return len(self.vars)

    def __str__(self):
        return self.__class__.__name__

# Using Queue -
#
# 1. create an instance
#     queue = Queue()
# 2. insert elements
#     queue.put(1)
# 3. Out an element
#     queue.out()
# 4. length of queue
#     queue.length()
# 5. Get all values in a queue
#     queue.show()

