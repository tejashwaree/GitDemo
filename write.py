#read the lines and store all line in list
#reverse the list
# store list back to tht file

with open("text.txt", "r") as reader:
    content = reader.readlines()  #[ajfgj , bfgjfgj, cat, dog, elephant,fox]
    # reversed(content) it will reveresed the content
    with open("text.txt", "w") as writer:
        for line in reversed(content):  #iterate the reveresed content line by line
            writer.write(line)


