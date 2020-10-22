def get_indices_of_item_weights(weights, length, limit):
    table = {}
    
    #checks that table can actually have sums
    if len(weights) <= 1:
        return None
    
    #adds each weight as the key with the index as the value in the hash table
    for index in range(0, length):
        if weights[index] not in table:
            table[weights[index]] = []
        #if duplicate numbers in weights have a list of indices that the numbers are located
        table[weights[index]].append(index)

    #finds the index of the numbers whose sum = limit
    sums = []
    for k in table:
        if limit - k in table:
            sums += (table[k])
    #tests want the list in descending order 
    sums.sort(reverse=True)
    
    return sums