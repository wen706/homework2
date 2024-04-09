def get_even_squares(num_list:list[int])->list[int]:
    """返回偶數平方的list"""
    return [x**2 for x in num_list if x % 2 == 0]
def get_odd_cubes(num_list:list[int])->list[int]:
    """返回奇數立方的list"""
    temp=list()
    for i in num_list:
        if i%2==1:
            temp.append(i**3)
    return temp
def get_sliced_list(num_list:list[int])->list[int]:
    """返回 num_list 從第 5 個元素開始到最後一個元素"""
    return num_list[4:]
def format_numbers(num_list:list[int])->list[str]:
    """返回一個列表,其中每個數字都被格式化為 8 個字元的寬度"""
    return ["{:>8d}".format(x) for x in num_list ]
num_list =[1,2,3,4,5,6,7,8,9]
num_list1=get_even_squares(num_list)
num_list2=get_odd_cubes(num_list)
num_list3=get_sliced_list(num_list)

print(",".join(format_numbers(num_list1)))
print(",".join(format_numbers(num_list2)))
print(",".join(format_numbers(num_list3)))