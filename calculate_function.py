def calculate_discount(price, discount_percent):
    #Code written by Edom Mengich
    #Email: mengicheduu@gmail.com
    
    """
    Calculate the final price after applying a discount.
    If the discount_percent is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    print("Welcome to the Discount Calculator!")
    print("Designed with love by Edom Mengich (mengicheduu@gmail.com)")

    # Prompting the user for input
    try:
        
        original_price = float(input("Please enter the original price of the item: $"))
        discount_percent = float(input("Please enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percent)

        # Provide feedback
        if final_price != original_price:
            print(f"Great news! You've got a discount of {discount_percent}%!")
            print(f"The final price after the discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price remains: ${original_price:.2f}")

    except ValueError:
        print("Oops! Please enter valid numerical values for price and discount percentage. Let's try again!")

if __name__ == "__main__":
    main()