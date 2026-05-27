import random

def int_check(question, min_num, infiniteMode=False, allowExit=False):

    while True:
        error = f"Please enter an integer more than / equal to {min_num}."

        to_check = input(question)

        # check for infinite mode
        if to_check == "" and infiniteMode == True:
            return "infinite"
        elif to_check == "xxx" and allowExit == True:
            return "xxx"
        
        try:
            response = int(to_check) # convert response to integer as comparing strings to integers will always return false

            # checks that the number is more than / equal to the minimum number
            if response < min_num:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

def instruction():
    print('''

**** Instructions ****

To begin, choose the number of questions (or press <enter> for
infinite mode)

Then, try your best to answer all the questions that show up.

Enter <xxx> to end the game at any time.

Good luck!

    ''')

# Main routine starts here

# Initialise game variables
mode = "regular"
game_history = []
operators = ["+","-","*","/"]
questions_played = 0
question_incorrect = 0

print("Mathematics Quiz")
print()

# Instructions

want_instructions = string_checker("Do you want to read the instructions? ")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of questions / infinite mode along with range.
num_questions = int_check("How many questions would you like? Push <enter> for infinite mode: ", 1, True)
range_max = int_check("What would you like the range to be? e.g 1 to 12. \n\n1 to ", 2)

if num_questions == "infinite":
    mode = "infinite"
    num_questions = 1

# Game loop starts here
while questions_played < num_questions:

    # questions headings
    if mode == "infinite":
        questions_heading = f"\nQuestion {questions_played + 1} (Infinite Mode, enter <xxx> to exit.)"
    else:
        questions_heading = f"\nQuestion {questions_played + 1} of {num_questions}"

    print(questions_heading)
    print()

    # get randomised integers and operators 
    randOp = random.choice(operators)
    randInt1 = random.randint(1,range_max)

    # ensure answer is a full number and can not be negative and make a display operator for multiplication and division
    if randOp == "+":
        randInt2 = random.randint(1,range_max)
        displayOp = "+"
    elif randOp == "*":
        randInt2 = random.randint(1,range_max)
        displayOp = "x"
    elif randOp == "-":
        randInt2 = random.randint(1, randInt1)
        displayOp = "-"
    elif randOp == "/":
        divisibleNumbers = [] # create a list to store divisible numbers

        for num in range(1,range_max + 1): # create a loop to run the checker for each number from 1 to range_max
            # divide the first random integer by the number of the loop
            divFloat = randInt1 / num
            divInteger = int(divFloat) # convert to an integer to get rid of the decimal place

            # if the number is not zero, then there is left over numbers from the float value
            if divFloat - divInteger == 0:
                divisibleNumbers.append(num) # add the number to the divisible numbers list

        displayOp = "÷"
        randInt2 = random.choice(divisibleNumbers) # choose a random number from the divisible list
            

    # calculate answer and get user response
    answer = int(eval(f"{randInt1} {randOp} {randInt2}")) # convert to integer to get rid of decimal place if question is division
    user_response = int_check(f"{randInt1} {displayOp} {randInt2} = ", 0, False, True)

    # If user choice is the exit code, break the loop
    if user_response == "xxx":
        break
    
    if user_response == answer:
        feedback = "correct!"
    else:
        feedback = f"incorrect, answer was {answer}."
        question_incorrect += 1 # Adjust question incorrect counter

    # Set up question feedback and output it to user.
    # Add it to the game history list (include the question number)
    question_feedback = f"{user_response} was {feedback}"
    history_item = f"Question {questions_played + 1} was {randInt1} {displayOp} {randInt2}, your answer of {question_feedback}"

    print(question_feedback)
    game_history.append(history_item)

    questions_played += 1

    # If users are in infinite mode, increase number of questions!
    if mode == "infinite":
        num_questions += 1


# Game loop ends here

# Game history / statistics area

if questions_played > 0:
    # Calculate Statistics

    questions_correct = questions_played - question_incorrect
    percent_correct = questions_correct / questions_played * 100
    percent_incorrect = question_incorrect / questions_played * 100

    print()
    print("Game statistics")
    print(f"Correct: {percent_correct:.2f}% \t "
        f"Incorrect: {percent_incorrect:.2f}% \t ")

    want_history = string_checker("Do you want to see your game history? ")
    if want_history == "yes":
        for item in game_history:
            print(item)
else:
    print("Oops - you chickened out!")