class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        d = {')':'(','}':'{',']':'['}
        st = collections.deque()
        for bracket in s:
            if bracket in ('(','{','['):
                st.append(bracket)
            else:
                if st:
                    if st.pop() != d[bracket]:
                        return False
                else:
                    if bracket not in ('(','{','['):
                        return False
            # print(st)
        # print('next')
        if st:
            # print('s is not empty')
            return False
        return True
                