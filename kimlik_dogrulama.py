def encodeTc(tc):
    sum = 0
    for i in tc:
        sum += int(i)
    tc+= str(sum)[-1]
    return tc
def decodeTc(girilen_tc):
    if len(girilen_tc)!=11:
        print("Geçerli bi tc gir amk")
        return
    encodedtc=encodeTc(girilen_tc[0:10])
    return girilen_tc == encodedtc
def tclogin():
    a = input("Tc giriniz ")
    result = decodeTc(a)
    if result == None:
        quit()
    elif not result:
        print("Sahte tc")
    elif result:
        print("Giriş başarılı")
tclogin()