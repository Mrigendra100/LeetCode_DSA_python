def pyramid(n):
    """Print a pyramid of stars with n rows."""
    print("Pyramid Pattern:")
    for i in range (1, n+1):
        
        for _ in range( n- i ):
            print(" " , end="")
        
            
            
        for _ in range( 2*i -1):
            print("*" , end="")
        
        print()
    # print()

def rectangle(rows, cols):
    """Print a solid rectangle of stars."""
    print("Rectangle Pattern:")
    for _ in range(rows):
        for _ in range(cols):
            print("*", end=" ")
        print()
    print()

def diamond(n):
    """Print a diamond pattern of stars with n rows."""
    print("Diamond Pattern:")
    for i in range(1, n + 1):
        for _ in range(n-i):
            print(" ", end="")
        for _ in range(2*i -1):
            print("*", end="")
        print()
    for i in range(n-1 ,0 , -1):
        for _ in range(n-i):
            print(" ", end="")
        for _ in range(2*i -1):
            print("*", end="")
        print()


# rectangle(10,12)        
# pyramid(10)
diamond(10)