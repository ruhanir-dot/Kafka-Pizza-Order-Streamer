import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        validPizzaNames = [
            "Margherita", 
            "Pepperoni", 
            "Hawaiian", 
            "Veggie", 
            "BBQ Chicken", 
            "Meat Lovers",
        ]
        return validPizzaNames[random.randint(0, len(validPizzaNames)-1)]
    