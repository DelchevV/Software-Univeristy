def logged(func_ref):
    def wrapper(*args):
        result = f"you called {func_ref.__name__}{args}" + "\n"
        result += "it returned " + str((func_ref(*args)))

        return result

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))




