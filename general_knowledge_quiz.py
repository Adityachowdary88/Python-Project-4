
print("Welcome to the General Knowledge Quiz!")

score = 0

answer1 = input("1. What is the national bird of India? ")

if answer1.lower() == "peacock":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")

answer2 = input("2. Which planet is closest to the sun?")

if answer2.lower() == "mercury":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")

answer3 = input("3. Which gas do humans need to breathe?")

if answer3.lower() == "oxygen":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")

answer4 = input("4. How many continents are there in the world?")

if answer4.lower() == "seven":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")

print("\nQuiz Completed!")
print("Your Final Score is:", score, "/4")
