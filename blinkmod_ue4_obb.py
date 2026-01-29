import os
import time
import pyfiglet
from colorama import Fore, init

init(autoreset=True)
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow(text):
    out = ""
    c = 0
    for ch in text:
        if ch != " ":
            out += colors[c % len(colors)] + ch
            c += 1
        else:
            out += ch
    return out

def banner():
    os.system("clear")
    ascii = pyfiglet.figlet_format("BLINK MOD", font="big")
    print(rainbow(ascii))
    print(Fore.WHITE + "      UE4 OBB UNPACK & REPACK TOOL")
    print(Fore.WHITE + "      Created by BLINK\n")
    time.sleep(1)

def unpack_obb():
    obb_file = input("Enter OBB file name: ")
    output_folder = "Unpacked_OBB"

    if not os.path.exists(obb_file):
        print("[✖] OBB file not found!")
        return

    os.makedirs(output_folder, exist_ok=True)
    cmd = f"ue4pak unpack {obb_file} {output_folder}"
    os.system(cmd)
    print(f"[✔] OBB unpacked to '{output_folder}'")

def repack_obb():
    folder = "Unpacked_OBB"
    output_obb = "BLINKMOD.obb"

    if not os.path.exists(folder):
        print(f"[✖] Folder '{folder}' not found!")
        return

    cmd = f"ue4pak pack {folder} {output_obb}"
    os.system(cmd)
    print(f"[✔] OBB repacked to '{output_obb}'")

def main():
    banner()
    print("1. OBB Unpack")
    print("2. OBB Repack")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        unpack_obb()
    elif choice == "2":
        repack_obb()
    elif choice == "3":
        exit()
    else:
        print("[✖] Invalid choice")

if __name__ == "__main__":
    main()
