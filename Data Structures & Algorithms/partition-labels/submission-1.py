from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        freq = Counter(s)

        i = 0
        ans = []

        while i < len(s):

            new = {}
            j = i

            while True:

                new[s[j]] = new.get(s[j], 0) + 1

                if all(new[c] == freq[c] for c in new):
                    break

                j += 1

            ans.append(s[i:j+1])
            i = j + 1

        return [len(x) for x in ans]