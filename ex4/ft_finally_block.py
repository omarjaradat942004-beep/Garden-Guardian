class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        GardenError.__init__(self, message)


def water_plant(plant_name: str) -> None:
    if (plant_name != plant_name.capitalize()):
        raise PlantError("Caught PlantError: Invalid plant name to water:"
                         f"{plant_name}ending tests and returning"
                         "to main Closing wateing system")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(e)
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


if (__name__ == "__main__"):
    test_watering_system()
