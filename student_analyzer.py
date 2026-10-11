def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"{subject}marks(0-100):"))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100!")
        except ValueError:
            print("Please enter numbers only!")

def get_student_data():
    students = []
    subjects = ["Maths","Science","English"]

    n = int(input("How many students? "))
    for i in range(n):
        print(f"\nStudent {i + 1}")
        name = input("  Name: ")
        marks = {}
        for sub in subjects:
            marks[sub] = get_marks(sub)

        total = sum(marks.values())
        avg = total / len(subjects)

        students.append({
            "name": name,
            "marks": marks,
            "total": total,
            "average": round(avg, 2),
            "grade": get_grade(avg)
        })
    return students


def print_report(students):
    students = sorted(students, key=lambda s: s["total"], reverse=True)
    print("\n" + "=" * 55)
    print(f"{'Rank':<8}{'Name':<15}{'Total':<10}{'Average':<10}{'Grade':<10}")
    print("=" * 55)

    for rank, s in enumerate(students, start=1):
        print(f"{rank:<8}{s['name']:<15}{s['total']:<10}{s['average']:<10}{s['grade']:<10}")
    print("=" * 55)

    topper = max(students, key=lambda s: s["total"])
    lowest = min(students, key=lambda s: s["total"])
    class_avg = sum(s["average"] for s in students) / len(students)

    print(f"Topper        : {topper['name']} ({topper['total']})")
    print(f"Lowest        : {lowest['name']} ({lowest['total']})")
    print(f"Class Average : {class_avg:.2f}")

    passed = sum(1 for s in students if s["grade"] != "Fail")
    print(f"Pass / Fail   : {passed} / {len(students) - passed}")


def main():
    print("=== Student Marks Analyzer ===")
    students = get_student_data()
    print_report(students)


main()