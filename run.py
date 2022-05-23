from product import Product

if __name__ == '__main__':
    prod = Product('174948842042')
    prod.sample_current_price()
    print(prod.price_history)