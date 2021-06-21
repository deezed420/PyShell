import json
import pickle

class colors:
    CRED = '\033[91m'
    CORANGE = '\033[93m'
    CEND = '\033[0m'
variables = []
alphabet = list('abcdefghijklmnopqrstuvwxyz')
nums = list('0123456789')
operators = ['+','-','*','/','%','**','//']
def process(input_str):
    inSTR = input_str.split()
    commands = ['print','var','math']
    try:
        command = inSTR[0]
    except IndexError:
        pass
    else:
        command = inSTR[0]
        if command in variables:
            with open('savefile.dat', 'rb') as f:
                print(f"{command} = {pickle.load(f)}")
        else:
            if command in commands:
                if command == "print":
                    try:
                        arg1 = inSTR[1]
                    except IndexError:
                        print(f"{colors.CORANGE}Usage: print <text>\nOutput: <text inputted>{colors.CEND}")
                    else:
                        arg1 = inSTR[1]
                        # MaxArgs is 1
                        if arg1 in variables:
                            with open('savefile.dat', 'rb') as f:
                                print(pickle.load(f))
                        else:
                            print(arg1)
                elif command == "var":
                    try:
                        arg1 = inSTR[1]
                        arg2 = inSTR[2]
                        arg3 = inSTR[3]
                    except IndexError:
                        print(f"{colors.CORANGE}Usage: var <var name> = <var value>\nOutput: New var <var name> was made with value <var value>{colors.CEND}")
                    else:
                        arg1 = inSTR[1]
                        arg3 = inSTR[3]
                        # MaxArgs is 3
                        with open('savefile.dat', 'ab') as f:
                            pickle.dump(arg3, f, protocol=2)
                            variables.append(arg1)
                            print(f"New variable '{arg1}' was made with value {arg3}")
                elif command == "math":
                    try:
                        arg1 = inSTR[1]
                    except IndexError:
                        print(f"{colors.CORANGE}Usage: math <equation>\nOutput: <answer>{colors.CEND}")
                    else:
                        inSTR.remove('math')
                        if not any(map(lambda v: v in list(inSTR), alphabet)):
                            if any(map(lambda v: v in list(inSTR), nums)):
                                if any(map(lambda v: v in list(inSTR), operators)):
                                    try:
                                        print(eval(''.join(inSTR)))
                                    except Exception as error:
                                        print(error)
                                else:
                                    print(f'{colors.FAIL}Invalid Usage!{colors.ENDC}')
                            else:
                                print(f'{colors.FAIL}Invalid Usage!{colors.ENDC}')
                        else:
                            print(f'{colors.FAIL}Invalid Usage!{colors.ENDC}')
                else:
                    print(f"{colors.CRED}internal error!{colors.CEND}")
            else:
                print(f"{colors.CRED}Invalid Command{colors.CEND}")
