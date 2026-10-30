class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            sortedstring=''.join(sorted(s))
            if sortedstring not in dic:
                dic[sortedstring]=[]
            dic[sortedstring].append(s)

        return list(dic.values())
            

    

        