# Let's say we have the number 1234, and we want to reverse it, which means we want to make it 4321. Here's how we can do it step by step:

# Start with an empty result: We'll start with an empty result, which is just a number with no digits. Let's call it reversed_num, and for now, it's 0.

# Take the last digit of the original number: We start with the rightmost digit of the original number, which is 4 in our example.

# Add the last digit to the reversed number: We take the 4 from the original number and add it to the right side of our reversed_num. So now, reversed_num is 4.

# Remove the last digit from the original number: Now, we remove the 4 from the original number, and it becomes 123.

# Repeat the process: We go back to step 2 and repeat the process. We take the last digit of the new original number, which is 3.

# Add it to the reversed number: We add 3 to the right side of our reversed_num, so it becomes 43.

# Remove the last digit from the original number: We remove the 3 from the original number, and it becomes 12.

# Repeat again: We go back to step 2 again and take the last digit, which is 2.

# Add it to the reversed number: We add 2 to the right side of our reversed_num, so it becomes 432.

# Remove the last digit from the original number: We remove the 2 from the original number, and it becomes 1.

# Repeat one last time: We take the last digit, which is 1.

# Add it to the reversed number: We add 1 to the right side of our reversed_num, so it becomes 4321.

# Remove the last digit from the original number: We remove the 1 from the original number, and it becomes 0.

# Now, the original number is empty, and our reversed_num is 4321, which is the reverse of the original number, 1234. We're done!



# Input the original number
original_number = int(input("Enter a number: "))

given_number = original_number

# Start with an empty result
reversed_num = 0

# Repeat the process until the original number becomes empty
while original_number > 0:
    # Take the last digit of the original number
    last_digit = original_number % 10
    
    # Add it to the reversed number
    reversed_num = (reversed_num * 10) + last_digit
    
    # Remove the last digit from the original number
    original_number = original_number // 10

# Print the reversed number
print("Reversed number:", reversed_num)


if(given_number == reversed_num):
    print("Palindrome Number")
else:
    print("Is Not a Palindrome Number")
