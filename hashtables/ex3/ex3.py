def intersection(arrays):
    freq = {}
    
    for array in arrays:
        for num in array:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
    

    return [key for key in freq if freq[key] == len(arrays)]



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
