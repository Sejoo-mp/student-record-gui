import tkinter as tk
from tkinter import messagebox

COURSES = ["math", "AP", "BP", "data", "english"]

class Student:
    def __init__(self , Coefficient ,  id, name, number_phone, grades, student_number):
        self.id = id
        self.name = name
        self.number_phone = number_phone
        self.grades = grades
        self.Coefficient = Coefficient
        self.student_number = student_number

    def average(self):
        total = sum(score * self.Coefficient[course] for course, score in self.grades.items())
        return total / sum(self.Coefficient.values())
    
    def get_Academic_Record(self):
        return f"id : {self.id} , name is : {self.name} , your number phone is : {self.number_phone} , your grades is : {self.grades} , your student number is : {self.student_number} , Coefficient is : {self.Coefficient} , your average is : {self.average()}"


class MenuOfSelect:
    def __init__(self, root):
        self.root = root
        root.title("Menu")
        self.Extend_button = tk.Button(root, text="Extend Student", command=self.open_form)
        self.Extend_button.grid(row=0, column=0, rowspan=2,padx=5, pady=10)
        
                
        self.search_button = tk.Button(root, text="Search", command=self.search)
        self.search_button.grid(row=0, column=1, rowspan=2, padx=5, pady=10)
        
    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        MenuOfSelect(self.root) 
        
    def open_form(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        StudentApp(self.root)

    def search(self):
        self.root.title("Search Menu")
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Id:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.Id_entry = tk.Entry(self.root, width=30)
        self.Id_entry.grid(row=0, column=1, padx=10)
        
        tk.Button(self.root, text="Go Back", command=self.go_back).grid(row=3, column=0, columnspan=2, pady=10)

        self.get_search = tk.Button(self.root, text="Search", command=self.do_search)
        self.get_search.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.go_to_extend = tk.Button(self.root, text="Go To Extend Student", command=self.open_form)
        self.go_to_extend.grid(row=2, column=0, columnspan=2, pady=10)
        
    def do_search(self):
        target_id = self.Id_entry.get().strip()

        if not target_id:
            messagebox.showerror("Error", "Id can not be empty!")
            return

        try:
            with open("student.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith(f"id : {target_id} ,"):
                        messagebox.showinfo("Result", line)
                        return
        except FileNotFoundError:
            messagebox.showerror("Error", "student.txt not found!")
            return

        messagebox.showerror("Not found", f"No student with id {target_id}")

class StudentApp:
    def __init__(self, root):
        self.root = root
        root.title("Student Record")

        tk.Label(root, text="Id:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.Id_entry = tk.Entry(root, width=30)
        self.Id_entry.grid(row=0, column=1, padx=10)
        
        tk.Label(root, text="Name:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=1, column=1, padx=10)

        tk.Label(root, text="Phone:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=2, column=1, padx=10)

        tk.Label(root, text="Student number:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.number_entry = tk.Entry(root, width=30)
        self.number_entry.grid(row=3, column=1, padx=10)

        self.grade_entries = {}
        self.Coefficient_entries = {}
        
        for i, course in enumerate(COURSES):
            row = 4 + i * 2

            tk.Label(root, text=f"{course} grade:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(root, width=30)
            entry.grid(row=row, column=1, padx=10)
            self.grade_entries[course] = entry

            tk.Label(root, text=f"{course} Coefficient:").grid(row=row + 1, column=0, sticky="w", padx=10, pady=5)
            entry = tk.Entry(root, width=30)
            entry.grid(row=row + 1, column=1, padx=10)
            self.Coefficient_entries[course] = entry
        tk.Button(root, text="Submit", command=self.submit).grid(row=14, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Go Back", command=self.go_back).grid(row=15, column=0, columnspan=2, pady=10)
    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        MenuOfSelect(self.root)
            
        
        
    def submit(self):
        id = self.Id_entry.get().strip()
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        student_number = self.number_entry.get().strip()

        if not id or not name or not phone or not student_number:
            messagebox.showerror("Error", "Id, name, phone and student number can not be empty!")
            return

        grades = {}
        Coefficient = {}
        for course, entry in self.grade_entries.items():
            try:
                score = float(entry.get())
            except ValueError:
                messagebox.showerror("Error", f"{course}: please enter a number!")
                return
            if not (0 <= score <= 20):
                messagebox.showerror("Error", f"{course}: grade must be between 0 and 20!")
                return
            grades[course] = score
        for course , entry in self.Coefficient_entries.items():
            try:
                zarib = int(entry.get())
            except ValueError:
                messagebox.showerror("ERROR" , f"{course}: please enter a number!")
                return  
            if not (1 <= zarib <= 6):
                    messagebox.showerror("Error", f"{course}: coefficient must be between 1 and 6!")
                    return
            Coefficient[course] = zarib
        s = Student(Coefficient , id,name, phone, grades, student_number)
        record = s.get_Academic_Record()

        with open("student.txt", "a", encoding="utf-8") as f:
            f.write(record + "\n")

        messagebox.showinfo("Saved", record)


if __name__ == "__main__":
    root = tk.Tk()
    MenuOfSelect(root)
    root.mainloop()