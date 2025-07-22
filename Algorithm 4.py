import re
import hashlib
import os
import json
from getpass import getpass
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class PasswordAdvisor:
    """
    A friendly password strength advisor that educates without being restrictive
    """
    def __init__(self):
        self.common_passwords = self._load_common_passwords()
        self.strength_labels = {
            0: (Fore.RED + "❌ Risky", "Consider strengthening"),
            1: (Fore.RED + "❌ Weak", "Easy to compromise"),
            2: (Fore.YELLOW + "⚠️ Fair", "Could be stronger"),
            3: (Fore.YELLOW + "⚠️ Good", "Meets basic standards"),
            4: (Fore.GREEN + "✅ Strong", "Hard to crack"),
            5: (Fore.GREEN + "✅ Robust", "Excellent security")
        }

    def _load_common_passwords(self):
        """Load common passwords from file if available"""
        try:
            with open("common_passwords.txt") as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            return [
                "password", "123456", "qwerty", 
                "abc123", "letmein", "welcome"
            ]

    def analyze(self, password):
        """Provide detailed analysis without being dictatorial"""
        analysis = {
            "length": len(password),
            "has_upper": bool(re.search(r'[A-Z]', password)),
            "has_lower": bool(re.search(r'[a-z]', password)),
            "has_digit": bool(re.search(r'\d', password)),
            "has_special": bool(re.search(r'[^A-Za-z0-9]', password)),
            "is_common": password.lower() in self.common_passwords,
            "has_repeats": bool(re.search(r'(.)\1{2,}', password)),
            "has_spaces": ' ' in password
        }

        return analysis

    def calculate_score(self, analysis):
        """Flexible scoring system"""
        score = 0
        
        # Length scoring (more forgiving)
        if analysis["length"] >= 12: score += 2
        elif analysis["length"] >= 8: score += 1
        
        # Character diversity
        if analysis["has_upper"]: score += 1
        if analysis["has_lower"]: score += 1
        if analysis["has_digit"]: score += 1
        if analysis["has_special"]: score += 1
        
        # Penalties (not absolute blockers)
        if analysis["is_common"]: score = max(0, score - 2)
        if analysis["has_repeats"]: score = max(0, score - 1)
        
        return min(5, score)  # Cap at maximum score

    def generate_report(self, password):
        """User-friendly feedback report"""
        analysis = self.analyze(password)
        score = self.calculate_score(analysis)
        label, description = self.strength_labels[score]
        
        report = [
            f"\n{Style.BRIGHT}Password Analysis{Style.RESET_ALL}",
            f"{label}: {description} ({score}/5)",
            f"Length: {analysis['length']} characters"
        ]
        
        # Positive reinforcement first
        positives = []
        if analysis["length"] >= 8: 
            positives.append("✓ Meets minimum length")
        if analysis["has_upper"] and analysis["has_lower"]:
            positives.append("✓ Has both cases")
        if analysis["has_digit"]:
            positives.append("✓ Contains numbers")
        if analysis["has_special"]:
            positives.append("✓ Includes special chars")
            
        if positives:
            report.append("\n" + Fore.GREEN + "Strengths:")
            report.extend(f"- {p}" for p in positives)
        
        # Constructive suggestions
        suggestions = []
        if analysis["length"] < 12:
            suggestions.append("Consider 12+ characters for better security")
        if not analysis["has_special"]:
            suggestions.append("Special characters (!@#) add strength")
        if analysis["is_common"]:
            suggestions.append("Avoid common dictionary words")
        if analysis["has_repeats"]:
            suggestions.append("Repeating characters reduce security")
            
        if suggestions:
            report.append("\n" + Fore.YELLOW + "Suggestions:")
            report.extend(f"- {s}" for s in suggestions)
        
        return "\n".join(report)

    def store_password(self, password):
        """Optional secure storage with user consent"""
        salt = os.urandom(16).hex()
        hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        
        try:
            with open("passwords.json", "a") as f:
                json.dump({"salt": salt, "hash": hashed}, f)
                f.write("\n")
            return True
        except Exception as e:
            print(Fore.RED + f"Storage error: {e}")
            return False

def main():
    advisor = PasswordAdvisor()
    
    while True:
        print(f"\n{Fore.CYAN}🔐 Password Advisor (type 'quit' to exit)")
        password = getpass("Enter password: ")
        
        if password.lower() == 'quit':
            break
            
        print(advisor.generate_report(password))
        
        # User choice section
        print(f"\n{Style.DIM}What would you like to do?")
        choice = input(
            "1. Try another password\n"
            "2. Store this password securely\n"
            "3. Continue with this password\n"
            "Choice: "
        )
        
        if choice == "2":
            if advisor.store_password(password):
                print(Fore.GREEN + "✓ Password stored securely")
            else:
                print(Fore.RED + "✗ Storage failed")
        elif choice == "3":
            print(Fore.GREEN + "✓ Proceeding with your password choice")
            break

if __name__ == "__main__":
    main()