class Flight:
    """
    General Flight class.
    This class contains attributes and methods
    that are shared by all flight types.
    """

    def __init__(self, flight_number, departure_city,
                 arrival_city, base_fare):

        # Shared attributes
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.base_fare = base_fare

    def display_flight_info(self):
        """
        Display general flight information.
        This method can be inherited directly
        by subclasses.
        """

        print("\n===== Flight Information =====")
        print(f"Flight Number : {self.flight_number}")
        print(f"Departure City: {self.departure_city}")
        print(f"Arrival City  : {self.arrival_city}")
        print(f"Base Fare     : ${self.base_fare:.2f}")

    def calculate_price(self):
        """
        Return the base fare.
        Can be overridden by subclasses.
        """

        return self.base_fare