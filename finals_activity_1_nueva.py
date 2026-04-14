# Ruzzel Nueva
# Part 1: Identify & Create(Warm-up)
print("\nPart 1: Creation")

# A tuple of 5 favorite fruits
fruits = ("Mango", "Apple", "Banana", "Grapes", "Orange")

# A list of 5 daily tasks
daily_tasks = ["Exercise", "Study", "Code", "Eat", "Sleep"]

# A set of unique numbers 
unique_numbers = set([1, 2, 2, 3, 4, 4, 5])

# A dictionary with keys
student_info = {
    "name": "Ruzzel",
    "age": 19,
    "course": "BSIT"}

print("Fruits (Tuple):", fruits)
print("Daily Tasks (List):", daily_tasks)
print("Unique Numbers (Set):", unique_numbers)
print("Student Info (Dictionary):", student_info)

# Part 2: Manipulation Challenge
print("\nPart 2: Manipulation")

# List Tasks

# Add a new task
daily_tasks.append("Playing Volleyball")

# Remove one task
daily_tasks.remove("Sleep")

# Sort the list
daily_tasks.sort()
print("\nUpdated List:", daily_tasks)

# Tuple Tasks
print("\nTuple Task:")
temp_list = list(fruits) # Unlocked (Convert to List)
temp_list[1] = "Strawberry"  # Modified (Change the value)
fruits = tuple(temp_list) # Locked (Convert back to Tuple)
print(fruits)
# It's just the same with the Assignemnt 1, Because tuple is immutable
# Here I created a way to modify, so we need first to convert to the list (that is mutable and can be change) by the use of list() function
# After changing the value, retured it to tuple() to be immutable or protected again the data."

# The code will only error when changing the value directly
# This means that once the values are assigned, they cannot be changed, added to, or deleted.
# fruits[0] = "Strawberry"

# Set Tasks

# Add a number
unique_numbers.add(6)

# Remove a number
unique_numbers.remove(1)

# Show how duplicates are removed
# In line, the set() constructor is automatic removing of duplicates.
# So the [1, 2, 2, 3, 4, 4, 5] will be {1, 2, 3, 4, 5}.
print("\nSet:", unique_numbers)

# This are the two duplicate that has been remove
print("\nDuplicates that were removed:", 2, 4)

# Dictionary Tasks
# Add a new key "grade"
student_info["grade"] = 1.25

# Update "age"
student_info["age"] = 19
print("\nAll keys and values:", student_info.items())
