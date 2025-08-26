def main_menu():
    print("======MAİN MENÜ======")
    print("1 -> Yeni Müşteri Kayıt")
    print("2 -> Müşteri Girişi")
    print("3 -> Çalışan Girişi")
    print("4 -> Çıkış\n")

    while(True):
        try:
            choice = int(input("Lütfen Seçiminizi Yapınız: "))

            if choice == 1:
                print("Yeni Müşteri Kayıt Seçildi. Yöneldiriliyorsunuz...\n")
                return choice
            elif choice == 2:
                print("Müşteri Girişi Seçildi. Yöneldiriliyorsunuz...\n")
                return choice
            elif choice == 3:
                print("Çalışan Girişi Seçildi. Yöneldiriliyorsunuz...\n")
                return choice
            elif choice == 4:
                print("Çıkış Seçildi. Yönlendiriliyorsunuz...\n")
                return choice
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyiniz.\n")

        except (ValueError,TypeError) as e:
            print(f"Tekar Deneyiniz. Hata Oluştu {e}\n")
