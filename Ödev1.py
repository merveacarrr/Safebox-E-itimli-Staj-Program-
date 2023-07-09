def giris():
    kullanici_adi = input("Kullanıcı adını giriniz:")
    sifre = input("Şifrenizi giriniz:")

    with open("kullanici_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            bilgiler = satir.strip().split(",")
            dosya_kullanici_adi = bilgiler[0]
            dosya_sifre = bilgiler[1]

            if kullanici_adi == dosya_kullanici_adi and sifre == dosya_sifre:
                print("Giriş yapıldı!")
                return
    print("Hatalı kullanıcı adı veya şifre girişi yapıldı!")

giris()