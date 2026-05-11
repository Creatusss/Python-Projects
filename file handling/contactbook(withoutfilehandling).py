class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def cont(self):
        print(f"{self.name} | {self.phone}")

print("   Contact Book\nName & Phone Number")

Person1 = Contact("Charles", "09123456789")
Person1.cont()

Person2 = Contact("Vence", "09876543219")
Person2.cont()