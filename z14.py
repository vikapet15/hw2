N = cnt_kn = int(input())
cnt_sik = cnt_gal = 0

if N // 29 != 0:
    cnt_sik = N // 29
    cnt_kn %= 29
    if cnt_sik // 17 != 0:
        cnt_gal = cnt_sik // 17
        cnt_sik %= 17

if cnt_gal > 0:
    print(f"{cnt_gal} галлеонов")
if cnt_sik > 0:
    print(f"{cnt_sik} сиклей")
if cnt_kn > 0:
    print(f"{cnt_kn} кнатов")