class Node:
    def __init__(self, v):
        self.val = v
        self.minValue = v


class MinStack():
    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val):
        self.st.append(val)
        minVal = min(val, self.minSt[-1] if self.minSt else val)
        self.minSt.append(minVal)
        return

    def pop(self):
        self.st.pop()
        self.minSt.pop()

    def top(self):
        return self.st[-1]

    def getMin(self):
        return self.minSt[-1]


m = MinStack()  # return None
print(m.push(-2))  # return None
print(m.push(0))  # return None
print(m.push(-3))  # return None
print(m.getMin())  # return -3
print(m.pop())  # return None
print(m.top())  # return 0
print(m.getMin())  # return -2
