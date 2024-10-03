class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        1. Intuition: 
        - Use two pointers, one for buying and one for selling. The goal is to find the pair of buy and sell prices 
          that gives the maximum profit. Start by assuming you buy on the first day and sell on the second day. 
          As we move the sell pointer, we adjust the buy pointer whenever a lower price is found, and we calculate 
          potential profit for each sell transaction.
          
        2. Approach: 
        - Traverse through the prices list once while comparing each price with the minimum price before it. 
        - Update the max profit if a higher profit can be achieved with the current buy and sell prices.
        
        3. Complexity:
        - Time complexity: O(n), where n is the number of days (prices.length). We are only visiting each price once.
        - Space complexity: O(1), as we are using only a few variables to keep track of profit and pointers.
        """

        buy_pointer = 0  # Pointer for buying
        sell_pointer = 1  # Pointer for selling
        max_profit = 0  # Initialize max profit to zero

        # Iterate through the price list
        while sell_pointer < len(prices):

            # Calculate the current profit (selling price - buying price)
            current_profit = prices[sell_pointer] - prices[buy_pointer]

            # If the current sell price is greater than or equal to the buy price, calculate profit
            if prices[sell_pointer] >= prices[buy_pointer]:
                max_profit = max(max_profit, current_profit)  # Update the max profit if current profit is larger

            else:
                # If the sell price is lower than the buy price, update the buy pointer
                buy_pointer = sell_pointer

            sell_pointer += 1  # Move the sell pointer to the next day

        return max_profit
