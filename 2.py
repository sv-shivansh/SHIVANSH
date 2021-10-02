# Printing words in reverse order
str = "My name is               Shivansh"
temp = len(str)
for i in range(len(str)-1, -1, -1):
    if(str[i]== " "):
        print(str[i+1:temp], end=" ")
        temp = i
space = str.find(" ")
print(str[:space], end = " ")
