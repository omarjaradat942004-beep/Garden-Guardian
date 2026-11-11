def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    try:
        Input: str = "23a"
        print("=== Garden Temperature ===\n")
        print(f"Input data is ’{Input}’")
        input_temperature(Input)
        print(f"Temperature is now {Input}°C")
    except ValueError:
        print(f"Caught input_temperature error:10:"
              f"’{Input}’invalid literal for int() with base")

    print("All tests completed - program didn’t crash!")


if (__name__ == "__main__"):
    test_temperature()
