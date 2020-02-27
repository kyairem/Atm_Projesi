import time as zaman
import os
print("******************hoşgeldiniz***************")
zaman.sleep(2)
kayit=[]
bakiye=0
yatirilacak_para=0
cekilecek_para=0
while 1:
    print("1:para yatırma\n2:para cekme\n3:bakiye sorgulama\n4:geçmiş işlemler\nq:çıkış")
    zaman.sleep(1)
    islem=input("islemi giriniz:")
    kayit.append((islem))
    if (islem =='q'):
        break
    elif (islem != '1' and islem !='2' and islem !='3' and islem !='4'):
        print("******************yanlış tuşlama")
        zaman.sleep(1)
    elif (islem == '1'):
        yatirilacak_para=int(input("yatırlacak para:"))
        zaman.sleep(1)
        bakiye = bakiye + yatirilacak_para
    elif (islem == '2'):
        cekilecek_para=int(input("cekilecek para:"))
        zaman.sleep(1)
        if (cekilecek_para>bakiye):
            print("***************islem olanaksızdır")
            zaman.sleep(1)
            continue
        bakiye = bakiye - cekilecek_para
    elif (islem =='3'):
        print("Hesapınızda ki güncel bakiye:{}".format(bakiye))
        zaman.sleep(1)
    elif (islem == '4'):
        print("yapılan islem kayıtları:\n************************")
        zaman.sleep(2)
        for i in kayit:
            if (i=='1'):
                print("para yatırma")
            elif (i =='2'):
                print("para cekme")
            elif (i=='3'):
                print("bakiye sorgulama")
            elif (i == '4'):
                print("islem sorgulama") 
        print("***************************")






