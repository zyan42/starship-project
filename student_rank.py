
align = 150
divider = (66 * '-').center(align)  # heading's settings
divider2 = (30 * '*').center(align)

# heading
print(divider)
print('student marks and rank updater'.title().center(align))
print(divider)

print('\n')

# 3 lists
names = ['manish', 'jayant', 'aditya', 'jon snow', 'shivam', 'david']
marks = [99, 74, 66, 34, 22, 18]
rank = []


def find_index(new_marks, marks, index):
    # print(index)
    for i in range(len(marks)):
        if new_marks[index] == marks[i]:
            return i


def replace_values(new_marks, marks):
    for i in range(len(marks)):
        new_marks.append(marks[i])


def max_marks(names, new_marks, marks):
    n = new_marks.index(max(new_marks))
    # print(marks.index(max(new_marks)))
    print((59 * ' '), 'name:', names[find_index(new_marks, marks, n)], end='')
    print('(' + str(new_marks[n]) + ')')


def display_info(names, marks, rank, new_marks):
    print('Names\tMarks(out of 100)\t Rank'.center(align))
    print('\n')
    replace_values(new_marks, marks)
    # print(marks)
    new_marks.sort(reverse=True)
    # print(new_marks)
    # print(marks)
    for i in range(len(names)):
        n = find_index(new_marks, marks, i)
        print((59 * ' '), names[n], end='')
        print('\t', new_marks[i], '\t'.expandtabs(21), end='')
        rank.append(i + 1)
        print(rank[i])


def update_marks(names, marks):
    print('Update Marks\n'.center(align))
    print('Names\tUpdate Marks(out of 100)'.center(align))
    print('\n')
    i = 0

    while (i < len(marks)):
        print((59 * ' '), names[i], '\t'.expandtabs(21), end='')
        updated_marks = int(input())
        if (updated_marks >= 0 and updated_marks <= 100):
            marks[i] = updated_marks
            i += 1
        else:
            print('\n')
            print('!!! Invalid value!!!'.center(align))
            print('!!! Enter value betweeen 0 and 100 !!!'.center(align))
            continue


flag = 1
while (flag != 0):
    # displaying options
    print(divider2)
    text = 'Select one option:\n '.center(align)
    opt_1 = '1) Display name, marks and rank'.center(152)
    opt_2 = '2) Update marks'.center(136)
    opt_3 = '3) Display name with max marks'.center(align)
    # opt_4 = '4) Rise/decline in rank (all students)'.center(158)
    # opt_5 = '5) Rise/decline in rank (by name)'.center(153)
    opt_4 = '4) Exit'.center(127)

    # printing the display options
    print(text)
    print(opt_1)
    print(opt_2)
    print(opt_3)
    # print(opt_4)
    # print(opt_5)
    print(opt_4)

    print('\n')
    a = input(70 * ' ' + 'Option: ')
    print('\n')

    if (a == '1'):
        new_marks = []
        update = marks
        display_info(names, marks, rank, new_marks)

    elif (a == '2'):

        update_marks(names, marks)
    elif (a == '3'):
        # print(new_marks)
        max_marks(names, new_marks, marks)
    elif (a == 'exit' or a == 'Exit' or a == '4'):
        flag = 0
    else:
        print('!!! Invalid option, Please select a valid option !!!'.center(align + 10))
        print('\n')
print('\n')
