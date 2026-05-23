import sqlite3
from abc import ABC, abstractmethod


# =====================================================================
# 1. THE FISH PRODUCT HIERARCHY (Factory Pattern)
# =====================================================================
class Fish(ABC):
    """Abstract Base Class for all fish types."""
    @abstractmethod
    def get_category(self) -> str:
        pass


class Goldfish(Fish):
    def get_category(self) -> str:
        return "Freshwater (Coldwater)"


class Shark(Fish):
    def get_category(self) -> str:
        return "Marine (Apex Predator)"


class Angelfish(Fish):
    def get_category(self) -> str:
        return "Freshwater (Tropical)"


class Tuna(Fish):
    def get_category(self) -> str:
        return "Marine (Pelagic Open Ocean)"


class Salmon(Fish):
    def get_category(self) -> str:
        return "Anadromous (Migratory)"


# =====================================================================
# 2. THE FISH FACTORY (Factory Pattern)
# =====================================================================
class FishFactory:
    """Factory to validate and instantiate permitted fish objects."""
    VALID_FISH = {"goldfish", "shark", "angelfish", "tuna", "salmon"}

    @staticmethod
    def create_fish(fish_type: str) -> Fish:
        normalized_type = fish_type.strip().lower()
        
        if normalized_type not in FishFactory.VALID_FISH:
            raise ValueError(f"'{fish_type}' is not permitted in this aquarium.")
        
        if normalized_type == "goldfish": return Goldfish()
        if normalized_type == "shark": return Shark()
        if normalized_type == "angelfish": return Angelfish()
        if normalized_type == "tuna": return Tuna()
        if normalized_type == "salmon": return Salmon()


# =====================================================================
# 3. THE AQUARIUM MANAGER (Singleton Pattern + SQLite CRUD)
# =====================================================================
class AquariumManager:
    """Singleton class handling database persistence and CRUD operations."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AquariumManager, cls).__new__(cls)
            # Initialize connection to local SQLite database file
            cls._instance.conn = sqlite3.connect("aquarium.db")
            cls._instance.cursor = cls._instance.conn.cursor()
            cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        """Creates the inventory table if it doesn't already exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                fish_name TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                count INTEGER NOT NULL DEFAULT 0
            )
        """)
        self.conn.commit()
        
    # --- CLOSE ---
    def close(self):
        self.conn.close()

    # --- CREATE / UPDATE ---
    def add_or_update_fish(self, fish_name: str, count: int):
        """UPSERT operation: Adds fish quantity or updates existing entry."""
        if count <= 0:
            print("❌ Quantity must be greater than 0.")
            return

        try:
            # Validate via Factory
            fish_obj = FishFactory.create_fish(fish_name)
            category = fish_obj.get_category()
            display_name = fish_name.strip().capitalize()

            # SQLite UPSERT clause (inserts or adds to existing quantity)
            self.cursor.execute("""
                INSERT INTO inventory (fish_name, category, count)
                VALUES (?, ?, ?)
                ON CONFLICT(fish_name) DO UPDATE SET count = count + excluded.count
            """, (display_name, category, count))
            self.conn.commit()
            print(f"✅ Successfully added/updated {count} {display_name}(s) in the database.")
        except ValueError as e:
            print(f"❌ Error: {e}")

    # --- READ ---
    def display_status(self):
        """Fetches and displays all records from the database."""
        self.cursor.execute("SELECT fish_name, category, count FROM inventory WHERE count > 0")
        rows = self.cursor.fetchall()

        print("\n" + "="*55)
        print("          SQLITE LIVE AQUARIUM INVENTORY          ")
        print("="*55)
        
        if not rows:
            print("The aquarium database is currently empty (or all counts are 0).")
        else:
            print(f"{'Fish Type':<15} | {'Category':<28} | {'Count':<5}")
            print("-" * 55)
            for row in rows:
                print(f"{row[0]:<15} | {row[1]:<28} | {row[2]:<5}")
        print("="*55 + "\n")

    # --- DELETE / REDUCE ---
    def remove_fish(self, fish_name: str, count: int):
        """Reduces fish count, or completely deletes row if count hits 0."""
        display_name = fish_name.strip().capitalize()
        
        # Check if fish exists
        self.cursor.execute("SELECT count FROM inventory WHERE fish_name = ?", (display_name,))
        row = self.cursor.fetchone()
        
        if not row:
            print(f"❌ {display_name} is not in the aquarium.")
            return

        current_count = row[0]
        if count >= current_count:
            # Delete completely if removing equal or more than current stock
            self.cursor.execute("DELETE FROM inventory WHERE fish_name = ?", (display_name,))
            print(f"🗑️ All {display_name}s have been removed from the database.")
        else:
            # Reduce count
            self.cursor.execute("UPDATE inventory SET count = count - ? WHERE fish_name = ?", (count, display_name))
            print(f"📉 Removed {count} {display_name}(s). New balance: {current_count - count}")
            
        self.conn.commit()


# =====================================================================
# 4. INTERACTIVE USER INTERFACE
# =====================================================================
def main():
    aquarium = AquariumManager()
    
    print("Welcome to the SQLite-Powered Aquarium Management System!")
    print("Permitted species: Goldfish, Shark, Angelfish, Tuna, Salmon\n")
    
    while True:
        print("Options: [1] Add/Update Fish (C/U) [2] View Status (R) [3] Remove Fish (D) [4] Exit")
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            name = input("Enter fish name: ")
            try:
                qty = int(input(f"How many {name}s to add? "))
                aquarium.add_or_update_fish(name, qty)
            except ValueError:
                print("❌ Please enter a valid integer for quantity.")
                
        elif choice == '2':
            aquarium.display_status()
            
        elif choice == '3':
            name = input("Enter fish name to remove: ")
            try:
                qty = int(input(f"How many {name}s to remove? "))
                aquarium.remove_fish(name, qty)
            except ValueError:
                print("❌ Please enter a valid integer for quantity.")
                
        elif choice == '4':
            aquarium.close()
            print("Closing database connection. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()