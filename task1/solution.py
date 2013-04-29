SIGNS = {
    range(101, 120): "Козирог",
    range(120, 219): "Водолей",
    range(219, 321): "Риби",
    range(321, 421): "Овен",
    range(421, 521): "Телец",
    range(521, 621): "Близнаци",
    range(631, 722): "Рак",
    range(722, 823): "Лъв",
    range(823, 923): "Дева",
    range(923, 1023): "Везни",
    range(1023, 1122): "Скорпион",
    range(1122, 1222): "Стрелец",
    range(1222, 1232): "Козирог"}


def what_is_my_sign(day, month):
    date = month * 100 + day
    for range_sign in SIGNS.keys():
        if date in range_sign:
            return SIGNS[range_sign]
