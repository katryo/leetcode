import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        else:
            self.arr.append(val)
            self.dic[val] = len(self.arr)-1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            top_val = self.arr[-1]
            target_idx = self.dic[val]

            self.arr[target_idx] = top_val
            self.arr.pop()

            self.dic[top_val] = target_idx
            self.dic.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # return random.sample(self.arr, 1)[0]
        return self.arr[random.randint(0, len(self.arr) - 1)]


# r = RandomizedSet()
# r.insert(0)
# r.remove(0)
# r.insert(-1)
# r.remove(0)
# print(r.getRandom())
# print(r.getRandom())
# print(r.getRandom())
# print(r.getRandom())
# print(r.getRandom())
# print(r.getRandom())
# print(r.getRandom())
# print(r.getRandom())

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(10)
# param_2 = obj.remove(10)
# param_3 = obj.getRandom()