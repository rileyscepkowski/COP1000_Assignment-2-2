import unittest
import sys

# Function to calculate age in 2050
def calculate_age_in_2050(current_age, current_year):
    return current_age + (2050 - current_year)

# Unit tests
class TestAgeCalculation(unittest.TestCase):

    def test_age_calculation_1(self):
        # Test case for current age 30 in year 2025
        result = calculate_age_in_2050(30, 2025)
        self.assertEqual(result, 55)  # Expected result is 55

    def test_age_calculation_2(self):
        # Test case for current age 40 in year 2025
        result = calculate_age_in_2050(40, 2025)
        self.assertEqual(result, 65)  # Expected result is 65

# Main program logic
def main():
    myCurrentAge = 20  # Replace with your actual current age
    currentYear = 2025  # Replace with the actual current year

    # Calculate age in 2050
    myNewAge = calculate_age_in_2050(myCurrentAge, currentYear)

    # Print results
    print("My Current Age is " + str(myCurrentAge))
    print("I will be " + str(myNewAge) + " in 2050.")

if __name__ == "__main__":
    # Check command-line argument to determine what to run
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        # Run unit tests if the argument "-t" is passed
        print("Running unit tests...")
        unittest.main(argv=['first-arg-is-ignored'], exit=False)  # Prevents exit after running tests
    else:
        # Run main logic if no arguments or something else is passed
        main()