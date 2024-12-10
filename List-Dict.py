def convert_to_dict(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]  # Correctly assign key-value pairs
    return result

students = [[1, 'Anabelle', 'A'], [2, 'Laura', 'L'], [3, 'Ifecinachi', 'I']]
print("\nOriginal list of lists: ")
print(students)

print("\nConverted list to Dictionary:")
print(convert_to_dict(students))

