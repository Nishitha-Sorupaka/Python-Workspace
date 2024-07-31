class Base:
    def __init__(self):
        self.__protected_member = "I am protected"

    def get_private_member(self):
        return self.__private_member

class Derived(Base):
    def __init__(self):
        super().__init__()
        #print(self.__protected_member)  # Accessible in subclass

base_instance = Base()
der_instance = Derived()
print(base_instance._Base__protected_member)
#print(der_instance._protected_member)
#print(base_instance._protected_member)
