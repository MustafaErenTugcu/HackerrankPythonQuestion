# 1 . soru 

def flatten_list(lst):
    result = []

    def recursive_flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                recursive_flatten(item)
            else:
                result.append(item)

    recursive_flatten(lst)
    return result

# Test
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten_list(input_list)
print(output_list)  # Output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
# 2. soru 
def reverse_list(lst):
    result = []
    for item in lst[::-1]:  # Tersine sıralanmış halde elemanlara ulaşırız
        if isinstance(item, list):
            result.append(reverse_list(item))  # Alt-listeleri de tersine döndürerek ekleriz
        else:
            result.append(item)
    return result

# Test
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)  # Output: [[[7, 6, 5], [4, 3], [2, 1]]]
