# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# class NestedIterator(object):
#
#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#         flat = []
#         for nested_integer in nestedList:
#             if nested_integer.isInteger():
#                 flat.append(nested_integer.getInteger())
#                 continue
#             n_ints = nested_integer.getList()
#             iter = NestedIterator(n_ints)
#             while iter.hasNext():
#                 flat.append(iter.next())
#         self.flattened = flat
#         self.cur = -1
#
#     def next(self):
#         """
#         :rtype: int
#         """
#         self.cur += 1
#         return self.flattened[self.cur]
#
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.cur < len(self.flattened)-1


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80142/8-line-Python-Solution

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()  # flatten the top nested integer
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """

        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.stack.append(top)
                return True
            self.stack += top.getList()[::-1]
        return False
