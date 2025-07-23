import main
# Create an instance of the class
cli = main.PyServerCLI()

# Get all callable methods that don't start with '__'
methods = [func for func in dir(cli) if callable(getattr(cli, func)) and not func.startswith("__")]

# Execute each method and print the result (if any)
for method in methods:
    try:
        result = getattr(cli, method)()
        print(f"{method}() -> {result}")
    except Exception as e:
        print(f"{method}() raised an exception: {e}")
