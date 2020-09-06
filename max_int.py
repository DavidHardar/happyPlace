# Our program should accept as many positive integers as it takes before our user inputs a negative integer.
# Our program should output the biggest integer of the ones that were input.
# 1. Accept inital input.
# 2. Use a while loop to accept a new input.
# 3. If input is larger than previous replace max_int.
# 4. If input is bigger or is equal to zero go back to step 2.
# 5. If input is smaller than 0 print the largest number.

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while num_int >= 0:
    max_int = max(num_int, max_int)
    num_int = int(input("Input a number: "))   
    
print("The maximum is", max_int)    # Do not change this line
