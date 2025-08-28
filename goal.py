import datetime
import math


class Goal:
    def __init__(self, target_name, total_sum, category, datetime_now,
                 status="в процессе", balance=0):
        self._target_name = target_name
        self._total_sum = total_sum
        self._category = category
        self.status = status
        self._datetime_now = datetime_now
        self.balance = balance
        self.increase_balance = {}
        self.decrease_balance = {}

    def __str__(self):
        return (f"Название цели: {self._target_name}\n"
                f"Итоговая сумма: {self._total_sum}\n"
                f"Текущий баланс: {self.balance}\n"
                f"Категория: {self._category}\n"
                f"Статус цели: {self.status}\n"
                f"Время создания цели: {self._datetime_now}\n")

    def set_total_sum(self, total_sum):
        self._total_sum = total_sum

    def set_target_name(self, target_name):
        self._target_name = target_name

    def set_category(self, category):
        self._category = category

    def set_datetime_now(self, datetime_now):
        self._datetime_now = datetime_now

    def get_category(self):
        return self._category

    def get_total_sum(self):
        return self._total_sum

    def get_target_name(self):
        return self._target_name

    def get_datetime_now(self):
        return self._datetime_now

    def print_increase_balance(self):
        if len(self.increase_balance) == 0:
            print("История пополнений отсутствует\n")
        else:
            increase_balance = {}
            for key, value in self.increase_balance.items():
                increase_balance[key] = value
            for outclass_key in increase_balance.keys():
                print(f"Номер пополнения: {outclass_key}\n"
                      f"Сумма пополнения: {increase_balance[outclass_key][0]}\n"
                      f"Дата пополнения: {increase_balance[outclass_key][1]}\n")

    def print_decrease_balance(self):
        if len(self.decrease_balance) == 0:
            print("История снятий отсутствует\n")
        else:
            decrease_balance = {}
            for key, value in self.decrease_balance.items():
                decrease_balance[key] = value
            for outclass_key in decrease_balance.keys():
                print(f"Номер снятия: {outclass_key}\n"
                      f"Сумма снятия: {decrease_balance[outclass_key][0]}\n"
                      f"Дата снятия: {decrease_balance[outclass_key][1]}\n")

    def increase_balance_func(self):
        check = True
        while check:
            try:
                numb = float(input("Введите сумму для увеличения баланса: "))
            except Exception:
                print("Ошибка. Сумма должна быть положительным числом.\n")
            else:
                if numb == 0:
                    print("Ошибка. Сумма не должна равняться 0.\n")
                elif numb < 0:
                    print("Ошибка. Сумма не должна быть отрицательной.\n")
                else:
                    while check:
                        try:
                            date_now = datetime.datetime.strptime(
                                input("Введите дату в формате "
                                      "дд.мм.гггг: "), "%d.%m.%Y")
                        except Exception:
                            print("Ошибка. Дата должна быть в формате "
                                  "дд.мм.гггг (пример:10.01.2020).\n")
                        else:
                            if date_now < datetime.datetime.strptime(
                                    Goal.get_datetime_now(self), "%d.%m.%Y"):
                                print("Ошибка. Дата не может быть раньше даты "
                                      "начала цели.\n")
                            else:
                                self.balance += numb
                                self.increase_balance[len(self.increase_balance)+1] = (
                                    numb, date_now.strftime("%d.%m.%Y"))
                                print("Баланс увеличен.\n")
                                check = False

    def decrease_balance_func(self):
        check = True
        while check:
            try:
                numb = float(input("Введите сумму для уменьшения баланса ("
                                 "пример: -100): "))
            except Exception:
                print("Ошибка. Сумма должна быть отрицательным числом.\n")
            else:
                if numb == 0:
                    print("Ошибка. Сумма не должна равняться 0.\n")
                elif numb > 0:
                    print("Ошибка. Сумма не должна быть положительной.\n")
                elif abs(numb) > self.balance:
                    print("Ошибка. Сумма не должна превышать текущий "
                          "баланс.\n")
                else:
                    while check:
                        try:
                            date_now = datetime.datetime.strptime(
                                input("Введите дату в формате "
                                      "дд.мм.гггг: "), "%d.%m.%Y")
                        except Exception:
                            print("Ошибка. Дата должна быть в формате "
                                  "дд.мм.гггг (пример:10.01.2020).\n")
                        else:
                            if date_now < datetime.datetime.strptime(
                                    Goal.get_datetime_now(self), "%d.%m.%Y"):
                                print("Ошибка. Дата не может быть раньше даты "
                                      "начала цели.\n")
                            else:
                                self.balance -= numb
                                self.decrease_balance[len(self.increase_balance)+1] = (
                                    numb, date_now.strftime("%d.%m.%Y"))
                                print("Баланс уменьшен.\n")
                                check = False

    def del_increase_balance(self):
        if len(self.increase_balance) == 0:
            print("Пополнения отсутствуют.\n")
        else:
            while True:
                try:
                    numb = int(input("Введите номер пополнения для удаления: "))
                except Exception:
                    print("Ошибка. Номер должен быть числом.\n")
                else:
                    if numb == 0:
                        print("Ошибка. Номер не должен равняться 0.\n")
                    elif numb < 0:
                        print("Ошибка. Номер не должна быть отрицательным.\n")
                    elif numb not in self.increase_balance.keys():
                        print("Ошибка. Номер отсутствует в списке "
                              "пополнений.\n")
                    elif Goal.get_total_sum(self) - list(
                            self.increase_balance[numb])[0] < 0:
                        print("Ошибка. Общая сумма накоплений не может быть "
                              "отрицательной\n")
                    else:
                        self.balance -= list(self.increase_balance[numb])[0]
                        self.increase_balance.pop(numb)
                        break

    def del_decrease_balance(self):
        if len(self.decrease_balance) == 0:
            print("Снятия отсутствуют.")
        else:
            while True:
                try:
                    numb = int(input("Введите номер снятия для удаления: "))
                except Exception:
                    print("Ошибка. Номер должен быть числом.\n")
                else:
                    if numb == 0:
                        print("Ошибка. Номер не должен равняться 0.\n")
                    elif numb < 0:
                        print("Ошибка. Номер не должна быть отрицательным.\n")
                    elif numb not in self.decrease_balance.keys():
                        print("Ошибка. Номер отсутствует в списке снятий.\n")
                    else:
                        self.balance += list(self.decrease_balance[numb])[0]
                        self.decrease_balance.pop(numb)
                        break

    def progress(self):
        result = (self.balance / self._total_sum * 100)
        return int(result)

    def status_progress(self):
        if int(self.balance) >= int(self._total_sum):
            self.status = "выполнена"
            return self.status

    def json(self):
        data = {}
        data["target_name"] = self._target_name
        data["total_sum"] = self._total_sum
        data["balance"] = self.balance
        data["category"] = self._category
        data["status"] = self.status
        data["datetime_now"] = self._datetime_now
        data["dates_increase_balance"] = self.increase_balance
        data["dates_decrease_balance"] = self.decrease_balance
        return data

    def future_date(self):
        if len(self.increase_balance) == 0:
            return f"Баланс не увеличивался\n"
        elif (datetime.datetime.strptime(
                Goal.get_datetime_now(self), "%d.%m.%Y") ==
              datetime.datetime.strptime(list(
                self.increase_balance.values())[-1][1], "%d.%m.%Y")):
            return f"С последнего пополнения не прошло достаточно времени\n"
        else:
            last_datetime = datetime.datetime.strptime(list(
                self.increase_balance.values())[-1][1], "%d.%m.%Y")
            if len(self.increase_balance) > 1:
                for value in self.increase_balance.values():
                    if (datetime.datetime.strptime(value[1], "%d.%m.%Y") >
                            last_datetime):
                        last_datetime = datetime.datetime.strptime(value[1],
                                                                   "%d.%m.%Y")
            first_datetime = datetime.datetime.strptime(
                Goal.get_datetime_now(self), "%d.%m.%Y")
            date_difference = (last_datetime - first_datetime).days
            future_days = (math.ceil(Goal.get_total_sum(self) / math.ceil(
                    self.balance / date_difference)) - (self.balance /
                                                        date_difference))
            future_datetime = (last_datetime + datetime.timedelta(
                days=future_days)).strftime("%d.%m.%Y")
            return f"Вы достигните цели приблизительно: {future_datetime}\n"
