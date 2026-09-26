class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        knowledge_dict = {k: v for k, v in knowledge}
        result = []
        cur_key = []
        inside = False
        for ch in s:
            if ch == '(':
                inside = True
            elif ch == ')':
                key_str = "".join(cur_key)
                result.append(knowledge_dict.get(key_str, '?'))
                cur_key = []
                inside = False
            else:
                if inside:
                    cur_key.append(ch)
                else:
                    result.append(ch)
        return "".join(result)
        