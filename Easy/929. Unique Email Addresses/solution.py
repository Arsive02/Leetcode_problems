class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in emails:
            x,y = i.split('@')
            p = ''
            for a in x:
                if a == '+':
                    break
                if a == '.':
                    continue
                p += a
            result = p + '@' + y
            s.add(result)
        return len(s)
