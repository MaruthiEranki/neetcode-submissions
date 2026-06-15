class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ord_dict = {}
        res_list = []
        for each_str in strs:
            sorted_str = ''.join(sorted(each_str))
            if (sorted_str in ord_dict):
                res_list[ord_dict[sorted_str]].append(each_str)
            else:
                ord_dict[sorted_str] = len(res_list)
                res_list.append([each_str])
        return res_list