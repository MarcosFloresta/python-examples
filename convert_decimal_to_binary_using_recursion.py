# Function to print binary number using recursion
def convert_to_binary(n):
   if n > 1:
       convert_to_binary(n//2)
   print(n % 2, end='')

# decimal number
dec = 34
convert_to_binary(dec)