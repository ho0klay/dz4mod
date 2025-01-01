a = [5, 10, 12, 16, 25, 40, 67, 50]
print(a)

value = int(input('Введите число: '))

left = 0
right = len(a) - 1
center = (left + right) // 2

while a[center] != value:
    if value > a[center]:
        left = center + 1
    else:
        right = center - 1
    center = (left + right) // 2
    if left >= right:
        break

if value == a[center]:
    print('ID =', center)
else:
    print('No value')
