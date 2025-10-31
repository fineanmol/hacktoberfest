# Contributing to Hacktoberfest Starter Project 🎃

Welcome to the Hacktoberfest Starter Project! We're excited to have you here. This document will guide you through the process of making your first contribution to open source.

## Table of Contents

- [What is Hacktoberfest?](#what-is-hacktoberfest)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Contribution Tasks](#contribution-tasks)
- [Pull Request Process](#pull-request-process)
- [Code of Conduct](#code-of-conduct)
- [Additional Resources](#additional-resources)

## What is Hacktoberfest?

Hacktoberfest is a month-long celebration from **October 1st - 31st** sponsored by **Digital Ocean** and **GitHub** to get people involved in Open Source. Learn more at [hacktoberfest.com](https://hacktoberfest.com/).

## Getting Started

### Prerequisites

- A GitHub account
- Git installed on your local machine
- Basic knowledge of Git commands

### Setup Instructions

1. **Fork this repository**
   - Click the Fork button in the top right of this page
   - Select your profile to create a fork

2. **Clone your forked repository**
   ```bash
   git clone https://github.com/your-username/hacktoberfest.git
   ```

3. **Navigate to the project directory**
   ```bash
   cd hacktoberfest
   ```

4. **Create a new branch**
   ```bash
   git checkout -b branch-name
   ```
   Use a descriptive branch name like `add-yourname` or `add-hello-world-python`

5. **Make your changes** (see [Contribution Tasks](#contribution-tasks) below)

6. **Stage your changes**
   ```bash
   git add .
   ```

7. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of your changes"
   ```
   Write a clear, concise commit message

8. **Push to your fork**
   ```bash
   git push origin branch-name
   ```

9. **Create a Pull Request**
   - Go to your forked repository on GitHub
   - Click the "New Pull Request" button
   - Ensure the base repository is the original and compare branch is your branch
   - Add a title and description explaining your changes
   - Submit the pull request

10. **Wait for review**
    - A maintainer will review your PR
    - Make any requested changes if needed
    - Once approved, your PR will be merged!

## How to Contribute

Choose **one or all** of the following tasks to contribute:

## Contribution Tasks

### 1. Add Your Name

Add your information to the `CONTRIBUTING.md` file using the following format:

```markdown
#### Name: [YOUR NAME](GitHub link)
- Place: City, State, Country
- Bio: Who are you?
- GitHub: [GitHub account name](GitHub link)
```

**Example:**
```markdown
#### Name: [Jane Doe](https://github.com/janedoe)
- Place: San Francisco, California, USA
- Bio: Full-stack developer passionate about open source
- GitHub: [janedoe](https://github.com/janedoe)
```

### 2. Add a Profile Page

Create a `Your_Name.md` file in the `profiles` directory. Use the following template:

```markdown
# Your Name

### Location

Your City/Country

### Academics

Your School

### Interests

- Some Things You Like

### Development

- Inventor of the My Pillow

### Projects

- [My Project](GitHub Link) Short Description

### Profile Link

[Your Name](GitHub Link)
```

**Example:**
```markdown
# Jane Doe

### Location

San Francisco, USA

### Academics

University of California, Berkeley

### Interests

- Web Development
- Machine Learning
- Open Source

### Development

- Full Stack Developer at Tech Company
- Open Source Contributor

### Projects

- [Awesome Project](https://github.com/janedoe/awesome-project) A cool web app built with React

### Profile Link

[Jane Doe](https://github.com/janedoe)
```

### 3. Create a "Hello, World!" Script

Add a `hello_world_yourusername.xx` script to the `scripts` directory in any language of your choice.

**Requirements:**
- Name your file: `hello_world_yourusername.extension`
  - Example: `hello_world_janedoe.js` or `hello_world_janedoe.py`
- Include comments with:
  - Language name
  - Environment/Runtime
  - Your name
  - Your GitHub profile link
- Place the file in the appropriate language folder

**Template:**
```javascript
// LANGUAGE: JavaScript
// ENV: Node.js
// AUTHOR: Your Name
// GITHUB: https://github.com/yourusername

console.log('Hello, World!');
```

**More Examples:**

**Python:**
```python
# LANGUAGE: Python
# ENV: Python 3
# AUTHOR: Your Name
# GITHUB: https://github.com/yourusername

print('Hello, World!')
```

**Java:**
```java
// LANGUAGE: Java
// ENV: JDK 11+
// AUTHOR: Your Name
// GITHUB: https://github.com/yourusername

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**C++:**
```cpp
// LANGUAGE: C++
// ENV: GCC
// AUTHOR: Your Name
// GITHUB: https://github.com/yourusername

#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

## Pull Request Process

1. **Ensure your code follows the guidelines** outlined in this document
2. **Update documentation** if you're adding new features
3. **Test your changes** before submitting
4. **Write a clear PR description** explaining what you've done and why
5. **Link any relevant issues** in your PR description
6. **Be patient** - maintainers will review your PR as soon as possible
7. **Respond to feedback** - if changes are requested, make them promptly

### PR Title Format

Use clear, descriptive titles:
- `Add: [Your Name] to contributors`
- `Add: Hello World script in Python`
- `Add: Profile page for [Your Name]`

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and considerate in your interactions.

### Guidelines

- **Be respectful** - treat everyone with respect and kindness
- **Be inclusive** - welcome newcomers and help them learn
- **Be collaborative** - work together and share knowledge
- **Be patient** - remember everyone was a beginner once
- **No harassment** - we have zero tolerance for harassment of any kind

## Additional Resources

### Beginner Guides

- [First Contributions Tutorial](https://github.com/firstcontributions/first-contributions) - A hands-on tutorial for making your first contribution
- [GitHub's Hello World Guide](https://guides.github.com/activities/hello-world/) - Learn GitHub basics
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/) - Comprehensive guide

### Git & GitHub

- [Managing Your Forked Repo](https://help.github.com/articles/fork-a-repo/)
- [Syncing a Fork](https://help.github.com/articles/syncing-a-fork/)
- [Keep Your Fork Synced](https://gist.github.com/fineanmol/f9b8943230e7031ae78cdcd1755bef32)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

### Markdown

- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Awesome README Examples](https://github.com/matiassingers/awesome-readme)

### Licensing

- [Choose a License](https://choosealicense.com) - Help choosing the right license for your project

## Recognition

All contributors will be recognized in our README.md file. Thank you for your contributions! 🎉

### Our Amazing Contributors ♥️

A big thank you to all our contributors! Your efforts make this project possible.

<!-- Contributors list will be automatically updated -->

## Questions?

If you have any questions or need help, feel free to:
- Open an issue in this repository
- Reach out to the maintainers
- Check existing issues and discussions

## Happy Hacking! 🚀

Remember to **star this repository** ⭐ if you had fun contributing!

---

**Celebrate Open Source!** Every contribution, no matter how small, makes a difference. Welcome to the community! 🎃

## Contributors List

<!-- Add your name below this line -->

#### Name: [Anmol Agarwal](https://github.com/fineanmol)
- Place: Delhi, India
- Bio: Full Stack Developer and Open Source Enthusiast
- GitHub: [fineanmol](https://github.com/fineanmol)

<!-- New contributors, add your details above this line -->
