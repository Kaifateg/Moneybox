import datetime


category_list = []


def goal_target_name():
    target_name = str(input("Введите название цели: ")).capitalize()
    return target_name


def goal_total_sum():
    while True:
        try:
            total_sum = float(input("Введите сумму цели: "))
        except Exception:
            print("Ошибка. Сумма должна быть положительным числом.")
        else:
            if total_sum == 0:
                print("Ошибка. Сумма не должна равняться 0.")
            elif total_sum < 0:
                print("Ошибка. Сумма не должна быть отрицательной.")
            else:
                break
    return total_sum


def goal_category():
    print(f"Список категорий: {category_list}")
    while True:
        category = str(input("Введите название категории из списка: "
                             "")).capitalize()
        if category not in category_list:
            print("Ошибка. Категория должна быть выбрана из списка.\n")
        else:
            break
    return category


def goal_datetime_now():
    while True:
        try:
            date_now = datetime.datetime.strptime(
                input("Введите дату в формате "
                      "дд.мм.гггг: "), "%d.%m.%Y")
        except Exception:
            print("Ошибка. Дата должна быть в формате "
                  "дд.мм.гггг (пример:10.01.2020).")
        else:
            str_date_now = datetime.datetime.strftime(date_now, "%d.%m.%Y")
            break
    return str_date_now
