
# String exercie solution: 

```python
# Given variables
sentence = "Python is an amazing programming language"
user_input = "  Hello World!  "

# TODO: Complete these tasks and print each result
# 1. Find the length of 'sentence'
length = len(sentence)

# 2. Convert 'sentence' to uppercase
uppercase_sentence = sentence.upper()

# 3. Count how many times the letter 'a' appears in 'sentence'
count_a = sentence.count('a')

# 4. Split 'sentence' into a list of words
word_list = sentence.split(" ")

# 5. Get the first word from 'sentence' (hint: use split and indexing)
first_word = sentence.split(" ")[0]

# 6. Remove extra spaces from 'user_input' and convert to lowercase
clean_input = user_input.strip().lower()

# 7. Check if 'sentence' starts with "Python"
starts_with_python = sentence.startswith("Python")

# 8. Replace "amazing" with "awesome" in 'sentence'
new_sentence = sentence.replace("amazing", "awesome")

print("Results:")
print(f"Length: {length}")
print(f"Uppercase: {uppercase_sentence}")
print(f"Count of 'a': {count_a}")
print(f"First word: {first_word}")
print(f"Clean input: {clean_input}")
print(f"Starts with Python: {starts_with_python}")
print(f"New sentence: {new_sentence}")

```

#### OUTPUT:

```bash
Results:
Length: 41
Uppercase: PYTHON IS AN AMAZING PROGRAMMING LANGUAGE
Count of 'a': 6
First word: Python
Clean input: hello world!
Starts with Python: True
New sentence: Python is an awesome programming language

```

# List exercise solution

```python
# Starting data
fruits = ["apple", "banana", "orange"]
numbers = [5, 2, 8, 1, 9, 3, 2]
shopping_list = []

# TODO: Complete these operations
# 1. Add "grape" to the end of fruits
fruits.append("grape")

# 2. Insert "mango" at the beginning of fruits
fruits.insert(fruits.index("apple"),"mango")

# 3. Remove "banana" from fruits
fruits.remove("banana")

# 4. Create a sorted version of numbers (don't modify original)
sorted_numbers = sorted(numbers)

# 5. Add these items to shopping_list one by one: "milk", "bread", "eggs"
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")

# 6. Get the last item from fruits using negative indexing
last_fruit = fruits[-1]

# 7. Get the first 3 items from shopping_list using slicing
first_three_items = shopping_list[0:3]

# 8. Create a reversed version of fruits
fruits_reversed = fruits[::-1]

# 9. Find the maximum and minimum values in numbers
max_num = max(numbers)
min_num = min(numbers)

# 10. Get the length of the shopping_list
list_length = len(shopping_list)

# 11. Check if "apple" is in fruits
has_apple = "apple" in fruits

# 12. Get the index of "orange" in fruits
orange_index = fruits.index("orange")


# 13. Count how many times the number 2 appears in numbers
count_twos = numbers.count(2)

print("Final Results:")
print(f"Fruits: {fruits}")
print(f"Sorted numbers: {sorted_numbers}")
print(f"Shopping list: {shopping_list}")
print(f"Last fruit: {last_fruit}")
print(f"First 3 shopping items: {first_three_items}")
print(f"Max number: {max_num}, Min number: {min_num}")
print(f"Has apple: {has_apple}")
print(f"Orange index: {orange_index}")
print(f"Count number 2 occurence: {count_twos}")
```

#### OUTPUT:
```bash
Final Results:
Fruits: ['mango', 'apple', 'orange', 'grape']
Sorted numbers: [1, 2, 2, 3, 5, 8, 9]
Shopping list: ['milk', 'bread', 'eggs']
Last fruit: grape
First 3 shopping items: ['milk', 'bread', 'eggs']
Max number: 9, Min number: 1
Has apple: True
Orange index: 2
Count number 2 occurence: 2
``` 


# Tuple exercise solution

```python
# Given data
student_info = ("Alice", 20, "Computer Science", 3.8)
coordinates = (3, 4)
rgb_color = (255, 128, 0)

# TODO: Complete these tasks
# 1. Unpack student_info into separate variables
name, age, major, gpa = student_info

# 2. Access the second element of coordinates
y_coordinate = coordinates[1]

# 3. Create a tuple with the days of the week
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday",  "Sunday")

# 4. Try to modify coordinates (this should cause an error - comment it out after testing)
# coordinates[0] = 5

# 5. Create a tuple with just one element (remember the comma!)
single_tuple = (1,)

# 6. Unpack RGB values
red, green, blue = rgb_color 

# 7. Calculate distance from origin using coordinates (x² + y²)
x, y = coordinates
distance_squared = x**2 + y**2

# 8. Create a tuple of the first 3 even numbers
even_numbers_tuple = (2, 4, 6)

# 9. Convert the student_info tuple to a list, modify it, then back to tuple
student_list = list(student_info)
student_list[1] = 21  # Update age
updated_student = tuple(student_list)

# 10. Count how many items are in weekdays
num_weekdays = len(weekdays)

# 11. Get the last two elements of student_info using slicing
last_two = student_info[-2:]

# 12. Check if "Computer Science" is in student_info
has_cs = "Computer Science" in student_info

# 13. Find the index of 20 in student_info
age_index = student_info.index(20)

print("Results:")
print(f"Student name: {name}, Age: {age}")
print(f"Y coordinate: {y_coordinate}")
print(f"RGB values - Red: {red}, Green: {green}, Blue: {blue}")
print(f"Distance squared from origin: {distance_squared}")
print(f"Single tuple: {single_tuple}")
print(f"Updated student: {updated_student}")
print(f"Number of weekdays: {num_weekdays}")
print(f"Last two info items: {last_two}")
print(f"Check if 'Computer Science' in tuple : {has_cs}")
print(f"Index of 20 : {age_index}")
```

#### OUTPUT:
```bash
Results:
Student name: Alice, Age: 20
Y coordinate: 4
RGB values - Red: 255, Green: 128, Blue: 0
Distance squared from origin: 25
Single tuple: (1,)
Updated student: ('Alice', 21, 'Computer Science', 3.8)
Number of weekdays: 7
Last two info items: ('Computer Science', 3.8)
Check if 'Computer Science' in tuple : True
Index of 20 : 1
```

# Dictionary Exercise solution

```python
# Starting data
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
inventory = {}
person = {"name": "John", "age": 30, "city": "New York"}

# TODO: Complete these operations
# 1. Add a new student "Diana" with grade 88
student_grades["Diana"] = 88

# 2. Update Bob's grade to 95
student_grades["Bob"] = 95

# 3. Get Alice's grade
alice_grade = student_grades["Alice"]

# 4. Remove Charlie from the dictionary
del student_grades["Charlie"]

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
person["age"] = 31
person["occupation"] = "Engineer"

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

#### OUTPUT:
```bash
Results:
Student grades: {'Alice': 85, 'Bob': 95, 'Diana': 88}
Alice's grade: 85
Inventory: {'apples': 50, 'bananas': 30, 'oranges': 25}
Person info: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}
Total fruits: 105
Number of students: 3
Student names: ['Alice', 'Bob', 'Diana']
All grades: [85, 95, 88]
Eve exists: False
David's grade: 0
```

## Dictionary Practical challenge solution
**Problem Statement**: Create a dictionary to store information about your favorite movies, including title, year, and rating. Then practice adding, updating, and retrieving information

```python
# dictionary declaration
favorite_movies = {
     "Inception": {"year": 2010, "rating": 9.0},
    "Interstellar": {"year": 2014, "rating": 8.6},
    "The Dark Knight": {"year": 2008, "rating": 9.1}
}

# print dictionary
print(f"Favorite Movies: {favorite_movies}")

# Adding item to dictionary
favorite_movies["The Matrix"] = {"year": 1998, "rating": 8.5}

# print dictionary
print(f"After addition: {favorite_movies}")

# Updating the dictionary
favorite_movies["The Matrix"] = {"year": 1999, "rating" : 8.7}
print(f"After updating: {favorite_movies}")

# retrieving information from the dictionary
print("\nRetrieving dictionary information: \n")
for movie, movieinfo in favorite_movies.items():
    print(f"Name: {movie}, Year: {movieinfo["year"]}, Rating: {movieinfo["rating"]}")
```

#### OUTPUT:
```bash
Favorite Movies: {'Inception': {'year': 2010, 'rating': 9.0}, 'Interstellar': {'year': 2014, 'rating': 8.6}, 'The Dark Knight': {'year': 2008, 'rating': 9.1}}
After addition: {'Inception': {'year': 2010, 'rating': 9.0}, 'Interstellar': {'year': 2014, 'rating': 8.6}, 'The Dark Knight': {'year': 2008, 'rating': 9.1}, 'The Matrix': {'year': 1998, 'rating': 8.5}}
After updating: {'Inception': {'year': 2010, 'rating': 9.0}, 'Interstellar': {'year': 2014, 'rating': 8.6}, 'The Dark Knight': {'year': 2008, 'rating': 9.1}, 'The Matrix': {'year': 1999, 'rating': 8.7}}

Retrieving dictionary information: 

Name: Inception, Year: 2010, Rating: 9.0
Name: Interstellar, Year: 2014, Rating: 8.6
Name: The Dark Knight, Year: 2008, Rating: 9.1
Name: The Matrix, Year: 1999, Rating: 8.7
```

# Mixed Practice Exercies solution

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
student_name, test1, test2, test3 = student_info

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

#### OUTPUT:

```bash
Final Results:
Fruit list: ['apple', 'banana', 'orange', 'grape']
Student summary: Bob scored 85, 92, and 88 with an average of 88.3
Laptop total value: $14999.85
Most expensive price: $999.99
Prices only: {'laptop': 999.99, 'mouse': 25.99, 'keyboard': 75.5}
First fruit starts with 'a': True
Number of products: 3
All test scores: (85, 92, 88)
```

# Quick Practice Challenges Solution

## String challenge

**Problem Statement**: Take the string "Hello World" and create a new string with just the first and last character.

```python
mystring = "Hello World"
newstring = mystring[0] + mystring[-1]
print(f"New String: {newstring}")
```
#### OUTPUT:
```bash
New String: Hd
```

## List challenge

**Problem Statement**: Start with [1, 3, 5, 7, 9] and use indexing and list methods to insert 2 between 1 and 3.

```python
mylist = [1, 3, 5, 7, 9] 

index_of_3 = mylist.index(3)
mylist.insert(index_of_3,2)
print(mylist)
```
#### OUTPUT
```bash
[1, 2, 3, 5, 7, 9]
```

## Tuple challenge

**Problem Statement** : Create a tuple of your top 3 favorite colors, then access each one using indexing and print them.

```python
mytuple = ("Red", "Gree", "Blue")

print(f"First color: {mytuple[0]}")
print(f"Second color: {mytuple[1]}")
print(f"Third color: {mytuple[2]}")

```

#### OUTPUT:
```bash
First color: Red
Second color: Gree
Third color: Blue
```

## Dictionary challenge 

**Problem Statement**: Create a simple phone book with 3 contacts (name as key, phone number as value), then practice looking up numbers and adding new contacts.

```python
phonebook = {
     "Arya": "123-456-7890",
    "Pranit": "987-654-3210",
    "Jane": "555-123-4567"
}

print(f"Check Arya's phone number: {phonebook['Arya']}")


phonebook["Rishab"] = "111-222-3333"
print(f"After adding: {phonebook}")

phonebook["Arya"] = "999-888-7777"
print("After updating Arya's number:", phonebook)

print("Iterate over contacts")
for name,number in phonebook.items():
    print(f"{name}: {number}")
```

#### OUTPUT:
```bash
Check Arya's phone number: 123-456-7890
After adding: {'Arya': '123-456-7890', 'Pranit': '987-654-3210', 'Jane': '555-123-4567', 'Rishab': '111-222-3333'}
After updating Arya's number: {'Arya': '999-888-7777', 'Pranit': '987-654-3210', 'Jane': '555-123-4567', 'Rishab': '111-222-3333'}
Iterate over contacts
Arya: 999-888-7777
Pranit: 987-654-3210
Jane: 555-123-4567
Rishab: 111-222-3333
```