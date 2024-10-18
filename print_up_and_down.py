def print_up_and_down(n):
    if n == 0:
        return 0
    print(n)              
    print_up_and_down(n-1)
    print(n)     
   
