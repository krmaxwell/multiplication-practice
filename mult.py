import random
import sys

done = False

if len(sys.argv) > 1:
    prodmax = int(sys.argv[1])
else:
    prodmax = 10

while not done:
    factor1 = random.randrange(prodmax)
    factor2 = random.randrange(prodmax)
    answer = -10000
    while int(answer) != factor1 * factor2:
        prompt = "%d x %d = " % (factor1, factor2)
        answer = raw_input(prompt)
        try:
            if answer[0] == 'Q' or answer[0] == 'q':
                done = True
                break
            elif int(answer) != factor1 * factor2:
                print "Hrm, try that again..."
        except:
            print "What? I didn't understand you. Type 'q' to quit."
            answer = -10000
    if not done:
        print "Great job! Now for another one..."
    else:
        print "See ya next time!"
