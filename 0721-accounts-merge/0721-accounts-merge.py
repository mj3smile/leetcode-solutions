class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ranks = dict()
        parent = dict()

        def getRootParent(a):
            if a not in parent:
                parent[a] = a
                return a   
            if parent[a] == a:
                return a
            parent[a] = getRootParent(parent[a])
            return parent[a]
        
        def getRanks(a):
            return ranks.get(a, 0)

        def merge(a1, a2):
            p1, p2 = getRootParent(a1), getRootParent(a2)
            if p1 == p2:
                return
            if getRanks(p1) > getRanks(p2):
                parent[p2] = p1
            elif getRanks(p1) < getRanks(p2):
                parent[p1] = p2
            else:
                parent[p2] = p1
                ranks[p1] = getRanks(p1) + 1
            
        for i in accounts:
            a1 = i[1]
            for j in range(1, len(i)):
                merge(a1, i[j])
        
        groups = dict()
        first_names = dict()
        for i in accounts:
            first_name = i[0]
            p = getRootParent(i[1])
            groups[p] = groups.get(p, {""})
            first_names[p] = first_name

            for j in range(1, len(i)):
                groups[p].add(i[j])
        
        result = list()
        for p, accounts in groups.items():
            a = sorted(list(accounts))
            a[0] = first_names[p]
            result.append(a)
        
        return result