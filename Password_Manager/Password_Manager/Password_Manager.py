import random

karakterler=("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

uzunluk=int(input("şifreniz kaç karakter olsun?:"))

parola=("")

for i in range(uzunluk):
    karakter=random.choice(karakterler)
    parola+=karakter

print("parolanız:",parola)
