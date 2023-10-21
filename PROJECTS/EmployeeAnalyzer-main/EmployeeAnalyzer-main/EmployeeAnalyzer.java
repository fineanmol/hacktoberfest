import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

class EmployeeData {
    String positionID;
    String positionStatus;
    Date time;
    Date timeOut;
    String timecardHours;
    Date payCycleStartDate;
    Date payCycleEndDate;
    String employeeName;
    String fileNumber;

    EmployeeData(String positionID, String positionStatus, Date time, Date timeOut, String timecardHours,
                 Date payCycleStartDate, Date payCycleEndDate, String employeeName, String fileNumber) {
        this.positionID = positionID;
        this.positionStatus = positionStatus;
        this.time = time;
        this.timeOut = timeOut;
        this.timecardHours = timecardHours;
        this.payCycleStartDate = payCycleStartDate;
        this.payCycleEndDate = payCycleEndDate;
        this.employeeName = employeeName;
        this.fileNumber = fileNumber;
    }
}

public class EmployeeAnalyzer {
    public static void main(String[] args) {
        String filename = "employee_records.csv"; // Replace with your input file path
        List<EmployeeData> records = readEmployeeRecordsFromCSV(filename);

        for (EmployeeData record : records) {
            if (workedForSevenConsecutiveDays(records, record.employeeName)) {
                System.out.println(record.employeeName + " has worked for 7 consecutive days.");
            }
            if (hasShortBreakBetweenShifts(records, record.employeeName)) {
                System.out.println(record.employeeName + " has less than 10 hours between shifts but greater than 1 hour.");
            }
            if (workedForMoreThan14Hours(records, record.employeeName)) {
                System.out.println(record.employeeName + " has worked for more than 14 hours in a single shift.");
            }
            System.out.println("------------------------");
        }
    }

    private static List<EmployeeData> readEmployeeRecordsFromCSV(String filename) {
        List<EmployeeData> records = new ArrayList<>();
        SimpleDateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy");

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            br.readLine(); // Skip the header line
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                String positionID = parts[0];
                String positionStatus = parts[1];
                Date time = parseDate(parts[2]);
                Date timeOut = parseDate(parts[3]);
                String timecardHours = parts[4];
                Date payCycleStartDate = parseDate(parts[5]);
                Date payCycleEndDate = parseDate(parts[6]);
                String employeeName = parts[7];
                String fileNumber = parts[8];

                records.add(new EmployeeData(positionID, positionStatus, time, timeOut, timecardHours,
                        payCycleStartDate, payCycleEndDate, employeeName, fileNumber));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return records;
    }

    private static Date parseDate(String dateString) {
        if (dateString.isEmpty()) {
            return null;
        }
        try {
            SimpleDateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy");
            return dateFormat.parse(dateString);
        } catch (ParseException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static boolean workedForSevenConsecutiveDays(List<EmployeeData> records, String name) {
        int consecutiveDays = 0;
        for (EmployeeData record : records) {
            if (record.employeeName.equals(name)) {
                consecutiveDays++;
                if (consecutiveDays == 7) {
                    return true;
                }
            } else {
                consecutiveDays = 0;
            }
        }
        return false;
    }

    private static boolean hasShortBreakBetweenShifts(List<EmployeeData> records, String name) {
        for (int i = 0; i < records.size() - 1; i++) {
            EmployeeData currentRecord = records.get(i);
            EmployeeData nextRecord = records.get(i + 1);

            if (currentRecord.employeeName.equals(name) && nextRecord.employeeName.equals(name) &&
                    currentRecord.timeOut != null && nextRecord.time != null) { // Added null checks
                long timeDifferenceHours = (nextRecord.time.getTime() - currentRecord.timeOut.getTime()) / 3600000;
                if (timeDifferenceHours > 1 && timeDifferenceHours < 10) {
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean workedForMoreThan14Hours(List<EmployeeData> records, String name) {
        for (EmployeeData record : records) {
            if (record.employeeName.equals(name) && record.time != null && record.timeOut != null) { // Added null checks
                long shiftHours = (record.timeOut.getTime() - record.time.getTime()) / 3600000;
                if (shiftHours > 14) {
                    return true;
                }
            }
        }
        return false;
    }
}
