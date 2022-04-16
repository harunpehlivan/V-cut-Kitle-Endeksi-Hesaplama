 
boy = float(input("Boyunuzu Giriniz '(m)': Örnek 1.73----:"))
kilo = float(input("Kilonuzu Giriniz '(kg)': Örnek: 78----:"))
 
endeks = kilo/(boy**2)
 
if endeks<18.5:
    print("Zayıfsınız")
elif endeks > 18.5 and endeks <=25 :
    print("Normalsiniz")
elif endeks > 25 and endeks <=30:
    print("Kilolusunuz")
elif endeks > 30:
    print("Dikkat! obezsiniz")