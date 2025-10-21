"""
Advanced Password Generator with Security Features
Author: AI Assistant
GitHub: https://github.com/fineanmol/hacktoberfest
Language: Python
Description: A comprehensive password generator with security analysis, strength checking, and multiple generation methods
"""

import random
import string
import secrets
import hashlib
import re
import math
from datetime import datetime
import json
import os


class PasswordGenerator:
    """Advanced password generator with security features"""
    
    def __init__(self):
        self.common_passwords = self._load_common_passwords()
        self.password_history = []
        
    def _load_common_passwords(self):
        """Load common passwords for security checking"""
        common_passwords = [
            'password', '123456', 'password123', 'admin', 'qwerty',
            '123456789', '12345678', '12345', '1234', '1234567',
            'dragon', 'abc123', 'football', 'monkey', 'letmein',
            '111111', 'dragon', 'master', 'hello', 'freedom',
            'whatever', 'qazwsx', 'trustno1', '654321', 'jordan23',
            'harley', 'password1', '1234', 'robert', 'matthew',
            'jordan', 'asshole', 'daniel', 'andrew', 'joshua',
            'michael', 'charlie', 'michelle', 'jessica', 'james'
        ]
        return set(common_passwords)
    
    def generate_password(self, length=12, include_uppercase=True, include_lowercase=True,
                        include_numbers=True, include_symbols=True, exclude_similar=True,
                        exclude_ambiguous=True, method='secure'):
        """
        Generate a password with specified criteria
        
        Args:
            length: Password length (default: 12)
            include_uppercase: Include uppercase letters (default: True)
            include_lowercase: Include lowercase letters (default: True)
            include_numbers: Include numbers (default: True)
            include_symbols: Include symbols (default: True)
            exclude_similar: Exclude similar characters (default: True)
            exclude_ambiguous: Exclude ambiguous characters (default: True)
            method: Generation method ('secure', 'random', 'pronounceable')
        
        Returns:
            Generated password string
        """
        if method == 'secure':
            return self._generate_secure_password(length, include_uppercase, include_lowercase,
                                                include_numbers, include_symbols, exclude_similar, exclude_ambiguous)
        elif method == 'random':
            return self._generate_random_password(length, include_uppercase, include_lowercase,
                                                include_numbers, include_symbols, exclude_similar, exclude_ambiguous)
        elif method == 'pronounceable':
            return self._generate_pronounceable_password(length)
        else:
            raise ValueError("Method must be 'secure', 'random', or 'pronounceable'")
    
    def _generate_secure_password(self, length, include_uppercase, include_lowercase,
                                include_numbers, include_symbols, exclude_similar, exclude_ambiguous):
        """Generate cryptographically secure password"""
        charset = self._build_charset(include_uppercase, include_lowercase, include_numbers,
                                    include_symbols, exclude_similar, exclude_ambiguous)
        
        if not charset:
            raise ValueError("No character set available with current settings")
        
        # Ensure at least one character from each required category
        password_chars = []
        
        if include_uppercase:
            password_chars.append(secrets.choice(string.ascii_uppercase))
        if include_lowercase:
            password_chars.append(secrets.choice(string.ascii_lowercase))
        if include_numbers:
            password_chars.append(secrets.choice(string.digits))
        if include_symbols:
            password_chars.append(secrets.choice('!@#$%^&*()_+-=[]{}|;:,.<>?'))
        
        # Fill remaining length with random characters
        remaining_length = length - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(secrets.choice(charset))
        
        # Shuffle the password
        random.shuffle(password_chars)
        
        password = ''.join(password_chars)
        
        # Store in history
        self.password_history.append({
            'password': password,
            'timestamp': datetime.now().isoformat(),
            'method': 'secure',
            'length': length
        })
        
        return password
    
    def _generate_random_password(self, length, include_uppercase, include_lowercase,
                                 include_numbers, include_symbols, exclude_similar, exclude_ambiguous):
        """Generate random password using Python's random module"""
        charset = self._build_charset(include_uppercase, include_lowercase, include_numbers,
                                    include_symbols, exclude_similar, exclude_ambiguous)
        
        if not charset:
            raise ValueError("No character set available with current settings")
        
        password = ''.join(random.choice(charset) for _ in range(length))
        
        # Store in history
        self.password_history.append({
            'password': password,
            'timestamp': datetime.now().isoformat(),
            'method': 'random',
            'length': length
        })
        
        return password
    
    def _generate_pronounceable_password(self, length):
        """Generate pronounceable password using syllables"""
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        password = ''
        for i in range(length):
            if i % 2 == 0:  # Even positions: consonants
                password += random.choice(consonants)
            else:  # Odd positions: vowels
                password += random.choice(vowels)
        
        # Capitalize first letter
        password = password.capitalize()
        
        # Store in history
        self.password_history.append({
            'password': password,
            'timestamp': datetime.now().isoformat(),
            'method': 'pronounceable',
            'length': length
        })
        
        return password
    
    def _build_charset(self, include_uppercase, include_lowercase, include_numbers,
                      include_symbols, exclude_similar, exclude_ambiguous):
        """Build character set based on requirements"""
        charset = ''
        
        if include_uppercase:
            charset += string.ascii_uppercase
        if include_lowercase:
            charset += string.ascii_lowercase
        if include_numbers:
            charset += string.digits
        if include_symbols:
            charset += '!@#$%^&*()_+-=[]{}|;:,.<>?'
        
        # Remove similar characters
        if exclude_similar:
            similar_chars = '0Oo1lI|'
            charset = ''.join(c for c in charset if c not in similar_chars)
        
        # Remove ambiguous characters
        if exclude_ambiguous:
            ambiguous_chars = '{}[]()/\\\'"`~,;.<>'
            charset = ''.join(c for c in charset if c not in ambiguous_chars)
        
        return charset
    
    def check_password_strength(self, password):
        """
        Analyze password strength and return detailed report
        
        Args:
            password: Password to analyze
        
        Returns:
            Dictionary with strength analysis
        """
        analysis = {
            'password': password,
            'length': len(password),
            'entropy': self._calculate_entropy(password),
            'strength_score': 0,
            'strength_level': '',
            'issues': [],
            'recommendations': [],
            'is_common': password.lower() in self.common_passwords,
            'character_analysis': self._analyze_characters(password),
            'pattern_analysis': self._analyze_patterns(password)
        }
        
        # Calculate strength score
        score = 0
        
        # Length scoring
        if analysis['length'] >= 12:
            score += 25
        elif analysis['length'] >= 8:
            score += 15
        elif analysis['length'] >= 6:
            score += 10
        
        # Character variety scoring
        char_analysis = analysis['character_analysis']
        if char_analysis['has_uppercase']:
            score += 10
        if char_analysis['has_lowercase']:
            score += 10
        if char_analysis['has_numbers']:
            score += 10
        if char_analysis['has_symbols']:
            score += 15
        
        # Entropy scoring
        if analysis['entropy'] >= 60:
            score += 20
        elif analysis['entropy'] >= 40:
            score += 15
        elif analysis['entropy'] >= 20:
            score += 10
        
        # Deduct points for issues
        if analysis['is_common']:
            score -= 30
            analysis['issues'].append('Password is in common passwords list')
        
        if analysis['pattern_analysis']['has_sequences']:
            score -= 15
            analysis['issues'].append('Contains sequential characters')
        
        if analysis['pattern_analysis']['has_repetition']:
            score -= 10
            analysis['issues'].append('Contains repeated characters')
        
        if analysis['pattern_analysis']['has_keyboard_patterns']:
            score -= 20
            analysis['issues'].append('Contains keyboard patterns')
        
        # Determine strength level
        if score >= 80:
            analysis['strength_level'] = 'Very Strong'
        elif score >= 60:
            analysis['strength_level'] = 'Strong'
        elif score >= 40:
            analysis['strength_level'] = 'Moderate'
        elif score >= 20:
            analysis['strength_level'] = 'Weak'
        else:
            analysis['strength_level'] = 'Very Weak'
        
        analysis['strength_score'] = max(0, min(100, score))
        
        # Generate recommendations
        if analysis['length'] < 8:
            analysis['recommendations'].append('Use at least 8 characters')
        if not char_analysis['has_uppercase']:
            analysis['recommendations'].append('Include uppercase letters')
        if not char_analysis['has_lowercase']:
            analysis['recommendations'].append('Include lowercase letters')
        if not char_analysis['has_numbers']:
            analysis['recommendations'].append('Include numbers')
        if not char_analysis['has_symbols']:
            analysis['recommendations'].append('Include symbols')
        if analysis['entropy'] < 40:
            analysis['recommendations'].append('Increase randomness')
        
        return analysis
    
    def _calculate_entropy(self, password):
        """Calculate password entropy in bits"""
        charset_size = 0
        
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            charset_size += 32  # Approximate symbol count
        
        if charset_size == 0:
            return 0
        
        entropy = len(password) * math.log2(charset_size)
        return entropy
    
    def _analyze_characters(self, password):
        """Analyze character composition"""
        return {
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_numbers': bool(re.search(r'[0-9]', password)),
            'has_symbols': bool(re.search(r'[^a-zA-Z0-9]', password)),
            'unique_chars': len(set(password)),
            'char_distribution': {char: password.count(char) for char in set(password)}
        }
    
    def _analyze_patterns(self, password):
        """Analyze password patterns"""
        patterns = {
            'has_sequences': False,
            'has_repetition': False,
            'has_keyboard_patterns': False
        }
        
        # Check for sequences
        sequences = ['123', 'abc', 'qwe', 'asd', 'zxc']
        for seq in sequences:
            if seq in password.lower():
                patterns['has_sequences'] = True
                break
        
        # Check for repetition
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                patterns['has_repetition'] = True
                break
        
        # Check for keyboard patterns
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for row in keyboard_rows:
            for i in range(len(row) - 2):
                pattern = row[i:i+3]
                if pattern in password.lower():
                    patterns['has_keyboard_patterns'] = True
                    break
        
        return patterns
    
    def generate_passphrase(self, word_count=4, separator='-', capitalize=True):
        """
        Generate a memorable passphrase
        
        Args:
            word_count: Number of words in passphrase
            separator: Separator between words
            capitalize: Whether to capitalize words
        
        Returns:
            Generated passphrase
        """
        # Common word lists for passphrases
        words = [
            'apple', 'banana', 'cherry', 'dragon', 'eagle', 'forest', 'garden',
            'house', 'island', 'jungle', 'knight', 'ladder', 'mountain', 'ocean',
            'palace', 'queen', 'river', 'sunset', 'tower', 'umbrella', 'village',
            'water', 'yellow', 'zebra', 'adventure', 'beautiful', 'creative',
            'dancing', 'electric', 'fantastic', 'gigantic', 'harmony', 'incredible',
            'jubilant', 'knowledge', 'luminous', 'magnificent', 'nostalgic',
            'optimistic', 'peaceful', 'quixotic', 'radiant', 'serene', 'tranquil',
            'universe', 'victorious', 'wonderful', 'xenial', 'youthful', 'zealous'
        ]
        
        selected_words = [secrets.choice(words) for _ in range(word_count)]
        
        if capitalize:
            selected_words = [word.capitalize() for word in selected_words]
        
        passphrase = separator.join(selected_words)
        
        # Store in history
        self.password_history.append({
            'password': passphrase,
            'timestamp': datetime.now().isoformat(),
            'method': 'passphrase',
            'length': len(passphrase)
        })
        
        return passphrase
    
    def generate_pin(self, length=6):
        """Generate a secure PIN"""
        pin = ''.join(secrets.choice(string.digits) for _ in range(length))
        
        # Store in history
        self.password_history.append({
            'password': pin,
            'timestamp': datetime.now().isoformat(),
            'method': 'pin',
            'length': length
        })
        
        return pin
    
    def save_password_history(self, filename='password_history.json'):
        """Save password generation history to file"""
        with open(filename, 'w') as f:
            json.dump(self.password_history, f, indent=2)
    
    def load_password_history(self, filename='password_history.json'):
        """Load password generation history from file"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.password_history = json.load(f)
    
    def get_password_history(self):
        """Get password generation history"""
        return self.password_history
    
    def clear_password_history(self):
        """Clear password generation history"""
        self.password_history = []
    
    def hash_password(self, password, algorithm='sha256'):
        """Hash a password using specified algorithm"""
        if algorithm == 'sha256':
            return hashlib.sha256(password.encode()).hexdigest()
        elif algorithm == 'sha512':
            return hashlib.sha512(password.encode()).hexdigest()
        elif algorithm == 'md5':
            return hashlib.md5(password.encode()).hexdigest()
        else:
            raise ValueError("Unsupported hash algorithm")
    
    def verify_password_strength(self, password, min_score=60):
        """Verify if password meets minimum strength requirements"""
        analysis = self.check_password_strength(password)
        return analysis['strength_score'] >= min_score


def demo_password_generator():
    """Demonstrate password generator functionality"""
    print("=== Advanced Password Generator Demo ===\n")
    
    generator = PasswordGenerator()
    
    # Generate different types of passwords
    print("1. Secure Password Generation:")
    secure_password = generator.generate_password(length=16, method='secure')
    print(f"   Generated: {secure_password}")
    
    analysis = generator.check_password_strength(secure_password)
    print(f"   Strength: {analysis['strength_level']} ({analysis['strength_score']}/100)")
    print(f"   Entropy: {analysis['entropy']:.2f} bits")
    
    print("\n2. Pronounceable Password:")
    pronounceable = generator.generate_password(length=12, method='pronounceable')
    print(f"   Generated: {pronounceable}")
    
    print("\n3. Passphrase Generation:")
    passphrase = generator.generate_passphrase(word_count=4, separator='-')
    print(f"   Generated: {passphrase}")
    
    print("\n4. PIN Generation:")
    pin = generator.generate_pin(length=6)
    print(f"   Generated: {pin}")
    
    print("\n5. Password Strength Analysis:")
    test_passwords = [
        'password123',
        'MyStr0ng!P@ssw0rd',
        '123456',
        'P@ssw0rd!2024'
    ]
    
    for pwd in test_passwords:
        analysis = generator.check_password_strength(pwd)
        print(f"   '{pwd}': {analysis['strength_level']} ({analysis['strength_score']}/100)")
        if analysis['issues']:
            print(f"     Issues: {', '.join(analysis['issues'])}")
        if analysis['recommendations']:
            print(f"     Recommendations: {', '.join(analysis['recommendations'])}")
    
    print("\n6. Password History:")
    history = generator.get_password_history()
    for entry in history[-3:]:  # Show last 3 entries
        print(f"   {entry['method']}: {entry['password']} (length: {entry['length']})")
    
    print("\n=== Demo Complete ===")


def interactive_password_generator():
    """Interactive password generator"""
    generator = PasswordGenerator()
    
    print("=== Interactive Password Generator ===")
    print("1. Generate secure password")
    print("2. Generate pronounceable password")
    print("3. Generate passphrase")
    print("4. Generate PIN")
    print("5. Check password strength")
    print("6. View password history")
    print("7. Clear password history")
    print("8. Save password history")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-8): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            length = int(input("Password length (default 12): ") or "12")
            include_upper = input("Include uppercase? (y/n, default y): ").strip().lower() != 'n'
            include_lower = input("Include lowercase? (y/n, default y): ").strip().lower() != 'n'
            include_num = input("Include numbers? (y/n, default y): ").strip().lower() != 'n'
            include_sym = input("Include symbols? (y/n, default y): ").strip().lower() != 'n'
            
            password = generator.generate_password(
                length=length,
                include_uppercase=include_upper,
                include_lowercase=include_lower,
                include_numbers=include_num,
                include_symbols=include_sym,
                method='secure'
            )
            print(f"Generated password: {password}")
            
            analysis = generator.check_password_strength(password)
            print(f"Strength: {analysis['strength_level']} ({analysis['strength_score']}/100)")
            
        elif choice == '2':
            length = int(input("Password length (default 12): ") or "12")
            password = generator.generate_password(length=length, method='pronounceable')
            print(f"Generated password: {password}")
            
        elif choice == '3':
            word_count = int(input("Number of words (default 4): ") or "4")
            separator = input("Separator (default '-'): ").strip() or "-"
            capitalize = input("Capitalize words? (y/n, default y): ").strip().lower() != 'n'
            
            passphrase = generator.generate_passphrase(
                word_count=word_count,
                separator=separator,
                capitalize=capitalize
            )
            print(f"Generated passphrase: {passphrase}")
            
        elif choice == '4':
            length = int(input("PIN length (default 6): ") or "6")
            pin = generator.generate_pin(length=length)
            print(f"Generated PIN: {pin}")
            
        elif choice == '5':
            password = input("Enter password to analyze: ").strip()
            analysis = generator.check_password_strength(password)
            
            print(f"\nPassword Analysis:")
            print(f"Strength: {analysis['strength_level']} ({analysis['strength_score']}/100)")
            print(f"Length: {analysis['length']}")
            print(f"Entropy: {analysis['entropy']:.2f} bits")
            print(f"Common password: {analysis['is_common']}")
            
            if analysis['issues']:
                print(f"Issues: {', '.join(analysis['issues'])}")
            if analysis['recommendations']:
                print(f"Recommendations: {', '.join(analysis['recommendations'])}")
                
        elif choice == '6':
            history = generator.get_password_history()
            if history:
                print("\nPassword History:")
                for i, entry in enumerate(history[-10:], 1):  # Show last 10
                    print(f"{i}. {entry['method']}: {entry['password']} ({entry['timestamp']})")
            else:
                print("No password history found.")
                
        elif choice == '7':
            generator.clear_password_history()
            print("Password history cleared.")
            
        elif choice == '8':
            filename = input("Filename (default 'password_history.json'): ").strip() or "password_history.json"
            generator.save_password_history(filename)
            print(f"Password history saved to {filename}")
            
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    # Run the demo
    demo_password_generator()
    
    # Uncomment the line below for interactive mode
    # interactive_password_generator()
