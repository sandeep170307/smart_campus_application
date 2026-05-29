# Smart Campus Information System
# Integrated Mini Project

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Student Registration & Grade Evaluation
# -------------------------------

students = []

def register_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    score = float(input("Enter exam score: "))

    # Grade Evaluation
    if score >= 90:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    student = {
        "name": name,
        "age": age,
        "score": score,
        "grade": grade,
        "remark": remark
    }

    students.append(student)

    print("\nStudent Registered Successfully!")
    print("Grade:", grade)
    print("Remark:", remark)


# -------------------------------
# Course Enrollment Management
# -------------------------------

def enroll_courses():
    courses = []
    max_courses = 5

    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course = input("Enter course name (or done): ")

        if course.lower() == "done":
            break

        credits = input("Enter course credits: ")

        if not credits.isdigit():
            print("Invalid credits! Skipping...")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credits must be positive!")
            continue

        courses.append((course, credits))

    print("\nEnrolled Courses:")
    for c, cr in courses:
        print(c, "-", cr, "credits")


# -------------------------------
# Student Record Display
# -------------------------------

def display_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for s in students:
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Score:", s["score"])
        print("Grade:", s["grade"])
        print("Remark:", s["remark"])
        print("----------------------")


# -------------------------------
# Sorting and Searching
# -------------------------------

def sort_students():
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

    print("\nStudents Sorted by Score:")
    for s in sorted_students:
        print(s["name"], "-", s["score"])


def search_student():
    target = input("Enter student name to search: ")

    found = False

    for s in students:
        if s["name"].lower() == target.lower():
            print("\nStudent Found")
            print(s)
            found = True
            break

    if not found:
        print("Student not found.")


# -------------------------------
# Fee Calculation using Function
# -------------------------------

def calculate_fee(tuition, hostel=0, transport=0):
    return tuition + hostel + transport


def fee_module():
    tuition = float(input("Enter tuition fee: "))
    hostel = float(input("Enter hostel fee: "))
    transport = float(input("Enter transport fee: "))

    total = calculate_fee(tuition, hostel, transport)

    print("Total Fee =", total)


# -------------------------------
# File Handling
# -------------------------------

def save_records():
    with open("student_records.txt", "w") as file:
        file.write("Name,Age,Score,Grade\n")

        for s in students:
            file.write(f"{s['name']},{s['age']},{s['score']},{s['grade']}\n")

    print("Records saved successfully.")


def read_records():
    try:
        with open("student_records.txt", "r") as file:
            print("\nStored Records:")
            print(file.read())

    except FileNotFoundError:
        print("File not found!")


# -------------------------------
# Directory Scanning
# -------------------------------

class EmptyFolderError(Exception):
    pass


def scan_directory():
    path = input("Enter directory path: ")

    try:
        if not os.path.exists(path):
            raise FileNotFoundError("Invalid path!")

        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level

            print(f"{indent}{os.path.basename(root)}/")

            for f in files:
                print(" " * 4 * (level + 1) + f)

            if not files and not dirs:
                raise EmptyFolderError("Empty Folder Detected")

    except FileNotFoundError as e:
        print(e)

    except EmptyFolderError as e:
        print(e)

    except Exception as e:
        print("Unexpected Error:", e)


# -------------------------------
# Performance Analytics
# -------------------------------

def performance_analysis():

    if len(students) == 0:
        print("No student data available.")
        return

    data = {
        "Name": [s["name"] for s in students],
        "Score": [s["score"] for s in students]
    }

    df = pd.DataFrame(data)

    print("\n--- Student Data ---")
    print(df)

    scores = np.array(df["Score"])

    print("\nMean Score:", np.mean(scores))
    print("Median Score:", np.median(scores))
    print("Standard Deviation:", np.std(scores))

    # Graph
    plt.bar(df["Name"], df["Score"])
    plt.title("Student Performance")
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.show()


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
    print("1. Register Student")
    print("2. Course Enrollment")
    print("3. Display Student Records")
    print("4. Sort Students")
    print("5. Search Student")
    print("6. Fee Calculation")
    print("7. Save Records to File")
    print("8. Read Records from File")
    print("9. Scan Directory")
    print("10. Performance Analysis")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        enroll_courses()

    elif choice == "3":
        display_students()

    elif choice == "4":
        sort_students()

    elif choice == "5":
        search_student()

    elif choice == "6":
        fee_module()

    elif choice == "7":
        save_records()

    elif choice == "8":
        read_records()

    elif choice == "9":
        scan_directory()

    elif choice == "10":
        performance_analysis()

    elif choice == "11":
        print("Exiting System...")
        break

    else:
        print("Invalid choice! Try again.")