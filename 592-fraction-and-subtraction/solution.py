from math import gcd

class Solution:
    def fractionAddition(self, expression):
        results = [[-0, 1]]
        cur = []
        num = ''
        for i in range(len(expression) - 1, -1, -1):
            if expression[i].isnumeric():
                num = expression[i] + num
                if i == 0:
                    cur.insert(0, int(num))
                    results.insert(0, cur)
            if expression[i] == '/':
                cur.insert(0, int(num))
                num = ''
            if expression[i] == '+':
                cur.insert(0, int(num))
                results.insert(0, cur)
                num = ''
                cur = []
            if expression[i] == '-':
                cur.insert(0, - int(num))
                results.insert(0, cur)
                num = ''
                cur = []

        # a: 20, b: 5
        def lcm(a, b):
            # 5
            ab_gcd = gcd(a, b)
            return a * b // ab_gcd

        lcm_den = 1
        for i in range(len(results)):
            lcm_den = lcm(lcm_den, results[i][1])

        nume = 0
        for i in range(len(results)):
            nume += results[i][0] * lcm_den // results[i][1]

        if nume == 0:
            return '0/1'
        num_den_gcd = gcd(nume, lcm_den)
        return '%d/%d' % (nume // num_den_gcd, lcm_den // num_den_gcd)


s = Solution()
print(s.fractionAddition("-1/2+1/2"))
print(s.fractionAddition("-1/2+1/2+1/3"))



    # def fractionAddition(self, expression):
    #     """
    #     :type expression: str
    #     :rtype: str
    #     """
    #     results = [[-0, 1]]
    #     cur = []
    #     num = ''
    #     for i in range(len(expression) - 1, -1, -1):
    #         if expression[i].isnumeric():
    #             num = expression[i] + num
    #             if i == 0:
    #                 cur.insert(0, int(num))
    #                 results.insert(0, cur)
    #         if expression[i] == '/':
    #             cur.insert(0, int(num))
    #             num = ''
    #         if expression[i] == '+':
    #             cur.insert(0, int(num))
    #             results.insert(0, cur)
    #             num = ''
    #             cur = []
    #         if expression[i] == '-':
    #             cur.insert(0, - int(num))
    #             results.insert(0, cur)
    #             num = ''
    #             cur = []
    #     print(results)
    #     den = 1
    #     for elem in results:
    #         den *= elem[1]
    #     nume = 0
    #     for i, elem in enumerate(results):
    #         nume += elem[0] * den // elem[1]
    #
    #     if nume == 0:
    #         return '0/1'
    #
    #     for i in range(2, 100):
    #         while nume % i == 0 and den % i == 0:
    #             nume //= i
    #             den //= i
    #
    #     return str(nume) + '/' + str(den)

