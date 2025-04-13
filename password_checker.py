
---

## 🐍 password_checker.py (Main Script)

Here’s the main Python script:

```python
import re

COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty", "abc123", "111111",
    "123123", "admin", "letmein", "welcome", "passw0rd"
]

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        suggestions.append("Use a longer password (12+ characters)")

    # Character types
    if re.search(r"[a-z]", password):
        score += 10
    else:
        suggestions.append("Include lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 10
    else:
        suggestions.append("Include uppercase letters")

    if re.search(r"\d", password):
        score += 10
    else:
        suggestions.append("Include numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 10
    else:
        suggestions.append("Include special characters (!@#...)")

    # Dictionary/Common word check
    lower_pwd = password.lower()
    for word in COMMON_PASSWORDS:
        if word in lower_pwd:
            suggestions.append(f"Avoid common words like \"{word}\"")
            score -= 10
            break

    return score, suggestions

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    score, tips = check_password_strength(password)

    print(f"\nScore: {score}/100")
    if score >= 80:
        print("Strength: ✅ Strong")
    elif score >= 60:
        print("Strength: ⚠️ Moderate")
    else:
        print("Strength: ❌ Weak")

    if tips:
        print("\nSuggestions:")
        for tip in tips:
            print(f"- {tip}")
