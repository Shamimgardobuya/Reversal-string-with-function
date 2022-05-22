def reversing(people):
    z=people[::-1]
    print(z)
# b=str(input("Enter a word"))
def greet(name):
    return f"Hello{name}"   
def greet_multiple(*names): # asterix tell interpreter that i don't know the length now iteration starts.
    for name in names:
          print(f"Hello {name}")
          
