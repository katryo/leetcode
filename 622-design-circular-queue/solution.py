class MyCircularQueue2:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.maxsize = k
        self.size = 0
        self.arr = [0] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.maxsize:
            return False
        if self.head == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail+1) % self.maxsize
        self.arr[self.tail] = value
        self.size += 1

        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        if self.size == 1:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head+1) % self.maxsize
        self.size -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.size > 0:
            return self.arr[self.head]
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.size > 0:
            return self.arr[self.tail]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.maxsize


class Node:
    def __init__(self, v):
        self.next = None
        self.prev = None
        self.val = v


class MyCircularQueue:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.maxsize = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.maxsize:
            return False
        n = Node(value)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.prev = n
            n.next = self.tail
            self.tail = n
        self.size += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False

        if self.head.prev:
            self.head.prev.next = None
        self.head = self.head.prev
        if not self.head:
            self.tail = None
        self.size -= 1

        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.size > 0:
            return self.head.val
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.size > 0:
            return self.tail.val
        return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.maxsize


s = MyCircularQueue(3)
print('-----')
print(s.enQueue(1))
print(s.enQueue(2))
print(s.enQueue(3))
print(s.enQueue(4))
print(s.Rear())
print(s.isFull())
print(s.deQueue())
print(s.enQueue(4))
print(s.Rear())
print('-----')

s = MyCircularQueue2(3)
print('-----')
print(s.enQueue(1))
print(s.enQueue(2))
print(s.enQueue(3))
print(s.enQueue(4))
print(s.Rear())
print(s.isFull())
print(s.deQueue())
print(s.enQueue(4))
print(s.Rear())
print('-----')
