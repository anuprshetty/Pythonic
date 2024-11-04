class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise CustomException("custom error")
except CustomException as e:
    print(e)
