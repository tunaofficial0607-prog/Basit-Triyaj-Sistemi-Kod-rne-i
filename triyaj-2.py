def triyajskoru():
    skor = 0
    kanama = input("Kanama var mı? (evet/hayır): ").lower()
    nabiz_durum = input("Nabız durumu (düşük/normal/yüksek/ciddi): ").lower()
    nabiz = int(input("Nabzı kaç? (bpm): "))
    yas = int(input("Yaş: "))
    sicaklik = float(input("Sıcaklık: "))
    solunum = int(input("Solunum: "))
    spo2 = int(input("SpO2: "))
    ayiklik = input("Ayık mı? (evet/hayır): ").lower()


    # Kanama değerlendirmesi
    if kanama == "evet":
        skor += 3

    # Nabız durumu değerlendirmesi
    if nabiz_durum == "düşük" or nabiz_durum == "yüksek":
        skor += 2
    elif nabiz_durum == "ciddi":
        skor += 3

    # Nabız değerlendirmesi
    if nabiz < 40 or nabiz > 130:
        skor += 3
    elif 40 <= nabiz <= 50 or 110 <= nabiz <= 130:
        skor += 2
    elif 51 <= nabiz <= 60 or 101 <= nabiz <= 110:
        skor += 1

    # Yaş değerlendirmesi
    if yas < 1:
        skor += 3
    elif 1 <= yas < 5:
        skor += 2
    elif 5 <= yas < 12:
        skor += 1

    # Sıcaklık değerlendirmesi
    if sicaklik < 35 or sicaklik > 39:
        skor += 3
    elif 35 <= sicaklik < 36 or 38 < sicaklik <= 39:
        skor += 2
    elif 36 <= sicaklik <= 38:
        skor += 1

    # Solunum değerlendirmesi
    if solunum < 10 or solunum > 30:
        skor += 3
    elif (10 <= solunum < 12) or (25 < solunum <= 30):
        skor += 2
    elif (12 <= solunum < 15) or (20 < solunum <= 25):
        skor += 1


    # SpO2 değerlendirmesi
    if spo2 < 90:
        skor += 3

    # Ayıklık değerlendirmesi
    if ayiklik == "hayır":
        skor += 3
    if skor >= 15:
        print("Sırada öncelikli acil müdahale gerektirir.")
    elif skor >= 10:
        print("Sırada kısmi öncelikli acil müdahale gerektirir.")
    elif skor >= 5:
        print("Sırada öncelikli acil müdahale gerektirmez.")
    else:
        print("Düşük risk.")
    print("Toplam skor:",skor)
triyajskoru()