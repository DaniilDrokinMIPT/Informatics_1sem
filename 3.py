def zerk(n):
    for x in range(len(n) // 2 + 1):
        if n[x] in ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8'] and n[len(n) - 1 - x] != n[x]:
            return False
        if n[x] == 'E'  and n[len(n) - 1 - x] != '3':
            return False
        if n[x] == 'J'  and n[len(n) - 1 - x] != 'L':
            return False
        if n[x] == 'S'  and n[len(n) - 1 - x] != '2':
            return False
        if n[x] == 'Z'  and n[len(n) - 1 - x] != '5':
            return False
        if n[x] == '3'  and n[len(n) - 1 - x] != 'E':
            return False
        if n[x] == 'L'  and n[len(n) - 1 - x] != 'J':
            return False
        if n[x] == '2'  and n[len(n) - 1 - x] != 'S':
            return False
        if n[x] == '5'  and n[len(n) - 1 - x] != 'Z':
            return False
        if n[x] not in ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8', 'E', 'J', 'S', 'Z', '3', 'L', '2', '5']:
            return False
    return True


def pal(n):
    if n[::-1] == n:
        return True
    return False


s = input()
if pal(s) and zerk(s):
    print(f"{s} is a mirrored palindrome.")
elif zerk(s) and not pal(s):
    print(F"{s} is a mirrored string.")
elif pal(s) and not zerk(s):
    print(f"{s} is a regular palindrome.")
else:
    print(f"{s} is not a palindrome.")