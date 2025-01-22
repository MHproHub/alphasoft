import ctypes
import os

class PowerSettingsManager:
    def __init__(self):
        self.GUID_MAX_POWER_SAVINGS = "{a1841308-3541-4fab-bc81-f71556f20b4a}"
        self.GUID_MIN_POWER_SAVINGS = "{8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c}"
        self.GUID_BALANCED = "{381b4222-f694-41f0-9685-ff5bb260df2e}"

    def set_power_scheme(self, scheme_guid):
        """Set the power scheme to the given GUID."""
        try:
            command = f"powercfg /SETACTIVE {scheme_guid}"
            os.system(command)
            print(f"Power scheme set to {scheme_guid}")
        except Exception as e:
            print(f"Failed to set power scheme: {e}")

    def get_current_power_scheme(self):
        """Get the current active power scheme."""
        try:
            result = os.popen("powercfg /GETACTIVESCHEME").read()
            print("Current power scheme:", result)
        except Exception as e:
            print(f"Failed to get current power scheme: {e}")

    def customize_power_settings(self, balance=True):
        """Switch between balanced and high performance power settings."""
        if balance:
            self.set_power_scheme(self.GUID_BALANCED)
        else:
            self.set_power_scheme(self.GUID_MIN_POWER_SAVINGS)

def main():
    manager = PowerSettingsManager()
    print("Welcome to AlphaSoft: Custom Power Setting Manager")
    
    while True:
        print("\nChoose an option:")
        print("1. Set High Performance")
        print("2. Set Balanced")
        print("3. Get Current Power Scheme")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.customize_power_settings(balance=False)
        elif choice == '2':
            manager.customize_power_settings(balance=True)
        elif choice == '3':
            manager.get_current_power_scheme()
        elif choice == '4':
            print("Exiting AlphaSoft.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()