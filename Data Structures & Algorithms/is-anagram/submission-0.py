class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash={}
        t_hash={}
        for letter in s:
            if letter in s_hash:
                s_hash[letter]+=1
            else:
                s_hash[letter]=1
        for letter in t:
            if letter in t_hash:
                t_hash[letter]+=1
            else:
                t_hash[letter]=1
            
        
        if s_hash==t_hash:
            return True
        else:
            return False

