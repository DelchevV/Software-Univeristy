def type_check(check_for_type):
    def decorator(func_ref):
        def wrapper(el):
            if isinstance(el, check_for_type):
                return func_ref(el)
            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))

