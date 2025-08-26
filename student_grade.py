# School record

record = []

print('------Student Grades------')

while True:
	student_name = str(input('Enter the student name:\n'))
	student_grade_1 = float(input('Enter the students first grade:\n'))
	student_grade_2 = float(input('Enter the students second grade:\n'))
	grade_average = (student_grade_1 + student_grade_2)/ 2
	
	record.append([student_name, [student_grade_1, student_grade_2], grade_average])
	
	user_continue = input('Continue?[y/n]\n').strip().lower()[0]
	if user_continue in 'nN':
		print('Program closed')
		break
		
print('-=' * 30)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-' * 26)

for i, student in enumerate(record):
	print(f'{i+1:<4}{student[0]:<10}{student[2]:>8.1f}')
	
while True:
	find_student = int(input('Enter the number of the student: [999 to stop] \n'))
	find_student -= 1
	if find_student == 999:
		break
	if find_student <= len(record) - 1:
		print(f'{record[find_student][0]}s grades are {record[find_student][1]}')
	