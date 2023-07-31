from collections import UserDict, UserList


class Field:
    def __init__(self, value):
         self.value = value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str(self)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record():
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones =  []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        if phone.value not in [phone.value for phone in self.phones]:
            self.phones.append(phone)
            return print(f"Номер {phone} було добавлено до контакту {self.name} та збережено.")
        return print (f"Номер {phone} вже записаний у номерах контакту {self.name}")
    
    def change_phone(self,old_phone,new_phone):
        for i,p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[i] = new_phone
                return print(f"Старий номер {old_phone} було змінено на новий номер {new_phone}")
        print (f"Старий номер {old_phone} не знайдено. Новий номер {new_phone} був доданий до контакту {self.name}")
        self.phones.append(new_phone)   

    def __str__(self):
        return f"{self.name}:{' '.join(str(rec) for rec in self.phones)}"

 
class AddressBook(UserDict):
    #def __init__(self):
        #self.phone_book = {}

    #def show_all(self):
        #return self.phone_book
    
    def add_rec(self, record: Record):
        self.data[record.name.value] = record
        return print(f"Контакт {record} було добавлено.")
    
    def __str__(self) -> str:
        return "\n".join(str(rec) for rec in self.data.values())
    
    
def error(function):
    def error_processing(list_input):
        try:
            return function(list_input)
        except ValueError:
            return print("Трапилася помилка: ValueError")
        except IndexError:
            return print("Трапилася помилка: IndexError Було введено не вірні данні")
        except TypeError:
            return print("Трапилася помилка: TypeError")
    return error_processing


import re

def hi(*args):
    return print("How can I help you?")

@error
def add(list_input):
    name = Name(list_input[1])
    phone = Phone(list_input[2])
    rec: Record = phone_book.get(str(name))
    #print(rec,"rec")
    #print(phone_book.get(str(name)),"phone_book.get(str(name))")
    if rec:
        return rec.add_phone(phone)
    rec = Record(name,phone)
    phone_book.add_rec(rec)

def change(list_input):
    if len(list_input) < 4:
        return print("Для зміни номеру введіть після команди 'change' ім'я та номер який треба змінити та новий номер.")
    if len(list_input) >= 4:
        for i in phone_book.keys():
            if (list_input[1]) == i:
                old_ph = Phone(list_input[2])
                new_ph = Phone(list_input[3])
                rec: Record = phone_book.get(str(i))
                if rec:
                    rec.change_phone(old_ph,new_ph)
                return None
    print("Контакт з таким ім'ям не знайдено тому було сформовано новий контакт та збережено обидва номери")              
    name = Name(list_input[1])
    phone = Phone(list_input[2])
    #rec = Record(Name(list_input[1]), Phone(list_input[2]))
    #phone_book.add_rec(rec.add_phone(Phone(list_input[3])))
    rec = Record(name, phone)
    phone = Phone(list_input[3])
    rec.add_phone(phone)
    phone_book.add_rec(rec)

def phone(list_input):
    for i in phone_book.keys():
            if (list_input[1]) == i:
                return print(f"Ваш контакт:\n{phone_book[i]}")
    return print(f"Ваш контакт {list_input[1]} не знайдено.")        

def show_all(*args):
    print("Ваш список контактів:")
    print(phone_book)
    return phone_book

def not_know():
    str_out = "Сommands not recognized.\nEnter commands that I know: "
    for i in list_out:
        str_out += (str(i) + ", ")
    str_out += "if you want me to finish working.\nOr one of the commands: "
    for i in dict_def.keys():
        str_out += (i + ", ")
    str_out += "if you want me to help you."
    return str_out

def  double_commands(list):
    if (len(list)>1) and ((list[0] == "show") and (list[1].lower() == "all")):
        return "show all" 
    else:
        return list[0]

phone_book = AddressBook()

list_out = ["good bye","close","exit"]
dict_def = {"hello": hi, "add": add, "change": change, "phone": phone, "show": show_all }

def bot_start():
    print("\nHi, I'm a helper bot))). How can I help you?")
    list_command = []
    while True:
        input_text = input("Waiting for commands: ").lower()
        list_command = re.split(r"[ ]+",input_text)
        if list_command[0] in dict_def.keys():
            dict_def[list_command[0]](list_command)
        elif input_text in list_out:
            print("Good bye!")
            break
        else:
            print(not_know())

bot_start()