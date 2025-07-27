using System;

public class PackageExpress
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Welcome to Package Express. Please follow the instructions below.");

        // Get package weight from the user.
        double weight;
        Console.Write("Please enter the package weight: ");
        while (!double.TryParse(Console.ReadLine(), out weight))
        {
            Console.WriteLine("Invalid input. Please enter a numeric value for weight.");
            Console.Write("Please enter the package weight: ");
        }

        // Check if the package is too heavy.
        if (weight > 50)
        {
            Console.WriteLine("Package too heavy to be shipped via Package Express. Have a good day.");
            Console.ReadLine(); // Keep console open
            return;
        }

        // Get package dimensions (width, height, length) from the user.
        double width, height, length;

        Console.Write("Please enter the package width: ");
        while (!double.TryParse(Console.ReadLine(), out width))
        {
            Console.WriteLine("Invalid input. Please enter a numeric value for width.");
            Console.Write("Please enter the package width: ");
        }

        Console.Write("Please enter the package height: ");
        while (!double.TryParse(Console.ReadLine(), out height))
        {
            Console.WriteLine("Invalid input. Please enter a numeric value for height.");
            Console.Write("Please enter the package height: ");
        }

        Console.Write("Please enter the package length: ");
        while (!double.TryParse(Console.ReadLine(), out length))
        {
            Console.WriteLine("Invalid input. Please enter a numeric value for length.");
            Console.Write("Please enter the package length: ");
        }

        // Calculate total dimensions to check if the package is too big.
        double totalDimensions = width + height + length;

        if (totalDimensions > 50)
        {
            Console.WriteLine("Package too big to be shipped via Package Express.");
            Console.ReadLine(); // Keep console open
            return;
        }

        // Calculate the shipping quote based on dimensions and weight.
        // Formula: (width * height * length * weight) / 100
        double dimensionsProduct = width * height * length;
        double productWithWeight = dimensionsProduct * weight;
        double quote = productWithWeight / 100;

        // Display the final shipping quote, formatted as currency.
        Console.WriteLine($"Your estimated total for shipping this package is: ${quote:F2}");

        Console.WriteLine("Thank you!");
        Console.ReadLine(); // Keep console open after displaying the quote
    }
}
