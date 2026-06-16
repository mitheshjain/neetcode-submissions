class Solution:
    def isValid(self, s: str) -> bool:
        q=deque()
        map={
            "}":"{",
            ")":"(",
            "]":"["
        }

        for c in s:
            if c not in map.keys():
                q.append(c)
            else:
                if not q:
                    return False
                else:
                    val = q.pop()
                    print(val)
                    if val!=map.get(c):
                        return False
        return False if q else True