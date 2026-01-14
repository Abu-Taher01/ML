# Goal: Write a generator to read a 'fake' 100 GB file line-by-line. 
# Deep dive: Using yield line allows you to process datasets larger than 
#            your machine's physical RAM. This is the standard for Big Data procesing in Python.

def chunk_reader(data,size):
    for i in range(0,len(data),size):
        yield data[i:i+size]


for chunk in chunk_reader("ABCDEFGHZK", 3):
    print(chunk)

             