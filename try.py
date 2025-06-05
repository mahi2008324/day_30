pattern = []  # 2D list for rows

for i in range(7):
    row = []
    
    # Letter K (6 columns)
    for j in range(6):
        if j == 0 or i + j == 3 or i - j == 3:
            row.append("K")
        else:
            row.append(" ")
    
    # Space between K and L (2 columns)
    row.append(" ")
    row.append(" ")
    
    # Letter L (4 columns)
    for j in range(4):
        if j == 0 or i == 6:
            row.append("L")
        else:
            row.append(" ")
    
    pattern.append(row)

# Now pattern is a list of lists (7 rows x 12 columns)
# Print the pattern:
for row in pattern:
    print(" ".join(row))
