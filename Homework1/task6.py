def count_words(fileName):
    sum = 0
    try:
        
        files = open(fileName, 'r')
        
        words = files.read()
        word = words.split()
        sum += len(word)
        files.close()
    except:
        print("file not found")
    
    return sum

print(count_words("CS4300/Homework1/test1.txt"))
print(count_words("CS4300/Homework1/test2.txt"))
print(count_words("CS4300/Homework1/task6_read_me.txt"))

assert(count_words("CS4300/Homework1/test1.txt")) == 4
assert(count_words("CS4300/Homework1/test2.txt")) == 8
assert(count_words("CS4300/Homework1/task6_read_me.txt")) == 104