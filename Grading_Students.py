
def gradingStudents(grades):

    for i in range(len(grades)):
        if grades[i] > 37 and (grades[i] + 1) % 5 == 0:
            grades[i] = grades[i] + 1

        elif grades[i] > 37 and (grades[i] + 2) % 5 == 0:
            grades[i] = grades[i] + 2

    return grades


test_array = [73, 67, 38, 33]
print(gradingStudents(test_array))
