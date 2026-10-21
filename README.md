# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

* Create parent and child classes
* Use inheritance to extend functionality
* Understand class and instance namespaces
* Demonstrate shallow and deep copying
* Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation Summary

For this assignment, I created a Python program that demonstrates object-oriented programming concepts through a student and course management example.

I created a parent class named `ParentClass` that stores a person's name and age. It also includes a class variable representing the organization and a method that displays information about the object.

I then created a child class named `ChildClass` that inherits from `ParentClass`. The child class adds a student ID, a list of courses, and a program class variable. It also overrides the parent's `display_info()` method and includes a method for enrolling students in courses.

I demonstrated class and instance namespaces by creating two student objects and examining their attributes using `__dict__`. I also added an attribute to only one object to demonstrate how instance attributes can differ between objects.

I demonstrated shallow and deep copying by creating copies of a student object containing a nested course list. After modifying the original object's course grade, I observed that the shallow copy reflected the change while the deep copy retained the original grade.

For my student-created extension, I added a `calculate_average()` method that calculates a student's average grade across enrolled courses. The method also handles an empty course list by returning `0.0`.

Finally, I used the `main()` function to create and test parent and child objects, demonstrate inheritance, enroll a student in courses, calculate an average grade, and run the namespace and copying demonstrations.

## Testing

I ran the Python program in PyCharm and verified that it executed successfully.

The program successfully demonstrated:

* Parent and child class creation.
* Inheritance and method overriding.
* Access to class and instance attributes.
* Instance namespace inspection using `__dict__`.
* Differences between shallow and deep copying.
* Course enrollment and average-grade calculation.

The copying demonstration confirmed that the original object and shallow copy shared the same nested course list, while the deep copy maintained an independent course list.

After changing the original course grade from `90` to `100`, the original and shallow copy both displayed `100`, while the deep copy retained the grade of `90`. The student-created extension also calculated an average grade of `90.00` for a student with grades of `92` and `88`.

The program finished successfully with exit code `0`.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this to managing overhead, practical application development, and future use.

### Reflection

For this assignment, I learned how object-oriented programming works in Python, particularly inheritance, namespaces, and shallow versus deep copying. I created a student management program to demonstrate these concepts. My parent class stored basic information about a person, while my child class inherited those attributes and added student-specific functionality.

One challenge I encountered was understanding why modifying the original object's nested course list also changed the shallow copy but not the deep copy. I overcame this by running the program and comparing the results of both copying methods.
Another challenge I faced was understanding GitHub and having to upload everything correctly. In fact, I am still unsure if I did this correctly. This was my first time using GitHub.

Compared to procedural programming, OOP organizes code into classes and objects rather than relying primarily on functions and sequential instructions. This can make programs easier to maintain and allows developers to reuse existing code. However, OOP can introduce additional complexity and overhead when creating and managing classes, which may not be necessary for smaller programs.

I can apply OOP when developing applications that manage students, courses, inventories, or other related information. These concepts will help me build more organized, reusable, and maintainable programs in future projects.
