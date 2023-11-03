meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "L": "İngilizcede 'Loser/Ezik' kelimesinin kısaltması",
    "BRB": "İngilizcede 'Be Right Back/Hemen geliyorum' kelimesinin kısaltması",
    "YOLO": "İngilizcede 'You Only Live Once/Sadece bir kere yaşarsın' kelimesinin kısaltması",
    "DM": "İngilicede 'Direct Message/Direkt Mesaj' kelimesinin kısaltması",
}

word = input("Öğrenmek istediğiniz bir kelimeyi giriniz: ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Girdiğiniz kelime sözlükte bulunamadı.")
