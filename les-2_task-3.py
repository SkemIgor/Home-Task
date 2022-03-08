my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

ind = 0
while ind < len(my_list):
    if my_list[ind].isdigit():
        my_list.insert(ind, '"')
        my_list[ind + 1] =  f'{int(my_list[ind + 1]):02}'
        my_list.insert(ind + 2, '"')
        ind += 2
    elif (my_list[ind].startswith('+' or '-')) and my_list[ind][1:].isdigit():

        my_list.insert(ind, '"')
        my_list[ind + 1] = f'{my_list[ind + 1][0]}{int(my_list[ind + 1]):02}'
        my_list.insert(ind + 2, '"')
        ind += 2
    ind += 1

info_str = ' '.join(my_list)
print(info_str)

