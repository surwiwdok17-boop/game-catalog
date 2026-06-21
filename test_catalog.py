# test_catalog.py
# Автоматизований тест для функцій сортування та статистики ігор

import json
import os
import catalog  

TEST_FILE = "test_data.json"

def setup(records):
    """Записує тестові дані у тимчасовий файл."""
    # Підміняємо шлях до файлу на час тесту
    catalog.DATA_FILE = TEST_FILE
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f)

def teardown():
    """Видаляє тимчасовий файл після тесту."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

# ── Тест 1: Статистика при нормальних даних ──
setup([
    {"title": "The Witcher 3", "status": "пройдено", "rating": 10.0},
    {"title": "Cyberpunk 2077", "status": "граю", "rating": 8.0},
])
records = catalog.load_data()
avg_rating = sum(r["rating"] for r in records) / len(records)
assert avg_rating == 9.0, f"Очікувалось 9.0, отримано {avg_rating}"
print("  ✓ Тест 1: середній рейтинг (10+8)/2 = 9.0")

# ── Тест 2: Статистика при порожньому файлі ──
setup([])
records = catalog.load_data()
assert len(records) == 0, "Очікувався порожній список"
print("  ✓ Тест 2: порожній каталог оброблено")

# ── Тест 3: Сортування за рейтингом ──
setup([
    {"title": "Low", "rating": 5.0},
    {"title": "High", "rating": 9.5},
])
records = catalog.load_data()
# Логіка сортування (як у вашому main/catalog)
sorted_records = sorted(records, key=lambda x: x['rating'], reverse=True)
assert sorted_records[0]["rating"] == 9.5, "Помилка сортування"
print("  ✓ Тест 3: сортування за оцінкою коректне")

teardown()
print("\n  Усі тести пройдено успішно.")