def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    try:
        Input: str = "215"
        print("=== Garden Temperature ===\n")
        print(f"Input data is ’{Input}’")
        input_temperature(Input)
        if (int(Input) > 40):
            raise Exception(f"Caught input_temperature error:"
                            f"{Input}°C is too hot for plants (max 40°C)")
        if (int(Input) < 0):
            raise Exception(f"Caught input_temperature error:"
                            f"{Input}°C is too cold for plants (min 0°C)")
        print(f"Temperature is now {Input}°C")
    except ValueError:
        print(f"Caught input_temperature error:10:"
              f"’{Input}’invalid literal for int() with base")
    except Exception as e:
        print(e)

    print("All tests completed - program didn’t crash!")


if (__name__ == "__main__"):
    test_temperature()
