class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = list()

        i = 0
        while i < len(path):
            if path[i] == "/":
                i += 1
                continue
            # elif path[i] == ".":
            #     dots = ""
            #     while i < len(path):
            #         if path[i] == "/":
            #             break
            #         dots += path[i]
            #         i += 1
            #     if len(dots) > 2:
            #         dirs.append(dots)
            #     elif len(dots) == 2 and dirs:
            #         dirs.pop()
            else:
                dirName = ""
                while i < len(path) and path[i] != "/":
                    dirName += path[i]
                    i += 1
                
                if dirName == "..":
                    if dirs: dirs.pop()
                elif dirName != ".":
                    dirs.append(dirName)
        
        return "/" + "/".join(dirs)