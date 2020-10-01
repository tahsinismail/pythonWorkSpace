#python3
import time
#Defining list with predefined fibonacci sequence
sequence = [0,1]

#Defining function to generate the sequence
def fibonacciSequence(n):
    #Start time of the function
    start_time = time.time()
    for i in range(n):
        if i > 0 < n:
            newSequence = sequence[i-1] + sequence[i]
            sequence.append(newSequence)
            
    #Elapsed time during execution
    elapsed_time = time.time() - start_time
    
    return "FibonacciSequence: \n\n{}  \n\nexecuted in : {:.7f}".format(sequence, elapsed_time)

if __name__ == '__main__':

    while True: 
        try:
            #Accepting only a postive integer number
            input_n = int(input("Enter a postive integer number: ")) 
            assert(input_n  > 0)
            break 
        except:
            print('Please enter a valid integer number\nand number have to be greater than 0')

    print(fibonacciSequence(input_n))