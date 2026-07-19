class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replacements_map = {text: text}
        for k, v in replacements:
            replacements_map[k] = v
        
        def resolve(k):
            parts = list()
            i = 0
            r = replacements_map[k]
            while i < len(r):
                part = ""
                if r[i] == "%":
                    i += 1
                    var_key = ""
                    while i < len(r) and r[i] != "%":
                        var_key += r[i]
                        i += 1
                    part = resolve(var_key)
                    i += 1
                else:
                    while i < len(r) and r[i] != "%":
                        part += r[i]
                        i += 1
                parts.append(part)
            
            replacements_map[k] = "".join(parts)
            return replacements_map[k]

        return resolve(text)
            
