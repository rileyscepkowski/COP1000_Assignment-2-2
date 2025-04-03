# This program calculates your age in the year 2050.
# Input:  None
# Output: Your current age followed by your age in 2050

# Create your variables here
myCurrentAge = 20 # Replace with current age
currentYear = 2025 # Replace with current year

# Calculate age in 2050
myNewAge = myCurrentAge + (2050 - currentYear)

# Print results
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")


import unittest

# Function to calculate age in 2050
def calculate_age_in_2050(current_age, current_year):
    return current_age + (2050 - current_year)

# Main program logic
if __name__ == "__main__":
    myCurrentAge = 20  # Replace with current age
    currentYear = 2025  # Replace with current year

    # Calculate age in 2050
    myNewAge = calculate_age_in_2050(myCurrentAge, currentYear)

    # Print results
    print("My Current Age is " + str(myCurrentAge))
    print("I will be " + str(myNewAge) + " in 2050.")

    # Unit tests
    class TestAgeCalculation(unittest.TestCase):

        def test_age_calculation(self):

            # Test case for current age 30 in year 2025
            result= calculate_age_in_2050(30, 2025)
            self.assertEqual(result, 55) # Expected result is 55

            # Test case for current age 40 in year 2025
            result= calculate_age_in_2050(40, 2025)
            self.assertEqual(result, 65)    # Expected result is 65
            
if __name__ == "__main__":
    # Run unit tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)