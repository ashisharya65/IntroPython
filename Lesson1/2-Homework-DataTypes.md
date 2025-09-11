# Interactive Python Exercises: Strings, Tuples, Lists, and Dictionaries

## Exercise 1: String Basics
**Practice string methods and operations**

```python
# Given variables
sentence = "Python is an amazing programming language"
user_input = "  Hello World!  "

# TODO: Complete these tasks and print each result
# 1. Find the length of 'sentence'
length = 

# 2. Convert 'sentence' to uppercase
uppercase_sentence = 

# 3. Count how many times the letter 'a' appears in 'sentence'
count_a = 

# 4. Split 'sentence' into a list of words
word_list = 

# 5. Get the first word from 'sentence' (hint: use split and indexing)
first_word = 

# 6. Remove extra spaces from 'user_input' and convert to lowercase
clean_input = 

# 7. Check if 'sentence' starts with "Python"
starts_with_python = 

# 8. Replace "amazing" with "awesome" in 'sentence'
new_sentence = 

print("Results:")
print(f"Length: {length}")
print(f"Uppercase: {uppercase_sentence}")
print(f"Count of 'a': {count_a}")
print(f"First word: {first_word}")
print(f"Clean input: {clean_input}")
print(f"Starts with Python: {starts_with_python}")
print(f"New sentence: {new_sentence}")
```

**Try this:** Create a variable with your full name and use string methods to print your first name, last name, and initials.

---

## Exercise 2: List Practice
**Working with list methods and operations**

```python
# Starting data
fruits = ["apple", "banana", "orange"]
numbers = [5, 2, 8, 1, 9, 3]
shopping_list = []

# TODO: Complete these operations
# 1. Add "grape" to the end of fruits
fruits.

# 2. Insert "mango" at the beginning of fruits
fruits.

# 3. Remove "banana" from fruits
fruits.

# 4. Create a sorted version of numbers (don't modify original)
sorted_numbers = 

# 5. Add these items to shopping_list one by one: "milk", "bread", "eggs"
shopping_list.
shopping_list.
shopping_list.

# 6. Get the last item from fruits using negative indexing
last_fruit = fruits

# 7. Get the first 3 items from shopping_list using slicing
first_three_items = shopping_list

# 8. Create a reversed version of fruits
fruits_reversed = fruits

# 9. Find the maximum and minimum values in numbers
max_num = 
min_num = 

# 10. Get the length of the shopping_list
list_length = 

# 11. Check if "apple" is in fruits
has_apple = 

# 12. Get the index of "orange" in fruits
orange_index = fruits.

# 13. Count how many times the number 2 appears in numbers
count_twos = numbers.

print("Final Results:")
print(f"Fruits: {fruits}")
print(f"Sorted numbers: {sorted_numbers}")
print(f"Shopping list: {shopping_list}")
print(f"Last fruit: {last_fruit}")
print(f"First 3 shopping items: {first_three_items}")
print(f"Max number: {max_num}, Min number: {min_num}")
print(f"Has apple: {has_apple}")
print(f"Orange index: {orange_index}")
```

**Challenge:** Start with the list [1, 2, 3, 4, 5] and use list operations to transform it into [5, 4, 3, 2, 1, 6].

---

## Exercise 3: Tuple Exploration
**Understanding tuple creation and unpacking**

```python
# Given data
student_info = ("Alice", 20, "Computer Science", 3.8)
coordinates = (3, 4)
rgb_color = (255, 128, 0)

# TODO: Complete these tasks
# 1. Unpack student_info into separate variables
name, age, major, gpa = 

# 2. Access the second element of coordinates
y_coordinate = coordinates

# 3. Create a tuple with the days of the week
weekdays = 

# 4. Try to modify coordinates (this should cause an error - comment it out after testing)
# coordinates[0] = 5

# 5. Create a tuple with just one element (remember the comma!)
single_tuple = 

# 6. Unpack RGB values
red, green, blue = 

# 7. Calculate distance from origin using coordinates (x² + y²)
x, y = coordinates
distance_squared = x**2 + y**2

# 8. Create a tuple of the first 3 even numbers
even_numbers_tuple = 

# 9. Convert the student_info tuple to a list, modify it, then back to tuple
student_list = list(student_info)
student_list[1] = 21  # Update age
updated_student = tuple(student_list)

# 10. Count how many items are in weekdays
num_weekdays = len(weekdays)

# 11. Get the last two elements of student_info using slicing
last_two = student_info

# 12. Check if "Computer Science" is in student_info
has_cs = 

# 13. Find the index of 20 in student_info
age_index = student_info.

print("Results:")
print(f"Student name: {name}, Age: {age}")
print(f"Y coordinate: {y_coordinate}")
print(f"RGB values - Red: {red}, Green: {green}, Blue: {blue}")
print(f"Distance squared from origin: {distance_squared}")
print(f"Single tuple: {single_tuple}")
print(f"Updated student: {updated_student}")
print(f"Number of weekdays: {num_weekdays}")
print(f"Last two info items: {last_two}")
```

**Real-world practice:** Create tuples for storing information that shouldn't change, like (latitude, longitude) coordinates or (width, height) dimensions.

---

## Exercise 4: Dictionary Operations
**Working with key-value pairs and dictionary methods**

```python
# Starting data
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
inventory = {}
person = {"name": "John", "age": 30, "city": "New York"}

# TODO: Complete these operations
# 1. Add a new student "Diana" with grade 88
student_grades["Diana"] = 

# 2. Update Bob's grade to 95
student_grades

# 3. Get Alice's grade
alice_grade = student_grades

# 4. Remove Charlie from the dictionary
del student_grades

# 5. Add items to inventory dictionary
inventory["apples"] = 50
inventory["bananas"] = 30
inventory["oranges"] = 25

# 6. Get all student names (keys)
student_names = list(student_grades.keys())

# 7. Get all grades (values)
all_grades = list(student_grades.values())

# 8. Get both names and grades together (items)
student_items = list(student_grades.items())

# 9. Check if "Eve" is in student_grades
eve_exists = "Eve" in student_grades

# 10. Get David's grade, but return 0 if he doesn't exist
david_grade = student_grades.get("David", 0)

# 11. Update person's age to 31 and add "occupation": "Engineer"
person["age"] = 
person["occupation"] = 

# 12. Calculate total fruit inventory
total_fruits = inventory["apples"] + inventory["bananas"] + inventory["oranges"]

# 13. Get the number of students in student_grades
num_students = len(student_grades)

# 14. Create a new dictionary with favorite colors
colors = {"primary": "blue", "secondary": "green", "accent": "red"}

# 15. Copy the person dictionary
person_copy = person.copy()

# 16. Get all inventory items as key-value pairs
inventory_items = list(inventory.items())

print("Results:")
print(f"Student grades: {student_grades}")
print(f"Alice's grade: {alice_grade}")
print(f"Inventory: {inventory}")
print(f"Person info: {person}")
print(f"Total fruits: {total_fruits}")
print(f"Number of students: {num_students}")
print(f"Student names: {student_names}")
print(f"All grades: {all_grades}")
print(f"Eve exists: {eve_exists}")
print(f"David's grade: {david_grade}")
```

**Practical challenge:** Create a dictionary to store information about your favorite movies, including title, year, and rating. Then practice adding, updating, and retrieving information.

---

## Exercise 5: Mixed Practice
**Combining all data types**

```python
# Complex data mixing all types
text_data = "apple,banana,orange,grape"
student_info = ("Bob", 85, 92, 88)  # name, test1, test2, test3
product_catalog = {
    "laptop": (999.99, 15),  # (price, quantity)
    "mouse": (25.99, 50),
    "keyboard": (75.50, 25)
}

# TODO: Complete these mixed exercises
# 1. Convert text_data into a list of fruits
fruit_list = text_data.split(",")

# 2. Unpack student information
student_name, test1, test2, test3 = 

# 3. Calculate student's average (manual calculation)
average_grade = (test1 + test2 + test3) / 3

# 4. Get laptop information from catalog
laptop_price, laptop_quantity = product_catalog["laptop"]

# 5. Create a formatted string with all fruit names
fruit_sentence = "My favorite fruits are: " + ", ".join(fruit_list)

# 6. Calculate total value of laptops in inventory
laptop_total_value = laptop_price * laptop_quantity

# 7. Create a new dictionary with just product names and prices
prices_only = {}
prices_only["laptop"] = product_catalog["laptop"][0]
prices_only["mouse"] = product_catalog["mouse"][0]
prices_only["keyboard"] = product_catalog["keyboard"][0]

# 8. Get the most expensive product price
all_prices = [product_catalog["laptop"][0], product_catalog["mouse"][0], product_catalog["keyboard"][0]]
max_price = max(all_prices)

# 9. Create a student summary string
student_summary = f"{student_name} scored {test1}, {test2}, and {test3} with an average of {average_grade:.1f}"

# 10. Check if any fruit starts with 'a'
first_fruit = fruit_list[0]
starts_with_a = first_fruit.startswith('a')

# 11. Get the number of different products
num_products = len(product_catalog)

# 12. Create a tuple of all test scores
all_scores = (test1, test2, test3)

print("Final Results:")
print(f"Fruit list: {fruit_list}")
print(f"Student summary: {student_summary}")
print(f"Laptop total value: ${laptop_total_value:.2f}")
print(f"Most expensive price: ${max_price:.2f}")
print(f"Prices only: {prices_only}")
print(f"First fruit starts with 'a': {starts_with_a}")
print(f"Number of products: {num_products}")
print(f"All test scores: {all_scores}")
```

---

## Quick Practice Challenges

Try these mini-exercises to reinforce your learning:

1. **String challenge:** Take the string "Hello World" and create a new string with just the first and last character.

2. **List challenge:** Start with [1, 3, 5, 7, 9] and use indexing and list methods to insert 2 between 1 and 3.

3. **Tuple challenge:** Create a tuple of your top 3 favorite colors, then access each one using indexing and print them.

4. **Dictionary challenge:** Create a simple phone book with 3 contacts (name as key, phone number as value), then practice looking up numbers and adding new contacts.