def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): A list of coin denominations available
        amount (int): The target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount, 
             or -1 if the amount cannot be made up exactly
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values
    """
    # Validate input
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive")
    
    # Special case: if amount is 0, no coins needed
    if amount == 0:
        return 0
    
    # Initialize dynamic programming array
    # Set to amount + 1 which is larger than max possible coin count
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    # Build solution bottom-up
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, -1 if no solution found
    return dp[amount] if dp[amount] <= amount else -1