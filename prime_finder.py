def prime_finder(n):
    lst = [] # Empty list to hold the prime numbers

    for i in range(2, (n + 1)): # Loop through the number. It is inclusive say 11
        # print(i, end=" ")
        # Output
        # 2 3 4 5 6 7 8 9 10 11

        # Loop through 2 3 4 5 6 7 8 9 10 11
        for j in range(2, i): # i is the input number for inner loop from the outer loop
            if i % j == 0:
                # Not prime number
                # Do nothing
                break
        else:
            # Prime number
            lst.append(i)
    return lst