
print (900 * 2 * 1.25 + 100 * 1 * 1.06)

robot_price = 900
robot_count = 2
robot_tax = 1.25
book_price = 100
book_count = 1
book_tax = 1.06

print (robot_price * robot_count * robot_tax + book_price * book_count * book_tax)

all_customers = [22, 32, 52]

print (all_customers[1])

customers_by_name = {"bob": "45", "anne": "25"}
print (customers_by_name["bob"])

robot = {"price": 900, "count": 2, "tax": 1.25}
book = {"price": 100, "count": 1, "tax": 1.06}

print (robot["price"]*2*1.25 + book["price"] * 1 * 1.06)

print (robot["price"]*robot["count"]*robot["tax"]+ book["price"] * book["count"] * book["tax"])

robot = Product()
robot.price = 900
robot.count = 2
robot.tax = 1.25

print (
	robot.price * robot.count * robot.tax + book.price * book.count * book.tax
	)

book = Product()
book.price = 100
book.count = 1
book.tax = 1.06
