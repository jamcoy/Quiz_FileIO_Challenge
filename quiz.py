import sys
GUESSES = 3


def play_or_write():
    user_choice = raw_input("Play (q)uiz, (w)rite questions or e(x)it? ")
    return user_choice


def write_questions():
    return 0


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
