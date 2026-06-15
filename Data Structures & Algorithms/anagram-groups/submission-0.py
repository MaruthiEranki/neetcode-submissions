class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        groupList = []
        for eachWord in strs:
            orderedKey = ''.join(map(str, sorted(eachWord)))
            if orderedKey in wordDict:
                wordDict[orderedKey].append(eachWord)
            else:
                wordDict[orderedKey] = [eachWord]
                
        for eachKey in wordDict:
            print(eachKey)
            groupList.append(wordDict[eachKey])

        return groupList

        