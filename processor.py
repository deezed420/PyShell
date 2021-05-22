import json
import pickle

with open('savefile.dat', 'wb'):
    pass
class colors:
    CRED = '\033[91m'
    CORANGE = '\033[93m'
    CEND = '\033[0m'
variables = []
def process(input_str):
    inSTR = input_str.split()
    commands = ['print','var']
    try:
        command = inSTR[0]
    except IndexError:
        pass
    else:
        command = inSTR[0]
        try:
            float(command)
        except ValueError:
            if command in variables:
                with open('savefile.dat', 'rb') as f:
                    print(f"{command}'s value is {pickle.load(f)}")
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
                    else:
                        print(f"{colors.CRED}internal error!{colors.CEND}")
                else:
                    print(f"{colors.CRED}Invalid Command{colors.CEND}")
                
        else:
            try:
                arg1 = inSTR[1]
                arg2 = inSTR[2]
            except IndexError:
                print(f"{colors.CRED}Invalid command{colors.CEND}")
            else:
                arg1 = inSTR[1]
                arg2 = inSTR[2]
                operators = ['+','-','*','/','%','**','//','<','>']
                if arg1 in operators:
                    if arg1 == "+":
                        print(float(command) + float(arg2))
                    elif arg1 == "-":
                        print(float(command) - float(arg2))
                    elif arg1 == "*":
                        print(float(command) * float(arg2))
                    elif arg1 == "/":
                        print(float(command) / float(arg2))
                    elif arg1 == "%":
                        print(float(command) % float(arg2))
                    elif arg1 == "**":
                        print(float(command) ** float(arg2))
                    elif arg1 == "//":
                        print(float(command) // float(arg2))
                    elif arg1 == "<":
                        if command < arg2:
                            print("Yes")
                        else:
                            print("No")
                    elif arg1 == ">":
                        if command > arg2:
                            print("Yes")
                        else:
                            print("No")
                    else:
                        print(f"{colors.CRED}Invalid Operator when tracing to arg1{colors.CEND}")
                else:
                    print(f"{colors.CRED}Invalid Operator when tracing to arg1{colors.CEND}")
