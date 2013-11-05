import random

done = False

while not done:
    factor1 = random.randrange(100)
    factor2 = random.randrange(100)
    answer = 0
    while int(answer) != factor1 * factor2:
        prompt = "%d x %d = " % (factor1, factor2)
        answer = raw_input(prompt)
        if answer[0] == 'Q' or answer[0] == 'q':
            done = True
            break
        # TODO: throws exception when answer can't be converted to a number
        elif int(answer) != factor1 * factor2:
            print "Hrm, try that again..."
    if not done:
        print "Great job! Now for another one..."
    else:
        print "See ya next time!"
