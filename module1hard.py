grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

stud_list = list(students)
stud_list_OK = []
stud_dict = {}
grades_avg = []

for i in range(len(stud_list)):
    minim = min(stud_list)
    grades_avg.append(sum(grades[i]) / len(grades[i]))
    stud_list_OK.append(minim)
    stud_list.remove(minim)
    stud_dict.update({stud_list_OK[i]: grades_avg[i]})
print(stud_dict)
