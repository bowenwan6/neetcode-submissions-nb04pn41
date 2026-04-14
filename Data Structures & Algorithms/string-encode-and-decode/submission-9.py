class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        idxs, res = [], ""
        for s in strs:
            idxs.append(len(s))
        for idx in idxs:
            res += str(idx) + ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:  # Corrected check
            return []
        
        idxs, res = [], []
        temp = ""
        for c in s:
            if c == '#':
                if temp:  # Only append if temp is not empty
                    idxs.append(int(temp))
                break
            elif c == ',':
                if temp:  # Avoid appending empty values
                    idxs.append(int(temp))
                    temp = ""
            else:
                temp += c

        i = s.find('#') + 1
        for idx in idxs:
            res.append(s[i:i+idx])  # Extract substring correctly
            i += idx
        return res