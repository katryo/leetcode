from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(list)

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        array = self.table[key]
        bisect.insort(array, (timestamp, value))

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key in self.table:
            array = self.table[key]
            idx = bisect.bisect(array, (timestamp, ""))
            if len(array) > idx and array[idx][0] == timestamp:
                return array[idx][1]
            if idx == 0:
                return ''
            target_idx = idx - 1
            return array[target_idx][1]
        else:
            return ''

# Your TimeMap object will be instantiated and called as such:
# kv = TimeMap()
# kv.set("foo", "high", 10)
# kv.set("foo", "low", 20)
# print(kv.get("foo", 5))
# print(kv.get("foo", 10))
# print(kv.get("foo", 15))
# print(kv.get("foo", 20))
# print(kv.get("foo", 24))
