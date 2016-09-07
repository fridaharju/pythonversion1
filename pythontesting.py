

class Product:
	def price_with_tax(self):
		return self.price * self.count * self.tax

	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax


robot = Product(price=900, count=2, tax=1.25)
book = Product(price=100, count=1, tax=1.06)



products =[Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)
]

print(
	products[0].price_with_tax()+
	products[1].price_with_tax()
	)

total_price= 0
for product in products:
	total_price = total_price + product.price_with_tax()


print(total_price)







