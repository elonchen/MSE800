# Single inheritance

## a class diagram 
```mermaid
classDiagram

class Flight {
    +flight_number: str
    +departure_city: str
    +arrival_city: str
    +base_fare: float
    +display_flight_info()
    +calculate_price()
}

class DomesticFlight {
    +seat_class: str
    +baggage_allowance: int
    +display_domestic_info()
    +calculate_price()
}

class InternationalFlight {
    +passport_required: bool
    +visa_required: bool
    +currency: str
    +show_international_rules()
    +calculate_price()
    +apply_tax()
}

Flight <|-- DomesticFlight
Flight <|-- InternationalFlight
```

## Inheritance Relationship

* **Flight** is the parent (superclass).
* **DomesticFlight** is the child (subclass).
* **InternationalFlight** is the child (subclass).
* The subclass inherits:

  * `flight_number`
  * `departure_city`
  * `arrival_city`
  * `base_fare`
  * `display_flight_info()`
* The subclass adds:

  * `seat_class`
  * `baggage_allowance`
  * `display_domestic_info()`

* The subclass also overrides * `calculate_price()` to demonstrate polymorphism.


