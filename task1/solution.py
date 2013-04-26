signs_dates = [19, 18, 20, 20, 20, 20, 21, 22, 22, 22, 21, 21]
signs_names = ["Козирог", "Водолей", "Риби", "Овен", "Телец", "Близнаци",
               "Рак", "Лъв", "Дева", "Везни", "Скорпион", "Стрелец"]


def what_is_my_sign(day=1, month=1):
    if month == 12:
        month = 0
    if day > signs_dates[month-1]:
        month += 1
    return signs_names[month-1]
