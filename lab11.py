def main():
    print("This program illustrates a chaotic function after 10 iterations")
    line1 = float(input("Enter a number between 0 and 1: "))
    line2 = float(input("Enter another number between 0 and 1: "))
    index=0
    for i in range(10):
        line1 = 3.9 * line1 * (1 - line1)
        line2 = 3.9 * line2 * (1 - line2)
        index=index+1

        
        
        
        print 


main()
