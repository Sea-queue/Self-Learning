class Student:

    def __init__(self, name, major, gpa, is_on_coop):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_coop = is_on_coop

    def student_name(self):
        return self.name

    def good_to_graduate(self):
        if self.is_on_coop:
            return True
        else:
            return False
