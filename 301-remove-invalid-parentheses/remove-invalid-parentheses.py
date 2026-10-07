class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        rem_left = 0
        rem_right = 0
        for ch in s:
            if ch == '(':
                rem_left += 1
            elif ch == ')':
                if rem_left > 0:
                    rem_left -= 1
                else:
                    rem_right += 1           
        result = set()
        path = []
        n = len(s)
        def backtrack(idx: int, l_rem: int, r_rem: int, open_bal: int):
            if open_bal < 0:
                return
            if idx == n:
                if l_rem == 0 and r_rem == 0 and open_bal == 0:
                    result.add("".join(path))
                return
            ch = s[idx]
            if ch == '(' and l_rem > 0:
                backtrack(idx + 1, l_rem - 1, r_rem, open_bal)
            elif ch == ')' and r_rem > 0:
                backtrack(idx + 1, l_rem, r_rem - 1, open_bal)
            path.append(ch)
            if ch == '(':
                backtrack(idx + 1, l_rem, r_rem, open_bal + 1)
            elif ch == ')':
                backtrack(idx + 1, l_rem, r_rem, open_bal - 1)
            else:
                backtrack(idx + 1, l_rem, r_rem, open_bal)
            path.pop()
        backtrack(0, rem_left, rem_right, 0)
        return list(result)
        