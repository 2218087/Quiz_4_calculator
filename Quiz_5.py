var = int(input("몇단까지 출력할까요?"))

print("구구단을 출력합니다")
def number(var):
    for x in range(1, var+1):
        print("-----[" + str(x) + "단]-----")
        for y in range(1, 10):
           print(x, "x", y, "=", x*y)

number(var)
