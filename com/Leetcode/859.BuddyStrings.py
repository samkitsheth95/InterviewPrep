def buddyStrings(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    if A == B:
        return len(A) - len(set(A)) >= 1
    sum = 0;
    for i in range(len(A)):
        if A[i] != B[i]:
            sum += 1
            if sum == 1:
                a = A[i]
                b = B[i]
            if sum == 2:
                if A[i] != b or B[i] != a:
                    return False
        if sum > 2:
            return False
    return sum == 2
print(buddyStrings("acccccb","bccccca"))
