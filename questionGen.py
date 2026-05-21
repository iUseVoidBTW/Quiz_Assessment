import random
operators = ["+","-","*","/"]

while True:
    # get randomised integers and operators 
    randOp = random.choice(operators)
    randInt1 = random.randint(1,12)

    # ensure answer is a full number and can not be negative 
    if randOp == "+" or randOp == "*":
        randInt2 = random.randint(1,12)
    elif randOp == "-":
        randInt2 = random.randint(1, randInt1)
    elif randOp == "/":
        divisibleNumbers = [] # create a list to store divisible numbers

        for num in range(1,12): # create a loop to run the checker for each number from 1 to 12
            # divide the first random integer by the number of the loop
            divFloat = randInt1 / num
            divInteger = int(divFloat)

            # print all numbers for debugging purposes
            print(f"Base number: {num}")
            print(f"divFloat: {divFloat}")
            print(f"divInteger: {divInteger}")

            # if the number is not zero, then there is left over numbers from the float value
            if divFloat - divInteger == 0:
                print("Number is divisible!")
                divisibleNumbers.append(divInteger) # add the number to the divisible numbers list
            else:
                print("Number is not divisible.")
            
            print()

        print(divisibleNumbers) # print the list for testing purposes
        randInt2 = random.choice(divisibleNumbers) # choose a random number from the divisible list
            

    # calculate answer and get user response
    answer = eval(f"{randInt1} {randOp} {randInt2}")
    user_response = input(f"{randInt1} {randOp} {randInt2} = ")

    # print out both user response and answer incase code is broken
    print(f"User: {user_response}")
    print(f"Answer: {answer}")
    
    # convert response to integer as comparing strings to integers will always return false
    if int(user_response) == answer:
        print("Correct")
    else:
        print(f"Incorrect, answer was {answer}.")