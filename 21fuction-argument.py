# def average(a, b, c=1):
#     print("The avarage is ", (a + b + c)/2)

def average(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("Average is : ",sum / len(numbers))
    #return 7
    return sum / len(numbers)       

#  #avarage(4, 6) 
# average(b=9)

# # def name(fname, mname = "jhon", lname = "Whatson"):
# #     print("Hello,", fname, mname, lname)


# # name("Amy", "Agarwal")  
c = average(5, 6, 7, 1)
print(c)