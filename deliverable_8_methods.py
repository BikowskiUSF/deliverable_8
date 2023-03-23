import numpy as np
# deliverable 8
# Method 1 Randomly populate a list with integer numbers between range of 10 and 50
def generate_list(length):
    lst = np.random.randint(10, 51, length)
    return lst.tolist()

# Method 2 Returns the summation of all the elements of a list
def sum_list(lst):
    return sum(lst)

# Ask user for number between 5 and 15
valid_input = False
while not valid_input:
    num = int(input("Enter a number between 5 and 15: "))
    if num >= 5 and num <= 15:
        valid_input = True
    else:
        print("Invalid input. Please try again.")

# Generate a list and print its elements
lst = generate_list(num)
print("The elements of the array are:", end=" ")
for i in lst:
    print(i, end=" ")

# Calculate and print the sum of all list elements
total = sum_list(lst)
print("\nThe sum is:", total)
