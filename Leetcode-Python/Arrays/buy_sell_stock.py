arr = [7,6,4,3,1]


def buy_and_sell_stock(nums: list):
    n = len(nums)
    mini_val = nums[0]
    profit = 0
    for i in range(n):
        # get the cost based on prev min value
        cost = nums[i] - mini_val
        # cal max profit
        profit = max(profit, cost)
        # get the updated min_val
        mini_val = min(mini_val, nums[i])
        
    return profit
        
    
print("maximum profit: ", buy_and_sell_stock(nums=arr))