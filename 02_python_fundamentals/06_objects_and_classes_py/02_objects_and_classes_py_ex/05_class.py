class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(float(grade))

    def get_average_grade(self):
        average = sum(self.grades) / len(self.students)
        return float(average)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {(self.get_average_grade()):.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)