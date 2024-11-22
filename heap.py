def heapify(a, n, i):
    mx = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[i] < a[l]:
        mx = l
    if r < n and a[mx] < a[r]:
        mx = r
    if mx != i:
        a[i], a[mx] = a[mx], a[i]
        heapify(a, n, mx)


def heapSort(a):
    n = len(a)
    for i in range(n//2, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


a = [14, 15, 5, 6, 9]
heapSort(a)
n = len(a)
for i in range(n):
    print(a[i], end=' ')
