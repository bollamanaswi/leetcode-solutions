class Solution(object):
    def maskPII(self, s):
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + '*****' + name[-1] + '@' + domain
        else:
            digits = ''
            for ch in s:
                if ch.isdigit():
                    digits += ch

            last = digits[-4:]

            if len(digits) == 10:
                return '***-***-' + last
            else:
                return '+' + '*' * (len(digits) - 10) + '-***-***-' + last