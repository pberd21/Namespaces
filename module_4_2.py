def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
# Попытка вызвать inner_function вне test_function это вызовет ошибку
# inner_function()  # Потому что вызовет NameError: name 'inner_function' is not defined
