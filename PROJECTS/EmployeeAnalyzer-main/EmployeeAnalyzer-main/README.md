# Employee Analyzer

The Employee Analyzer is a Java program that analyzes employee work patterns from a CSV file. It identifies employees who have:

- Worked for 7 consecutive days.
- Had less than 10 hours of break between shifts but greater than 1 hour.
- Worked for more than 14 hours in a single shift.

## Getting Started

### Prerequisites

- Java Development Kit (JDK)

### Usage

1. Clone the Git repository.
2. Compile the Java code: `javac EmployeeAnalyzer.java`
3. Run the program: `java EmployeeAnalyzer`
   - Replace `"employee_records.csv"` with your CSV file path.

## CSV Format

The program expects a CSV file with these columns:

1. Position ID
2. Position Status
3. Time
4. Time Out
5. Timecard Hours (as Time)
6. Pay Cycle Start Date
7. Pay Cycle End Date
8. Employee Name
9. File Number

Example CSV format:

