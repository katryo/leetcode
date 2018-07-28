import collections

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        changes = collections.defaultdict(int)
                
        def can_give_15():
            if changes[10] > 0 and changes[5] > 0:
                return True
            if changes[5] > 2:
                return True
            return False
        
        def give_15():
            print(changes)
            if changes[10] > 0 and changes[5] > 0:
                changes[10] -= 1
                changes[5] -= 1
                return
            if changes[5] > 2:
                changes[5] -= 3
            
        
        for bill in bills:
            if bill == 5:
                changes[5] += 1
                continue
            if bill == 10:
                if changes[5] == 0:
                    return False
                changes[10] += 1
                changes[5] -= 1
                continue
            
            assert bill == 20
            if can_give_15():
                give_15()
            else:
                return False
        return True

s = Solution()
#print(s.lemonadeChange([5,5,5,5,20,20,5,5,20,5]))
# print(s.lemonadeChange([5,5,5,10,5,20,5,10,5,20]))
# print(s.lemonadeChange([5,5,5,5,10,5,20,10,5,5]))
print(s.lemonadeChange([5,5,5,5,10,5,20,10,5,5]))

