
a = [[1,2,4], [3,5,6]]      # flat to a single list and sort

def func3(lst):
    rs = []
    for item in a:
        rs = rs + item
        
    return sorted(rs)
        

print(func3(a))


# flaten below list

b = [1, 2, [11,22,33, [10, 20, 30]], 20, 30, [90, 80]]

def func4(lst, rs = []):
    for item in lst:
        if isinstance(item, list) == False:
            rs.append(item)
        else:
            func4(item)
            
    return rs


print(func4(b))