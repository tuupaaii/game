from browser import document

def cek(ev):
    total = 0

    for i in range(1, 5):
        nilai = int(document[f"q{i}"].value)
        total += nilai

    if total >= 10:
        hasil = "Gizi harian kamu sudah sangat baik! Pertahankan yaa!😼"
    elif total >= 7:
        hasil = "Gizi kamu sudah cukup baik, tapi bisa ditingkatin lagi yaa 😸~"
    elif total >= 5:
        hasil = "Waduh, coba perhatiin kebiasaan makan kamu ya! Karena masih kurang sehat nih..😿"
    else:
        hasil = "Gizi harian kamu masih kurang banget.. yuk tingkatin kualitas makan kamu!😺"

    document["hasil"].text = hasil

document["submit"].bind("click", cek)
