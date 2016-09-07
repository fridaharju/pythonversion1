

class Product:
	def price_with_tax(self):
		total = self.price * self.count * self.tax
		if total > 500:
			return 0.9 * total
		else:
			return total

	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax




robot = Product(price=900, count=2, tax=1.25)
book = Product(price=100, count=1, tax=1.06)
flower = Product(price=50, count=3, tax=1.25)

total_price = robot.price_with_tax() + book.price_with_tax() + flower.price_with_tax()

print(total_price)







