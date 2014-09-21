def evenlyDivisible(n):
    counter = 0
    for i in range(1, 21):
        if n % i == 0:
            counter = counter + 1
            if counter == 20:
                return n
        else:
            return 1
 
def main():
    start_time = time.clock()
    n = 2520
    switch = 1
    while switch == 1:
        smallest = evenlyDivisible(n)
        if smallest != 1:
            print smallest
            switch = 0
        else:
            n += 2520
    run_time = time.clock() - start_time
    print "Run time = ", run_time
     
if __name__ == '__main__':
    main()
