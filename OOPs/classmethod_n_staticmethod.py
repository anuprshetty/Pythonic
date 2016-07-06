class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    # static methods are used to place functions inside a class.
    # Binding a function to a class or object.
    @staticmethod
    def static_method():
        print(f"Called static method")

    
classtest = ClassTest()
# instance_method
classtest.instance_method()
# class_method
ClassTest.class_method()
# static_method
classtest.static_method()
ClassTest.static_method()
