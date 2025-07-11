#1.Setup, Introduction and print()
print("Hello, Python!");
name="Vijayalakshmi";
age=32;
print("Name:",name,"Age:",age);
print("Apple","Banana","Cherry",sep=",");
a=42;
print(f"My Favorite Number is {a}.");
b=5;
c=7;
print(b+c);
# The print() function outputs the specified message or value to the console.
# It is commonly used to display information to the user or for debugging purposes.
# Example: print("Hello, world!") will display the text Hello, world! on the screen.
name="Vijayalakshmi";
age=32;
print("My Name is",name,"and I am",age,"years old.")
print("Apple","Banana","Cherry",sep="|");
print("Chennai\nIndia");

#2. Variables and Data Types
name="Vijayalakshmi";
print(name);
age=32;
print(age);
price=3.14;
print(price);
is_Student=True;
print(is_Student);
favorite_colors = ["blue", "green", "red"];
print(favorite_colors[1]);
coordinates = (10, 20);
print(coordinates[0]);
print(coordinates[1]);
car = {
    "brand": "Duster",
    "year": 2016
}
print(car["brand"]);
print(car["year"]);
unique_numbers = {1, 2, 3};
print(unique_numbers);
value = 10;
print("Before:", value);

value = 25;
print("After:", value);

name="Vijayalakshmi";
print(type(name));

#3. Data Types Examples
number=42;
print(number);
float_number=2.85;
print(float_number);
fav_quote="too good to be true";
print(fav_quote);
is_Student=True;
subjects = ["Math", "Science", "History", "English", "Art"];
print(subjects[-1]);
cities = ("London", "Paris", "Tokyo");
print(cities[0]);
student = {
    "name": "Banu",
    "grade": "A"
};
print(student);
numbers={1,1,1,2,2,2,3,3,3,3};
print(numbers);
mixed_list = ["Hello", 42, 3.14, True, None];

for item in mixed_list:
    print(f"Value: {item}, Type: {type(item)}");
value=461;
print(type(value));

#4. Data Types Examples
name = input("What is your name? ");
print(f"Hello, {name}!");

num1 = input("Enter the first number: ");
num2 = input("Enter the second number: ");
num1 = float(num1);
num2 = float(num2);
result = num1 + num2;
print("The sum is:", result);

age = input("Enter your age: ");
age = int(age);
next_year_age = age + 1;
print(f"Next year, you will be {next_year_age} years old.");

color = input("What is your favorite color? ");
print(f"Wow, {color} is a beautiful color!");

city = input("Enter your city: ");
country = input("Enter your country: ");
print(f"You live in {city}, which is located in {country}.");

price = float(input("Enter the original price: "));
discount = float(input("Enter the discount percentage (e.g., 20 for 20%): "));
discounted_price = price * (1 - discount / 100);
print(f"The price after a {discount}% discount is: ${discounted_price:.2f}");

hobbies = [];
for i in range(1, 4):
    hobby = input(f"Enter hobby #{i}: ");
    hobbies.append(hobby)
print("Your hobbies are:", hobbies);

name = input("Enter your name: ");
age = input("Enter your age: ");
print(f"{name} is {age} years old.");

num1 = float(input("Enter the first number: "));
num2 = float(input("Enter the second number: "));
result = num1 * num2;
print(f"The result of multiplying {num1} and {num2} is {result}");

user_input = input("Enter something: ");
print(type(user_input));

## 5. type() Function and Data Type Checks

my_variable = 3.14;
print(type(my_variable));

user_input = input("Enter something: ");
print(f"The type of the input is: {type(user_input)}");

num_str = input("Enter a number: ");
print(f"Type before conversion: {type(num_str)}");
num_int = int(num_str);
print(f"Type after conversion: {type(num_int)}");

mixed_list = [42, "hello", 3.14, True, None];
for item in mixed_list:
    print(f"Value: {item}, Type: {type(item)}");

print(type(True));

birth_year = input("Enter your birth year: ");
birth_year_int = int(birth_year);
print(type(birth_year_int));

my_tuple = (1, 2, 3);
print(type(my_tuple));

my_set = {1, 2, 3};
print(my_set);
print(type(my_set));

my_dict = {"name": "Alice", "age": 30};
print(type(my_dict["age"]));
print(type(my_dict["name"]));

num = input("Enter a number: ");
print(f"Type before conversion: {type(num)}");
num_float = float(num);
print(f"Type after conversion: {type(num_float)}");