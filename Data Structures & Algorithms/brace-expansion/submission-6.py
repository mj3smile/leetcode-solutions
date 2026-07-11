import string
class Solution:
    def expand(self, s: str) -> List[str]:
        lowercase_letters = set(string.ascii_lowercase)

        i = 0
        normalized_s = []
        while i < len(s):
            if s[i] == "{":    
                group = set()
                while s[i] != "}":
                    if s[i] in lowercase_letters:
                        group.add(s[i])
                    i += 1

                normalized_s.append(sorted(list(group)))
            else:
                normalized_s.append([s[i]])
            
            i += 1
        
        
        result = list()
        def construct(index, progress):
            if index == len(normalized_s):
                result.append("".join(progress))
                return

            for c in normalized_s[index]:
                progress.append(c)
                construct(index + 1, progress)
                progress.pop()
        
        construct(0, [])
        return result