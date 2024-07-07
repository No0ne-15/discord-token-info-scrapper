from colorama import Fore
import requests
import os, time
import fade

############################################
# This Script Has Been Made By No0ne-15    #
# Do not try to sell this script or if you #
# bought it then your got scammed.         #
# https://github.com/no0ne-15              #
############################################

def cls():
    os.system("cls" if os.name=="nt" else "clear")

cls()
os.system(f"TITLE Enter a User Token - Token Informations Scrapper - by github.com/No0ne-15")
token = input(f"{Fore.LIGHTMAGENTA_EX}Enter a{Fore.RESET} User Token\n{Fore.LIGHTMAGENTA_EX}>>  {Fore.RESET}")

r = requests.get("https://pastebin.com/raw/jQLiDQ2u")
version = r.json()["version"]
update_msg = r.json()["msg"]
discord_url = r.json()["discord"]

def version_checker():
    if version != "0.1":
        cls()
        print(f"{Fore.RED} {update_msg} {Fore.RESET}")
        input(f"{Fore.YELLOW} Type Enter to Continue {Fore.RESET}")
        exit()
    else: 
        return version

def check_token_type(token: str) -> str:
    if requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": token}).status_code == 200:
        return "User"
    else:
        return "Bot"

version = version_checker()
token_type = check_token_type(token)

def ui():
    cls()
    ui = f"""                                                 ▪   ▐ ▄ ·▄▄▄ 
                                                 ██ •█▌▐█▐▄▄·▪        ►  {Fore.LIGHTMAGENTA_EX}Version : {Fore.RESET}{version}
                                                 ▐█·▐█▐▐▌██▪  ▄█▀▄    ►  {Fore.LIGHTMAGENTA_EX}Credits : {Fore.RESET}no0ne_15
                                                 ▐█▌██▐█▌██▌.▐█▌.▐▌   ►  {Fore.LIGHTMAGENTA_EX}Discord : {Fore.RESET}{discord_url} 
                                                 ▀▀▀▀▀ █▪▀▀▀  ▀█▄▀▪     
{Fore.RESET}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"""
    ui = fade.purplepink(ui)
    print(ui)

def main():
    cls()
    if token_type == "User":
        ui()
        os.system(f"TITLE Press ENTER to Start - Token Informations Scrapper - by github.com/No0ne-15")
        input(f"\n\n\n\n\n\n                                          {Fore.LIGHTMAGENTA_EX} PRESS {Fore.RESET}ENTER {Fore.LIGHTMAGENTA_EX}TO START {Fore.RESET}INFO SCRAPPING")
        os.system(f"TITLE Account Infos - Token Informations Scrapper - by github.com/No0ne-15")
        cls()
        ui()
        a_infos = requests.get('https://discord.com/api/v10/users/@me', headers={'Authorization': token})
        account_info = f"""
                                          {Fore.LIGHTMAGENTA_EX}► User ID :{Fore.RESET} {a_infos.json()["id"]}
                                          {Fore.LIGHTMAGENTA_EX}► Username :{Fore.RESET} {a_infos.json()["username"]}
                                          {Fore.LIGHTMAGENTA_EX}► Public Name :{Fore.RESET} {a_infos.json()["global_name"]}
                                          {Fore.LIGHTMAGENTA_EX}► Email :{Fore.RESET} {a_infos.json()["email"]}
                                          {Fore.LIGHTMAGENTA_EX}► Phone :{Fore.RESET} {a_infos.json()["phone"] if a_infos.json()["phone"] else "None"}
                                          {Fore.LIGHTMAGENTA_EX}► MFA Enabled :{Fore.RESET} {a_infos.json()["mfa_enabled"]}
                                          {Fore.LIGHTMAGENTA_EX}► Country :{Fore.RESET} {a_infos.json()["locale"]}
                                          {Fore.LIGHTMAGENTA_EX}► Nitro :{Fore.RESET} {"None" if a_infos.json()["premium_type"] == 0 else "Nitro Classic" if a_infos.json()["premium_type"] == 1  else "Nitro Boost" if a_infos.json()["premium_type"] == 2  else "Nitro Basic" if a_infos.json()["premium_type"] == 3 else "Unknown"}   """
        print(account_info)
        input(f"\n\n                                          {Fore.LIGHTMAGENTA_EX}► Press {Fore.RESET}ENTER{Fore.LIGHTMAGENTA_EX} to search {Fore.RESET}Billing Infos")
        cls()
        x = requests.get('https://discord.com/api/users/@me/billing/payment-sources', headers={'Authorization': token})
        bill_infos = x.json()
        bill_address = bill_infos[0]["billing_address"]
        if bill_infos:
            payement_method = bill_infos[0]["type"]
            if payement_method == 1:
                ui()
                os.system(f"TITLE Billing Infos (Credit Card) - Token Informations Scrapper - by github.com/No0ne-15")
                billing_infos = f"""
                                          {Fore.LIGHTMAGENTA_EX}► Payement Method :{Fore.RESET} Credit Card
                                          {Fore.LIGHTMAGENTA_EX}► CC Brand :{Fore.RESET} {bill_infos[0]["brand"]}
                                          {Fore.LIGHTMAGENTA_EX}► CC Number :{Fore.RESET} ****-****-****-{bill_infos[0]["last_4"]} 
                                          {Fore.LIGHTMAGENTA_EX}► CC Expiry :{Fore.RESET} {bill_infos[0]["expires_month"]} / {bill_infos[0]["expires_year"]} 
                                          {Fore.LIGHTMAGENTA_EX}► CC Holder :{Fore.RESET} {bill_address["name"]} 

                                          {Fore.LIGHTMAGENTA_EX}► Adress 1 :{Fore.RESET} {bill_address["line_1"]} 
                                          {Fore.LIGHTMAGENTA_EX}► Adress 2 :{Fore.RESET} {bill_address["line_2"]} 
                                          {Fore.LIGHTMAGENTA_EX}► City :{Fore.RESET} {bill_address["city"]}
                                          {Fore.LIGHTMAGENTA_EX}► Postal Code :{Fore.RESET} {bill_address["postal_code"]}
                                          {Fore.LIGHTMAGENTA_EX}► State :{Fore.RESET} {bill_address["state"]}
                                          {Fore.LIGHTMAGENTA_EX}► Country :{Fore.RESET} {bill_address["country"]} """
                print(billing_infos)
                input(f"\n\n                                          {Fore.LIGHTMAGENTA_EX}► Press {Fore.RESET}ENTER{Fore.LIGHTMAGENTA_EX} to {Fore.RESET}Exit")
                exit()
            elif payement_method == 2:
                ui()
                os.system(f"TITLE Billing Infos (PayPal) - Token Informations Scrapper - by github.com/No0ne-15")
                billing_infos = f"""
                                          {Fore.LIGHTMAGENTA_EX}► Payement Method :{Fore.RESET} PayPal
                                          {Fore.LIGHTMAGENTA_EX}► Name :{Fore.RESET} {bill_address["name"]} 

                                          {Fore.LIGHTMAGENTA_EX}► Adress 1 :{Fore.RESET} {bill_address["line_1"]} 
                                          {Fore.LIGHTMAGENTA_EX}► Adress 2 :{Fore.RESET} {bill_address["line_2"]} 
                                          {Fore.LIGHTMAGENTA_EX}► City :{Fore.RESET} {bill_address["city"]}
                                          {Fore.LIGHTMAGENTA_EX}► Postal Code :{Fore.RESET} {bill_address["postal_code"]}
                                          {Fore.LIGHTMAGENTA_EX}► State :{Fore.RESET} {bill_address["state"]}
                                          {Fore.LIGHTMAGENTA_EX}► Country :{Fore.RESET} {bill_address["country"]} """
                print(billing_infos)
                input(f"\n\n{Fore.YELLOW}                                              {Fore.LIGHTMAGENTA_EX}► Press {Fore.RESET}ENTER{Fore.LIGHTMAGENTA_EX} to {Fore.RESET}Exit")
                exit()
        else:
            os.system(f"TITLE No Billing Info Found - Exiting in 5 seconds ...")
            print(f"\n\n\n\n\n\n\n\n\n                                           [{Fore.RED}!{Fore.RESET}] {Fore.RED}Error: {Fore.RESET} No Billing Info Found")
            input(f"\n\n{Fore.YELLOW}                                              {Fore.LIGHTMAGENTA_EX}► Press {Fore.RESET}ENTER{Fore.LIGHTMAGENTA_EX} to search {Fore.RESET}Billing Infos")
    else:
        cls()
        os.system(f"TITLE Invalid Token - Exiting in 5 seconds ...")
        print(f"\n\n\n\n\n\n\n\n\n                                           [{Fore.RED}!{Fore.RESET}] {Fore.RED}Error: {Fore.RESET} Invalid User Token")
        time.sleep(5)
        exit()

if __name__ == "__main__":
    main()