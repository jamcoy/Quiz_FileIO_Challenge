import sys
GUESSES = 3


def play_or_write():
    user_choice = raw_input("Play (q)uiz, (w)rite questions or e(x)it? ")
    return user_choice


def write_questions():
    user_question = ""
    count = 0
    new_questions = []
    new_answers = []
    while user_question != "SAVE":
        count += 1
        user_question = raw_input("Enter question " + str(count) + ", or SAVE if finished: ")
        if user_question == "SAVE":
            user_file = raw_input("Enter filename of new questions file: ")
            save_questions(user_file, zip(new_questions, new_answers))
            break
        else:
            user_answer = raw_input("Enter answer: ") + "\n"
            new_questions.append(user_question)
            new_answers.append(user_answer)
    return


def save_questions(filename, quiz):
    f = open(filename, 'w')
    for item in quiz:
        f.write(item[0])
        f.write(item[1])
    f.close()
    return


def get_questions():
    user_file = raw_input("Enter filename of questions file: ")
    with open(user_file) as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]


def play_quiz():
    try:
        questions = get_questions()
    except IOError:
        print 'Error: Questions file not found.'
        sys.exit()
    except IndexError:
        print 'Error: All questions in the questions file must have answers.'
        sys.exit()
    score = 0
    total = len(questions)
    for question, answer in questions:
        i = 1
        while i <= GUESSES:
            guess = raw_input("Guess " + str(i) + " of " + str(GUESSES) + ": " + question)
            i += 1
            if guess == answer:
                score += 1
                break
    print 'You got %s out of %s questions right' % (score, total)

choice = ""
while choice != "w" or choice != "q" or choice != "x":
    choice = play_or_write()
    if choice == "w":
        write_questions()
    elif choice == "q":
        play_quiz()
    elif choice == "x":
        sys.exit()
