def make_bold(func_ref):
    def wrapper(*args):
        result=func_ref(*args)
        return "<b>"+result+  "</b>"

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return "<i>" +result+ "</i>"

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return "<u>"+result+ "</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))


