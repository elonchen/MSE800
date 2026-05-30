from Flight import Flight
class InternationalFlight(Flight):

    def __init__(self, flight_number, departure_city, arrival_city,
                 base_fare, passport_required, visa_required, currency):

        super().__init__(flight_number, departure_city, arrival_city, base_fare)

        self.passport_required = passport_required
        self.visa_required = visa_required
        self.currency = currency

    # Method 1
    def show_international_rules(self):
        print("\n--- International Rules ---")
        print("Passport required:", self.passport_required)
        print("Visa required    :", self.visa_required)

    # Method 2 (override)
    def calculate_price(self):
        tax = self.base_fare * 0.15
        return self.base_fare + tax

    # Method 3
    def apply_tax(self):
        print("International tax applied (15%).")