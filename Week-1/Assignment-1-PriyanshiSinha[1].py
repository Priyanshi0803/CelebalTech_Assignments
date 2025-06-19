rows = 5

# Left-Aligned Lower Triangular
print("Left-Aligned Lower Triangular:")
for i in range(1, rows + 1):
    print("* " * i)

# Left-Aligned Upper Triangular
print("\nLeft-Aligned Upper Triangular:")
for i in range(rows, 0, -1):
    print("* " * i)

# Centered Pyramid
print("\nCentered Pyramid:")
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)

# Right-Aligned Lower Triangular Pa
print("\nRight-Aligned Lower Triangular:")
for i in range(1, rows + 1):
    spaces = "  " * (rows - i) 
    stars = "* " * i
    print(spaces + stars)

# Right-Aligned Upper Triangular Pattern
print("\nRight-Aligned Upper Triangular:")
for i in range(rows, 0, -1):
    spaces = "  " * (rows - i)
    stars = "* " * i
    print(spaces + stars)
