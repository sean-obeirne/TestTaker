#!/bin/python

import os
import sys

class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'


# PRACTICE_DIR = "/home/sean/documents/practice-tests/"
PRACTICE_DIR = "./practice-tests/"




contents = os.listdir(PRACTICE_DIR)
for i, c in enumerate(contents):
    print(f"  {Colors.BRIGHT_CYAN}{i+1}: {c}{Colors.RESET}")
choice = input(f"{Colors.YELLOW}select a test by number: {Colors.RESET}")
if choice in ('', 'q'):
    exit(0)

dir = PRACTICE_DIR + contents[int(choice)-1] + "/"
os.chdir(dir)
file = dir + contents[int(choice)-1]

action = 0

while action != "1":
    print(f"{Colors.BRIGHT_CYAN}  1. Take test")
    print(f"  2. Print answers{Colors.RESET}")
    action = input(f"{Colors.YELLOW}Select action: {Colors.RESET}")
    if action in ('', 'q'):
        exit(0)
    if action == '2':
        with open("answers", "r") as a:
            print(a.read())
            next = input(f"{Colors.YELLOW}continue...{Colors.RESET}").upper()
            continue


questions = []

with open("questions", "r") as q:

    # Construct questions
    qs = q.readlines()
    questions = []
    curline = 0
    qbuilder = ""
    for i, line in enumerate(qs):
        qline = line.strip("\n")
        if len(qline) == 0:
            continue
        if "." in qline[1:3] and i > 0:
            questions.append(qbuilder)
            qbuilder = ""
        qbuilder += qline + "\n"
    questions.append(qbuilder)
    # for ques in questions:
    #     print(ques)

    # ask questions

with open("answers", "w") as a, open("key", "r") as k:
    ks = k.readlines()
    
    for i, q in enumerate(questions):
        print('\033c', end="")
        print(f"{Colors.BRIGHT_CYAN}{q}{Colors.RESET}")
        answer = input(f"{Colors.YELLOW}answer: {Colors.RESET}").upper()
        print()
        while answer not in ("A", "B", "C", "D", "Q"):
            print(f"{Colors.RED}Invalid answer{Colors.RESET}")
            answer = input(f"{Colors.YELLOW}answer: {Colors.RESET}").upper()
        if answer == 'Q':
            exit(0)
        prefix = f"{i+1}. "
        correct_ans = f"{ks[i].split(" #")[0].split(". ")[1][0]}".upper()
        explanation = f"{ks[i].split("# ")[1]}"
        
        color = Colors.RED
        if correct_ans.strip() == answer.strip():
            color = Colors.GREEN
            print(f"{color}Correct!!!\n{Colors.RESET}")
            a.write(f"{color}✔   {prefix}{answer}\n")
        else:
            print(f"{color}Incorrect...\n{Colors.RESET}")
            a.write(f"{color}✗   {prefix}{answer} : {explanation.strip()}\n")
        
        print(f"    {Colors.YELLOW}You answered: {Colors.RESET}{color}{answer}{Colors.RESET}\t  {Colors.YELLOW}Correct Answer: {Colors.RESET}{color}{correct_ans}\n\n{explanation.strip()}{Colors.RESET}\n")
        

        next = input(f"{Colors.YELLOW}continue...{Colors.RESET}").upper()
        if next == 'Q':
            exit(0)
        print('\033c')
with open("answers", "r") as a:
    print(a.read())
    next = input(f"{Colors.YELLOW}quiting...{Colors.RESET}").upper()
