class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def removeSign(local_name):
            if '.' not in local_name and '+' not in local_name:
                return local_name
            name = ''
            for c in local_name:
                if c == '+': break
                if c == '.': continue
                name += c
            return name
        
        filtered = set()
        for e in emails:
            local_name, domain_name = e.split('@')
            local_name = removeSign(local_name)
            filtered.add(local_name + '@' + domain_name)
        
        return len(filtered)
            
            