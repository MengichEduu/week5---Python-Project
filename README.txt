CALCULATE_FUNCTION Project

Description
The `CALCULATE_FUNCTION` project is a Python script designed to calculate the final price of an item after applying a discount. The script only applies discounts that are **20% or more**, ensuring that minor discounts do not affect the original price. This tool is useful for individuals and businesses that want to quickly determine pricing after discounts.

Table of Contents
- [Installation]
- [Usage]
- [API Documentation]
- [Contributing]
- [License]
- [Acknowledgments]
- [Contact Information]

#Installation
	Prerequisites
	- Python 3.x

Steps
1. Clone the repository: 
   ```bash
   git clone https://github.com/MengichEduu/week5---Python-Project.git
2. Navigate to cloned directory
	cd repository

#Usage
To run the project, execute the script in your Python environment. The user will be prompted to enter the original price of an item and the discount percentage, for example:

Enter the original price of the item: 100
Enter the discount percentage: 25
The output will display the final price after the discount is applied, such as:

Discount applied! The final price is: $75.00
If the discount is less than 20%, the output will indicate that no discount was applied, for example:

No discount applied. The price remains: $100.00

#API Documentation
The main function in this project is calculate_discount(price, discount_percent), which calculates the discounted price based on the provided parameters.

Parameters:
	price (float): 
		The original price of the item.
	discount_percent (float): 
		The discount percentage to apply.
Returns:
	float: The final price after applying the discount if applicable; otherwise, it returns the original price.

#Contributions
Contributions are welcomed! If you would like to contribute to this project, please follow these guidelines: Fork the repository, create a new branch for your feature or fix, commit your changes, and push them to your fork. Finally, submit a pull request for review.

#License
No Licenses for now

#Acknowledgement
Thanks to the PLP community for giving me the chance to learn and grow through this assignment.

#Contact Information
For inquiries, feel free to reach out to Edom Mengich.
Email: mengicheduu@gmail.com