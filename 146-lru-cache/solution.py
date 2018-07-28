class LL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, key):
        new_head = Node(self)
        new_head.val = key
        new_head.next = self.head
        if new_head.next:
            new_head.next.prev = new_head
        self.head = new_head

        if not self.tail:
            self.tail = self.head
        self.size += 1


class Node(object):
    def __init__(self, l):
        self.next = None
        self.prev = None
        self.val = None
        self.list = l

    def delete(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next

        if self.list.tail is self:
            self.list.tail = self.prev
        if self.list.head is self:
            self.list.head = self.next
        self.list.size -= 1


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.q = LL()
        self.table = dict()
        self.qtable = dict() # key: key, value: pointer to the element in the queue

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.table:
            self._update_q(key)
            return self.table[key]

        return -1

    def _update_q(self, key):
        node = self.qtable[key]
        if self.q.head is node:
            return self.table[key]
        node.delete()
        del node
        self.q.append(key)
        self.qtable[key] = self.q.head;

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            self.table[key] = value
            self._update_q(key)
            return

        if self.q.size == self.capacity:
            lru_key = self.q.tail.val
            del self.table[lru_key]
            self.q.tail.delete()
        self.q.append(key)
        self.table[key] = value
        self.qtable[key] = self.q.head


# funcs = ["put","put","get","put","put","get"]
# vals = [[2,1],[2,2],[2],[1,1],[4,1],[2]]

# funcs = ["put","put","get","put","get","put","get","get","get"]
# vals = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
# funcs = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# vals = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29]]#,[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
# f_vals = zip(funcs, vals)
# Your LRUCache object will be instantiated and called as such:

# [9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11]]

# [null,null,null,1,null,-1,null,-1,3,4]
# obj = LRUCache(2)


# obj.put(10, 1)
# obj.put(9, 3)
# obj.get(10)
# obj.get(10)
# obj.put(6, 14)
# obj.put(3, 1)
# obj.get(3)
# obj.put(10, 11)
#
# for f_val in f_vals:
#     if f_val[0] == "put":
#         print(obj.put(f_val[1][0], f_val[1][1]))
#     else:
#         print(obj.get(f_val[1][0]))

