my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for i in my_list:
    if i.isdigit():
        new_list.extend(['"', f'{int(i):02}', '"'])        #new_list.extend([f'"{int(i):02}''"']) в таком виде нет пробелов в кавычках, но в список не
    elif i.startswith('+' or '-') and i[1:].isdigit():
        new_list.extend(['"', f'{i[0]}{int(i[1:]):2}', '"'])
    else:
        new_list.append(i)
print(new_list)
info = ' '.join(new_list)
print(info)