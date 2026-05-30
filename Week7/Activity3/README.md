# OOP Mini-Project: Smart Office IoT Management System

## Project Description

In modern offices, Internet of Things (IoT) technology is widely used to automate and manage smart devices such as lights, fans, and air conditioners. This mini-project simulates a simple Smart Office IoT Management System that allows users to create and manage different smart devices dynamically.

The system accepts user input to select a device type and then creates the corresponding smart device object automatically. Each device can display its current operating status. In addition, the system uses a single configuration manager to store global settings throughout the application runtime.

---

## Design Patterns Used

1. Factory Pattern
  Problem : The calling code should not know (or care) which concrete class
            it is instantiating — it just says "give me a fan".
  Solution: DeviceFactory.create(type) hides the constructor calls and
            returns the correct subclass. Adding a new device type only
            requires editing the factory, not every caller.

1. Singleton Pattern
  Problem : If multiple parts of the code each create their own
            ConfigManager, settings would be inconsistent and wasteful.
  Solution: ConfigManager.__new__ checks for an existing instance and
            returns it instead of creating a new one. The same object is
            always returned no matter how many times it is instantiated.





## Sample outputs
```
====================================================
   Smart Office IoT System
   Patterns: Factory + Singleton
====================================================
  office      : Main Office
  max devices : 10
  object id   : 4463859664


  ┌─ MENU ────────────────────────────────────┐
  │  1) Create device      5) Show config     │
  │  2) Turn ON device     6) Change office   │
  │  3) Turn OFF device    7) Verify singleton│
  │  4) Display all        0) Exit            │
  └───────────────────────────────────────────┘
  Choice: 7

  ConfigManager() call 1 → id=4463859664
  ConfigManager() call 2 → id=4463859664
  a is b → True  ✓ Singleton confirmed

  ┌─ MENU ────────────────────────────────────┐
  │  1) Create device      5) Show config     │
  │  2) Turn ON device     6) Change office   │
  │  3) Turn OFF device    7) Verify singleton│
  │  4) Display all        0) Exit            │
  └───────────────────────────────────────────┘
  Choice: 1


  Device types:  1) light   2) fan   3) ac
  Enter type: 1
  ✓ Created SmartLight  id=LIGHT-001

  ┌─ MENU ────────────────────────────────────┐
  │  1) Create device      5) Show config     │
  │  2) Turn ON device     6) Change office   │
  │  3) Turn OFF device    7) Verify singleton│
  │  4) Display all        0) Exit            │
  └───────────────────────────────────────────┘

  Choice: 2

  Registered devices:
    1. LIGHT-001
  Select device number: 1
  [SmartLight] LIGHT-001 → ON

  ┌─ MENU ────────────────────────────────────┐
  │  1) Create device      5) Show config     │
  │  2) Turn ON device     6) Change office   │
  │  3) Turn OFF device    7) Verify singleton│
  │  4) Display all        0) Exit            │
  └───────────────────────────────────────────┘
  Choice: 3

  Registered devices:
    1. LIGHT-001
  Select device number: 1
  [SmartLight] LIGHT-001 → OFF

  ┌─ MENU ────────────────────────────────────┐
  │  1) Create device      5) Show config     │
  │  2) Turn ON device     6) Change office   │
  │  3) Turn OFF device    7) Verify singleton│
  │  4) Display all        0) Exit            │
  └───────────────────────────────────────────┘
```