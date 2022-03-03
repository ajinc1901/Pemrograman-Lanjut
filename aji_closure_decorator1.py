def luas_segitiga(func):
    def inner(alas, tinggi):
        if alas < 5:
            print("\n* Karena nilai alas adalah " + str(alas) + " , maka akan diubah menjadi 5")
            alas = 5
        if tinggi < 5:
            print("* Karena nilai tinggi adalah " + str(tinggi) + " , maka akan diubah menjadi 5")
            tinggi = 5
        return func(alas, tinggi)
    return inner

@luas_segitiga
def div(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print("\nLuas Segitiga Adalah: ", luas)

print("****************** LUAS SEGITIGA ******************")
print("\n! Jika nilai alas < 5 maka akan diubah menjadi 5")
print("! Jika nilai tinggi < 5 maka akan diubah menjadi 5")
print(" ")   

alas = int(input("Masukkan Alas Segitiga : "))
tinggi = int(input("Masukkan Tinggi Segitiga : "))

div(alas, tinggi)