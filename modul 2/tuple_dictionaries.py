grade={("John", "Math"):5,("John", "English"):4,("Alice", "Biology"):4,("Bob", "Physics"):3.5,("Eve", "Music"):5}
john_math=grade[("John", "Math")]
grade[("Bob", "Math")]=3
print("John's grade in math is", john_math)
keys=list(grade.keys())
student, subject=keys[0]
print(f"{student}'s grade in", subject, "is", john_math)