# ── 1. Abstract Base Device (Abstraction + Encapsulation) ─────────────────

class SmartDevice:
    """Base class for every smart device in the office."""

    def __init__(self, device_id: str, name: str):
        self._device_id = device_id   # protected attribute
        self._name = name
        self._is_on = False

    # Encapsulated getters
    def get_id(self) -> str:
        return self._device_id

    def get_name(self) -> str:
        return self._name

    def is_on(self) -> bool:
        return self._is_on

    def turn_on(self):
        self._is_on = True
        print(f"  [{self._name}] {self._device_id} → ON")

    def turn_off(self):
        self._is_on = False
        print(f"  [{self._name}] {self._device_id} → OFF")

    def display_status(self):
        # Polymorphic method — each subclass can extend this
        state = "ON" if self._is_on else "OFF"
        print(f"  {self._device_id:<14} {self._name:<16} [{state}]", end="  ")
        self._show_detail()   # hook for subclass-specific info

    def _show_detail(self):
        # Default implementation: no extra detail
        print()


# ── 2. Concrete Device Classes (Inheritance + Polymorphism) ───────────────

class SmartLight(SmartDevice):
    """A dimmable smart light."""

    def __init__(self, device_id: str):
        super().__init__(device_id, "SmartLight")
        self._brightness = 70   # default brightness percent

    def set_brightness(self, level: int):
        self._brightness = max(0, min(100, level))
        print(f"  [{self._name}] brightness → {self._brightness}%")

    def _show_detail(self):  # override hook
        print(f"brightness={self._brightness}%")


class SmartFan(SmartDevice):
    """A variable-speed smart fan."""

    def __init__(self, device_id: str):
        super().__init__(device_id, "SmartFan")
        self._speed = 3   # default speed (1–5)

    def set_speed(self, level: int):
        self._speed = max(1, min(5, level))
        print(f"  [{self._name}] speed → {self._speed}/5")

    def _show_detail(self):
        print(f"speed={self._speed}/5")


class SmartAC(SmartDevice):
    """A smart air conditioner with temperature control."""

    def __init__(self, device_id: str):
        super().__init__(device_id, "SmartAC")
        self._temperature = 24   # default °C

    def set_temperature(self, temp: int):
        self._temperature = max(16, min(30, temp))
        print(f"  [{self._name}] temp → {self._temperature}°C")

    def _show_detail(self):
        print(f"temp={self._temperature}°C")


# ── 3. Factory Pattern ────────────────────────────────────────────────────

class DeviceFactory:
    """Creates SmartDevice objects without exposing their constructors."""

    _counter = 0   # class-level counter for unique IDs

    @classmethod
    def create(cls, device_type: str) -> SmartDevice:
        cls._counter += 1
        uid = f"{device_type.upper()}-{cls._counter:03d}"   # e.g. LIGHT-001

        if device_type == "light":
            return SmartLight(uid)
        elif device_type == "fan":
            return SmartFan(uid)
        elif device_type == "ac":
            return SmartAC(uid)
        else:
            raise ValueError(f"Unknown device type: '{device_type}'")


# ── 4. Singleton Pattern ──────────────────────────────────────────────────

class ConfigManager:
    """
    System-wide configuration — only ONE instance is allowed.
    Uses __new__ to enforce the singleton guarantee.
    """

    _instance = None   # class-level slot for the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialise()   # run setup only once
        return cls._instance

    def _initialise(self):
        self._office_name = "Main Office"
        self._max_devices = 10

    def get_office_name(self) -> str:
        return self._office_name

    def set_office_name(self, name: str):
        self._office_name = name

    def get_max_devices(self) -> int:
        return self._max_devices

    def display(self):
        print(f"  office      : {self._office_name}")
        print(f"  max devices : {self._max_devices}")
        print(f"  object id   : {id(self)}")


# ── 5. IoT System Controller ──────────────────────────────────────────────

class SmartOfficeSystem:
    """Coordinates device creation, storage, and user interaction."""

    def __init__(self):
        self._devices: dict[str, SmartDevice] = {}
        self._config = ConfigManager()   # always the same singleton

    # ── helpers ─────────────────────────────────────────────────────────

    def _separator(self):
        print("─" * 52)

    def _list_devices(self) -> list[str]:
        return list(self._devices.keys())

    def _pick_device(self) -> SmartDevice | None:
        ids = self._list_devices()
        if not ids:
            print("  No devices registered yet.")
            return None
        print("  Registered devices:")
        for i, did in enumerate(ids, 1):
            print(f"    {i}. {did}")
        try:
            choice = int(input("  Select device number: ")) - 1
            return self._devices[ids[choice]]
        except (ValueError, IndexError):
            print("  Invalid selection.")
            return None

    # ── menu actions ─────────────────────────────────────────────────────

    def cmd_create_device(self):
        print("\n  Device types:  1) light   2) fan   3) ac")
        raw = input("  Enter type: ").strip().lower()
        mapping = {"1": "light", "2": "fan", "3": "ac",
                   "light": "light", "fan": "fan", "ac": "ac"}
        dtype = mapping.get(raw)
        if not dtype:
            print("  Unknown type — skipped.")
            return

        if len(self._devices) >= self._config.get_max_devices():
            print(f"  Max device limit ({self._config.get_max_devices()}) reached.")
            return

        device = DeviceFactory.create(dtype)
        self._devices[device.get_id()] = device
        print(f"  ✓ Created {device.get_name()}  id={device.get_id()}")

    def cmd_turn_on(self):
        device = self._pick_device()
        if device:
            device.turn_on()

    def cmd_turn_off(self):
        device = self._pick_device()
        if device:
            device.turn_off()

    def cmd_display_all(self):
        if not self._devices:
            print("  No devices to display.")
            return
        self._separator()
        print(f"  {'DEVICE ID':<14} {'TYPE':<16} {'STATE':<6}  DETAIL")
        self._separator()
        for device in self._devices.values():
            device.display_status()   # polymorphic call
        self._separator()
        print(f"  Total: {len(self._devices)} device(s)  |  "
              f"Office: {self._config.get_office_name()}")

    def cmd_show_config(self):
        print()
        self._config.display()

    def cmd_change_office(self):
        name = input("  New office name: ").strip()
        if name:
            self._config.set_office_name(name)
            print(f"  ✓ Office name updated → '{name}'")

    def cmd_verify_singleton(self):
        # Prove that two "new" ConfigManagers are the same object
        a = ConfigManager()
        b = ConfigManager()
        same = a is b
        print(f"  ConfigManager() call 1 → id={id(a)}")
        print(f"  ConfigManager() call 2 → id={id(b)}")
        print(f"  a is b → {same}  {'✓ Singleton confirmed' if same else '✗ FAILED'}")

    # ── main loop ─────────────────────────────────────────────────────────

    def run(self):
        print("\n" + "=" * 52)
        print("   Smart Office IoT System")
        print("   Patterns: Factory + Singleton")
        print("=" * 52)
        self._config.display()
        print()

        menu = (
            "\n  ┌─ MENU ────────────────────────────────────┐\n"
            "  │  1) Create device      5) Show config     │\n"
            "  │  2) Turn ON device     6) Change office   │\n"
            "  │  3) Turn OFF device    7) Verify singleton│\n"
            "  │  4) Display all        0) Exit            │\n"
            "  └───────────────────────────────────────────┘"
        )

        actions = {
            "1": self.cmd_create_device,
            "2": self.cmd_turn_on,
            "3": self.cmd_turn_off,
            "4": self.cmd_display_all,
            "5": self.cmd_show_config,
            "6": self.cmd_change_office,
            "7": self.cmd_verify_singleton,
        }

        while True:
            print(menu)
            choice = input("  Choice: ").strip()
            if choice == "0":
                print("\n  System shutdown. Goodbye.\n")
                break
            action = actions.get(choice)
            if action:
                print()
                action()
            else:
                print("  Invalid option.")


# ── Entry point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    system = SmartOfficeSystem()
    system.run()