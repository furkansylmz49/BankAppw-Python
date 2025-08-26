from BankApp_func import main_menu
from BankApp_class import Customer,Employee

print("BankApp'i Kullandığınız İçin Teşekkürler. Hoş Geldiniz :)\n")
customers = list()
employee = Employee()

while(True):
    choice = main_menu()

    if choice == 1:
            while(True):
                try:
                    name = input("İsminizi Giriniz: ")
                    ID = int(input("ID'nizi Giriniz: "))
                    customers.append(Customer(name, ID, 0))
                    print("\nKayıt İşlemi Başarıyla Tamamlanmıştır. Ana Menüye Yönlendiriliyorsunuz...\n")
                    break

                except (ValueError,TypeError) as e:
                    print(f"\nBir Hata Oluştu, Nesne Oluşturulamadı: {e}")
                    print("Tekrar Yönlendiriliyorsunuz\n")


    elif choice == 2:
        while(True):
            try:
                name = input("İsminizi Giriniz: ")
                ID = int(input("ID'nizi Giriniz: "))

                bulundu = any(customers[i].name == name and customers[i].ID == ID for i in range(len(customers)))

                if bulundu:
                    index = next(i for i, c in enumerate(customers) if c.name == name and c.ID == ID)
                    print("\nGiriş Başarılı. Müşteri Menüsüne Yönlendiriliyorsunuz...\n")
                    break
                else:
                    print("Verdiğiniz Bilgiler İle Kayıtlı Kullanıcı Bulunamadı Tekrar Deneyiniz.\n")

            except (ValueError,TypeError) as e:
                print(f"\nBir Hata Oluştu, Giriş Yapılamadı: {e}")
                print("Tekrar Yönlendiriliyorsunuz\n")

        while(True):
            choice2 = customers[index].show_menu()

            if choice2 == 1:
                try:
                    value = int(input("Lütfen Para Yatırmak İstediğiniz Miktarı Giriniz: "))
                    customers[index].para_yatir(value)
                except (ValueError, TypeError) as e:
                    print(f"\nBir Hata Oluştu, Para Yatırılmadı: {e}")

                print("\nİşleminiz Tamamlanmıştır. Müşteri Menüsüne Yönlendiriliyorsunuz...\n")

            elif choice2 == 2:
                try:
                    value = int(input("Lütfen Para Çekmek İstediğiniz Miktarı Giriniz: "))
                    customers[index].para_cek(value)
                except (ValueError, TypeError) as e:
                    print(f"\nBir Hata Oluştu, Para Çekilemedi: {e}")

                print("\nİşleminiz Tamamlanmıştır. Müşteri Menüsüne Yönlendiriliyorsunuz...\n")

            elif choice2 == 3:
                try:
                    value = int(input("Lütfen Para Gönderme İstediğiniz Miktarı Giriniz: "))
                    ID = int(input("Para Göndermek İstediğiniz Kişinin ID'sini Giriniz: "))

                    other = next(item for item in customers if item.ID == ID)

                    customers[index].para_gonder(value,other)
                except (ValueError, TypeError) as e:
                    print(f"\nBir Hata Oluştu, Para Gönderilemdi: {e}")
                except StopIteration as e:
                    print(f"\nGirilen ID'de Bir Kişi Bulunamadı: {e}")

                print("\nİşleminiz Tamamlanmıştır. Müşteri Menüsüne Yönlendiriliyorsunuz...\n")

            elif choice2 == 4:
                print("Çıkış Yapılıyor. Ana Menüye Yönlendiriliyorsunuz...")
                break
    elif choice == 3:
        while(True):
            try:
                name = input("İsminizi Giriniz: ")
                ID = int(input("ID'nizi Giriniz: "))

                if employee.name == name and employee.ID == ID:
                    print("\nGiriş Başarılı Çalışan Menüsüne Yönlendiriliyorsunuz...\n")
                    break
                else:
                    print("\nKullanıcı Bilgileri Hatalı. Tekrar Deneyiniz.\n")

            except (ValueError,TypeError) as e:
                print(f"\nBir Hata Oluştu, Giriş Yapılamadı: {e}")
                print("Tekrar Yönlendiriliyorsunuz\n")

        while(True):
            choice2 = employee.show_menu()

            if choice2 == 1:
                try:
                    ID = int(input("Lütfen Bilgilerini Öğrenmek İstediğiniz Kişinin ID'sini Giriniz: "))
                    employee.show_info(ID,customers)
                    print("\nİşleminiz Tamamlanmıştır. Çalışan Menüsüne Yönlendiriliyorsunuz...\n")
                except (ValueError,TypeError) as e:
                    print(f"\nBir Hata Oluştu: {e}")
                    print("Çalışan Menüsüne Yönlendiriliyorsunuz...\n")
            if choice2 == 2:
                print("Çıkış Yapılıyor. Ana Menüye Yönlendiriliyorsunuz...")
                break
    elif choice == 4:
        print("Ziyaret Ettiğiniz İçin Teşşekürler. Yine Bekleriz :)")
        break







