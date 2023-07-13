average = []
studentx = []

for j in range(0, 5):
  student = []
  sumx = 0
  for i in range(0, 5):
      mark = int(input(f"Enter the marks of student {j+1}: "))
      student.append(mark)
      sumx += mark
  studentx.append(student)
  average.append(sumx/5)

print(studentx)
print(average)
    