

# The decorator to make it bold
def makebold(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        print('aaa')
        return "<b>" + fn() + "</b>"
    return wrapper

# The decorator to make it italic
def makeitalic(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        print('bbb')
        return "<i>" + fn() + "</i>"
    return wrapper


@makeitalic
@makebold
def say():
    return "hello"

def main1():
    print(say())

# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It's ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don't want to ever touch again.
# @my_shiny_new_decorator
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")


if __name__ == "__main__":
    # a_stand_alone_function()

    # equals below

    a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
    a_stand_alone_function_decorated()
    
    print()
    print(main1())


# which get  注意解析的顺序 另外 因为会失去原始名称和文档字符串 需要使用functools内置的 wraps 装饰器
# from functools import wraps
# Before the function runs
# I am a stand alone function, don't you dare modify me
# After the function runs
# ()
# bbb
# aaa
# <i><b>hello</b></i>
# None

