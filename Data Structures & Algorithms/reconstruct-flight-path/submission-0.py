class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # [[A,C],[C,A],[A,B]]
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        # A:[C, B], B:[], C:[A]
        route = []

        def dfs(airport: str):
            while adj[airport]:
                next_stop = adj[airport].pop()
                dfs(next_stop)
            route.append(airport)
        # dfs("A") will call dfs(B) first. Route appends B first
        # then dfs(A) call dfs(C), ...
        dfs("JFK")
        return route[::-1]