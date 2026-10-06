# # #function definition  
# # def calculate_discount (price, discountrate):
# #     discount = price * discountrate #function suite 
# #     return discount

# # print(calculate_discount(100, 0.2)) #function call

# # #function returns value
# # def calculate (a,b):
# #     return a + b, a*b

# # print(calculate(4,5)) # (9,20)
# # sum_value, product_value = calculate(4,5) #unpacking the tuple 

# # print(sum_value) # 9
# # print(product_value) # 20

# # def square(x):
# #     return x * x    

# # def apply_function(func, value):
# #     return func(value)

# # print(apply_function(square, 5)) # 25

# #Smart Vending Machine 

# dispensed_count = 0 
 
# def dispense_drink(drink): 
#     global dispensed_count

#     if drink == "Coke": 
#         print("Dispensing Coke") 
#         dispensed_count += 1 
 
#     elif drink == "Water": 
#         print("Dispensing Water") 
#         dispensed_count += 1 
 
#     elif drink == "Juice": 
#         print("Dispensing Juice") 
#         dispensed_count += 1 
 
#     else: 
#         return "Drink not available" 
 
# dispense_drink("Juice")
# dispense_drink("Coke")
# dispense_drink("Water")


# print("Total drinks dispensed:", dispensed_count)

# Week 4 

# my_list = ['abc', 123, True, 'fff', -5, 'abc', -500, [0,1,2]]
# print(my_list[:3:1]) # start,end,step

# print('abc' in my_list) #check whether the element is in the list or not 

# my_list.append('kristee') #automatically added at the end of the list 
# print(my_list)
# my_list.insert(5,'KT') #added at a specific position, must specify, (position, value)
# print(my_list)
# del my_list[-2]
# print(my_list)
# my_list.remove('abc') #removes the first occurrence of the value
# print(my_list)
# print(len(my_list)) #number of elements in the array

# while ('abc' in my_list):
#     my_list.remove('abc') #removes all occurrences of the value
# print(my_list)

#concatenation and repetition of lists
# my_list = [1,2,3]+[4,5,6] #concatenation of two lists
# print(my_list)
# my_list = [1,2,3]*3 #repetition of a list
# print(my_list)
# import copy 
# list1 = [10,[1,20],30]
# list2 = copy.deepcopy(list1) #deep copy of the list
# list2[1][0] = 99
# print(list1)
# print(list2)

#DICTIONARIES
student = {
    "name": "Ali",
    "mark": 75,
    "city": "Singapore"
}

student['gender'] = "m" #creates a new key-value pair in the dictionary
del student["mark"] #deletes the key-value pair from the dictionary
print(student['mark'])
student.clear() #removes all key-value pairs from the dictionary