class Solution:

    def encode(self, strs: list[str]) -> str:
        res: str = ""
        for s in strs: 
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> list[str]: 
        res: list[str] = [] 
        i: int = 0 

        while i < len(s):
            j: int = i 

            while s[j] != "#":
                j += 1
            
            length: int = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length 
        
        return res