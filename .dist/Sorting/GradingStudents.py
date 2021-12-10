def gradingStudents(grades):
    # Write your code here
    roundedGrades = []
    for i in range(len(grades)):
        if grades[i] < 38:
            roundedGrades.append(grades[i])
        elif grades[i] % 5 >=3 :
            roundedGrades.append(grades[i]+(5-grades[i]%5))
        else:
            roundedGrades.append(grades[i])
    return roundedGrades
