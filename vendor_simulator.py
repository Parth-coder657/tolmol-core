class VendorSimulator:
    def __init__(self, item_name, initial_inflated_price):
        self.item_name = item_name
        self.current_price = initial_inflated_price

    def respond(self, buyer_message):
        # Stubborn supplier logic for automated testing rounds
        self.current_price -= 2.0
        return f"Look, $38 is impossible for {self.item_name}. The absolute best I can do is ${self.current_price} per unit, and that's only because you are buying bulk."