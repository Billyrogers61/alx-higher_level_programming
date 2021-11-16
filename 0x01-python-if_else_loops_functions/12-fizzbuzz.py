'''
   fizbuzz - Function to check for multiples of 3 and 5.
   Return: mulitples 3 - 'Fizz'
           multiples 5 - "Buzz"
           multiples 3 & 5 - "FizzBuzz"
'''
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=' ')
        elif num % 5 == 0:
            print("Buzz", end=' ')
        elif num % 3 == 0:
            print("Fizz", end=' ')
        else:
            print(num, end=' ')
