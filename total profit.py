actual_cost=float(input("please enter the actual product price:"))
sale_amount = float(input("please enter the the sale amount:"))
if (sale_amount > actual_cost):
    amount = (sale_amount - actual_cost)
    print("total profit is ",amount)
else:
    print("no profit")
