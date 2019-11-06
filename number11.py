#This program sums up the "numeric value" of someones name
#By Arturo Ortiz
def main():
    #Gets information from the file names.txt
    
    fname= input("Enter filename: ")
    infile= open(fname, 'r')
    data= infile.read()
    outfile= open("output.txt", "w")
    
    namelst= data.split() #This will split all the names into individual values

                            #namelst= "arturo","tom","seb","zachary"

    for name in namelst:
        sum = 0
        for ch in name[:-1]:
            sum=sum+ord(ch)-96

        print(sum , file=outfile)        

#everytime it goes through the for loop it should add the value until there
#is no more items from list to go through
        
    infile.close()
    outfile.close()
    
        

main()
