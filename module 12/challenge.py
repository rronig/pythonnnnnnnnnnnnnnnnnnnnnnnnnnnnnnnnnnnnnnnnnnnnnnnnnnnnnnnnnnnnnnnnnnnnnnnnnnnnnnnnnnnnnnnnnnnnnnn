import tkinter as tk
from tkinter import messagebox


class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        height_m = self.height / 100
        bmi = self.weight / (height_m ** 2)
        return round(bmi, 1)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Healthy"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def get_info(self):
        return (f"\nName: {self.name}"
                f"\nAge: {self.age}"
                f"\nWeight: {self.weight}"
                f"\nHeight: {self.height}"
                f"\nBMI: {self.calculate_bmi()}"
                f"\nBMI Category: {self.get_bmi_category()}")


class Adult(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)


class Kids(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)

    def calculate_bmi(self):
        base_bmi = super().calculate_bmi()
        kids_bmi = base_bmi * 1.3
        return round(kids_bmi, 1)


class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.people = []  # store all persons added

        # Labels
        tk.Label(root, text="Enter your name:").grid(row=0, column=0, sticky="e")
        tk.Label(root, text="Enter your age:").grid(row=1, column=0, sticky="e")
        tk.Label(root, text="Enter your weight (kg):").grid(row=2, column=0, sticky="e")
        tk.Label(root, text="Enter your height (cm):").grid(row=3, column=0, sticky="e")

        # Entries
        self.name_entry = tk.Entry(root)
        self.age_entry = tk.Entry(root)
        self.weight_entry = tk.Entry(root)
        self.height_entry = tk.Entry(root)

        self.name_entry.grid(row=0, column=1)
        self.age_entry.grid(row=1, column=1)
        self.weight_entry.grid(row=2, column=1)
        self.height_entry.grid(row=3, column=1)

        # Button
        self.calc_button = tk.Button(root, text="Calculate BMI", command=self.run)
        self.calc_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Result
        self.result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        try:
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if age >= 18:
                return Adult(name, age, weight, height)
            else:
                return Kids(name, age, weight, height)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for age, weight, and height.")
            return None

    def print_results(self):
        if self.people:
            latest = self.people[-1]  # show only the latest added
            self.result_label.config(text=latest.get_info())

    def run(self):
        person = self.collect_user_data()
        if person:
            self.add_person(person)
            self.print_results()


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
