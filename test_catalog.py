# test_catalog.py

def test_calculate_average():
    # Тестові дані (ігри)
    games = [
        {"title": "Game 1", "rating": 8.0},
        {"title": "Game 2", "rating": 10.0}
    ]
    
    # Логіка обчислення 
    total_rating = sum(g['rating'] for g in games)
    avg = total_rating / len(games)
    
    # Перевірка: чи середнє дорівнює 9.0?
    assert avg == 9.0, f"Очікувалося 9.0, отримано {avg}"
    print("Тест успішно пройдено!")

if __name__ == "__main__":
    test_calculate_average()