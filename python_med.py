# -*- coding: utf-8 -*-
"""
python_med.py

Refactored for improved readability, formatting, and maintainability.
No functional changes were made to the original logic.
"""

# -----------------------------
# BASIC OPERATIONS
# -----------------------------

print(22 / 7)
print(22 // 7)
print(22 % 7)

# Assignment operator
a = 5  # Assign value to a
print(a)

x = [10, 20, 30]
x[0] = 1
print(x[0])

# -----------------------------
# RELATIONAL OPERATORS
# -----------------------------

print(3 == 3)
print(3 != 3)
print(3 > 1)
print(3 >= 3)
print(3 < 4)
print(3 <= 4)

# -----------------------------
# LOGICAL OPERATORS
# -----------------------------

print(not (2 == 2))
print((1 != 1) and (1 < 1))
print((1 >= 1) or (1 < 1))

# -----------------------------
# DATA STRUCTURES
# -----------------------------

# Set (removes duplicates automatically)
my_set = {1, 2, 3, 2}
print(my_set)

# Dictionary
my_dict = {"name": "Aneesh", "age": 18}
print(my_dict)

# List operations
my_list = ['a', 'e', 'i', 'o', 'u']
print(my_list.index('a'))

# -----------------------------
# LIST OPERATIONS
# -----------------------------

mylist = [1, 2, 3, 4, 4, 5]

print(mylist.count(4))

mylist.append(6)
print(mylist)

mylist.remove(6)
print(mylist)

del mylist[0:1]
print(mylist)

mylist.reverse()
print(mylist)

# Extend list
mycars = ["Ford", "BMW"]
mylist.extend(mycars)
print(mylist)

mylist.pop(-1)
print(mylist)

mylist.insert(0, 'M')
print(mylist)

# -----------------------------
# STRING OPERATIONS
# -----------------------------

mystring = "welcome to python"
print(mystring)
print(mystring[3])

# -----------------------------
# RUNNING SUM
# -----------------------------

def running_sum(nums):
    """Return running sum of list elements"""
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result

print(running_sum([10, 20, 30, 2, -1]))

# -----------------------------
# SUM OF ELEMENTS
# -----------------------------

def total_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(total_sum([10, 20, 30, 2, -1]))

# -----------------------------
# COUNT EVEN NUMBERS
# -----------------------------

def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

print(count_even([10, 2, 3, 5, 7, 9]))

# -----------------------------
# REVERSE LIST
# -----------------------------

def reverse_list(nums):
    return nums[::-1]

print(reverse_list([2, 4, 6, 8, 10]))

# -----------------------------
# SLICING
# -----------------------------

mylist = [1, 2, 3, 4, 5, 6, 8]
print(mylist[::2])
print(mylist[::3])
print(mylist[::-1])
print(mylist[::-2])
print(mylist[::-3])

# -----------------------------
# MAXIMUM ELEMENT
# -----------------------------

def find_max(nums):
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum

print(find_max([10, 2, 3, 5, 7, 9]))

# -----------------------------
# MINIMUM ELEMENT
# -----------------------------

def find_min(nums):
    minimum = nums[0]
    for n in nums:
        if n < minimum:
            minimum = n
    return minimum

print(find_min([10, 2, 3, 5, 7, 9]))

# -----------------------------
# MERGE TWO SORTED LISTS
# -----------------------------

def merge_lists(list1, list2):
    return sorted(list1 + list2)

print(merge_lists([1, 2, 3, 4], [5, 6, 7, 8]))

# -----------------------------
# SQUARE OF SORTED LIST
# -----------------------------

def square(nums):
    return sorted(x**2 for x in nums)

print(square([1, 2, 3, 4, 5]))

# -----------------------------
# MAX CUSTOMER DEPOSIT
# -----------------------------

def deposit(accounts):
    return max(sum(cust) for cust in accounts)

print(deposit([[100, 52], [3, 60]]))

# -----------------------------
# TWO SUM PROBLEM
# -----------------------------

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i

print(two_sum([2, 0, 11, 15], 26))

# -----------------------------
# GROCERY STORE SYSTEM
# -----------------------------

products = {
    "Apples": 50,
    "Bananas": 30,
    "Milk": 60,
    "Bread": 40,
    "Eggs": 70
}

cart = {}

def show_menu():
    print("\n===== Grocery Store Menu =====")
    print("1. Show products")
    print("2. Empty cart")
    print("3. Display menu")
    print("4. Add item")
    print("5. Remove item")
    print("6. Show cart")
    print("7. Exit")

show_menu()

while True:
    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        for item, price in products.items():
            print(item, ":", price)

    elif choice == "2":
        cart.clear()
        print("Cart is empty!")

    elif choice == "3":
        show_menu()

    elif choice == "4":
        item = input("Enter product: ")
        if item in products:
            qty = int(input("Enter quantity: "))
            cart[item] = cart.get(item, 0) + qty
            print("Added to cart")
        else:
            print("Item not available")

    elif choice == "5":
        item = input("Enter product to remove: ")
        if item in cart:
            qty = int(input("Quantity to remove: "))
            if qty >= cart[item]:
                del cart[item]
            else:
                cart[item] -= qty
            print("Updated cart")
        else:
            print("Item not in cart")

    elif choice == "6":
        total = 0
        for item, qty in cart.items():
            price = products[item] * qty
            total += price
            print(item, "x", qty, "=", price)
        print("Total:", total)

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice")