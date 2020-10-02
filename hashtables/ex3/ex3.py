def intersection(arrays):
    freq = {}
    
    for array in arrays:
        for num in array:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
    
    freq_list = list(freq.items())
    freq_list.sort(key=lambda t:t[1], reverse=True)
    
    iter = []
    
    for i in range(len(freq_list)):
        if freq_list[i][1] == len(arrays):
            iter.append(freq_list[i][0])
        else:
            break
    
    return iter



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
