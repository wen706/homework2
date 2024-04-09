def get_even_squares(num_list:list[int])->list[int]:
    return [x**2 for x in num_list if x % 2 == 0]#偶數的平方還是偶數,奇數的平方還是奇數

num_list =[1,2,3,4,5,6,7,8,9]

print(get_even_squares(num_list))