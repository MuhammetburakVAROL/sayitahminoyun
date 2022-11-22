def tahminoyunu():
    import random
    name = str(input("Hoşgeldiniz, oyuna başlamak için isminizi giriniz : "))
    print(f"Hoşgeldin, {name} ")
    print(50 * '*')
    number = random.randint(3,20)
    counter = 0
    while True:
        counter +=1
        a = int(input("1. sayıyı giriniz : "))
        b = int(input("2. sayıyı giriniz : "))
        c = int(input("3. sayıyı giriniz : "))
        print(50*'*')
        toplam = a + b + c
        if number < toplam:
            print("Daha küçük sayılar deneyiniz.")
            print(50 * '*')
            continue
        elif number > toplam:
            print('Daha büyük sayılar deneyiniz.')
            print(50 * '*')
            continue
        elif toplam > 20:
            print('Toplamları 20den küçük sayılar yazınız.')
            print(50 * '*')
            continue
        elif toplam == number:
            print(f'Tebrikler oyunu kazandınız...\nBilgisayarın seçtiği sayı : {number}\nSizin seçtiğiniz sayıların toplamı : {toplam}\nTahmin sayınız : {counter}')
            print(50 * '*')
            break
tahminoyunu()