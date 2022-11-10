//Name: Sufyan Chaudhry
//Date: 9/26/22
//Purpose: To Debug and make the program user-friendly
import javax.swing.*;
public class payRoll
{
	public static void main(String[] args)
	{
		int empCount; int empHours; int counter = 0;
		String name; String social; String hours; String rates;
		double empRate;
		String employeeCount = JOptionPane.showInputDialog( "Enter the number of employees: ");
		empCount = Integer.parseInt(employeeCount);
		do
			{
				name = JOptionPane.showInputDialog("Enter employee's full name:");
			
				social = JOptionPane.showInputDialog("Enter employee's SSN: ");
                hours = JOptionPane.showInputDialog("Enter the number of hours worked:" );
                empHours = Integer.parseInt(hours);
			
                rates = JOptionPane.showInputDialog("Enter the employee's rate of pay:");
                empRate = Double.parseDouble(rates);
			
                counter ++;
                displayPay(name, empHours, computePay(empHours, empRate));
            } 
		while(counter < empCount);
	}
	
	public static double computePay(int hrs, double rate)
	{ 
		double pay = 0; double normal;
		if(hrs > 40)
		{
			 hrs = hrs - 40;
			normal = rate * 40;
	        double payment = ((rate * 1.5) * hrs) + normal;
		}
		else
	        pay = hrs * rate;
			
		return pay;
	}
	
	public static void displayPay(String fullname, int hoursWorked, double grossPay)
	{
	    String allString = "";
	    allString = "Employee Name: " + fullname + "\n";
	    allString = allString + "Hours worked: " + hoursWorked + "\n";
	    allString = allString + "Gross Pay: $" + grossPay + "\n";
	   JOptionPane.showMessageDialog(null, allString, fullname + "'s" + " Gross Pay",
	    JOptionPane.INFORMATION_MESSAGE);
	}
	
}