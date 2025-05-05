rows = 2
left = [3, 5]
right = [3, 5]
spaces = [3, 1]

for i in range(rows):
    print(" " * ((5 - left[i]) // 2) + "*" * left[i] + " " * spaces[i] + "*" * right[i])

# for lower reversed pyramid
for i in range(6,0,-1):
    print(" "*(6-i) + "*"*(2*i-1))
