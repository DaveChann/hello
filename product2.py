products = []
while True:
	name = input('plz enter the name of product')
	if name == 'q':
	    break
	price = input('plz enter the price of the product')
	products.append([name,price])
print(products)

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
