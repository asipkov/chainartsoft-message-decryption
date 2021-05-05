with open('cipheredmessage.txt') as file:
    str_input = file.read()

del_duplicate = []

while True:
    for index, el in enumerate(str_input[:-1]):
        if el == str_input[index + 1]:
            del_duplicate.append(el + el)

    for el in del_duplicate:
        if el in str_input:
            str_input = str_input.replace(el, "")

    if del_duplicate:
        del_duplicate.clear()
        continue
    else:
        break

print(str_input)
