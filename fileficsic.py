
#not at all 
def show_basic_command():
    print("help = show all command")
    print("DgFg = change Degrees_celsius to Fahrenheit_degrees")
    
    

def main_logo():
    print("""

██████╗ ██╗  ██╗██╗   ██╗███████╗██╗ ██████╗███████╗          ██████╗ █████╗ ██╗     
██╔══██╗██║  ██║╚██╗ ██╔╝██╔════╝██║██╔════╝██╔════╝         ██╔════╝██╔══██╗██║     
██████╔╝███████║ ╚████╔╝ ███████╗██║██║     ███████╗         ██║     ███████║██║     
██╔═══╝ ██╔══██║  ╚██╔╝  ╚════██║██║██║     ╚════██║         ██║     ██╔══██║██║     
██║     ██║  ██║   ██║   ███████║██║╚██████╗███████║██╗██╗██╗╚██████╗██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝ ╚═════╝╚══════╝╚═╝╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
                                                       By DevJoe (Free for every one.)
                                                       https://web.facebook.com/DEVJOEHACKING/
                                                       https://web.facebook.com/Devjoe-1232712380223773/ 
                                                       https://www.youtube.com/channel/UCis7Z7TADm-q6xIyxgbzPkQ        

                                                       if you donate me this program has more update :)

                                                       thanks for help me 
                                                       type "help" in command to show all options.\n\n""")

#in main command now 
def Degrees_celsius_to_Fahrenheit_degrees(C):
    try:
        C = float(C)
        print("oC/5  =  oF-32/9")
        print("%s/5 = oF-32/9"%C)
        C = C / 5
        print(C,"X 9 = oF - 32")
        C = 9 * C
        print(C,"= oF - 32")
        print("oF =",C,"+","32\n\n")
        C = C + 32
        print("\t\t=","{:0.1f}".format(C),"oF")
    except NameError :
        print("Use only number try again !!")
    except EnvironmentError :
        print("Try again!!")
        
#in main command now 
def Degrees_celsius_to_Fahrenheit_degrees_for_int(C):
    try:
        C = int(C)
        print("oC/5  =  oF-32/9")
        print("%s/5 = oF-32/9"%C)
        C = C / 5
        print(C,"X 9 = oF - 32")
        C = 9 * C
        print(C,"= oF - 32")
        print("oF =",C,"+","32\n\n")
        C = C + 32
        print("\t\t=","{:0.2f}".format(C),"oF")
    except NameError :
        print("Use only number try again !!")
    except EnvironmentError :
        print("Try again!!")


#non in main command 
def fahrenheit_to_degrees_float(F):
    try:
        F = float(F)
        print("C = (5/9)x(F-32)")
        print("C = (5/9)x(%f-32)"%F)
        F = ((5/9)*(F-32))
        print("C ={:0.2f}".format(F))
    except NameError:
        print("Try again!!!")
    except EOFError:
        print("Try again!!!")
        
 #non in main command      
def Kelvin_to_Degrees_celsius(K):
    try:
        K = float(K)
        print("C = K-273")
        print("C = {:0.2f}-273".format(K))
        K = K - 273
        print("C =%0.1f"%K)
    except NameError:
        print("Try again!!!")
    except EOFError:
        print("Try again!!!")
   
def Kelvin_to_fahrenheit(K):
    print("F = 9/5(K - 273) + 32")
    print("F = 9/5({:%0.2f} - 273) + 32".format(K))
    print("F = ")
    
def main_command_input():
    while True:
        try:
            print("show all option and command 'H' \n\n")
            main_logo()
            user_input = input("command here > ")
            if user_input == "exit":
                exit()
            if user_input == "help":
                show_basic_command()
            if user_input == "DgFg":
                print("1.Float or 2.Intiger to cal ?")
                Float_or_intiger = input("1 or 2? >>>")
                if Float_or_intiger == "1":
                    print("if you want to back main command >> back")
                    cal_DgFg_float = input("DgFg float cal >>> ")
                    if cal_DgFg_float == 'back':
                        main_command_input()
                    Degrees_celsius_to_Fahrenheit_degrees(cal_DgFg_float)
                elif Float_or_intiger == "2":
                    print("if you want to back main command >> back")
                    cal_DgFg_intiger == input("DgFg intiger cal >>>")
                    if cal_DgFg_intiger == 'back':
                        main_command_input()
                    Degrees_celsius_to_Fahrenheit_degrees_for_int(cal_DgFg_intiger)
                
            if user_input =="FhDg":
                print("if you want to back main command >> back")
                FhDg = input("fahrenheit_to_degrees > ")
                fahrenheit_to_degrees_float(FhDg)
                if FhDg == "back":
                    main_command_input()
                elif FhDg == "exit":
                    exit()
               
            if user_input =='KvDg':
              print("if you want to back main command >> back") 
              KvDg = input("Kelvin_to_Degrees_celsius >")
              Kelvin_to_Degrees_celsius(KvDg)
              if KvDg == "back":
                  main_command_input()
              elif KvDg =="exit":
                  exit()
              


            if user_input == "KvFh":
                KvFh = input("Kelvin_to_fahrenheit > ")
                Kelvin_to_fahrenheit(KvFh)
                if KvFh =="back":
                    main_command_input()
                elif KvFh == "exit":
                    exit()
                

        except NameError: 
            print("Try again !!")
        except EOFError:
            if EOFError:
                sure_or_not = input(str("you want to exit? yes or no >>>"))
                if sure_or_not == 'yes':
                    print("close program now...")
                    exit()
                else:
                    main_command_input()




def main_center():
    main_logo()
    main_command_input()



main_center()