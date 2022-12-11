def even_parameters(func_ref):
    def wrapper(*args):
        for el in args:
            if isinstance(el, int) and el % 2 == 0:
                continue
            else:
                return 'Please use only even numbers!'

        return func_ref(*args)

    return wrapper


@even_parameters
def func(*args):
    return sum(args)


print(func(4, "4", 4))

