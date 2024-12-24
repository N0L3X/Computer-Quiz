print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :)")
score = 0

questions_and_answers = [
    ("What does CPU stand for?", "central processing unit"),
    ("What does RAM stand for?", "random access memory"),
    ("What does HDD stand for?", "hard disk drive"),
    ("What does SSD stand for?", "solid state drive"),
    ("What does GPU stand for?", "graphics processing unit"),
    ("What does OS stand for?", "operating system"),
    ("What does URL stand for?", "uniform resource locator"),
    ("What does HTML stand for?", "hypertext markup language"),
    ("What does HTTP stand for?", "hypertext transfer protocol"),
    ("What does BIOS stand for?", "basic input output system")
]

# Schleife durch alle Fragen und Antworten
for question, correct_answer in questions_and_answers:
    answer = input(question + " ")
    if answer.lower() == correct_answer:
        print("Correct!")
    else:
        print("Incorrect!")
        score += 1

# Endergebnis
print(f"You got {score} questions correct!")
print(f"You got {score * 10}%.")

