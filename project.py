class Student:
    def __init__(self , name , number_phone , grades , student_number):
        self.name = name
        self.number_phone = number_phone
        self.grades = grades
        self.student_number = student_number
    def average(self):
        return sum(self.grades.values()) / len(self.grades)
    def get_Academic_Record(self):
        return  f"name is : {self.name} , your number phone is : {self.number_phone} , your grades is : {self.grades} , your student number is : {self.student_number} , your average is : {self.average()}"
    
    
def main():
        name = get_value("plz enter your name : ")
        number_phone = get_value("plz enter your number_phone : ")
        grades = {}
        for course in ["math", "AP", "BP", "data", "english"]:
            while True:
                try:
                    score = float(input(f"plz enter your grade in {course} course : "))
                    if 0 <= score <= 20:
                        break
                    print("your score must be between 0 and 20 !!!")
                except ValueError:
                    print("plz enter a number !!!")
            grades[course] = score
        student_number = get_value("plz enter your student_number : ")
  
        s = Student(name , number_phone , grades , student_number)
        print(s.get_Academic_Record())
        with open("student.txt" , "a" , encoding="utf-8") as f:
            f.write(s.get_Academic_Record() + "\n")
        
        
        
        
def get_value(masseage):
    while True:
        value = input(masseage).strip()
        if value:
            break
        print("plz enter again !!!")
    return value
        
        
        
if __name__ == "__main__":
    main()