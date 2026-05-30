from Flight import Flight
# DomesticFlight inherits from Flight.
class DomesticFlight(Flight):
    """
    Additional attributes:
    - seat_class
    - baggage_allowance

    Additional method:
    - display_domestic_info()
    """

    def __init__(self, flight_number, departure_city,
                 arrival_city, base_fare,
                 seat_class, baggage_allowance):

        # Call parent constructor
        super().__init__(
            flight_number,
            departure_city,
            arrival_city,
            base_fare
        )

        # Domestic-flight-specific attributes
        self.seat_class = seat_class
        self.baggage_allowance = baggage_allowance

    def calculate_price(self):
        """
        Override the parent method.

        Domestic flights may charge extra
        depending on seat class.
        """

        if self.seat_class.lower() == "business":
            return self.base_fare + 120

        return self.base_fare
        
    # Display domestic-flight-specific details.
    def display_domestic_info(self):
        print("\n===== Domestic Flight Details =====")
        print(f"Seat Class       : {self.seat_class}")
        print(f"Baggage Allowance: {self.baggage_allowance} kg")
        print(f"Final Ticket Cost: ${self.calculate_price():.2f}")