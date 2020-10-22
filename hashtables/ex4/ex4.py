def has_negatives(a):
    hash = {}
    has_neg = []
    
    for num in a:
        #puts numbers in the list
        hash[num] = num
        #checks if the negative form of the number is in the hash
        if num != 0 and -num in hash:
            has_neg.append(abs(num))

    return has_neg


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))
