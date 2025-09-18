import datetime

class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

    def get_info(self):
        return f"Name: {self.__name}, City: {self.__city}, State: {self.__state}, Courses: {self.__courses}"

class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number, hackathon_date=None):
        super().__init__(name, city, state, courses)
        self.__student_number = student_number
        self.__hackathon_date = hackathon_date

    def SCF(self):
        print("Spring code fest is a code fest in spring in Prishtina")

    def organize_hackathon(self):
        self.__hackathon_date = datetime.date.today()
        print(f"Hackathon date set to: {self.__hackathon_date}")

    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Students: {self.__student_number}"

# Usage
ds = DS_Prishtina("DS", "Prishtina", "Kosovo", "Python, Java", 120)
print(ds.get_info())
ds.organize_hackathon()
