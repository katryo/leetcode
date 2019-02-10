from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        equals = defaultdict(set)
        not_equals = defaultdict(set)
        graph = {"==": equals, "!=": not_equals}

        def parse_equation(equation):
            # ex: ("==", "a", "b")
            return equation[1:3], equation[0], equation[3]

        nodes = set()

        for equation in equations:
            relation, left, right = parse_equation(equation)
            graph[relation][left].add(right)
            graph[relation][right].add(left)
            nodes.add(left)
            nodes.add(right)

        colors = {}

        # Returns False if the graph contradicts
        def dfs(start, cur_color):
            if start in colors:
                return
            colors[start] = cur_color
            same_color_nodes = graph['=='][start]
            for same_color_node in same_color_nodes:
                dfs(same_color_node, cur_color)

        for i, node in enumerate(nodes):
            dfs(node, i)

        for key in graph['!=']:
            for value in graph['!='][key]:
                if value in colors and key in colors and colors[value] == colors[key]:
                    return False
        return True


# s = Solution()
# print(s.equationsPossible(["a==b","b==a"]))
# print(s.equationsPossible(["a==b","b!=a"]))
# print(s.equationsPossible(["a==b","b==c","a==c"]))
# print(s.equationsPossible(["a==b","b!=c","c==a"]))
# print(s.equationsPossible(["c==c","b==d","x!=z"]))
