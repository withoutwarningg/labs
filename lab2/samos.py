def only_one_less_than_45(a, b, c):
    count = 0

    if a < 45:
        count += 1
    if b < 45:
        count += 1
    if c < 45:
        count += 1

    return count == 1


A = 50
B = 30
C = 60

result = only_one_less_than_45(A, B, C)
print(result)