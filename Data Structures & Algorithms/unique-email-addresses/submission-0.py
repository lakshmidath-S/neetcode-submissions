class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a=set()
        for i in emails:
            local,domain=i.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            normal=local+"@"+domain
            a.add(normal)
        return len(a)
