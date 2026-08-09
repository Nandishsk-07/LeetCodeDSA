class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        m, n = len(word1), len(word2)   
        last = [-1] * (n + 1)
        last[n] = m   
        curr = m - 1
        for j in xrange(n - 1, -1, -1):
            curr = min(curr, last[j + 1] - 1)
            while curr >= 0 and word1[curr] != word2[j]:
                curr -= 1
            last[j] = curr
            curr -= 1   
        seq = []
        i = 0
        used_mismatch = False 
        for j in xrange(n):
            while i < m:
                if word1[i] == word2[j]:
                    seq.append(i)
                    i += 1
                    break
                else:
                    if not used_mismatch and last[j + 1] > i:
                        seq.append(i)
                        used_mismatch = True
                        i += 1
                        break
                    else:
                        i += 1
        return seq if len(seq) == n else []