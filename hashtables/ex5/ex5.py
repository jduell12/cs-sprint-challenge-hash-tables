
def finder(files, queries):
    hash_tbl = {}
        
    for file in files:
        #only need last item in path name
        part = file.split('/')[-1]

        if part in hash_tbl:
            hash_tbl[part].append(file)
        else:
            hash_tbl[part] = [file]
    
    file_queries = []
    
    for query in queries:
        if query in hash_tbl:
            file_queries += hash_tbl[query]

    return file_queries


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
