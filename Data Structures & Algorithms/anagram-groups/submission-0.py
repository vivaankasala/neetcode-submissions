class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping={}
        for words in strs:
            key=''.join(sorted(words))
            if key not in grouping:
                grouping[key]=[]
            grouping[key].append(words)


        return list(grouping.values())
