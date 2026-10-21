"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable shared by instances unless overridden.
    organization = "Generic University"

    def __init__(self, name, age):
        # Instance variables.
        self.name = name
        self.age = age

    def display_info(self):
        """Return information about the person."""
        return (
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Organization: {self.organization}"
        )


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable belonging to the child class.
    program = "Computer Science"

    def __init__(self, name, age, student_id, courses=None):
        # Initialize attributes inherited from ParentClass.
        super().__init__(name, age)

        # New instance variables.
        self.student_id = student_id
        self.courses = courses if courses is not None else []

    # Override the parent's display_info() method.
    def display_info(self):
        """Return information about the student."""
        return (
            f"Student Name: {self.name}, "
            f"Age: {self.age}, "
            f"Student ID: {self.student_id}, "
            f"Program: {self.program}, "
            f"Organization: {self.organization}"
        )

    # New method demonstrating additional child-class functionality.
    def enroll_course(self, course_name, grade):
        """Add a course and its grade to the student's course list."""
        self.courses.append({
            "course_name": course_name,
            "grade": grade
        })

        print(f"{self.name} enrolled in {course_name}.")

    # Student-created extension:
    # Calculate the average grade across all enrolled courses.
    def calculate_average(self):
        """Return the average grade for all enrolled courses."""
        if not self.courses:
            return 0.0

        total = sum(course["grade"] for course in self.courses)
        return total / len(self.courses)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two objects of the child class.
    student1 = ChildClass("Alex", 20, "S1001")
    student2 = ChildClass("Jordan", 22, "S1002")

    # Access a class variable through the class itself.
    print("\nAccessing the class variable through the class:")
    print("Program:", ChildClass.program)

    # Access the same class variable through an object.
    print("\nAccessing the class variable through an object:")
    print("Student 1 program:", student1.program)
    print("Student 2 program:", student2.program)

    # Add a new attribute to only one object after creation.
    student1.favorite_subject = "Programming"

    print("\nAdding a new attribute to Student 1:")
    print("Student 1 favorite subject:", student1.favorite_subject)

    # Verify that Student 2 does not have this attribute.
    print(
        "Does Student 2 have favorite_subject?",
        hasattr(student2, "favorite_subject")
    )

    # Display each object's instance namespace.
    print("\nStudent 1 instance namespace (__dict__):")
    print(student1.__dict__)

    print("\nStudent 2 instance namespace (__dict__):")
    print(student2.__dict__)

    # Display information about the class namespace.
    print("\nChildClass namespace:")
    print(ChildClass.__dict__)

    # Demonstrate how an instance attribute can override
    # the class variable for one object.
    student2.program = "Information Technology"

    print("\nAfter changing Student 2's program:")
    print("Student 1 program:", student1.program)
    print("Student 2 program:", student2.program)
    print("Class program:", ChildClass.program)

    print("\nStudent 2 instance namespace after the change:")
    print(student2.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object containing nested mutable data.
    original = ChildClass(
        "Taylor",
        21,
        "S1003",
        courses=[
            {"course_name": "Python Programming", "grade": 90},
            {"course_name": "Database Systems", "grade": 85}
        ]
    )

    # A shallow copy creates a new outer object, but its nested
    # course list and dictionaries are shared with the original.
    shallow_copy = copy(original)

    # A deep copy creates a new outer object and independently
    # copies nested objects, including the course list and dictionaries.
    deep_copy = deepcopy(original)

    print("\nOriginal object before modification:")
    print(original.__dict__)

    print("\nShallow copy before modification:")
    print(shallow_copy.__dict__)

    print("\nDeep copy before modification:")
    print(deep_copy.__dict__)

    # Modify the nested data in the original object.
    original.courses[0]["grade"] = 100

    print("\nAfter changing the original's first course grade to 100:")

    print("\nOriginal object:")
    print(original.__dict__)

    print("\nShallow copy:")
    print(shallow_copy.__dict__)

    print("\nDeep copy:")
    print(deep_copy.__dict__)

    # Verify whether the course lists are shared.
    print("\nChecking the copying results:")

    print(
        "Original and shallow copy share the course list:",
        original.courses is shallow_copy.courses
    )

    print(
        "Original and deep copy share the course list:",
        original.courses is deep_copy.courses
    )

    print("\nFirst course grades after modification:")
    print("Original grade:", original.courses[0]["grade"])
    print("Shallow copy grade:", shallow_copy.courses[0]["grade"])
    print("Deep copy grade:", deep_copy.courses[0]["grade"])


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent-class object.
    print("\n=== Parent Class Object ===")

    person = ParentClass("Morgan", 35)

    print(person.display_info())

    # Create and test a child-class object.
    print("\n=== Child Class Object ===")

    student = ChildClass("Casey", 23, "S1004")

    print(student.display_info())

    # Demonstrate inheritance by accessing a class variable
    # defined in the parent class.
    print("\n=== Inheritance Demonstration ===")

    print("Organization inherited from ParentClass:", student.organization)

    # Demonstrate the new method in the child class.
    print("\n=== Course Enrollment ===")

    student.enroll_course("Python Programming", 92)
    student.enroll_course("Computer Networks", 88)

    print("Student courses:", student.courses)

    # Student-created extension:
    # Calculate and display the average course grade.
    print("\n=== Student-Created Extension ===")

    print(f"Average course grade: {student.calculate_average():.2f}")

    # Call the required demonstration functions.
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
