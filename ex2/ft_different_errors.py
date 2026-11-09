def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        print("Testing operation 0...")
        int("abc")
    elif (operation_number == 1):
        print("Testing operation 1...")
        10/0
    elif (operation_number == 2):
        print("Testing operation 2...")
        file = open("test.txt", "r")
        file.close()
    elif (operation_number == 3):
        print("Testing operation 3...")
        "hello" + 10
    else:
        print("Testing operation 4...")


def test_error_types() -> None:
    try:
        print("=== Garden Error Types Demo ===")
        garden_operations(2)
        print("Operation completed successfully")
    except ValueError:
        print("Caught ValueError: invalid literal for"
              "int() with base 10: ’abc’")
    except ZeroDivisionError:
        print("division by zero")
    except FileNotFoundError:
        print("[Errno 2] No such file or directory:")
    except TypeError:
        print("can only concatenate str (not int) to str")

    print("All error types tested successfully!")


test_error_types()
