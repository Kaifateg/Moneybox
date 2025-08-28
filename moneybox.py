import os
import json
import datetime
from commands import (new_goal, list_goal, del_goal, change_goals,
                      target_list, change_category, all_progress)
from goal import Goal
from add_goal_parameters import (goal_category, goal_datetime_now,
                                 goal_total_sum, goal_target_name,
                                 category_list)
from alerts import progress_alert, status_alert


def start_project():
    print("***Программа Копилка запущена***")
    commands = ["новая цель", "список целей", "удалить цель",
                "информация о цели", "изменение категорий",
                "общий прогресс", "выход"]

    file_path = "file.json"

    if os.path.isfile(file_path):
        with open("file.json", "r") as file:
            obj = json.load(file)
            for value in obj:
                if isinstance(value, dict):
                    goal = Goal(value["target_name"], value["total_sum"],
                                value["category"], value["datetime_now"],
                                value["status"], value["balance"])
                    goal.increase_balance = value["dates_increase_balance"].copy()
                    goal.decrease_balance = value["dates_decrease_balance"].copy()
                    goal.status_progress()
                    progress_alert(goal)
                    status_alert(goal)
                    target_list.append(goal.json())
                else:
                    if len(value) == 1:
                        category_list.append(*value)
                    else:
                        for add_value in value:
                            category_list.append(add_value)

    if len(category_list) == 0:
        print("Отсутствуют категории для создания целей.\n")
        while True:
            new_category = input("Добавьте название категории для "
                                 "организации целей(наберите Выход для "
                                 "окончания операции): ")
            if new_category.lower() != "выход":
                category_list.append(new_category.capitalize())
            print(f"Список категорий: {category_list}\n")
            if len(category_list) == 0:
                print("Необходимо добавить категорию.\n")
            elif new_category.lower() == "выход":
                print("Операция окончена.\n")
                break

    if len(target_list) == 0:
        print("Создайте свою первую цель.")
        goal = Goal(goal_target_name(), goal_total_sum(), goal_category(
        ), goal_datetime_now())
        target_list.append(goal.json())
        print("Цель создана\n")
        print(goal)

    while True:
        start_command = str(input("Введите одну из команд:\nНовая "
                                  "цель, Список целей\nУдалить цель, "
                                  "Информация о цели\nИзменение "
                                  "категорий\nОбщий прогресс, Выход\n: "
                                  "")).lower()
        if start_command not in commands:
            print("Ошибка. Команда отсутствует в списке.\n")
        else:
            if start_command == "выход":
                print("***Работа программы завершена***")
                break
            elif start_command == "новая цель":
                new_goal()
            elif start_command == "список целей":
                list_goal()
            elif start_command == "удалить цель":
                del_goal()
            elif start_command == "информация о цели":
                change_goals()
            elif start_command == "изменение категорий":
                change_category()
            elif start_command == "общий прогресс":
                all_progress()

    target_list.append(category_list)

    with open("file.json", "w") as file:
        json.dump(target_list, file, indent=1)
        print("***Создан файл file.json для хранения данных***")


start_project()

