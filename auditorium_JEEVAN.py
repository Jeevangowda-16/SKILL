print("theater seats\n")
H = int(input("Enter row size in auditorium:"))
L = 6
M = 10
R = 6
for i in range(H):
    left = '*' * L
    middle = '*' * M
    right = '*' * R

    print(left + '  ' + middle + '  ' + right)