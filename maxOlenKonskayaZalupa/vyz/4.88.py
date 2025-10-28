g_b, m_b = map(int, input("Дата рождения: год, месяц: ").split())
g_t, m_t = map(int, input("Текущая дата: год, месяц: ").split())

full_years = g_t - g_b - (1 if m_t < m_b else 0)
full_months = abs(m_t - m_b) if m_t >= m_b else (12 - m_b + m_t)
print(f"{full_years} лет, {full_months} месяцев")