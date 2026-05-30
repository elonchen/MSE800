from DomesticFlight import DomesticFlight

def main():

    # Create a DomesticFlight object
    flight1 = DomesticFlight(
        flight_number="NZ501",
        departure_city="Auckland",
        arrival_city="Wellington",
        base_fare=180.00,
        seat_class="Business",
        baggage_allowance=23
    )

    # Inherited method from Flight
    flight1.display_flight_info()

    # Subclass-specific method
    flight1.display_domestic_info()


# Run the program
if __name__ == "__main__":
    main()