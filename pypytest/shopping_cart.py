class ShoppingCart:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size
        pass
    
    def add(self, item):
        if self.size() == self.max_size:
            raise OverflowError("Cart is full!")
        self.items.append(item)
        pass
    
    def size(self):
        return len(self.items)
    
    def get_items(self):
        return self.items
    
    def get_total_price(self, prices):
        prices_arr = [prices[item] for item in self.items]
        return sum(prices_arr)