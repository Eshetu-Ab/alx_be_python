# Define the height of the pyramid which is not part of project but challenging task on the module.Hence not pushed to gitHub.
rows = 10

# Initialize the row counter
row = 0

# Outer loop to control the number of rows
while row < rows:
    # Print leading spaces
    spaces = rows - row - 1
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    
    # Print asterisks
    stars = 2 * row + 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    
    # Move to the next row
    print()
    row += 1
