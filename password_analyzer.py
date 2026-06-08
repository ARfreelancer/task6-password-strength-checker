# -----------------------------------------------
#  PASSWORD STRENGTH ANALYZER + GENERATOR
#  Cyber Security Internship - Task 6
#  Analyzes password strength and generates
#  strong passwords automatically!
# -----------------------------------------------

import re
import math
import random
import string
import datetime

REPORT_FILE = "password_report.txt"

# ---- COMMON WEAK PASSWORDS ---------------------
COMMON_PASSWORDS = [
    "password", "123456", "password123",
    "admin", "letmein", "qwerty", "abc123",
    "monkey", "master", "dragon", "111111",
    "baseball", "iloveyou", "trustno1",
    "sunshine", "princess", "welcome",
    "shadow", "superman", "michael"
]

# ---- WRITE HELPER ------------------------------
def write(text=""):
    print(text)
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def write_line():
    write("-" * 60)

def write_double():
    write("=" * 60)

def write_header(title):
    write()
    write_double()
    write("  " + title)
    write_double()

# ---- INIT REPORT -------------------------------
def init_report():
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("")
    write_double()
    write("  PASSWORD STRENGTH ANALYZER + GENERATOR")
    write("  Cyber Security Internship - Task 6")
    write("  Date: " + datetime.datetime.now().strftime(
          "%Y-%m-%d %H:%M:%S"))
    write_double()

# ---- ANALYZE PASSWORD --------------------------
def analyze_password(password):
    score   = 0
    issues  = []
    bonuses = []

    # ---- CHECK 1: Length
    length = len(password)
    if length < 6:
        issues.append("Too short! Minimum 8 characters needed")
        score += 0
    elif length < 8:
        issues.append("Short password - use at least 12 characters")
        score += 10
    elif length < 12:
        bonuses.append("Decent length (" + str(length) + " chars)")
        score += 20
    elif length < 16:
        bonuses.append("Good length (" + str(length) + " chars)")
        score += 30
    else:
        bonuses.append("Excellent length (" + str(length) + " chars)")
        score += 40

    # ---- CHECK 2: Uppercase
    upper = len(re.findall(r'[A-Z]', password))
    if upper == 0:
        issues.append("No uppercase letters (A-Z)")
    elif upper == 1:
        bonuses.append("Has uppercase letter")
        score += 10
    else:
        bonuses.append("Multiple uppercase letters (" +
                       str(upper) + ")")
        score += 15

    # ---- CHECK 3: Lowercase
    lower = len(re.findall(r'[a-z]', password))
    if lower == 0:
        issues.append("No lowercase letters (a-z)")
    elif lower == 1:
        bonuses.append("Has lowercase letter")
        score += 10
    else:
        bonuses.append("Multiple lowercase letters (" +
                       str(lower) + ")")
        score += 15

    # ---- CHECK 4: Numbers
    numbers = len(re.findall(r'[0-9]', password))
    if numbers == 0:
        issues.append("No numbers (0-9)")
    elif numbers == 1:
        bonuses.append("Has a number")
        score += 10
    else:
        bonuses.append("Multiple numbers (" + str(numbers) + ")")
        score += 15

    # ---- CHECK 5: Symbols
    symbols = len(re.findall(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]]',
                              password))
    if symbols == 0:
        issues.append("No symbols (!@#$%^&*)")
    elif symbols == 1:
        bonuses.append("Has a symbol")
        score += 15
    else:
        bonuses.append("Multiple symbols (" + str(symbols) + ")")
        score += 20

    # ---- CHECK 6: Common password check
    if password.lower() in COMMON_PASSWORDS:
        issues.append("DANGER: This is a very common password!")
        score = max(0, score - 50)

    # ---- CHECK 7: Repeated characters
    if re.search(r'(.)\1{2,}', password):
        issues.append("Has repeated characters (aaa, 111)")
        score = max(0, score - 10)

    # ---- CHECK 8: Sequential patterns
    sequences = ["123", "234", "345", "456", "567",
                 "678", "789", "abc", "bcd", "cde",
                 "qwerty", "asdf"]
    for seq in sequences:
        if seq in password.lower():
            issues.append("Has sequential pattern (" + seq + ")")
            score = max(0, score - 10)
            break

    # ---- CALCULATE ENTROPY
    charset = 0
    if upper > 0:   charset += 26
    if lower > 0:   charset += 26
    if numbers > 0: charset += 10
    if symbols > 0: charset += 32

    if charset > 0:
        entropy = round(length * math.log2(charset), 2)
    else:
        entropy = 0

    # ---- CRACK TIME ESTIMATE
    combinations = charset ** length if charset > 0 else 0
    guesses_per_sec = 1_000_000_000  # 1 billion per second

    if combinations > 0:
        seconds = combinations / guesses_per_sec
        if seconds < 60:
            crack_time = str(round(seconds, 2)) + " seconds"
        elif seconds < 3600:
            crack_time = str(round(seconds/60, 2)) + " minutes"
        elif seconds < 86400:
            crack_time = str(round(seconds/3600, 2)) + " hours"
        elif seconds < 31536000:
            crack_time = str(round(seconds/86400, 2)) + " days"
        elif seconds < 3153600000:
            crack_time = str(round(seconds/31536000, 2)) + " years"
        else:
            crack_time = str(round(
                seconds/3153600000, 2)) + " centuries"
    else:
        crack_time = "Instantly"

    # Cap score at 100
    score = min(score, 100)

    return {
        "score":      score,
        "length":     length,
        "upper":      upper,
        "lower":      lower,
        "numbers":    numbers,
        "symbols":    symbols,
        "entropy":    entropy,
        "crack_time": crack_time,
        "issues":     issues,
        "bonuses":    bonuses
    }

# ---- GET GRADE ---------------------------------
def get_grade(score):
    if score >= 90:
        return "A+", "UNCRACKABLE"
    elif score >= 80:
        return "A",  "VERY STRONG"
    elif score >= 70:
        return "B",  "STRONG"
    elif score >= 60:
        return "C",  "MODERATE"
    elif score >= 40:
        return "D",  "WEAK"
    else:
        return "F",  "VERY WEAK"

# ---- PRINT RESULT ------------------------------
def print_result(password, result, index):
    grade, label = get_grade(result['score'])

    # Mask password for display
    if len(password) > 4:
        masked = password[:2] + "*" * (len(password)-4) + \
                 password[-2:]
    else:
        masked = "*" * len(password)

    write()
    write("Password #" + str(index) +
          " : " + masked)
    write_line()
    write("Score        : " + str(result['score']) + "/100")
    write("Grade        : [" + grade + "] " + label)
    write("Length       : " + str(result['length']) + " characters")
    write("Uppercase    : " + str(result['upper']))
    write("Lowercase    : " + str(result['lower']))
    write("Numbers      : " + str(result['numbers']))
    write("Symbols      : " + str(result['symbols']))
    write("Entropy      : " + str(result['entropy']) + " bits")
    write("Crack Time   : " + result['crack_time'])

    # Score bar
    filled = int(result['score'] / 10)
    bar    = "#" * filled + "-" * (10 - filled)
    write("Strength Bar : [" + bar + "] " +
          str(result['score']) + "%")

    if result['bonuses']:
        write()
        write("GOOD:")
        for b in result['bonuses']:
            write("  [+] " + b)

    if result['issues']:
        write()
        write("NEEDS IMPROVEMENT:")
        for issue in result['issues']:
            write("  [-] " + issue)

# ---- GENERATE STRONG PASSWORD ------------------
def generate_password(length=16):
    write_header("STRONG PASSWORD GENERATOR")

    # Ensure all character types included
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+-=[]{}|")
    ]

    # Fill rest randomly
    all_chars = (string.ascii_letters +
                 string.digits +
                 "!@#$%^&*()_+-=[]{}|")
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle to avoid predictable pattern
    random.shuffle(password)
    generated = "".join(password)

    write("Generated Password : " + generated)
    write("Length             : " + str(len(generated)))

    # Analyze generated password
    result = analyze_password(generated)
    grade, label = get_grade(result['score'])

    write("Score              : " +
          str(result['score']) + "/100")
    write("Grade              : [" + grade + "] " + label)
    write("Crack Time         : " + result['crack_time'])
    write()
    write("SAVE THIS PASSWORD SECURELY!")
    write("Use a password manager like Bitwarden!")

    return generated

# ---- GENERATE PASSPHRASE -----------------------
def generate_passphrase():
    write_header("PASSPHRASE GENERATOR")

    words = [
        "Tiger", "Mountain", "River", "Castle",
        "Dragon", "Silver", "Falcon", "Thunder",
        "Crystal", "Ninja", "Phoenix", "Storm",
        "Galaxy", "Shadow", "Rocket", "Ocean",
        "Legend", "Viking", "Mystic", "Blazing"
    ]

    chosen = random.sample(words, 4)
    number = str(random.randint(10, 99))
    symbol = random.choice("!@#$%&*")

    passphrase = (chosen[0] + "-" + chosen[1] +
                  "-" + chosen[2] + "-" +
                  chosen[3] + number + symbol)

    write("Generated Passphrase: " + passphrase)
    write()
    write("Why passphrases are great:")
    write("  -> Easy to remember!")
    write("  -> Long = very hard to crack!")
    write("  -> Uses real words you can remember")
    write("  -> Adding numbers + symbols makes it stronger")

    result = analyze_password(passphrase)
    grade, label = get_grade(result['score'])
    write()
    write("Score      : " + str(result['score']) + "/100")
    write("Grade      : [" + grade + "] " + label)
    write("Crack Time : " + result['crack_time'])

    return passphrase

# ---- COMPARISON TABLE --------------------------
def comparison_table(passwords, results):
    write_header("PASSWORD COMPARISON TABLE")

    write(
        "No.".ljust(5) +
        "Password (masked)".ljust(22) +
        "Score".ljust(8) +
        "Grade".ljust(6) +
        "Crack Time"
    )
    write_line()

    for i, (pwd, res) in enumerate(
        zip(passwords, results), 1
    ):
        grade, label = get_grade(res['score'])
        if len(pwd) > 4:
            masked = pwd[:2] + "**" + pwd[-2:]
        else:
            masked = "****"

        write(
            str(i).ljust(5) +
            masked.ljust(22) +
            str(res['score']).ljust(8) +
            ("[" + grade + "]").ljust(6) +
            res['crack_time']
        )

# ---- RECOMMENDATIONS ---------------------------
def write_recommendations():
    write_header("PASSWORD BEST PRACTICES")

    tips = [
        "Use at least 12-16 characters minimum",
        "Mix uppercase, lowercase, numbers and symbols",
        "Never use personal info (name, birthday, phone)",
        "Never reuse the same password on multiple sites",
        "Use a password manager (Bitwarden is free!)",
        "Enable 2FA (Two Factor Authentication) always",
        "Use passphrases - easy to remember, hard to crack",
        "Change passwords immediately if breach detected",
        "Never share passwords via email or chat",
        "Avoid common substitutions like @ for a, 0 for o"
    ]

    write("TOP 10 PASSWORD BEST PRACTICES:")
    write_line()
    for i, tip in enumerate(tips, 1):
        write(str(i) + ". " + tip)

    write()
    write("COMMON PASSWORD ATTACKS:")
    write_line()
    attacks = {
        "Brute Force":
            "Tries every possible combination until found",
        "Dictionary":
            "Uses list of common words and passwords",
        "Credential Stuffing":
            "Uses leaked passwords from other breaches",
        "Phishing":
            "Tricks you into entering password on fake site",
        "Rainbow Table":
            "Uses pre-computed hash tables to crack passwords",
        "Shoulder Surfing":
            "Physically watching you type your password"
    }
    for attack, desc in attacks.items():
        write(attack + ":")
        write("  -> " + desc)
        write()

# ---- MENU --------------------------------------
def print_menu():
    print()
    print("=" * 60)
    print("  PASSWORD ANALYZER MENU")
    print("=" * 60)
    print("  1 -> Analyze a single password")
    print("  2 -> Analyze multiple passwords (batch)")
    print("  3 -> Generate a strong password")
    print("  4 -> Generate a passphrase")
    print("  5 -> Run full demo (all 8 test passwords)")
    print("  0 -> Exit and save report")
    print("-" * 60)

# ---- FULL DEMO ---------------------------------
def run_full_demo():
    write_header("FULL PASSWORD STRENGTH DEMO")
    write("Testing 8 passwords from weakest to strongest...")

    test_passwords = [
        "password",
        "Password1",
        "Pass@123",
        "P@ssw0rd!",
        "Cy6er$3cur!ty",
        "Tr0ub4dor&3",
        "X#9kL$mP2@nQ",
        "C*8vN!qR#2mP$xL7"
    ]

    results = []
    for i, pwd in enumerate(test_passwords, 1):
        result = analyze_password(pwd)
        print_result(pwd, result, i)
        results.append(result)

    comparison_table(test_passwords, results)
    write_recommendations()

    # Summary
    write_header("DEMO SUMMARY")
    write("Key Findings:")
    write_line()
    write("1. Length matters most - longer = harder to crack")
    write("2. Adding symbols dramatically increases strength")
    write("3. Common words make passwords very weak")
    write("4. Mix of all 4 types = strongest combination")
    write("5. Even 1 extra character = 10x harder to crack!")

# ---- MAIN --------------------------------------
if __name__ == "__main__":
    init_report()

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            write_header("SINGLE PASSWORD ANALYSIS")
            pwd = input("Enter password to analyze: ").strip()
            result = analyze_password(pwd)
            print_result(pwd, result, 1)

        elif choice == "2":
            write_header("BATCH PASSWORD ANALYSIS")
            print("Enter passwords one by one.")
            print("Type DONE when finished.")
            passwords = []
            results   = []
            i = 1
            while True:
                pwd = input("Password " + str(i) + ": ").strip()
                if pwd.upper() == "DONE":
                    break
                result = analyze_password(pwd)
                print_result(pwd, result, i)
                passwords.append(pwd)
                results.append(result)
                i += 1
            if passwords:
                comparison_table(passwords, results)

        elif choice == "3":
            length = input(
                "Password length? (default 16): ").strip()
            length = int(length) if length.isdigit() else 16
            generate_password(length)

        elif choice == "4":
            generate_passphrase()

        elif choice == "5":
            run_full_demo()

        elif choice == "0":
            write_recommendations()
            write_header("SESSION COMPLETE")
            write("Report saved to: " + REPORT_FILE)
            write("Generated at   : " +
                  datetime.datetime.now().strftime(
                  "%Y-%m-%d %H:%M:%S"))
            write_double()
            print()
            print("[OK] Full report saved to: " + REPORT_FILE)
            break
        else:
            print("[!] Invalid choice!")

        print()
        input("Press Enter to continue...")
