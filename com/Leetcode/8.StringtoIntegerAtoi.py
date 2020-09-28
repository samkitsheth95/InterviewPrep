class Solution:
    def myAtoi(self, str: str) -> int:
        intMax = 2147483647
        intMin = -2147483648
        for i in range(len(str)):
            if str[i] == " ":
                continue
            elif str[i] == '+' or str[i] == '-' or str[i].isdigit():
                num = 0
                sign = 1
                if str[i] == '+':
                    sign = 1
                    i += 1
                elif str[i] == '-':
                    sign = -1
                    i += 1
                while i < len(str) and str[i].isdigit():
                    num = num * 10 + (ord(str[i])-ord('0'))
                    i += 1
                    if num > intMax:
                        break
                return min(max(sign * num, intMin), intMax)
            else:
                return 0
        return 0


sol = Solution()
print(sol.myAtoi(" -42"))
