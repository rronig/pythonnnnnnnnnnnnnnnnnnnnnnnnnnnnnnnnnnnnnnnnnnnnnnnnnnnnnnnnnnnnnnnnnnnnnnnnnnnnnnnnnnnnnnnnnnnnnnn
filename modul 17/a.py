import streamlit as st

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


def main():
        st.title("BMI Calculator")
        # Labels
        st.write("Enter your name:")
        name_entry = st.text_input()
        st.write("Enter your age:")
        age_entry = st.number_input()
        st.write("Enter your weight (kg):")
        weight_entry = st.number_input()
        st.write("Enter your height (cm):")
        height_entry = st.number_input()
        s=st.form_submit_button("Calculate")

        if s:
            if name_entry and weight_entry>0 and height_entry>0:
                if age_entry < 18



# Run the GUI
if __name__ == "__main__":
    main()
