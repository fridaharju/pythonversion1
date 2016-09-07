

class Product:
	price = 0
	count = 0
	tax = 0
	name = ""

	def price_with_tax(self):
		total = self.price * self.count * self.tax
		if total > 500:
			return 0.9 * total
		else:
			return total

	def __init__(self, price, count, tax, name):
		self.price = price
		self.count = count
		self.tax = tax
		self.name = name
	
		




products =[Product(price=900, count=2, tax=1.25, name="frida"), Product(price=100, count=1, tax=1.06, name = "the best book ever")]


for product in products:
	print(product.name, product.price_with_tax())









