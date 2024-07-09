import java.util.Scanner;

public class SwitchExampleJava7 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a day of the week: ");
        String day = scanner.nextLine();

        String typeOfDay;
        switch (day) {
            case "Monday":
            case "Tuesday":
            case "Wednesday":
            case "Thursday":
            case "Friday":
                typeOfDay = "Weekday";
                break;
            case "Saturday":
            case "Sunday":
                typeOfDay = "Weekend";
                break;
            default:
                typeOfDay = "Invalid day";
                break;
        }

        System.out.println("Day type: " + typeOfDay);
        scanner.close();
    }
}
