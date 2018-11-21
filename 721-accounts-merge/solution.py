from collections import defaultdict

class DSU:
    def __init__(self, size):
        self.par = list(range(size))

    def find(self, id):
        if self.par[id] == id:
            return id
        ret = self.find(self.par[id])
        self.par[id] = ret
        return ret

    def union(self, ida, idb):
        self.par[self.find(ida)] = self.par[self.find(idb)]


class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(set)
        email_name = {}

        for account in accounts:
            name, emails = account[0], account[1:]
            email_name[emails[0]] = name
            for i in range(1, len(emails)):
                graph[emails[i-1]].add(emails[i])
                graph[emails[i]].add(emails[i-1])
                email_name[emails[i]] = name

        ans = []
        seen = set()
        for email in email_name:
            if email in seen:
                continue
            seen.add(email)
            stack = [email]
            component = [email]
            while stack:
                cur = stack.pop()
                for nei in graph[cur]:
                    if nei in seen:
                        continue
                    seen.add(nei)
                    stack.append(nei)
                    component.append(nei)
            ans.append([email_name[email]] + sorted(component))
        return ans


    # def accountsMerge(self, accounts):
    #     """
    #     :type accounts: List[List[str]]
    #     :rtype: List[List[str]]
    #     """
    #
    #     user_id = 0
    #     user_id_username = {}  # user_id: username
    #     user_id_email = defaultdict(set)
    #     email_user_ids = defaultdict(set)  # email: user_id
    #
    #     dsu = DSU(len(accounts))
    #
    #     for account in accounts:
    #         name, emails = account[0], account[1:]
    #         user_id_username[user_id] = name
    #         for email in emails:
    #             user_id_email[user_id].add(email)
    #             email_user_ids[email].add(user_id)
    #         user_id += 1
    #
    #     for email in email_user_ids:
    #         user_ids = list(email_user_ids[email])
    #         for i in range(1, len(user_ids)):
    #             dsu.union(user_ids[i-1], user_ids[i])
    #
    #     united_useremail = defaultdict(set)
    #     for uid in range(user_id):
    #         real_uid = dsu.find(uid)
    #         united_useremail[real_uid].update(user_id_email[uid])
    #
    #     ans = []
    #     for real_uid in united_useremail:
    #         ansitem = [user_id_username[real_uid]] + sorted(list(united_useremail[real_uid]))
    #         ans.append(ansitem)
    #
    #     return ans


# s = Solution()
# print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))
# print(s.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))