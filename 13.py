def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    count_str1 = {}
    count_str2 = {}
    
    for char in str1:
        if char in count_str1:
            count_str1[char] += 1
        else:
            count_str1[char] = 1
    
    for char in str2:
        if char in count_str2:
            count_str2[char] += 1
        else:
            count_str2[char] = 1
    
    return count_str1 == count_str2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
