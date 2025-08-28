import datetime
from goal import Goal
from add_goal_parameters import (goal_category, goal_datetime_now,
                                 goal_total_sum, goal_target_name,
                                 category_list)


target_list = []


def new_goal():
    goal = Goal(goal_target_name(), goal_total_sum(),
                goal_category(), goal_datetime_now())
    target_list.append(goal.json())
    print("Цель создана\n")
    print(goal)


def list_goal():
    for goal_dict in target_list:
        print((f"Название цели: {goal_dict['target_name']}\n"
               f"Итоговая сумма: {goal_dict['total_sum']}\n"
               f"Текущий баланс: {goal_dict['balance']}\n"
               f"Категория: {goal_dict['category']}\n"
               f"Статус цели: {goal_dict['status']}\n"
               f"Время создания цели:"
               f" {goal_dict['datetime_now']}\n"))


def del_goal():
    while True:
        if len(target_list) == 0:
            print("Цели отсутствуют.\n")
            break
        name_list = []
        for goals in target_list:
            name_list.append(goals["target_name"])
        print("***Названия целей***")
        print(*name_list, sep="\n")
        delete_goal = str(input("Для удаления введите название "
                                "цели из списка (или 'выход' для "
                                "отмены операции): ")).capitalize()
        if delete_goal == "Выход":
            print("Операция прервана.\n")
            break
        elif delete_goal not in name_list:
            print("Введённое название отсутствует в списке.\n")
        else:
            for goals in target_list:
                if goals["target_name"] == delete_goal:
                    target_list.remove(goals)
                    print(f"Цель {delete_goal} успешно удалена.\n")


def change_goals():
    if len(target_list) == 0:
        print("Цели отсутствуют.\n")
    else:
        while True:
            if len(target_list) == 0:
                print("Цели отсутствуют.\n")
                break
            name_list = []
            for goals in target_list:
                name_list.append(goals["target_name"])
            print("***Названия целей***")
            print(*name_list, sep="\n")
            change_goal = str(input("Для получения информации и внесения "
                                    "изменений введите название "
                                    "цели из списка (или 'выход' для "
                                    "отмены операции): ")).capitalize()
            if change_goal == "Выход":
                print("Операция прервана.\n")
                break
            elif change_goal not in name_list:
                print("Введённое название отсутствует в списке.\n")
            else:
                for index, goals in enumerate(target_list):
                    if goals["target_name"] == change_goal:
                        goal = Goal(goals["target_name"], goals["total_sum"],
                                    goals["category"], goals["datetime_now"],
                                    goals["status"], goals["balance"])
                        goal.increase_balance = goals["dates_increase_balance"].copy()
                        goal.decrease_balance = goals["dates_decrease_balance"].copy()
                        print(goal)
                        change_parameters(goal)
                        target_list[index] = goal.json()


def change_parameters(goal):
    goal_commands = ["изменить название цели", "изменить итоговую сумму",
                     "изменить категорию", "изменить время создания цели",
                     "увеличить баланс", "уменьшить баланс",
                     "история пополнений", "история снятий",
                     "изменить историю пополнений", "изменить историю снятий",
                     "узнать текущий прогресс", "общая информация",
                     "узнать прогнозную дату достижения цели", "выход"]
    while True:
        change_choice = str(input("Что вы хотите сделать? "
                                  "Введите одну из команд:\n"
                                  "Общая информация\n"
                                  "Изменить название цели, Изменить итоговую "
                                  "сумму\n"
                                  "Изменить категорию, Изменить время "
                                  "создания цели\n"
                                  "Увеличить баланс, Уменьшить баланс\n"
                                  "История пополнений, История снятий\n"
                                  "Изменить историю пополнений, "
                                  "Изменить историю снятий\n"
                                  "Узнать текущий прогресс, Узнать "
                                  "прогнозную дату достижения цели\n"
                                  "Выход\n: ")).lower()
        if change_choice not in goal_commands:
            print("Ошибка. Команда отсутствует в списке.\n")
        else:
            if change_choice == "выход":
                break
            elif change_choice == "изменить название цели":
                goal.set_target_name(input("Введите новое название цели: "))
                print(f"Внесено новое название: {goal.get_target_name()}\n")
            elif change_choice == "изменить итоговую сумму":
                goal.set_total_sum(goal_total_sum())
                print(f"Новая итоговая сумма: {goal.get_total_sum()}\n")
            elif change_choice == "изменить категорию":
                print(f"Список категорий: {category_list}")
                while True:
                    category = str(input("Введите новую категорию: "
                                         "")).capitalize()
                    if category not in category_list:
                        print("Ошибка. Категория должна быть выбрана из "
                              "списка.\n")
                    else:
                        goal.set_category(category)
                        break
                goal.set_category(input("Введите новую категорию: "))
                print(f"Новая категория: {goal.get_category()}\n")
            elif change_choice == "изменить время создания цели":
                while True:
                    try:
                        goal.set_datetime_now(datetime.datetime.strptime(
                            input("Введите дату в формате "
                                  "дд.мм.гггг: "), "%d.%m.%Y"))
                    except Exception:
                        print("Ошибка. Дата должна быть в формате "
                              "дд.мм.гггг (пример:10.01.2020).\n")
                    else:
                        if len(goal.increase_balance) > 0:
                            last_date = datetime.datetime.strftime(list(
                goal.increase_balance.values())[-1][1], "%d.%m.%Y")
                            for values in goal.increase_balance.values():
                                if (datetime.datetime.strptime(values[1],
                                                               '%d.%m.%Y') > last_date):
                                    last_date = datetime.datetime.strptime(values[1],
                                                               '%d.%m.%Y')
                            if last_date < goal.get_datetime_now():
                                print("Дата создания не может быть больше "
                                      "даты последнего пополнения.\n")
                            else:
                                break
                print(f"Новое время создания цели: "
                      f"{datetime.datetime.strftime(goal.get_datetime_now(), '%d.%m.%Y')}\n")
            elif change_choice == "увеличить баланс":
                goal.increase_balance_func()
                goal.status_progress()
            elif change_choice == "уменьшить баланс":
                goal.decrease_balance_func()
                goal.status_progress()
            elif change_choice == "история пополнений":
                goal.print_increase_balance()
            elif change_choice == "история снятий":
                goal.print_decrease_balance()
            elif change_choice == "изменить историю пополнений":
                goal.print_increase_balance()
                goal.del_increase_balance()
                goal.status_progress()
            elif change_choice == "изменить историю снятий":
                goal.print_decrease_balance()
                goal.del_decrease_balance()
                goal.status_progress()
            elif change_choice == "узнать текущий прогресс":
                print(f"Текущий прогресс цели составляет {goal.progress()}%\n")
            elif change_choice == "узнать прогнозную дату достижения цели":
                print(goal.future_date())
            elif change_choice == "общая информация":
                print(goal)


def change_category():
    category_commands = ["добавить категорию", "изменить категорию",
                         "удалить категорию", "выход"]
    while True:
        category_choice = str(input("Что вы хотите сделать? "
                                    "Введите одну из команд:\n"
                                    "Добавить категорию,"
                                    "Изменить категорию\n"
                                    "Удалить категорию, Выход\n:")).lower()
        if category_choice not in category_commands:
            print("Ошибка. Команда отсутствует в списке.\n")
        else:
            if category_choice == "выход":
                print("Операция остановлена\n")
                break
            if category_choice == "добавить категорию":
                while True:
                    new_category = str(input("Введите название новой "
                                             "категории: ")).capitalize()
                    if new_category in category_list:
                        print("Ошибка. Такая категория уже существует.\n")
                    else:
                        category_list.append(new_category)
                        print(f"Категория {new_category} добавлена\n")
                        break
            if category_choice == "изменить категорию":
                check = True
                print(f"Спикок категорий {category_list}\n")
                while check:
                    category_name = str(input("Введите название категории "
                                              "из списка для изменения: "
                                              "")).capitalize()
                    if category_name not in category_list:
                        print("Ошибка. Категория должна быть из списка.\n")
                    else:
                        while check:
                            category_change_name = str(input("Введите название "
                                                             "новой "
                                                             "категории: "
                                                             "")).capitalize()
                            if category_change_name in category_list:
                                print("Ошибка. Такая категория уже существует.\n")
                            else:
                                for index, value in enumerate(category_list):
                                    if value == category_name:
                                        category_list[index] = category_change_name
                                for goals in target_list:
                                    if goals["category"] == category_name:
                                        goals["category"] = category_change_name
                                check = False
            if category_choice == "удалить категорию":
                print(f"Спикок категорий {category_list}\n")
                while True:
                    del_category = str(input("Введите название категории из "
                                             "списка для удаления: "
                                             "")).capitalize()
                    for value in target_list:
                        if value["category"] == del_category:
                            print("Невозможно удалить категорию, "
                                  "использующуюся в текущих целях\n")
                    if del_category not in category_list:
                        print("Ошибка. Категория должна быть из списка.\n")

                    else:
                        category_list.remove(del_category)
                        print(f"Категория {del_category} удалена.\n")
                        break


def all_progress():
    if len(target_list) == 0:
        print("Цели отсутствуют.\n")
    else:
        all_total = 0
        all_balance = 0
        for total in target_list:
            all_total += float(total["total_sum"])
            all_balance += float(total["balance"])
        result = (all_balance / all_total) * 100
        print(f"Общий прогресс по всем целям составляет {int(result)}%\n")
