class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = []
        for s in strs:
            m = {}
            if len(s) == 0:
                m['-a'] = -1
                mapper.append(m)
                continue
            for ch in s:
                m[ch] = m.get(ch, 0) + 1
            mapper.append(m)
        print(mapper)
        visited = [0] * len(strs)
        result = []
        for i in range(len(strs)):
            if visited[i]: continue
            temp = [strs[i]]
            visited[i] = 1
            for j in range(i + 1, len(strs)):
                if visited[j]: continue
                check = 1
                for key, value in mapper[i].items():
                    print(key, value)
                    if value != mapper[j].get(key, 0):
                        print(1)
                        check = 0
                        break
                if check:
                    temp.append(strs[j])
                    visited[j] = 1
            result.append(temp)
        return result
        
