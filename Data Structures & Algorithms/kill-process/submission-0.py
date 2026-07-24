class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child = dict()

        for i in range(len(pid)):
            p = ppid[i]
            child[p] = child.get(p, list())
            child[p].append(pid[i])
        
        result = [kill]
        def findChilds(p):
            for c in child.get(p, list()):
                result.append(c)
                findChilds(c)
        
        findChilds(kill)
        return result