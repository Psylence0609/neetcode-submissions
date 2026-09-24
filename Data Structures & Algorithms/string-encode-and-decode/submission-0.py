class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        # print(",".join(sizes) + '#' + ''.join(strs))
        return ",".join(sizes) + '#' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        strs = ''
        for i, ch in enumerate(s):
            if ch == '#':
                sizes = [int(x) for x in s[:i].split(',')]
                strs = s[i + 1:]
                # print(i, sizes)
                break

        res = []
        begin = 0
        for l in sizes:
            res.append(strs[begin:begin + l])
            begin += l
        return res