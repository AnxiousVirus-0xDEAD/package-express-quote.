# Welcome message for the Package Express application.
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight from the user.
try:
    weight = float(input("Please enter the package weight: "))
except ValueError:
    # Handle cases where the user doesn't enter a number.
    print("Invalid input. Please enter a numeric value for weight.")
    exit()

# Check if the package is too heavy.
if weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package dimensions (width, height, length) from the user.
try:
    width = float(input("Please enter the package width: "))
    height = float(input("Please enter the package height: "))
    length = float(input("Please enter the package length: "))
except ValueError:
    # Ensure dimensions are numeric.
    print("Invalid input. Please enter numeric values for dimensions.")
    exit()

# Calculate total dimensions to check if the package is too big.
total_dimensions = width + height + length

if total_dimensions > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate the shipping quote based on dimensions and weight.
# Formula: (width * height * length * weight) / 100
dimensions_product = width * height * length
product_with_weight = dimensions_product * weight
quote = product_with_weight / 100

# Display the final shipping quote, formatted as currency.
print(f"Your estimated total for shipping this package is: ${quote:.2f}")

print("Thank you!")
