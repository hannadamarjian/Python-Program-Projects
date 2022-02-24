# Step 2: Go through the function:

def arithmetic_arranger(problems, answer):

    if len(problems) > 5:
        print("Error: Too many problems.")
        quit()
    first_operand = list()
    op_sign = list()
    second_operand = list()

    for problem in problems:
        pieces = problem.split()
        first_operand.append(pieces[0])
        op_sign.append(pieces[1])
        second_operand.append(pieces[2])

    for sign in op_sign:
        if sign == "*" or sign == "/":
            print("Error: Operator must be '+' or '-'.")
            quit()

    for op1 in first_operand:
        if len(op1) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        try:
            integer = int(op1)
        except:
            print("Error: Numbers must only contain digits.")
            quit()

    for op2 in second_operand:
        if len(op2) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        try:
            integer = int(op2)
        except:
            print("Error: Numbers must only contain digits.")
            quit()


    new_str1 = ''  # an empty string to add each of the stringed integers.
    str1 = '  '  # a string with two whitespaces for each sign.

    # For for first line:
    for i in range(len(first_operand)):  # length of first_operand is dependent upon how many numbers the user inputs.
        if len(str(first_operand[i])) < len(str(second_operand[i])):
            numb_of_spaces1 = len(str(second_operand[i])) - len(str(first_operand[i]))
            new_str1 = new_str1 + str1 + ' ' * numb_of_spaces1 + str(first_operand[i]) + ' ' * 4
        else:
            new_str1 = new_str1 + str1 + str(first_operand[i]) + ' ' * 4

    # For second line:
    new_str2 = ''  # a string with no whitespaces
    str2 = ' '  # a string with one whitespace

    # For third line, the number of underscores depends on the sign:
    new_str3 = ''

    for j in range(len(second_operand)):  # length of op_sign is dependent upon how many numbers the user inputs.
        if len(str(first_operand[j])) > len(str(second_operand[j])):
            numb_of_spaces2 = len(str(first_operand[j])) - len(str(second_operand[j]))
            new_str2 = new_str2 + str(op_sign[j]) + str2 + ' ' * numb_of_spaces2 + str(second_operand[j]) + ' ' * 4
            new_str3 = new_str3 + '_' * len(str(op_sign[j]) + str2 + ' ' * numb_of_spaces2 + str(second_operand[j])) + ' ' * 4
        else:
            new_str2 = new_str2 + str(op_sign[j]) + str2 + str(second_operand[j]) + ' ' * 4
            new_str3 = new_str3 + '_' * len(str(op_sign[j]) + str2 + str(second_operand[j])) + ' ' * 4

    # If the user wants the answers to their problems

    if answer == "True":
        new_str4 = ''  # create an empty string for the answers
        str4 = '  '  # string with two whitespaces
        str4_b = ' '  # string with one whitespace for negative numbers
        for m in range(len(op_sign)):
            if op_sign[m] == '+':
                outcome = int(first_operand[m]) + int(second_operand[m])
                if outcome >= 0 and (len(str(outcome)) > len(str(first_operand[m])) and len(str(outcome)) > len(str(second_operand[m]))):
                    new_str4 = new_str4 + str4_b + str(outcome) + ' '*4 # adds two spaces for 4 or less digits
                else:
                    new_str4 = new_str4 + str4 + str(outcome) + ' '*4 # adds one white space for 5 digits

            else:
                outcome = int(first_operand[m]) - int(second_operand[m])
                if outcome < 0:
                    new_str4 = new_str4 + str4_b + str(outcome) + ' '*4
                elif outcome == 0:
                    numb_of_spaces4 = len(str(first_operand[m])) - len(str(outcome))
                    new_str4 = new_str4 + str4 + ' ' * numb_of_spaces4 + str(outcome) + ' ' * 4
                else:
                    if len(first_operand[m]) == 4 and len(str(outcome)) == 4:
                        new_str4 = new_str4 + str4 + str(outcome) + ' '*4 # four digits for both first operand and outcome
                    elif len(first_operand[m]) == 4 and len(str(outcome)) == 3:
                        new_str4 = new_str4 + ' '*3 + str(outcome) + ' '*4 # four digits for first operand and three digits for outcome
                    elif len(first_operand[m]) == 4 and len(str(outcome)) == 2:
                        new_str4 = new_str4 + ' '*4 + str(outcome) + ' '*4 # four digits for first operand and two digits for outcome
                    elif len(first_operand[m]) == 4 and len(str(outcome)) == 1:
                        new_str4 = new_str4 + ' '*5 + str(outcome) + ' '*4 # four digits for first operand and one digit for outcome
                    elif len(first_operand[m]) == 3 and len(str(outcome)) == 3:
                        new_str4 = new_str4 + str4 + str(outcome) + ' '*4 # three digits for first operand and three digits for outcome
                    elif len(first_operand[m]) == 3 and len(str(outcome)) == 2:
                        new_str4 = new_str4 + ' '*3 + str(outcome) + ' '*4 # three digits for first operand and two digits for outcome
                    elif len(first_operand[m]) == 3 and len(str(outcome)) == 1:
                        new_str4 = new_str4 + ' '*4 + str(outcome) + ' '*4 # three digits for first operand and one digit for outcome
                    elif len(first_operand[m]) == 2 and len(str(outcome)) == 2:
                        new_str4 = new_str4 + str4 + str(outcome) + ' '*4 # two digits for first operand and two digits for outcome
                    elif len(first_operand[m]) == 2 and len(str(outcome)) == 1:
                        new_str4 = new_str4 + ' '*3 + str(outcome) + ' '*4 # two digits for first operand and one digit for outcome
                    else:
                        new_str4 = new_str4 + str4 + str(outcome) + ' '*4 # one digit for first operand and one digit for outcome
                outcome = str(outcome)
                outcome = outcome.lstrip('-')
                if len(outcome) == 5:
                    new_str4 = new_str4 + str4_b + outcome + ' ' * 4

        arranged_problems = new_str1 + '\n' + new_str2 + '\n' + new_str3 + '\n' + new_str4
        return arranged_problems
    else:
        arranged_problems = new_str1 + '\n' + new_str2 + '\n' + new_str3
        return arranged_problems


# Step 1: Working with the list (input):

problems = list() # an empty list; in other words, len(numlist) = 0.
while True: # start with numlist having length of 0.
    x = input("Please enter the sum or difference of two integers: ")
    problems.append(x)
    print(problems)
    inp = input("Are you done? ")
    if inp == "no" or inp == "No":
        continue
    else:
        break
answer = input("Please type 'True' if you want the answer to be included. ")

final_output = arithmetic_arranger(problems, answer) # Below is what will be contained in the function
print(final_output)











