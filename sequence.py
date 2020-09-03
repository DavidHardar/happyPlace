# Accept an input which determines the length of the sequence.
# Output the sequence.
# 1. Accept input
# 2. Use input to determine for how long the for loop will last.
# 3. take the sum of the last three numbers in the sequence.
# 4. Print the sequence.

n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 3
b = 2
c = 1
d = 0

for i in range(n):
    
    print_gildi = b+c+d
    a = print_gildi
    b,c,d = a,b,c
    

    print(print_gildi, end=' ')
    