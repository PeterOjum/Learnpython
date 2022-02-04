''' Need to give assumptions like assume at least one element, etc. '''
def is_diagonal(m):
    ''' At least one element. '''
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if c_index != r_index and not m[r_index][c_index] == 0:
                return False
    return True    

def is_upper_triangular(m):
    ''' At least one element. '''
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if c_index < r_index and not m[r_index][c_index] == 0:
                return False
    return True
    
def contains(m, x):
    for r in m:
        if x in r:
            return True
    return False

def biggest(m):
    big = m[0][0]
    for row in m:
        for item in row:
            if item > big:
                big = item
    return big
    
def biggest4(m):
    ''' At least one element.  Updating a variable. '''
    big = max(m[0])
    for row in m[1:]:
        if max(row) > big:
            big = max(row)
    return big
    
def biggest2(m):
    return max(max(row) for row in m)
    
def biggest3(m):
    return max(element for row in m for element in row)

def indices_biggest(m):
    max_num = biggest(m)
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if m[r_index][c_index] == max_num:
                return [r_index, c_index]
     
def indices_biggest2(m):
    ''' If we didn't have biggest '''
    max_num = m[0][0]
    max_pos = [0,0]
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if m[r_index][c_index] > max_num:              
                max_num = m[r_index][c_index]
                max_pos = [r_index, c_index]
    return max_pos
    
def indices_biggest3(m):
    vals = [(m[r][c],[r,c]) for r in range(len(m)) for c in range(len(m[0]))]
    return max(vals, key=lambda x: x[0])[1]
    
def second_biggest(m):
    ''' At least 2 elements. '''
    # see indices... for the spelled out way
    flat = [num for row in m for num in row]
    (big, second) = (flat[0], flat[1]) if flat[1] <= flat[0] else (flat[1], flat[0])
    # could just work with flat but want to do nested
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if m[r_index][c_index] > second and r_index + c_index:
                # avoid re-checking m[0, 0].  More efficient to do the first row
                # outside the nested loops instead of checking r + c over and over 
                if m[r_index][c_index] >= big:
                    second = big
                    big = m[r_index][c_index]
                else:
                    second = m[r_index][c_index]
    return second
    
def second_biggest2(m):
    return sorted(element for row in m for element in row)[-2]    
    
    
def indices_second_biggest2(m):
    # the easy one follows
    if len(m) == len(m[0]) == 1:
        return [0, 0]
    if len(m[0]) > 1:
        if m[0][0] >= m[0][1]:
            big, second = m[0][0], m[0][1]
            indices_big, indices_second = [0, 0], [0, 1]
        else:
            second, big = m[0][0], m[0][1]
            indices_second, indices_big = [0, 0], [0, 1]
    else:
        if m[0][0] >= m[1][0]:
            big, second = m[0][0], m[1][0]
            indices_big, indices_second = [0, 0], [1, 0]
        else:
            second, big = m[0][0], m[1][0]
            indices_second, indices_big = [0, 0], [1, 0]
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if m[r_index][c_index] > second and r_index + c_index:
                if m[r_index][c_index] >= big:
                    second = big
                    indices_second = indices_big
                    big = m[r_index][c_index]
                    indices_big = [r_index, c_index]
                else:
                    second = m[r_index][c_index]
                    indices_second = [r_index, c_index]
    return indices_second
    
def indices_second_biggest(m):
    if len(m) == len(m[0]) == 1:
        return [0, 0]
    second = second_biggest(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == second:
                return [i, j]

"""                
def is_symmetric(m):
    ''' Square matrix. Put this in a worksheet. '''
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if not m[r_index][c_index] == m[c_index][r_index]:
                return False
    return True 

def element_divisible_by_3(m):
    result = []
    for row in m:
        for element in row:
            if element % 3 == 0:
                result.append(element)
    return result
    
def element_divisible_by_32(m):
    return [element for row in m for element in row if element % 3 == 0]
"""

def substr_in_values(dct, srch_key):
    keys = []
    for key in dct:
        for string in dct[key]:
            if srch_key.lower() in string.lower():
                keys.append(key)
                break
    return sorted(keys)

def indices_divisible_by_3(m):
    result = []
    for r_index in range(len(m)):
        for c_index in range(len(m[0])):
            if (r_index + c_index) % 3 == 0:
                result.append(m[r_index][c_index])
    return result
    
def indices_divisible_by_32(m):
    return [m[r_index][c_index] for r_index in range(len(m)) for c_index in range(len(m[0])) if (r_index + c_index) % 3 == 0]
    
def sort_int_string(int_str):
    int_str = int_str.split()
    for i in range(len(int_str)):
        int_str[i] = int(int_str[i])
    int_str.sort()
    for i in range(len(int_str)):
        int_str[i] = str(int_str[i])
    return " ".join(int_str)
    
def sort_int_string2(int_str):
    return " ".join(str(i) for i in sorted(int(s) for s in int_str.split()))
    
def dups_lol(matrix):
    items = []
    for row in matrix:
        for item in row:
            if item in items:
                return True
            else:
                items.append(item)
    return False
    
def dups_lol2(matrix):
    flat = [item for row in matrix for item in row]
    return len(flat) > len(set(flat))
    
def dups_dict(dct):
    lol = []
    for key in dct:
        lol.append(dct[key])
    return dups_lol(lol)

"""    
def camelCase_2_underscores(string):
    if not string: 
        return ""
    result = string[0].lower()
    for ch in string[1:]:
        if ch.isupper():
            result += '_' + ch.lower()
        else:
            result += ch
    return result

def camelCase_2_underscores2(string):
    if not string: 
        return ""
    result = string[0].lower()
    for ch in string[1:]:
        result += '_' + ch.lower() if ch.isupper() else ch
    return result

def underscores_2_camelCase(string):
    if not string: 
        return ""
    list_of_words = string.split('_')
    result = list_of_words[0]
    for word in list_of_words[1:]:
        result += word.capitalize()
    return result

def underscores_2_camelCase4(string):
    if not string: 
        return ""
    list_of_words = string.split('_')
    return list_of_words[0] + ''.join(word.capitalize() for word in list_of_words[1:])

def underscores_2_camelCase2(string):
    if not string: 
        return ""
    previous_index = string.find('_')
    if previous_index < 0:
        return string
    result = string[:previous_index]
    current_index = string.find('_', previous_index + 1)
    while current_index >= 0:
        next_word = string[previous_index + 1:current_index]
        if next_word:
            result += next_word[0].upper() + next_word[1:]
        previous_index = current_index
        current_index = string.find('_', previous_index + 1)
    if previous_index + 1 < len(string):
        result += string[previous_index + 1].upper() + string[previous_index + 2:]
    return result
    
def underscores_2_camelCase3(string):
    if not string: 
        return ""
    result = ''
    i = 0
    while i < len(string):
        if string[i] == '_':
            if i + 1 == len(string):
                return result
            if string[i + 1] != '_':
                result += string[i + 1].upper()
                i += 1
        else:
            result += string[i]
        i += 1
    return result

def element_ip_replace(search_list, key, replacement=None):
    for i in range(len(search_list)):
        if search_list[i] == key:
            search_list[i] = replacement
            
def element_ip_replace2(search_list, key, replacement=None):
    for i in range(len(search_list)):
        search_list[i] = replacement if search_list[i] == key else search_list[i]
            
def element_nl_replace(search_list, key, replacement=None):
    nl = []
    for item in search_list:
        if item == key:
            nl.append(replacement)
        else:
            nl.append(item)
    return nl
            
def element_nl_replace2(search_list, key, replacement=None):
    return [replacement if item == key else item for item in search_list]
"""



    
    