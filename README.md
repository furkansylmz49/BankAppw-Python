# 🏦 BankApp

BankApp, Python ile yazılmış basit bir **banka sistemi simülasyonu** uygulamasıdır.  
Kullanıcılar hesap oluşturabilir, para yatırabilir, para çekebilir ve bakiye sorgulayabilirler.  
Proje **OOP (Object-Oriented Programming)** mantığını pekiştirmek için geliştirilmiştir.

---

## 🚀 Özellikler
- Kullanıcı oluşturma
- Para yatırma
- Para çekme
- Bakiye sorgulama
- Modüler yapı:  
  - `main.py` → Uygulamanın giriş noktası  
  - `BankApp_class.py` → Sınıflar (classes)  
  - `BankApp_func.py` → Fonksiyonlar  

---

## 🛠️ Kurulum

1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/BankAppWithPython.git
   cd BankAppWithPython
   ```

2. Sanal ortam oluşturun ve etkinleştirin:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   ```

3. Gerekli paketleri yükleyin (eğer varsa):
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Çalıştırma

```bash
python main.py
```

Eğer `.app` olarak paketlenmiş versiyonunu kullanmak istiyorsanız:  
- `dist/` klasöründeki `BankApp.app` dosyasına çift tıklayabilirsiniz.  

---

## 💻 Teknolojiler
- Python 3.13
- PyInstaller (Mac için `.app` oluşturmak için kullanıldı)

---

## 📦 Derleme (.app Oluşturma)

```bash
pyinstaller --onefile --windowed --icon=icon.icns main.py
```

- Çıktı dosyası `dist/` klasöründe bulunur.
- İkon eklemek istemiyorsanız `--icon` parametresini kaldırabilirsiniz.

---

## 📌 Notlar
- Bu proje tamamen **öğrenme amaçlı** geliştirilmiştir.  
- Mac üzerinde test edilmiştir.  

---

## 📜 Lisans
Bu proje kişisel kullanım içindir.  
