def progress_alert(goal):
    if 70 <= goal.progress() <= 99:
        print(f"Цель {goal.get_target_name()} почти выполнена.\n "
              f"Ваш прогресс {goal.progress()}%\n")


def status_alert(goal):
    if goal.status == "выполнена":
        print(f"Цель {goal.get_target_name()} достигнута.\n")