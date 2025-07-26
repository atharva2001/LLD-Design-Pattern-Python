class Student:
    def fake_attendance(self):
        pass 

class RealStudent(Student):

    def fake_attendance(self, subject):
        print(f"Faked attendace to: {subject} subject")


class ProxyStudent(Student):
    def __init__(self):
        self.hard_subject = ["maths", "english", "history"]
    def fake_attendance(self, subject):
        if subject.lower() in self.hard_subject:
            print(f"Can't fake attenadance in {subject}")
        else:
            self.real_student = RealStudent()
            self.real_student.fake_attendance(subject)

sham = ProxyStudent()
sham.fake_attendance("maths")
sham.fake_attendance("hindi")