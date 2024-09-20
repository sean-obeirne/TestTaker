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





os.chdir(sys.argv[1])
dir = os.path.basename(sys.argv[1][:-1]) # elim trailing /

num_questions = sys.argv[2]

questions = []

with open(dir + "-questions", "r") as q:

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
    # for ques in questions:
    #     print(ques)

    # ask questions

with open(dir + "-answers", "w") as a, open(dir + "-key", "r") as k:
    ks = k.readlines()
    
    print('\033c')
    for i, q in enumerate(questions):
        print(f"{Colors.CYAN}{q}{Colors.RESET}")
        answer = input(f"{Colors.YELLOW}answer: {Colors.RESET}").upper()
        print()
        if answer == 'Q':
            exit(0)
        prefix = f"{i+1} "
        correct_ans = f"{ks[i].split(" #")[0].split(". ")[1]}".upper()
        explanation = f"{ks[i].split("# ")[1]}"
        
        color = Colors.RED
        if correct_ans.strip() == answer.strip():
            color = Colors.GREEN
            print(f"{color}Correct!!!\n{Colors.RESET}")
        else:
            print(f"{color}Incorrect...\n{Colors.RESET}")
        
        print(f"    {Colors.YELLOW}You answered: {Colors.RESET}{color}{answer}{Colors.RESET}\t  {Colors.YELLOW}Correct Answer: {Colors.RESET}{color}{correct_ans}\n\n{explanation.strip()}{Colors.RESET}\n")
        

        a.write(f"{prefix}{answer}\n")
        next = input(f"{Colors.YELLOW}continue...{Colors.RESET}").upper()
        if next == 'Q':
            exit(0)
        print('\033c')
    print("asking questions")
