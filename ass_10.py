# my name is Hazem Alaswad

class PhoneDirectory:                                 # this is the phone directory class

    
    def __init__(self):                               # def __init__ is a constructor function to define variables
        self.__name = ""
        self.__number = ""

   
    def get_number(self):                             # def get_number is a function to get the number
        return self.__number

    
    def get_name(self):                               # def get_name is a funtion to get the name
        return self.__name

    
    def set_contact(self, name, number):              # def set_contact is a function to set contact details
        self.__name = name
        self.__number = number

    
    def is_valid_number(self):                        # def is_valid_number is a function to check if the number is valid
        try :
            num = int(self.__number)
            return True
        except:
            return False

    
    def is_valid_name(self):                          # def is_valid_name is a function to check if the name is valid
        name = self.__name.strip()
        if len(name)<2:
            return False

        return True

if __name__ == "__main__":                            # this is the main function
    p = PhoneDirectory()
    p.set_contact("Jack","9128883892")
    print(p.get_name(), p.get_number())
    print(" Valid Number? :", p.is_valid_number())
    print(" Valid Name? :", p.is_valid_name())
