from random import randint, choice
from time import sleep

try:
    def main():
        entries_list = []
        entries = input("How many Elements Are there?\n>> ")
        try:
            entries = int(entries)
        except:
            print("YOU HAD ONE FUCKING JOB, CHOOSE A NUMBER; A NUMBER!")
            main()
        print()
        for entry_num in range(entries):
            entries_list.append(input(f"What is Entry Number {entry_num+1}'s Alias?\n>> "))
            print("..", end = "\n\n")
        continue_q = input(f"Is this Right? (Y/n/q):\n\t{entries_list}\n>> ")
        if continue_q.lower() in ("y", ""):
            app(entries_list)
        
        elif continue_q.lower() == "n":
            main()
        
        elif continue_q.lower() == "q":
            print("Fuck off.")
            sleep(1)
            quit()
        
    def app(entries):
        def timerator():
            times = randint(randint(0,255), randint(256, 512))
            times *= randint(randint(8,16), randint(17,64))
            return times
        
        print(f"Ok, Calculating an OutPut out of {len(entries)} Entries...")
        if timerator() % 2 == 0:
            print("Trying Harder...")
            timerator()
        else:
            pass
        score = {}
        for obj in entries:
            score.update({obj: 0})
        
        silence = input("for the Last question, Should i Disable Silent Mode? It's \"True\" By default. (True, False)\n>> ")
        while silence.lower() not in ("true", "false", ""):
            print("\nYou messed up, Try again.")
            silence = input("Should i Disable Silent Mode? It's \"True\" By default. (True, False)\n>> ")

        for time in range(timerator()):
            score[choice(entries)] += 1
            if silence.lower() == "false":
                print(score)

        sleep(1)
        print("~!----------------------------------------!~")
        print("Done Calculating, Getting Results...")
        sleep(0.2)
        print("Okay, Finished! Printing Results...")
        sleep(0.2)
        print(f"So, This is The score for Each of the Elements you Gave Me:\n")
        for element in score:
            print(score, end = "\n\n")
        winner = max(score, key=score.get)
        print("...and The Winner is NO ONE BUT!!!!:\n")
        sleep(2)
        print(winner + " !!!!!!!!!")
        sleep(2)
        print(f"This is All Made Up, You Know. Playing with Luck and Stuff... {winner} !")
        print(f"(after --> {timerator()} <-- Attempts by the way.")
        reset_q = input("Should i Restart the app or quit? (q/r)\n>> ")
        if reset_q.lower() == "q":
            print("fuck off Bitch.")
            sleep(2)
            exit()
        elif reset_q.lower() == "r":
            print("Restarting...")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            main()
        elif reset_q.lower() not in ("q", "r"):
            print("You messed up, but ima Close up anyway;")
            sleep(3)
            exit()
        #return winner # Uncomment if you ever Wanted to add Saving-To-File Feature to this Miserable program.
    main()

except KeyboardInterrupt:
    print("\nI Understand, Bye.")

finally:
    print("\nApp Exited/Terminated.")