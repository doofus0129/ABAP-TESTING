# ABAP Coding Challenges Platform

An interactive web-based platform for learning ABAP programming through coding challenges, inspired by CodingBat. Built with Flask and CodeMirror.

## Features

- **Progressive Difficulty Levels**: Beginner, Medium, and Intermediate challenges
- **Interactive Code Editor**: Light-themed CodeMirror editor with syntax highlighting
- **Real-time Testing**: Run tests against your code and see immediate feedback
- **Hints and Solutions**: Click "Show Answer" to reveal the correct solution
- **Responsive Design**: Clean, modern UI that works on desktop and mobile

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Code Editor**: CodeMirror
- **ABAP Interpreter**: Custom Python-based ABAP syntax parser and executor

## Getting Started

### Prerequisites

- Python 3.7+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/doofus0129/ABAP-TESTING.git
   cd ABAP-TESTING
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`

## Challenge Structure

### Beginner Level (10 problems)
- Basic syntax: WRITE statements, variables, data types
- Simple operations: concatenation, assignment

### Medium Level (10 problems)
- Control structures: IF-ELSE, loops
- Data manipulation: strings, numbers

### Intermediate Level (20 problems)
- Advanced features: internal tables, complex logic
- Real-world scenarios: data processing, calculations

## How to Use

1. Select a difficulty level from the homepage
2. Choose a challenge
3. Write your ABAP code in the editor
4. Click "Run Tests" to check your solution
5. Use "Show Answer" if you need help
6. Progress through challenges with the "Next Challenge" button

## ABAP Interpreter Features

The platform includes a custom ABAP interpreter that supports:
- DATA declarations
- WRITE statements
- IF/ELSE conditions
- DO loops
- LOOP AT for internal tables
- String operations (concatenation, length)
- Basic arithmetic

## Contributing

Feel free to contribute by:
- Adding new challenges
- Improving the ABAP interpreter
- Enhancing the UI/UX
- Fixing bugs

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by [Your Name] - A learning project for ABAP programming education.

---

*Note: This is a simplified ABAP interpreter for educational purposes. It does not support all ABAP features and is not intended for production use.*