marks_scored = [('A',20),('B',25),('C',40)]

def student_check(marks_scored):

    current_max = 0
    student_name= ''

    for student,marks in marks_scored:
        if marks> current_max:
            current_max = marks
            student_name =student
        else:
            pass

    return(student_name,current_max)

student_check(marks_scored)
print(student,marks)
