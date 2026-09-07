from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def main():
    print("1. Топ-5 студентів за середнім балом:")
    print(select_1())
    print()

    print("2. Студент із найвищим середнім балом з предмета id=1:")
    print(select_2(1))
    print()

    print("3. Середній бал у групах з предмета id=1:")
    print(select_3(1))
    print()

    print("4. Середній бал на потоці:")
    print(select_4())
    print()

    print("5. Курси викладача id=1:")
    print(select_5(1))
    print()

    print("6. Студенти групи id=1:")
    print(select_6(1))
    print()

    print("7. Оцінки студентів групи id=1 з предмета id=1:")
    print(select_7(1, 1))
    print()

    print("8. Середній бал, який ставить викладач id=1:")
    print(select_8(1))
    print()

    print("9. Курси студента id=1:")
    print(select_9(1))
    print()

    print("10. Курси, які студенту id=1 читає викладач id=1:")
    print(select_10(1, 1))
    print()


if __name__ == "__main__":
    main()