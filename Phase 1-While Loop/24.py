'''24. Print all factors of the given number.'''

# n = int(input("Enter a number: "))
# print("Factors of", n, "are:")
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)
        
        
#------------------------------optimised------------------------

n = int(input("Enter a number: "))
print("Factors of", n, "are:")

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        print(i)
        if i != n // i:
            print(n // i)