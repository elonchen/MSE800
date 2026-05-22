```mermaid
sequenceDiagram
    actor Client
    participant DogFactory
    participant Dog

    Client->>DogFactory: create_product(kind=None)
    activate DogFactory
    DogFactory-->>Client: Dog instance (currently None due to unimplemented method)
    deactivate DogFactory

    Client->>Dog: run()
    Dog-->>Client: prints "I'm a Dog, I can run!!"


classDiagram
    class Factory {
        <<abstract>>
        +create_product(kind)
    }

    class AnimalFactory {
        +AnimalFactory()
        +create_product(kind)
    }

    class DogFactory {
        +create_product(kind)
    }

    class CatFactory {
        +create_product(kind)
    }

    class Animals {
        <<abstract>>
        +run()
    }

    class Dog {
        +run()
    }

    class Cat {
        +Cat()
        +run()
    }

    Factory <|-- AnimalFactory
    Factory <|-- DogFactory
    Factory <|-- CatFactory

    Animals <|-- Dog
    Animals <|-- Cat
```

DogFactory does not produce Dog instances



