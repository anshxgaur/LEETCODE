class Solution(object):
    def numUniqueEmails(self, emails):

        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            normalized = local + '@' + domain
            unique.add(normalized)
        return len(unique)
