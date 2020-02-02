class Node(object):
    def __init__(self, _key, _val):
        self.key = _key
        self.val = _val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: 'int'):
        self.cap = capacity
        self.size = 0
        self.val_map = {}
        self.node_map = {}
        self.list = None
        self.tail = None

    def get(self, key: 'int') -> 'int':
        print('get', self.tail)
        if key in self.val_map:
            # TODO: update the linkedlist.

            # [x] 1. delete the node
            node = self.node_map[key]
            self._delete_node(node)

            # 2. append the new node to the top of the list
            new_node = Node(key)
            self._append_new_node(new_node)

            return self.val_map[key]
        return -1

    def _delete_node(self, node):
        print('delete')
        # node is at the head and the tail
        # node is at the head
        if node == self.list:
            self.list = node.next
            if node == self.tail:
                self.tail = None

        # node is at the tail
        elif not node.next:
            print('tail delete')
            prev = node.prev
            if prev:
                prev.next = None
            self.tail = prev

        # node is in the middle
        else:
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next

        self.size -= 1

    def _append_new_node(self, node):
        print('append')
        if not self.list:
            self.list = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def _evict_oldest(self):
        print('evict')
        if not self.list:
            print('not self.head')
            return
        ret = self.list
        self._delete_node(self.list)
        return ret

    def put(self, key: 'int', value: 'int') -> 'None':
        print('put', self.tail)

        if key in self.val_map:
            old_node = self.node_map[key]
            self._delete_node(old_node)
            new_node = Node(key)
            self._append_new_node(new_node)
            self.node_map[key] = new_node
            self.val_map[key] = value
            return self.val_map[key]
        # self.list is None
        if not self.list:
            # [x] TODO: cap == 0
            if self.cap > 0:
                new_node = Node(key)
                self._append_new_node(new_node)
                self.val_map[key] = value
                self.node_map[key] = self.list
            return

        # cache size is less than cap
        if self.size < self.cap:
            new_node = Node(key)
            self.val_map[key] = value
            self.node_map[key] = new_node
            self._append_new_node(new_node)

        else:  # evict the most old memory
            removed_node = self._evict_oldest()
            print('removed_node', removed_node.key)
            del self.node_map[removed_node.key]
            del self.val_map[removed_node.key]
            new_node = Node(key)
            self.node_map[key] = new_node
            self.val_map[key] = value
            self._append_new_node(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)