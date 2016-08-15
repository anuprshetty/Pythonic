class Father:

    def __init__(self):
        print("Father class constructor")
        print(f"Base classes of Father class: {Father.__bases__}")

    def __del__(self):
        print("Father class destructor")

    def show_father(self):
        print("Father class method")


class Son(Father):

    def __init__(self):
        super().__init__()
        print("Son class constructor")
        print(f"Base classes of Son class: {Son.__bases__}")

    def __del__(self):
        print("Son class destructor")
        super().__del__()

    def show_son(self):
        print("Son class method")


class GrandSon(Son):

    def __init__(self):
        super().__init__()
        print("GrandSon class constructor")
        print(f"Base classes of GrandSon class: {GrandSon.__bases__}")
    
    def __del__(self):
        print("GrandSon class destructor")
        super().__del__()

    def show_grand_son(self):
        print("Grand son class method")


grand_son = GrandSon()
grand_son.show_grand_son()
grand_son.show_son()
grand_son.show_father()
del grand_son
print("program ends")
