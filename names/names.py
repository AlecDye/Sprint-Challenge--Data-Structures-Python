import time

start_time = time.time()

# hint: import a data structure?

# navigate into names directory and run "py names.py"

# Start runtime: 4.5285 seconds
# Ideal runtime: under 1.0 seconds

# Anything better than 4.5 seconds is technically optimized?

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:  # O(n)
#     for name_2 in names_2:  # O(n)
#         if name_1 == name_2:  # O(1)?
#             duplicates.append(name_1)

# current time complexity O(n^2)? - Polynomial, not good

# run for every name in names_1 file
for name in names_1:  # O(n)
    # compares the name in file 1 against the name in file 2
    if name in names_2 == name:  # O(1)
        # if they are the same append to list
        duplicates.append(name)

# current runtime: 0.9193115234375 seconds (woo!)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
