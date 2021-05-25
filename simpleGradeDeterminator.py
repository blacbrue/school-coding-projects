gredSains = str(input("Masukkan gred bagi Subjek Sains: "))
gredMate = str(input("Masukkan gred bagi Subjek Matematik: "))

if gredSains == "A":
    if gredMate == 'A':
        print("Tahniah! Anda layak ke Alitan Sains")
    else:
        print('Maaf! Anda tidal layak ke Aliran Sains')
else:
    print('Maaf! Anda tidal layak ke Aliran Sains')