from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,ID):
        self._name = name
        self._ID = ID

    @abstractmethod
    def show_menu(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self,value):
        pass

    @name.deleter
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def ID(self):
        pass

    @ID.setter
    @abstractmethod
    def ID(self,value):
        pass

    @ID.deleter
    @abstractmethod
    def ID(self):
        pass

class Customer(User):
    count = 0

    def __init__(self,name,ID,balance):
        super().__init__(name,ID)
        self.__balance = balance
        Customer.count += 1

    @classmethod
    def getCount(cls):
        return cls.count

    def show_menu(self):
        print("======CUSTOMER MENÜ======")
        print("1 -> Para Yatır")
        print("2 -> Para Çek")
        print("3 -> Başka Hesaba Para Gönder")
        print("4 -> Çıkış\n")

        while (True):
            try:
                choice = int(input("Lütfen Seçiminizi Yapınız: "))

                if choice == 1:
                    print("Para Yatır Seçildi. Yöneldiriliyorsunuz...\n")
                    return choice
                elif choice == 2:
                    print("Para Çek Seçildi. Yöneldiriliyorsunuz...\n")
                    return choice
                elif choice == 3:
                    print("Başka Hesaba Para Gönder Seçildi. Yöneldiriliyorsunuz...\n\n")
                    return choice
                elif choice == 4:
                    print("Çıkış Seçildi. Yönlendiriliyorsunuz...\n")
                    return choice
                else:
                    print("Geçersiz seçim. Lütfen tekrar deneyiniz.\n")

            except (ValueError, TypeError) as e:
                print(f"Tekar Deneyiniz. Hata Oluştu {e}")

    def para_yatir(self,value):
        self.__balance += value
        print(f"\nSayın {self._name} Hesabınıza {value} Başarıyla Yatırılmıştır.")
        print(f"Güncel Bakiye: {self.__balance}")

    def para_cek(self,value):
        if self.__balance < value:
            print("\nBakiyeniz Yetersiz İşlem Tamamlanamamıştır")
            return
        self.__balance -= value
        print(f"\nSayın {self._name} Hesabınızdan {value} Başarıyla Çekilmiştir.")
        print(f"Güncel Bakiye: {self.__balance}")

    def para_gonder(self,value,other):
        if self.__balance < value:
            print("\nBakiyeniz Yetersiz İşlem Tamamlanamamıştır")
            return
        self.__balance -= value
        other.balance += value
        print(f"\nSayın {self._name} Hesabınızdan {value} Başarıyla Gönderilmiştir.")
        print(f"Güncel Bakiye: {self.__balance}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("Girdi Boş Olamaz")
        self._name = value

    @name.deleter
    def name(self):
        self._name = None
        print("Name Attribute'si Silinmiştir")

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self,value):
        if not value:
            raise ValueError("Girdi Boş Olamaz")
        self._ID = value

    @ID.deleter
    def ID(self):
        self._ID = None
        print("ID Attribute'si Silinmiştir")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,value):
        if not value:
            raise ValueError("Girdi Boş Olamaz")
        self.__balance = value

    @balance.deleter
    def balance(self):
        self.__balance = None
        print("Balance Attribute'si Silinmiştir")

class Employee(User):

    def __init__(self):
        super().__init__("Admin",12345)

    def show_menu(self):
        print("======EMPLOYEE MENÜ======")
        print("1 -> Bilgi Göster")
        print("2 -> Çıkış\n")

        while (True):
            try:
                choice = int(input("Lütfen Seçiminizi Yapınız: "))

                if choice == 1:
                    print("Bilgi Seçildi. Yöneldiriliyorsunuz...\n")
                    return choice
                elif choice == 2:
                    print("Çıkış Seçildi. Yönlendiriliyorsunuz...\n")
                    return choice
                else:
                    print("Geçersiz seçim. Lütfen tekrar deneyiniz.\n")

            except (ValueError, TypeError) as e:
                print(f"Tekar Deneyiniz. Hata Oluştu {e}")

    def show_info(self,ID,customers: list[Customer]):
        for i in range(int(Customer.getCount())):
            if customers[i].ID == ID :
                print(f"Müsşetrinin İsmi: {customers[i].name}")
                print(f"Müşterinin ID'si: {customers[i].ID}")
                print(f"Müşterinin Bakiyesi: {customers[i].balance}")
                return
        else:
                print("Girmiş olduğunuz ID'de bir kayıt bulunamadı.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("Girdi Boş Olamaz")
        self._name = value

    @name.deleter
    def name(self):
        self._name = None
        print("Name Attribute'si Silinmiştir")

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self,value):
        if not value:
            raise ValueError("Girdi Boş Olamaz")
        self._ID = value

    @ID.deleter
    def ID(self):
        self._ID = None
        print("ID Attribute'si Silinmiştir")








