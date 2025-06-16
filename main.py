class house():

    company_name = "Awesome building comppany"

    inflation_coefficient = 1.08

    def __init__(self, address, state, Alarm, price):
        """ The self let's you know that a certain attribute changes from object to object. """
        self.address = address
        self.state = state
        self.Alarm  = Alarm
        self.price = price

    def correctPriceMethod(self):
        self.price = self.price * self.inflation_coefficient

apartment1 = house(123, "california", False, 300000)
apartment2 = house(5678, "california", False, 300000)
apartment3price = 300000

# ----------------------------------
apartment1.correctPriceMethod()

# -----------------------------------
house.correctPriceMethod(apartment2)

# -----------------------------------
def correctPricefunction(apartment):
    return apartment * 1.08

print(apartment3price)

apartment3price = correctPricefunction(apartment3price)
print(apartment3price)