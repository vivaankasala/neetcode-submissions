class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic={}
        for word in strs:
            sorted_str= ''.join(sorted(word))
            if sorted_str not in anagram_dic:
                anagram_dic[sorted_str]=[]
            
            anagram_dic[sorted_str].append(word)
        return list(anagram_dic.values())
            


