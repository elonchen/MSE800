Here is a breakdown of the architectural design patterns, components, and data flow used in this Aquarium Management System.

---

### 1. High-Level Architectural Layout

```
                  ┌──────────────────────────────┐
                  │      Main Loop / UI Layer    │
                  └──────────────┬───────────────┘
                                 │ Interacts with
                                 ▼
                  ┌──────────────────────────────┐
                  │    AquariumManager (Host)    │ ◄─── Ensures single state
                  │     [ Singleton Pattern ]    │      & direct DB link
                  └──────────────┬───────────────┘
                                 │
           ┌─────────────────────┴─────────────────────┐
           ▼ Uses                                      ▼ Coordinates
┌──────────────────────┐                     ┌──────────────────┐
│     FishFactory      │                     │ SQLite Database  │
│ [ Factory Pattern ]  │                     │  (aquarium.db)   │
└──────────┬───────────┘                     └──────────────────┘
           │ Instantiates based on input
           ▼
┌──────────────────────────────────────────────────────┐
│  Polymorphic Products: Goldfish, Shark, Tuna, etc.   │
└──────────────────────────────────────────────────────┘

```

---

### 2. Deep Dive Into the Design Patterns

#### A. The Singleton Pattern (`AquariumManager`)

In an architectural system, an inventory data store or database pipeline must have a **Single Source of Truth**. If multiple parts of a program created their own instances of an aquarium manager, they would compete for file access to the SQLite database, causing write-locks, thread collisions, or mismatched memory counters.

* **How it works:** By overriding the `__new__` method, Python intercepts the creation of the class. If an instance already exists, it ignores subsequent constructor calls and hands back the exact same memory address.
* **Architectural benefit:** Centralizes the SQLite pipeline connection. Only one database connection is open and active during runtime.

#### B. The Factory Pattern (`FishFactory`)

The user interface passes string data (like `"Goldfish"` or `"Shark"`). If the UI layer explicitly instantiated these objects using hardcoded conditionals, the user-facing side of the application would become tightly coupled to individual data classes.

* **How it works:** The UI doesn't know (and doesn't care) how many classes exist or how they are named. It simply handles a string to `FishFactory.create_fish(string)`. The factory functions as a gatekeeper, processing text, checking it against whitelist security arrays (`VALID_FISH`), and spitting out an initialized, polymorphic class object.
* **Architectural benefit:** Decouples creation logic from implementation logic. If you want to add a 6th fish category down the line, you don't touch the database layer or the UI layer; you change only the Factory.

#### C. Polymorphism / Inheritance (`Fish` Interface)

Every specific fish class inherits from an Abstract Base Class (ABC) named `Fish`.

* **How it works:** The base class enforces a contractual architectural obligation via `@abstractmethod`. Every subclass must implement `get_category()`.
* **Architectural benefit:** Safe code execution. The `AquariumManager` can invoke `.get_category()` confidently on *any* object returned by the factory, without worrying about what exact animal species it is dealing with.

---

### 3. Data Flow Execution Lifecycle (The CRUD Pipeline)

Let's look at what happens under the hood when a user chooses to **Create/Update** an entry:

1. **Input Capturing:** The UI captures user parameters (`"shark"`, `2`).
2. **Factory Interception:** The string is piped to `FishFactory`. The factory matches it against permitted components, creates a `Shark()` instance, and yields it back to the core runtime manager.
3. **Data Extraction:** The `AquariumManager` calls the structural `.get_category()` method on the newly minted object to retrieve its contextual category metadata (`"Marine (Apex Predator)"`).
4. **Database Persistence Layer:** The manager issues a prepared SQL transaction statement to the local SQLite storage layer using an **UPSERT** statement logic flow:
```sql
INSERT INTO inventory (fish_name, category, count) VALUES (?, ?, ?)
ON CONFLICT(fish_name) DO UPDATE SET count = count + excluded.count;

```


