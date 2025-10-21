# Advanced Password Generator

A comprehensive Python tool for generating secure passwords with advanced security features, strength analysis, and multiple generation methods.

## Features

### Password Generation Methods
- **Secure Generation**: Cryptographically secure passwords using `secrets` module
- **Random Generation**: Standard random password generation
- **Pronounceable Passwords**: Human-readable passwords using syllable patterns
- **Passphrases**: Memorable multi-word passwords
- **PIN Generation**: Secure numeric codes

### Security Features
- **Strength Analysis**: Comprehensive password strength evaluation
- **Entropy Calculation**: Mathematical entropy measurement
- **Common Password Detection**: Checks against known weak passwords
- **Pattern Analysis**: Detects sequences, repetitions, and keyboard patterns
- **Character Analysis**: Detailed character composition analysis

### Advanced Capabilities
- **Password History**: Track generated passwords with timestamps
- **Customizable Criteria**: Flexible character set and length options
- **Hash Generation**: Create hashes using various algorithms
- **Export/Import**: Save and load password history
- **Interactive Mode**: User-friendly command-line interface

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from password_generator import PasswordGenerator

# Create generator instance
generator = PasswordGenerator()

# Generate secure password
password = generator.generate_password(length=16, method='secure')
print(f"Generated password: {password}")

# Check password strength
analysis = generator.check_password_strength(password)
print(f"Strength: {analysis['strength_level']} ({analysis['strength_score']}/100)")
```

### Advanced Usage

```python
# Generate password with specific criteria
password = generator.generate_password(
    length=20,
    include_uppercase=True,
    include_lowercase=True,
    include_numbers=True,
    include_symbols=True,
    exclude_similar=True,
    exclude_ambiguous=True,
    method='secure'
)

# Generate passphrase
passphrase = generator.generate_passphrase(
    word_count=5,
    separator='-',
    capitalize=True
)

# Generate PIN
pin = generator.generate_pin(length=8)
```

### Password Analysis

```python
# Analyze password strength
analysis = generator.check_password_strength("MyPassword123!")

print(f"Strength Level: {analysis['strength_level']}")
print(f"Strength Score: {analysis['strength_score']}/100")
print(f"Entropy: {analysis['entropy']:.2f} bits")
print(f"Length: {analysis['length']}")
print(f"Is Common: {analysis['is_common']}")

if analysis['issues']:
    print(f"Issues: {', '.join(analysis['issues'])}")

if analysis['recommendations']:
    print(f"Recommendations: {', '.join(analysis['recommendations'])}")
```

## Password Strength Analysis

The tool provides comprehensive password strength analysis including:

### Strength Levels
- **Very Strong** (80-100): Excellent security
- **Strong** (60-79): Good security
- **Moderate** (40-59): Acceptable security
- **Weak** (20-39): Poor security
- **Very Weak** (0-19): Very poor security

### Analysis Components
- **Length**: Password length scoring
- **Character Variety**: Uppercase, lowercase, numbers, symbols
- **Entropy**: Mathematical randomness measurement
- **Pattern Detection**: Sequences, repetitions, keyboard patterns
- **Common Password Check**: Against known weak passwords

### Security Recommendations
- Minimum length requirements
- Character set diversity
- Pattern avoidance
- Entropy improvement suggestions

## Generation Methods

### 1. Secure Generation (`secrets` module)
- Uses cryptographically secure random number generator
- Recommended for production use
- Ensures true randomness

### 2. Random Generation (`random` module)
- Uses standard random number generator
- Suitable for non-security critical applications
- Faster generation

### 3. Pronounceable Passwords
- Uses vowel-consonant patterns
- Easier to remember and type
- Good balance of security and usability

### 4. Passphrases
- Multi-word combinations
- High entropy with memorability
- Recommended by security experts

### 5. PIN Generation
- Numeric codes only
- Suitable for short-term use
- Configurable length

## Character Set Options

### Character Types
- **Uppercase Letters**: A-Z
- **Lowercase Letters**: a-z
- **Numbers**: 0-9
- **Symbols**: !@#$%^&*()_+-=[]{}|;:,.<>?

### Exclusion Options
- **Similar Characters**: Exclude 0, O, o, 1, l, I, |
- **Ambiguous Characters**: Exclude {}[]()/\\'"`~,;.<>

## Password History Management

```python
# View password history
history = generator.get_password_history()
for entry in history:
    print(f"{entry['method']}: {entry['password']} ({entry['timestamp']})")

# Save history to file
generator.save_password_history('my_passwords.json')

# Load history from file
generator.load_password_history('my_passwords.json')

# Clear history
generator.clear_password_history()
```

## Hash Generation

```python
# Generate hashes
password = "MySecurePassword123!"
sha256_hash = generator.hash_password(password, 'sha256')
sha512_hash = generator.hash_password(password, 'sha512')
md5_hash = generator.hash_password(password, 'md5')

print(f"SHA256: {sha256_hash}")
print(f"SHA512: {sha512_hash}")
print(f"MD5: {md5_hash}")
```

## Interactive Mode

Run the interactive demo for hands-on exploration:

```python
from password_generator import interactive_password_generator
interactive_password_generator()
```

## Security Best Practices

### Password Generation
- Use secure generation method for important passwords
- Include all character types (uppercase, lowercase, numbers, symbols)
- Use minimum length of 12-16 characters
- Avoid common patterns and sequences

### Password Management
- Don't reuse passwords across accounts
- Use password managers for storage
- Enable two-factor authentication
- Regularly update passwords

### Strength Requirements
- Minimum entropy of 40 bits
- Avoid common passwords
- Check against breach databases
- Use unique passwords for each account

## Examples

### Example 1: Generate Strong Password

```python
generator = PasswordGenerator()

# Generate a strong password
password = generator.generate_password(
    length=16,
    include_uppercase=True,
    include_lowercase=True,
    include_numbers=True,
    include_symbols=True,
    method='secure'
)

# Verify strength
if generator.verify_password_strength(password, min_score=80):
    print(f"Strong password generated: {password}")
else:
    print("Password does not meet strength requirements")
```

### Example 2: Password Analysis

```python
# Analyze multiple passwords
passwords = [
    "password123",
    "MyStr0ng!P@ssw0rd",
    "123456",
    "P@ssw0rd!2024"
]

for pwd in passwords:
    analysis = generator.check_password_strength(pwd)
    print(f"'{pwd}': {analysis['strength_level']} ({analysis['strength_score']}/100)")
```

### Example 3: Batch Password Generation

```python
# Generate multiple passwords
passwords = []
for i in range(5):
    pwd = generator.generate_password(length=12, method='secure')
    passwords.append(pwd)

# Analyze all generated passwords
for pwd in passwords:
    analysis = generator.check_password_strength(pwd)
    print(f"{pwd}: {analysis['strength_level']}")
```

## Contributing

Areas for improvement:
- Add more hash algorithms (bcrypt, scrypt, Argon2)
- Implement password breach checking
- Add GUI interface
- Create web-based version
- Add password policy validation
- Implement password strength meter widget
- Add support for custom word lists

## Requirements

- Python 3.6+
- Standard library modules only (no external dependencies)

## License

This project is open source and available under the MIT License.

## Security Notice

This tool is designed for educational and development purposes. For production use:
- Always use cryptographically secure random number generators
- Implement proper password hashing (bcrypt, scrypt, Argon2)
- Follow security best practices
- Consider using established password managers
