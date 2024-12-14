a, b, c = map(int,input().split())
d, e, f = map(int,input().split())
print(abs(((a * 60 * 60) + (b * 60) + c) - ((d * 60 * 60) + (e * 60) + f)))