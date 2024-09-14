from colorama import Fore, Style
import time
import os

class windows:
    def displayWinLogo():
        print(f"""
                                                           {Fore.RED}█████{Fore.RESET}
                                                        {Fore.RED}███████████{Fore.RESET}
                                                       {Fore.RED}██████████████{Fore.RESET}  {Fore.GREEN}█           ██
                                                      {Fore.RED}██████████████{Fore.RESET}  {Fore.GREEN}████     █████
                                                     {Fore.RED}██████████████{Fore.RESET}  {Fore.GREEN}██████████████
                                                    {Fore.RED}██████████████{Fore.RESET}  {Fore.GREEN}██████████████
                                                   {Fore.RED}██        ████{Fore.RESET}  {Fore.GREEN}██████████████
                                                      {Fore.BLUE}██████{Fore.RESET}        {Fore.GREEN}████████████{Fore.RESET}
                                                 {Fore.BLUE}██████████████{Fore.RESET}  {Fore.YELLOW}█{Fore.RESET}    {Fore.GREEN}█████{Fore.RESET}    
                                                {Fore.BLUE}██████████████{Fore.RESET}  {Fore.YELLOW}█████{Fore.RESET}       {Fore.YELLOW}██{Fore.RESET}
                                               {Fore.BLUE}██████████████{Fore.RESET}  {Fore.YELLOW}██████████████{Fore.RESET}
                                              {Fore.BLUE}██████████████{Fore.RESET}  {Fore.YELLOW}██████████████{Fore.RESET}
                                             {Fore.BLUE}██████████████{Fore.RESET}  {Fore.YELLOW}██████████████{Fore.RESET}
                                            {Fore.BLUE}██         ███{Fore.RESET}  {Fore.YELLOW}██████████████{Fore.RESET}
                              Microsoft®                       {Fore.YELLOW}█████████{Fore.RESET}    ™""")
        
    def displayWinText():
        print(f"""
                                                                                 {Fore.RED}__  ___ __{Fore.RESET}  
                                   __        ___           _                     {Fore.RED}\ \/ / '_ \{Fore.RESET}                          
                                   \ \      / (_)_ __   __| | _____      _____    {Fore.RED}>  <| |_) |{Fore.RESET}                             
                                    \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / / __|  {Fore.RED}/_/\_\ .__/{Fore.RESET}                                     
                                     \ V  V / | | | | | (_| | (_) \ V  V /\__ \       {Fore.RED}|_|{Fore.RESET}                                       
                                      \_/\_/  |_|_| |_|\__,_|\___/ \_/\_/ |___/ 
              """)
        
    def displayLoadingBar(x):
        print(f"""\n\n\n
                                        ┌──────────────────────────────────┐
                                        │{Fore.BLUE+x+Fore.RESET} │
                                        └──────────────────────────────────┘
              """)
        
    def loadFunction():
        load = "                                  "
        while True:
            for i in range(24):
                windows.displayWinLogo()
                windows.displayWinText()
                windows.displayLoadingBar(load[:33])
                if i >2:
                    load = "  " + load
                else:
                    load = " ██" + load
                time.sleep(0.25)
                os.system("cls")

    def FinalProduct():
        os.system("cls")
        while True:
            windows.loadFunction()

windows.FinalProduct()