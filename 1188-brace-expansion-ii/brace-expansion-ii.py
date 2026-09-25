class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        stack = []
        cur_union = set()
        cur_product = {""}
        for ch in expression:
            if ch.isalpha():
                cur_product = {word + ch for word in cur_product}
            elif ch == '{':
                stack.append((cur_union, cur_product))
                cur_union = set()
                cur_product = {""}
            elif ch == ',':
                cur_union |= cur_product
                cur_product = {""}
            elif ch == '}':
                inner_result = cur_union | cur_product
                prev_union, prev_product = stack.pop()
                cur_product = {p + w for p in prev_product for w in inner_result}
                cur_union = prev_union
        return sorted(list(cur_union | cur_product))
        