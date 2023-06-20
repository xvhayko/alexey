def solution(s, t):
    k = min(s // 3, (t - 1) // 2)
    return s*t + s + s*k - 3*k*(k+1)//2