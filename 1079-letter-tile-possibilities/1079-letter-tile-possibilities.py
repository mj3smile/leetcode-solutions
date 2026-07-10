class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        def track(index, curr, visited):
            if index in visited:
                return

            visited.add(index)
            curr = curr + tiles[index]
            for t in range(len(tiles)):
                if t in visited:
                    continue
                track(t, curr, visited)
            
            result.add(curr)
            visited.remove(index)
        
        for i in range(len(tiles)):
            track(i, "", set())
        # print(result)
        return len(result)
                