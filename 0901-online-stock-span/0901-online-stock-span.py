class StockSpanner:
    def __init__(self):
        self.prices = list()
        self.span = list()

    def next(self, price: int) -> int:
        result = 1
        i = len(self.prices) - 1
        while i >= 0 and self.prices[i] <= price:
            result += self.span[i]
            i -= self.span[i]
        self.prices.append(price)
        self.span.append(result)
        return result
            



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)