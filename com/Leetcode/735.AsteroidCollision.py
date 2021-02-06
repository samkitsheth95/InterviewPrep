from typing import List


class Solution:

    def asteroidCollisionClever(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                # when break is executed else dose not run
                # else will be executed when while is false
                # while running
                break
            else:
                ans.append(new)
        return ans

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if stack and stack[-1] > 0 and i < 0:
                discard = False
                while stack and stack[-1] > 0 and not discard:
                    top, x = abs(stack[-1]), abs(i)
                    if x >= top:
                        stack.pop()
                        if x == top:
                            discard = True
                    else:
                        discard = True
                if not discard:
                    stack.append(i)
            else:
                stack.append(i)
        return stack


sol = Solution()
print(sol.asteroidCollision(asteroids=[10, 2, -5]))
