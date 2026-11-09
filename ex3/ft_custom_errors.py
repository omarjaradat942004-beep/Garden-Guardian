class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        GardenError.__init__(self, message)


def testing_planterror() -> None:
    try:
        print("Testing PlantError...")
        wilting: bool = True
        if (wilting):
            raise PlantError()
    except PlantError as e:
        print("Caught PlantError: ", end="")
        print(e)
    print("All custom error types work correctly!")


def testing_watererror() -> None:
    try:
        print("Testing WaterError...")
        water: int = 20
        if (water < 50):
            raise WaterError()
    except WaterError as e:
        print("Caught WaterError: ", end="")
        print(e)
    print("All custom error types work correctly!")


def testing_everything() -> None:
    print("Testing catching all garden errors...")
    try:
        wilting: bool = True
        if (wilting):
            raise PlantError()
    except GardenError as e:
        print("Caught GardenError: ", end="")
        print(e)

    try:
        water: int = 20
        if (water < 50):
            raise WaterError()
    except GardenError as e:
        print("Caught GardenError: ", end="")
        print(e)
    print("All custom error types work correctly!")


testing_planterror()
print()
testing_watererror()
print()
testing_everything()
