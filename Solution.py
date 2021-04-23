def decode(b, x):
    try:
        return int(str(x), b)
    except:
        return None

cnt = {}

n = int(input())
for _ in range(n):
    b, x = map(int, input().split())
    val = decode(b, x)
    if val != None:
        cnt[val] = cnt.get(val, 0) + 1

ans = sum(x * (x - 1) // 2 for x in cnt.values())
print(ans)
