import os
import subprocess

# Define ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Colorful banner
banner = f"""{GREEN}

 ___  _   _  ____   ___  ___ __  _ _   ___ __  
| __|/ \ | |// __| |_ _|| __/ _|| U | | o )  \ 
| _|| o ||  (| _|   | | | _( (_ |   | | o \ o )
|_| |_n_||_|\\___|   |_| |___\__||_n_| |___/__/ 
                                                                             \033[1;91m
   _____ __  ______  __  _____   ______   
  / ___// / / / __ \/ / / /   | / ____/   
  \__ \/ /_/ / / / / /_/ / /| |/ / __     
 ___/ / __  / /_/ / __  / ___ / /_/ /     
/____/_/ /_/\____/_/ /_/_/  |_\____/                                                         
{RESET}"""

# Colorful info
info = f"""{YELLOW}
--------------------------------------------------------
Author     : {CYAN}@SHOHAG_VAII{YELLOW}
Github     : {CYAN}@ShohagVaii{YELLOW}
Telegram   :{CYAN} @FAKE_TECH_BD{YELLOW}
TOOLS      : {CYAN}MEMEFI COIN UP{YELLOW}
------------------------------------------------------
\033[1;30m 𝘕𝘰𝘵 𝘍𝘰𝘳 𝘚𝘦𝘭𝘭, 𝘐𝘵’𝘴 𝘛𝘰𝘵𝘢𝘭𝘭𝘺 𝘍𝘳𝘦𝘦
--------------------------------------------------------{RESET}
"""

os.system("clear")
print(banner)
print(info)

auth_token = input(f"{MAGENTA}Enter your Query Id: {RESET}")

# Step 2: Delete the old query_id.txt file if it exists
file_path = 'query_id.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{GREEN}----------------------------------------------------------{RESET}")
else:
    print(f"{YELLOW}does not exist, creating a new one.{RESET}")

# Step 3: Save the new auth token into query_id.txt
with open(file_path, 'w') as file:
    file.write(auth_token)
    print(f"{GREEN}----------------------------------------------------------{RESET}")

# Step 4: Run memefi.py
try:
    subprocess.run(['python', 'memefi.py'])
except Exception as e:
    print(f"{RED}Failed to run memefi.py: {e}{RESET}")
