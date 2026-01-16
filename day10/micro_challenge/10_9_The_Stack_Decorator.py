# Goal: Apply two decorators: @bold and @italic to a string returning function. 
# Deep dive: Decorators stack from bottom to top (Inner to Outer).
#            @bold @italic becomes bold(italic(func())). Order matters!

from functools import wraps
def bold(func):
    @wraps(func)
    def wrap():
        return f"<b>{func()}</b>"
    return wrap

def italic(func):
    def wrap():
        return f"<i>{func()}</i>"
    return wrap


@bold
@italic
@bold
def text():
    return "Hello"

print(text())