# 🎓 Student Grade Records

A command-line tool for creating and managing a simple school record. Users can enter student names and grades, view a summary of averages, and then look up the detailed grades for any specific student.

## Features

* **Student Data Entry**: Add multiple students with their names and two corresponding grades.
* **Automatic Averaging**: The script automatically calculates the average for each student.
* **Formatted Summary Table**: Displays a clean, aligned table showing each student's number, name, and final average.
* **Individual Grade Lookup**: After the summary is displayed, users can query the specific grades of any student by their number in the list.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `student_grade.py`).
3.  Run the script from your terminal:
    ```sh
    python student_grade.py
    ```
4.  **Phase 1: Data Entry**: Enter the name and two grades for each student. When asked to `Continue?`, enter `y` to add another student or `n` to finish.
5.  **Phase 2: Summary**: Once data entry is complete, a summary table will be displayed.
6.  **Phase 3: Lookup**: You can then enter a student's number to see their individual grades. Enter `999` to stop the lookup and exit the program.

### Example Session

```sh
> python student_grade.py
------Student Grades------
Enter the student name:
John
Enter the students first grade:
8.5
Enter the students second grade:
9.5
Continue?[y/n]
y
Enter the student name:
Maria
Enter the students first grade:
7.0
Enter the students second grade:
8.0
Continue?[y/n]
n
Program closed
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
No. NAME         AVERAGE
--------------------------
1   John               9.0
2   Maria              7.5
Enter the number of the student: [999 to stop] 
1
Johns grades are [8.5, 9.5]
Enter the number of the student: [999 to stop] 
999
```
