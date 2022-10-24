chiều_cao = float(input("nhâp chiều cao (đơn vị là m): "))
cân_nặng = float(input ("nhập cân nặng (đơn vị kg): "))
if (cân_nặng / chiều_cao**2) < 16:
    print("gầy cấp độ III")
elif 16 <= cân_nặng / (chiều_cao**2) < 17:
    print("gầy cấp độ II")
elif 17 <= cân_nặng / (chiều_cao**2) < 18.5:
    print("gầy cấp độ I")
elif 18.5 <= cân_nặng / (chiều_cao**2) < 25:
    print("bình thường")
elif 25 <= cân_nặng / (chiều_cao**2) < 30:
    print("thừa cân")
elif 30 <= cân_nặng / (chiều_cao**2) < 35:
    print("béo phì câp độ I")
elif 35 <= cân_nặng / (chiều_cao**2) < 40:
    print("béo phì câp độ II")
elif 40 < cân_nặng / (chiều_cao**2):
    print("béo phì câp độ III")
