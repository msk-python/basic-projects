import os 
os.system('cls')

class history():
    
    def show():
        os.system('cls')
        file = open("projects/Calculator/history.txt", "r")
        print("\n#------------------ History ------------------# \n")
        for x in file:
            print(x)
        print("\n#------------------ End History ------------------# \n")
        file.close()

    def clear():
        file = open("projects/Calculator/history.txt", "w")
        file.write("")
        os.system('cls')
        print("All History Clear")

    def update_history(value):
        file = open("projects/Calculator/history.txt", "a")
        file.write(value)
        file.close()

#------------------------------------ Start While loop ------------------------------------#
while True:
    a = input("\n Enter a value:")
    if "q" in a:
        os.system('cls')
        print("#------------------ Thanks for Using Me ------------------#\n")
        break
    elif "h" in a:
        history.show()
        continue
    elif "c" in a:
        history.clear()
        continue
    #------------------------------ Result Calculation -------------------#

    result = eval(a)
    os.system('cls')
    print(f'{a} : {result}')
    history.update_history(f'{a} : {result}\n')
    #------------------------------ End Result Calculation -------------------#
#------------------------------------ End While loop ------------------------------------#
