def toLowerCase(self, s: str) -> str:
        s = list(s)
        
        for i in range(len(s)):
            if ord(s[i]) <= 90 and ord(s[i]) >= 65:
                s[i] = chr(ord(s[i])+32)
        return ''.join(s)