
list1 = [1, 1, 2, 3, 3, 4, 4, 4, 5, 0, 6]
new = []


def sort_list(copy):
    for i in copy:
        if i in new:
            continue
        else:
            new.append(i)

    return new


new_list = sort_list(list1)
print(new_list)