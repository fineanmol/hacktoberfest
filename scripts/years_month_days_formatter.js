class YearsMonthsDaysFormatter {
    static convertDaysToYearsMonthsDays(days) {
        const years = Math.floor(days / 365);
        const months = Math.floor((days % 365) / 30);
        days = (days % 365) % 30;

        const result = `${years} Years ${months} Months ${days} Days`;

        return result ? result : "0 Years 0 Months 0 Days";
    }
}

// Example usage:
const days = 500; // Replace with your desired number of days
const formatted = YearsMonthsDaysFormatter.convertDaysToYearsMonthsDays(days);
console.log(formatted);
