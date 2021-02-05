txt = input('Напиши или введи цифры ')
my_list = list(txt)
print('ввели', my_list)
a = 0
for i in range(len(my_list) // 2):
     my_list[a], my_list[a + 1] = my_list[a + 1], my_list[a]
     a += 2
print('итог ', my_list)