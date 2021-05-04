pizza_orders = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]

temp_num = 0
total_pizza = 0

def orders_done():
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join([str(e) for e in employees])}")


while pizza_orders and employees:
    if pizza_orders[0] > 10 or pizza_orders[0] <= 0:
        pizza_orders.pop(0)
        continue
    if pizza_orders[0] <= employees[-1]:
        total_pizza += pizza_orders[0]
        pizza_orders.pop(0)
        employees.pop(-1)

    elif pizza_orders[0] > employees[-1]:
        pizza_orders[0] -= employees[-1]
        total_pizza += employees[-1]
        employees.pop(-1)

    if len(pizza_orders) == 0:
        break

if len(pizza_orders) > 0:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")

elif len(pizza_orders) == 0:
    orders_done()

"""
example input

11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1

"""