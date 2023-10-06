#include <iostream>
#include <fstream>
#include <string>
#include <ctime>

class AttendanceSystem {
public:
    void markAttendance(const std::string& studentName) {
        std::ofstream outputFile("attendance.txt", std::ios::app);
        if (outputFile.is_open()) {
            time_t now = time(0);
            char* dt = ctime(&now);

            outputFile << "Name: " << studentName << ", Date: " << dt;

            std::cout << "Attendance marked for: " << studentName << std::endl;

            outputFile.close();
        } else {
            std::cerr << "Error: Unable to open the file." << std::endl;
        }
    }
};

int main() {
    AttendanceSystem attendanceSystem;
    std::string studentName;

    std::cout << "Enter student name: ";
    std::getline(std::cin, studentName);

    attendanceSystem.markAttendance(studentName);

    return 0;
}
