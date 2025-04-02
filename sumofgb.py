def calculate_gp_sum(first_term, common_ratio, n_terms):
    """
    Calculate the sum of a finite geometric progression.
    
    Parameters:
    first_term (float): The first term of the progression (a)
    common_ratio (float): The common ratio (r)
    n_terms (int): Number of terms to sum
    
    Returns:
    float: The sum of the geometric progression
    """
    # Check if common ratio is 1 (special case)
    if common_ratio == 1:
        return first_term * n_terms
    
    # Use the formula: S = a(1-r^n)/(1-r)
    # where a is the first term, r is the common ratio, and n is the number of terms
    gp_sum = first_term * (1 - common_ratio ** n_terms) / (1 - common_ratio)
    return gp_sum

# Get user input
try:
    first_term = float(input("Enter the first term of the geometric progression: "))
    common_ratio = float(input("Enter the common ratio: "))
    n_terms = int(input("Enter the number of terms to sum: "))
    
    # Calculate and display the result
    result = calculate_gp_sum(first_term, common_ratio, n_terms)
    print(f"\nThe sum of the first {n_terms} terms of the geometric progression is: {result}")
    
    # Optionally show the terms
    show_terms = input("\nWould you like to see all the terms? (y/n): ").lower()
    if show_terms == 'y':
        terms = [first_term * (common_ratio ** i) for i in range(n_terms)]
        print("\nTerms of the geometric progression:")
        print(", ".join(str(term) for term in terms))
        print(f"Sum = {result}")
        
except ValueError:
    print("Error: Please enter valid numeric values.")