# 🔐 Password Strength Analyzer & Generator

A comprehensive Python-based cybersecurity tool that analyzes password strength, detects vulnerabilities, estimates crack time, calculates entropy, and generates secure passwords and passphrases.

## 📌 Project Overview

This project was developed as part of a Cyber Security Internship Task to demonstrate password security concepts and best practices.

The application evaluates passwords using multiple security criteria and provides detailed feedback to help users create stronger and more secure credentials.

---

## 🚀 Features

### Password Strength Analysis
- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numeric characters
- Detects special symbols
- Identifies common weak passwords
- Detects repeated characters
- Detects sequential patterns

### Security Metrics
- Password strength score (0–100)
- Security grade classification
- Entropy calculation
- Estimated crack time
- Detailed recommendations

### Password Generation
- Secure random password generator
- Strong passphrase generator
- Automatic strength evaluation of generated passwords

### Reporting
- Generates detailed password reports
- Password comparison table
- Security recommendations
- Common password attack awareness

---

## 🛡️ Password Evaluation Criteria

The analyzer evaluates passwords using the following rules:

| Rule | Requirement |
|--------|-------------|
| Length | Minimum 12 characters recommended |
| Uppercase | At least one uppercase letter (A-Z) |
| Lowercase | At least one lowercase letter (a-z) |
| Numbers | At least one numeric digit (0-9) |
| Symbols | At least one special character (!@#$%^&*) |

---

## 📊 Test Password Results

| Password | Score | Rating |
|-----------|--------|---------|
| password | 4% | Very Weak |
| Password1 | 28% | Weak |
| Pass@123 | 52% | Good |
| P@ssw0rd! | 68% | Strong |
| Cy6er$3cur!ty | 84% | Very Strong |
| Tr0ub4dor&3 | 86% | Very Strong |
| X#9kL$mP2@nQ | 94% | Excellent |
| C*8vN!qR#2mP$xL7 | 100% | Perfect |

> ⚠️ These passwords are used only for testing and demonstration purposes.

---

## 📂 Project Structure

```
Password-Strength-Analyzer/
│
├── password_analyzer.py
├── password_report.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/password-strength-analyzer.git
```

Navigate to the project folder:

```bash
cd password-strength-analyzer
```

Run the program:

```bash
python password_analyzer.py
```

---

## 🎮 Menu Options

The application provides:

```text
1 → Analyze a single password
2 → Analyze multiple passwords
3 → Generate a strong password
4 → Generate a passphrase
5 → Run full demo
0 → Exit
```

---

## 🔐 Password Security Best Practices

- Use at least 12–16 characters.
- Combine uppercase, lowercase, numbers, and symbols.
- Avoid personal information.
- Never reuse passwords.
- Use a password manager.
- Enable Two-Factor Authentication (2FA).
- Prefer long passphrases when possible.

---

## 🚨 Common Password Attacks

### Brute Force Attack
Attempts every possible combination.

### Dictionary Attack
Uses lists of commonly used passwords.

### Credential Stuffing
Uses leaked credentials from previous breaches.

### Phishing
Tricks users into entering passwords on fake websites.

### Rainbow Table Attack
Uses precomputed hash tables to crack passwords.

### Shoulder Surfing
Observing a user while entering credentials.

---

## 🎯 Learning Outcomes

Through this project, users can:

- Understand password security principles.
- Learn how password complexity affects security.
- Explore entropy and crack-time estimation.
- Generate stronger passwords.
- Improve cybersecurity awareness.

---

## 🏆 Technologies Used

- Python 3
- Regular Expressions (re)
- Math Module
- Random Module
- String Module
- Datetime Module

---

## 📜 License

This project is created for educational and cybersecurity learning purposes.

---

## 👨‍💻 Author

Developed as part of a Cyber Security Internship Task on Password Security and Strength Evaluation.
