INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_sum = 0
python_sum = 0
english_sum = 0
count = 0

best_student_name = ""
best_average = -1.0

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    for line in f:  #йдемо по списку студентів
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        name = parts[0]
        math = float(parts[1])
        python = float(parts[2])
        english = float(parts[3])

        math_sum += math
        python_sum += python
        english_sum += english
        count += 1

        current_average = (math + python + english) / 3 #середній бал на студента

        if current_average > best_average:
            best_average = current_average
            best_student_name = name

if count > 0:
    math_average = math_sum / count #середні бали
    python_average = python_sum / count
    english_average = english_sum / count
else:
    math_average = python_average = english_average = 0

result = (
    f"Середній бал по класу:\n"
    f"math: {math_average}\n"
    f"python: {python_average}\n"
    f"english: {english_average}\n"
    f"Найкращий студент: {best_student_name} його бал: {best_average}"
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    out.write(result)

print(result)