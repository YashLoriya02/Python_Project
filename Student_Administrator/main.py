import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

conn = sqlite3.connect("student_database.db")
cursor = conn.cursor()

def enter_student_data():
    student_id = student_id_entry.get()
    student_name = student_name_entry.get()
    student_surname = student_surname_entry.get()
    dob = dob_entry.get()

    cursor.execute('''
        INSERT INTO Student (StudentId, StudentName, StudentSurname, DOB)
        VALUES (?, ?, ?, ?)
    ''', (student_id, student_name, student_surname, dob))

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student data entered successfully!")

def enter_test_data():
    test_id = test_id_entry.get()
    student_id = student_id_test_entry.get()
    student_name = student_name_entry.get()
    date_of_test = date_of_test_entry.get()
    physics_marks = physics_marks_entry.get()
    chemistry_marks = chemistry_marks_entry.get()
    maths_marks = maths_marks_entry.get()

    conn = sqlite3.connect("student_database.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Test (TestId, StudentId, StudentName, DateOfTest, PhysicsMarks, ChemistryMarks, MathsMarks)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (test_id, student_id, student_name, date_of_test, physics_marks, chemistry_marks, maths_marks))

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Test data entered successfully!")

def show_graphical_data():
    student_id = student_id_graph_entry.get()

    conn = sqlite3.connect("student_database.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT TestId, PhysicsMarks, ChemistryMarks, MathsMarks
        FROM Test
        WHERE StudentId = ?
    ''', (student_id,))

    data = cursor.fetchall()

    if not data:
        messagebox.showwarning("Warning", f"No data found for StudentId {student_id}")
        return

    test_ids, physics_marks, chemistry_marks, maths_marks = zip(*data)

    test_ids = list(map(str, test_ids))

    fig, ax = plt.subplots()
    ax.plot(test_ids, physics_marks, label='Physics', color='blue', marker='o')
    ax.plot(test_ids, chemistry_marks, label='Chemistry', color='green', marker='o')
    ax.plot(test_ids, maths_marks, label='Maths', color='red', marker='o')
    
    ax.set_xlabel('Test Id')
    ax.set_ylabel('Marks')
    ax.legend()

    graph_window = tk.Toplevel(window)
    graph_window.title("Graphical Data")
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    conn.close()

window = tk.Tk()
window.title("Student Database GUI")

# Student Data Entry
tk.Label(window, text="Enter Student Data").grid(row=0, column=0, columnspan=2)
tk.Label(window, text="Student Id:").grid(row=1, column=0)
student_id_entry = tk.Entry(window)
student_id_entry.grid(row=1, column=1)
tk.Label(window, text="Student Name:").grid(row=2, column=0)
student_name_entry = tk.Entry(window)
student_name_entry.grid(row=2, column=1)
tk.Label(window, text="Student Surname:").grid(row=3, column=0)
student_surname_entry = tk.Entry(window)
student_surname_entry.grid(row=3, column=1)
tk.Label(window, text="DOB:").grid(row=4, column=0)
dob_entry = tk.Entry(window)
dob_entry.grid(row=4, column=1)

tk.Button(window, text="Enter Student Data", command=enter_student_data).grid(row=5, column=0, columnspan=2)

# Test Data Entry
tk.Label(window, text="Enter Test Data").grid(row=6, column=0, columnspan=2)
tk.Label(window, text="Test Id:").grid(row=7, column=0)
test_id_entry = tk.Entry(window)
test_id_entry.grid(row=7, column=1)
tk.Label(window, text="Student Id:").grid(row=8, column=0)
student_id_test_entry = tk.Entry(window)
student_id_test_entry.grid(row=8, column=1)
tk.Label(window, text="Physics Marks:").grid(row=9, column=0)
physics_marks_entry = tk.Entry(window)
physics_marks_entry.grid(row=9, column=1)
tk.Label(window, text="Chemistry Marks:").grid(row=10, column=0)
chemistry_marks_entry = tk.Entry(window)
chemistry_marks_entry.grid(row=10, column=1)
tk.Label(window, text="Maths Marks:").grid(row=11, column=0)
maths_marks_entry = tk.Entry(window)
maths_marks_entry.grid(row=11, column=1)
tk.Label(window, text="Date of Test:").grid(row=12, column=0)
date_of_test_entry = tk.Entry(window)
date_of_test_entry.grid(row=12, column=1)

tk.Button(window, text="Enter Test Data", command=enter_test_data).grid(row=13, column=0, columnspan=2)

tk.Label(window, text="Show Graphical data of Student=").grid(row=14, column=0, sticky=tk.W)
student_id_graph_entry = tk.Entry(window)
student_id_graph_entry.grid(row=14, column=1, sticky=tk.W)
tk.Button(window, text="Show Graphical Data", command=show_graphical_data).grid(row=14, column=5, sticky=tk.W)

window.mainloop()

conn.close()