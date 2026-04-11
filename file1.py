#take input of word 
x = input("please enter the word ")
#take input of character 
y = input("please enter your own character")
i = 0
count = 0 
#loop will to find the occurence of character 
while(i < len(x)): #string operation 

    if(x[i]==y): #condition 1 
        count = count + 1 
    i = i + 1 
#display the result
print("the total number of times",y,"has occured =" , count)        