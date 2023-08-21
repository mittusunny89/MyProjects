my_list = ['orange','apple','coconut','grape','coco']
new_list = []

while my_list:
    min = my_list[0]
    for item in my_list:
        if item < min:
            min = item
    new_list.append(min)
    my_list.remove(min)
print(new_list)