a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # global a                      # Task 2.1
        # nonlocal a                    # Task 2.2
        a = "I am local variable!"
        print(a)
    inner_function()                    # Task 1


enclosing_funcion()                     # Task 1