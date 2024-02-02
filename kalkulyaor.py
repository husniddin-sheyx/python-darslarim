def kalkulyator(raqam1, raqam2, amal):
    if amal == '+':
        return raqam1 + raqam2
    elif amal == '-':
        return raqam1 - raqam2
    elif amal == '*':
        return raqam1 * raqam2
    elif amal == '/':
        if raqam2 != 0:
            return raqam1 / raqam2
        else:
            return "No'lga bo'lish mumkin emas"
    else:
        return "Noto'g'ri amal"
raqam1 = float(input("Birinchi raqamni kiriting: "))
amal = input("Amalni tanlang (+, -, *, /): ")
raqam2 = float(input("Ikkinchi raqamni kiriting: "))
natija = kalkulyator(raqam1, raqam2, amal)
print(f"Natija: {natija}")
