#-------------------------
def new_game():
    guesses =[]
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses,guesses)
#-------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#-------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")



#-------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#-------------------------

questions = {"How many drinks a day should men drink and women drink?: " : "B",
             "How many minutes a day of exercise should you have?: " : "A",
             "How long should you stretch before a workout?: " : "A",
             "How long should your workout routine be?: " : "C",
             "How many hours of sleep should you get a night?: " : "C"}

options = [["A. Men: 20 cups; Women: 17 cups", "B. Men: 15.5 cups; Women: 11.5 cups", "C. Men: 25 cups; Women: 5 cups", "D. Men: 2 cups; Women: 1 cup"],
           ["A. 30 minutes", "B. 5 minutes", "C. 10 minutes", "D. 120 minutes"],
           ["A. 5-10 minutes", "B. 30-45 minutes", "C. 120 minutes", "D. 60 minutes"],
           ["A. 30-45 minutes", "B. 50 minutes", "C. 75-150 minutes", "D. 20 minutes" ],
           ["A. 3-4 hours", "B. 1-2 hours", "C. 7-9 hours", "D. 5-6 hours"]]

new_game()

while play_again():
    new_game()

print("Thanks for trying out the Fitness Quiz!")
