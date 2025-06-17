# Store the student GPA and student test score in two variables.
# Using nested conditionals check if the student is eligible for a full scholarship, partial, or no scholarship.
# Scholarship criteria:
# 3.  If a student has a GPA greater or equal to 3.5, and a test score of higher than 65, they’re eligible for a full scholarship.
# a.  If a student has a GPA greater or equal to 3.5, and a test score between 50 and 65, they’re eligible for a partial scholarship.
# b.  If a student has a GPA greater or equal to 3.5 but test score lower than 50, they’re not eligible for a scholarship.
# c.  If a student has a GPA lower than 3.5, they’re not eligible for a scholarship.
gpa=float(input("What is the GPA: "))
test=int(input("What is the test score: "))
if gpa>=3.5 and test>=65:
    print("Full scholarship")
elif gpa>=3.5 and 50<test<65:
    print("partial scholarship")
elif gpa>=3.5 and 50>test:
    print("no scholarship")
elif gpa<3.5:
    print("no scholarship")
