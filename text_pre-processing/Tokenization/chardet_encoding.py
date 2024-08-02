## using chardet library to determine text encoding of a file
# look at the first ten thousand bytes to guess the character encoding
import chardet

with open(data_path, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

# check what the character encoding might be
print(result)
