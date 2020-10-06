
import sys
import os
import time
import json
import concurrent.futures
import threading
import conio.h

def main():
    if len(sys.argv) != 5:
        print("Wrong number of command-line arguments")
        sys.exit(1)
    print("Select which program to run:")
    print("1 - "+sys.argv[1])
    print("2 - "+sys.argv[2])
    print("3 - "+sys.argv[3])
    print("4 - "+sys.argv[4])
    print("5 - all at once")
    print("0 - exit")
    option = int(input("Option: "))
    os.system('cls')
    if option == 0:
        sys.exit(1)
    elif option > 0 and option < 5:
        single_tape(option)
    elif option == 5:
        threading()   

    else:
        print("Incorrect input!")
        main()

def single_tape(option):
    jfile = open(sys.argv[option], "r")
    data = json.load(jfile)
    jfile.close()

    pos = int(data["initialTapePosition"])-1
    tape = list(data["tape"])
    rules = data["rules"]
    state = '0'
    
    while True:
        cursor = ["-"]*len(tape)
        cursor[pos] = "^"
        print()
        print(*tape)
        print(*cursor)
        print()
        match = False
        
        for row in rules:
            if row["state"] == state and row["read"] == tape[pos]:
                tape[pos] = row["write"]
                x = 1 if row["move"]=="R" else -1
                pos += x
                state = row["nextState"]
                match = True
                break
        if match == False or pos == -1 or pos == len(tape):
            break
        get
        time.sleep(0.05)
        os.system('cls')
    time.sleep(3)
    main()

def threading():
    op = [1,2,3,4]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(single_tape, op)
main()


