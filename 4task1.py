#task1
n=int(input("Enter a number: "))
def factorial(n): 
    if n<=1 :
        f=1
        return f
         
    else:
        f=n*factorial(n-1)
        return f
          
a=factorial(n)
print("Factorial of ",n, "is: ",a)   

