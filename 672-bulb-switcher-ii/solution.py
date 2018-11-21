from itertools import product


class Solution:
    def flipLights(self, n, m):
        seen = set()
        for cand in product((0, 1), repeat=4):
            if sum(cand) % 2 == m % 2:
                if m >= sum(cand):
                    lights = []
                    for i in range(min(n, 3)):
                        light = 1
                        light ^= cand[0]
                        light ^= cand[1] and i % 2 == 1
                        light ^= cand[2] and i % 2 == 0
                        light ^= cand[3] and i % 3 == 0
                        lights.append(light)
                    seen.add(tuple(lights))
        return len(seen)

    # def flipLights(self, n, m):
    #     """
    #     :type n: int
    #     :type m: int
    #     :rtype: int
    #     """
    #
    #     if m > 4:
    #         if m % 2 == 1:
    #             m = 3
    #         else:
    #             m = 4
    #
    #     def flipped(x):
    #         if x:
    #             return 0
    #         return 1
    #
    #     def flip_all(lights):
    #         for a in range(len(lights)):
    #             lights[a] = flipped(lights[a])
    #
    #     def flip_even(lights):
    #         for a in range(len(lights)):
    #             if a % 2 == 0:
    #                 lights[a] = flipped(lights[a])
    #
    #     def flip_odd(lights):
    #         for a in range(len(lights)):
    #             if a % 2:
    #                 lights[a] = flipped(lights[a])
    #
    #     def flip_3k(lights):
    #         for a in range(len(lights)):
    #             if (a+1) % 3 == 1:
    #                 lights[a] = flipped(lights[a])
    #
    #     if m == 4:
    #         ans = {'1' * min(n, 6)}
    #         for i in range(2):
    #             for j in range(2):
    #                 for k in range(2):
    #                     for l in range(2):
    #                         lights = [1] * min(n, 6)
    #                         if i: flip_all(lights)
    #                         if j: flip_even(lights)
    #                         if k: flip_odd(lights)
    #                         if l: flip_3k(lights)
    #                         ans.add(''.join(str(num) for num in lights))
    #         return len(ans)
    #
    #     if m == 3:
    #         ans = set()
    #         for i in range(2):
    #             for j in range(2):
    #                 for k in range(2):
    #                     lights = [1] * min(n, 6)
    #                     if i: flip_all(lights)
    #                     if j: flip_even(lights)
    #                     if k: flip_odd(lights)
    #                     ans.add(''.join(str(num) for num in lights))
    #         for i in range(2):
    #             for j in range(2):
    #                 for l in range(2):
    #                     lights = [1] * min(n, 6)
    #                     if i: flip_all(lights)
    #                     if j: flip_even(lights)
    #                     if l: flip_3k(lights)
    #                     ans.add(''.join(str(num) for num in lights))
    #         for i in range(2):
    #             for k in range(2):
    #                 for l in range(2):
    #                     lights = [1] * min(n, 6)
    #                     if i: flip_all(lights)
    #                     if k: flip_odd(lights)
    #                     if l: flip_3k(lights)
    #                     ans.add(''.join(str(num) for num in lights))
    #         for j in range(2):
    #             for k in range(2):
    #                 for l in range(2):
    #                     lights = [1] * min(n, 6)
    #                     if j: flip_even(lights)
    #                     if k: flip_odd(lights)
    #                     if l: flip_3k(lights)
    #                     ans.add(''.join(str(num) for num in lights))
    #         return len(ans)
    #
    #     def check_two(a, b):
    #         lights = [1] * min(n, 6)
    #         if a == 0:
    #             flip_all(lights)
    #         if a == 1 or b == 1:
    #             flip_even(lights)
    #         if a == 2 or b == 2:
    #             flip_odd(lights)
    #         if b == 3:
    #             flip_3k(lights)
    #
    #         ans.add(''.join(str(num) for num in lights))
    #
    #     if m == 2:
    #         ans = {'1' * min(n, 6)}
    #         check_two(0, 1)
    #         check_two(0, 2)
    #         check_two(0, 3)
    #         check_two(1, 2)
    #         check_two(1, 3)
    #         check_two(2, 3)
    #         return len(ans)
    #
    #     if m == 1:
    #         ans = set()
    #         lights = [1] * min(n, 6)
    #         flip_all(lights)
    #         ans.add(''.join(str(n) for n in lights))
    #
    #         lights = [1] * min(n, 6)
    #         flip_even(lights)
    #         ans.add(''.join(str(n) for n in lights))
    #
    #         lights = [1] * min(n, 6)
    #         flip_odd(lights)
    #         ans.add(''.join(str(n) for n in lights))
    #
    #         lights = [1] * min(n, 6)
    #         flip_3k(lights)
    #         ans.add(''.join(str(n) for n in lights))
    #
    #         return len(ans)
    #     return 1


# s = Solution()
# print(s.flipLights(3, 4))
# print(s.flipLights(2, 2))
# print(s.flipLights(1, 0))
# print(s.flipLights(3, 2))
# print(s.flipLights(5, 3))
# print(s.flipLights(1, 1))
# print(s.flipLights(2, 1))
# print(s.flipLights(3, 1))
# print(s.flipLights(3, 1))
