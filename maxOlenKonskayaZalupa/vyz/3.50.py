h = int(input("Введите часы (1-12): "))
m = int(input("Введите минуты (0-59): "))
def diff_angle(h_, m_):
    hour_angle = (30 * (h_ % 12) + 0.5 * m_) % 360
    min_angle = (6 * m_) % 360
    diff = abs(hour_angle - min_angle)
    return min(diff, 360 - diff)
min_to_coincide = None
min_to_perpendicular = None
for t in range(1, 12 * 60 + 1):  # полный цикл в минутах
    mm = (m + t) % 60
    hh = (h + (m + t) // 60)
    hh = hh if hh <= 12 else hh - 12
    d = diff_angle(hh, mm)
    if min_to_coincide is None and (d < 1e-5):
        min_to_coincide = t
    if min_to_perpendicular is None and (abs(d - 90) < 1e-3 or abs(d - 270) < 1e-3):
        min_to_perpendicular = t
    if min_to_coincide is not None and min_to_perpendicular is not None:
        break
print(f"Минут до совпадения стрелок: {min_to_coincide}")
print(f"Минут до перпендикулярности: {min_to_perpendicular}")
