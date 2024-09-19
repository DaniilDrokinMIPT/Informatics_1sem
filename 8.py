n = int(input())
a = list(map(int, input().split()))
for element in a:
    count = 0
    for x in a:
        if x < element:
            count += 1
    if count == len(a) // 2:
        print(element)
        break
