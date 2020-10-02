def get_indices_of_item_weights(weights, length, limit):
    table = {}
    
    for index in range(length):
        table[weights[index]] = index
        
    print(table)

    if limit in table:
        return table[limit]
    else:
        sums = []
        for k in table:
            if limit - k in table:
                sums.append(table[k])
        return sums 

if __name__ == "__main__":
    # weights = [ 4, 6, 10, 15, 16 ]
    # length = 5
    # limit = 21
    # #[3, 1] --> indices of weights whose sum = 21
    # print(get_indices_of_item_weights(weights, length, limit))
    
    weights_2 = [4, 4]
    print(get_indices_of_item_weights(weights_2, 2, 8))