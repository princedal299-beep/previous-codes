# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# f = open("demo.txt","r")
# data = f.read(5)
# print(data)

# f.close()  # isme ham only 5 characters read karenge, baki data read nahi hoga.



#reads one line at a time

# f = open("demo.txt","r")

# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()


#wriring to a file

# f = open("demo.txt","a")
# f.write("\ni want to becone a ai engineer")#this ia a asppend method.
# f.close()



# f = open("demo.txt","w")
# f.write("i want to becone a ai engineer")#ye h write mode jisme agr ham likhte h to phele ka data delter ho jayega or naya data us file me jud jayega.
# f.close()


#agr apn a or w mode me foi file kholte h or agr wo exit nhi krti to ye apne aap us file ko create kr deta hai.

# f = open("sample.txt","w")
# f.close()

# f = open("sample.txt","a")
# f.close()

# f = open("demo.txt","r+")
# f.write("i want to becone a ai engineer")
# print(f.read())
# f.close()
#isme read and overwrite kar skte h .


#with syntax

# with open("demo.txt","r")as f:  #alias bolte h as ko
#     data = f.read()
#     print(data)

 #ye better verison h kisi bhi file ko open krne h ka

 #deleating a file

# import os
# os.remove("sample.txt")


#practise question
#create a new file called practise.txt and write the following lines in it.

# with open("practise.txt","w") as f:
#     f.write("hi everyone\nwe are learing file I/O\n")
#     f.write("using java.\n i like programming in java")


#wap that replace occurances of java with python in the above file.


# with open("practise.txt","r") as f:
#     data = f.read()

# new_data =  data.replace("java","python")
# print(new_data)



# with open("practise.txt","w") as f:
#     f.write(new_data)



#search if the word "learning" exists in the file or not.
# word = "learing"
# with open("practise.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("word found")
#     else:
#         print("word not found")


#function ke form me likhna ho isko to wo bhi kr skte h h
# def check_for_word():
#     word = "learing"
#     with open("practise.txt","r") as f:
#          data = f.read()
#     if(data.find(word) != -1):
#         print("word found")
#     else:
#         print("word not found")
# check_for_word()





#write a fucntion to find in which line of the file does the word "learning" occur first.print -1 if word not found.

# def check_for_word():
#     word = "learing"
#     with open("practise.txt","r") as f:
#          data = f.read()
#     if(data.find(word) != -1):
#         print("word found")
#     else:
#         print("word not found")
# check_for_word()


# def check_for_line():
#     word = "learing"
#     data = True
#     line_no = 1
#     with open("practise.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
            
#             line_no +=1
#     return -1        
# print(check_for_line())





#from a file conatining numbers seperated by comma, print the count of even numbers.
# 1,2,76,84,90,101

count = 0
with open("practise.txt","r") as f:
    data = f.read()
    

    nums = data.split(",")
    for val in nums:
        if (int(val)% 2 == 0):
            count += 1
    print(count)

