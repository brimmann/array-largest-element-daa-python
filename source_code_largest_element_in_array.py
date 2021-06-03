import matplotlib.pyplot as plt #This library was imported for plotting graph for growth function

#MY_MAX algorithm implementation
def my_max(list1): 
    max = list1[0] 
    for x in list1: 
        if x > max : 
             max = x 
    return max

list1 = [5, 10, 4, 54, 81] 
print("Largest element is:", my_max(list1))

#Growth Function of Max Element for Worst Case Scenario is T(n) = n

def worst_case_fun(n):
    return n

#Calculating domain and range of the function.

fun_range = []
for i in range(0, 10):
     fun_range.append(i)

fun_domain = []
for value in fun_range:
     fun_domain.append(worst_case_fun(value))

#Plotting graph for the given range and domain.

plt.plot(fun_range, fun_domain)
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("MAX ALGORITH TIME COMPLEXITY GRAPH")
plt.text(3, 4, "By Mohammad Rashid 3927")
plt.show()
