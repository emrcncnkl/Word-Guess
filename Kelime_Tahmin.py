import random
print('''
 ___  __    _______   ___       ___  _____ ______   _______       
|\  \|\  \ |\  ___ \ |\  \     |\  \|\   _ \  _   \|\  ___ \      
\ \  \/  /|\ \   __/|\ \  \    \ \  \ \  \\\__\ \  \ \   __/|     
 \ \   ___  \ \  \_|/_\ \  \    \ \  \ \  \\|__| \  \ \  \_|/__   
  \ \  \\ \  \ \  \_|\ \ \  \____\ \  \ \  \    \ \  \ \  \_|\ \  
   \ \__\\ \__\ \_______\ \_______\ \__\ \__\    \ \__\ \_______\ 
    \|__| \|__|\|_______|\|_______|\|__|\|__|     \|__|\|_______| 
                                                                  
                                                                  
                                                                  
 _________  ________  ___  ___  _____ ______   ___  ________      
|\___   ___\\   __  \|\  \|\  \|\   _ \  _   \|\  \|\   ___  \    
\|___ \  \_\ \  \|\  \ \  \\\  \ \  \\\__\ \  \ \  \ \  \\ \  \   
     \ \  \ \ \   __  \ \   __  \ \  \\|__| \  \ \  \ \  \\ \  \  
      \ \  \ \ \  \ \  \ \  \ \  \ \  \    \ \  \ \  \ \  \\ \  \ 
       \ \__\ \ \__\ \__\ \__\ \__\ \__\    \ \__\ \__\ \__\\ \__\
        \|__|  \|__|\|__|\|__|\|__|\|__|     \|__|\|__|\|__| \|__|
                                                                  
                                                                  
                                                                  
''')
kelimeler = ["elma", "bilgisayar", "kitap", "sandalye", "masa", "gözlük", "telefon", "kalem", "defter", "saat", "ayakkabı", "çanta", "şapka", "ceket", "pantolon", "gömlek", "kazak", "aydınlatma", "televizyon", "radyo", "mikrofon", "hoparlör", "kulaklık", "klavye", "fare", "yazıcı", "tarayıcı", "kamera", "kamera", "çamaşır makinesi", "buzdolabı", "fırın", "mikrodalga", "bulaşık makinesi", "davlumbaz", "blender", "tost makinesi", "kettle", "saç kurutma makinesi", "jilet", "diş fırçası", "tarak", "ayna", "şemsiye", "çorap", "ayakkabı", "bot", "sandalet", "terlik", "sneaker", "cüzdan", "anahtar", "cep telefonu", "tablet"]

oyuna_devam = 'e'
while oyuna_devam == 'e':
    secilen_kelime = random.choice(kelimeler)
    tahminler = []
    yanlis_tahmin_sayisi = 0
    limit = 5

    while yanlis_tahmin_sayisi < limit:
        tahmin = input("Tahmin ettiğiniz harfi girin: ")
        tahmin = tahmin.lower()

        if tahmin in secilen_kelime:
            print("Doğru Tahmin!")
            tahminler.append(tahmin)
        else:
            print("Yanlış Tahmin...")
            yanlis_tahmin_sayisi += 1

        for harf in secilen_kelime:
            if harf not in tahminler:
                print("Oyun devam ediyor.")
                break
        else:
            print("Doğru Tahmin! Bildiniz.")
            break

    if yanlis_tahmin_sayisi >= limit:
        print("Üzgünüm, oyunu kaybettiniz.")

    oyuna_devam = input("Başka bir oyun oynamak ister misiniz? (e/h)")
    oyuna_devam = oyuna_devam.lower()
