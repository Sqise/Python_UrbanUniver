immutable_var = 1, '2', False, [3, 4, True], 9.99
print (immutable_var)
# immutable_var[0] = 2
# операция выше невыполнима, поскольку
# переменная immutable_var является кортежем, а не списком
mutable_list = [9.99, [3, 4, True], False, '2', 1, 'yes']
print('old list: ', mutable_list)
mutable_list[0] = mutable_list[0] + 3
mutable_list[3] = mutable_list[3] * 3
mutable_list[5] = mutable_list[5].upper()
print('new list: ', mutable_list)
