import time,os,colorama,termcolor,keyboard
from termcolor import colored
from colorama import Fore,Back
money = 0

def menu01():
    print(Back.BLUE + "###########################################" + Back.BLACK)
    print(Back.LIGHTMAGENTA_EX + "################## Hello ##################" + Back.BLACK)
    print(Fore.BLUE + "   |\---/|" + Back.BLACK)
    print(Fore.BLUE + "   | ,_, |" + Back.BLACK)
    print(Fore.BLUE + "    \_`_/-..----." + Back.BLACK)
    print(Fore.BLUE + " ___/ `   ' ,""+   \ " + Back.BLACK)
    print(Fore.BLUE + "(__...'   __\    |`.___.';" + Back.BLACK)
    print(Fore.BLUE + "  (_,...'(_,.`__)/'.....+ " + Back.BLACK)
    print(Fore.GREEN + "                              money: 0", "$" + Back.BLACK)
    print(Fore.RED + "        click SPACE to mine bitcoin        " + Back.BLACK)
    print(Fore.RED + "        SHOP - SOON        " + Back.BLACK)
    print(Fore.RED + " NOTE:             save game isn't added yet  " + Back.BLACK)
    print(Back.BLUE + "###########################################" + Back.BLACK)

    while True:
     if keyboard.is_pressed('space'):
        if not was_pressed:
            was_pressed = True
            global money
            money += 1
            print(Back.BLUE + "###########################################" + Back.BLACK)
            print(Back.LIGHTMAGENTA_EX + "################## Hello ##################" + Back.BLACK)
            print(Fore.BLUE + "   |\---/|" + Back.BLACK)
            print(Fore.BLUE + "   | ,_, |" + Back.BLACK)
            print(Fore.BLUE + "    \_`_/-..----. " + Back.BLACK)
            print(Fore.BLUE + " ___/ `   ' ,""+   \ " + Back.BLACK)
            print(Fore.BLUE + "(__...'   __\    |`.___.';" + Back.BLACK)
            print(Fore.BLUE + "  (_,...'(_,.`__)/'.....+" + Back.BLACK)
            print(Fore.GREEN + "                              money: ", money, "$" + Back.BLACK)
            print(Fore.RED + "        click SPACE to mine bitcoin        " + Back.BLACK)
            print(Fore.RED + "        SHOP - SOON        " + Back.BLACK)
            print(Fore.RED + " NOTE:           save game isn't added yet    " + Back.BLACK)
            print(Back.BLUE + "###########################################" + Back.BLACK)
            
     else:
        was_pressed = False
    
### Loding init ###
print( """
      
                 ,.=ctE55ttt553tzs.,                               
             ,,c5;z==!!::::  .::7:==it3>.,                         
          ,xC;z!::::::    ::::::::::::!=c33x,                      
        ,czz!:::::  ::;;..===:..:::   ::::!ct3.                    
      ,C;/.:: :  ;=c!:::::::::::::::..      !tt3.                  
     /z/.:   :;z!:::::J  :E3.  E:::::::..     !ct3.                
   ,E;F   ::;t::::::::J  :E3.  E::.     ::.     \ttL               
  ;E7.    :c::::F******   **.  *==c;..    ::     Jttk              
 .EJ.    ;::::::L                   "\:.   ::.    Jttl             
 [:.    :::::::::773.    JE773zs.     I:. ::::.    It3L            
;:[     L:::::::::::L    |t::!::J     |::::::::    :Et3            
[:L    !::::::::::::L    |t::;z2F    .Et:::.:::.  ::[13
E:.    !::::::::::::L               =Et::::::::!  ::|13  
E:.    (::::::::::::L    .......       \:::::::!  ::|i3    
[:L    !::::      ::L    |3t::::!3.     ]::::::.  ::[13 
!:(     .:::::    ::L    |t::::::3L     |:::::; ::::EE3
 E3.    :::::::::;z5.    Jz;;;z=F.     :E:::::.::::II3[            
 Jt1.    :::::::[                    ;z5::::;.::::;3t3             
  \z1.::::::::::l......   ..   ;.=ct5::::::/.::::;Et3L             
   \t3.:::::::::::::::J  :E3.  Et::::::::;!:::::;5E3L              
    "cz\.:::::::::::::J   E3.  E:::::::z!     ;Zz37`               
      \z3.       ::;:::::::::::::::;='      ./355F                 
        \z3x.         ::~======='         ,c253F                   
          "tz3=.                      ..c5t32^                     
             "=zz3==...         ...=t3z13P^                        
                 `*=zjzczIIII3zzztE3>*^`                
                 
  ____  _ _            _                      
 |  _ \(_) |          (_)                     
 | |_) |_| |_ ___ ___  _ _ __                 
 |  _ <| | __/ __/ _ \| | '_ \                
 | |_) | | || (_| (_) | | | | |               
 |____/|_|\__\___\___/|_|_| |_|               
           (_)     (_)                        
  _ __ ___  _ _ __  _ _ __   __ _             
 | '_ ` _ \| | '_ \| | '_ \ / _` |            
 | | | | | | | | | | | | | | (_| |            
 |_| |_| |_|_|_| |_|_|_| |_|\__, |            
                             __/ |            
      _                 _   |___/             
     (_)               | |     | |            
  ___ _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
 / __| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
 \__ \ | | | | | | |_| | | (_| | || (_) | |   
 |___/_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
 
 
MENU LOADING...
      """)
time.sleep(2)
menu01()
    