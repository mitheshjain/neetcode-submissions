class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        all_keys = map.keys()
        stack = []
        for char in s:
            if char in all_keys:
                stack.append(char)
            else:
                if stack:
                    val = stack.pop()
                    if char != map[val]:
                        return False
                else:
                    return False
        return not stack