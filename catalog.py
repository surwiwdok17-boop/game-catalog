import json
import os
from colorama import init, Fore
init(autoreset=True)

DATA_FILE = "games_catalog.json"

def load_data():
    if not os.path.exists(DATA_FILE): return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(games):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(games, f, ensure_ascii=False, indent=2)

def print_games(games, title="КАТАЛОГ"):
    if not games:
        print(Fore.RED + "\n У каталозі пусто.")
        return
    

    max_title = max([len(g['title']) for g in games] + [5]) + 2
    max_plat = max([len(g['platform']) for g in games] + [9]) + 2
    max_stat = max([len(g['status']) for g in games] + [6]) + 2

    header = f" {title} | {'Назва':<{max_title}} | {'Платформа':<{max_plat}} | {'Статус':<{max_stat}} | Оцінка"
    print(f"\n{header}")
    print("-" * len(header))
    
    for i, g in enumerate(games, 1):
        print(f" {i:<7} | {g['title']:<{max_title}} | {g['platform']:<{max_plat}} | {g['status']:<{max_stat}} | {g['rating']}")

def add_game():
    title = input(" Назва гри: ").strip()
    platform = input(" Платформа: ").strip()
    print(" 1-граю, 2-пройдено, 3-відкладено")
    choice = input(" Виберіть статус (1-3): ")
    statuses = {"1": "граю", "2": "пройдено", "3": "відкладено"}
    status = statuses.get(choice, "невідомо")
    
    while True:
        try:
            rating = float(input(" Оцінка (0-10): "))
            if 0 <= rating <= 10: break
            print(Fore.RED + " Помилка: введіть число від 0 до 10.") 
        except ValueError:
            print(Fore.RED + " Помилка: введіть число!")
            
    games = load_data()
    games.append({"title": title, "platform": platform, "status": status, "rating": rating})
    save_data(games)
    print(Fore.GREEN + " ✓ Гру успішно додано!")

def delete_game():
    games = load_data()
    print_games(games)
    try:
        idx = int(input("\n Введіть номер гри для видалення: ")) - 1
        if 0 <= idx < len(games):
            removed = games.pop(idx)
            save_data(games)
            print(Fore.GREEN + f" ✓ Гру '{removed['title']}' видалено.")
        else:
            print(Fore.RED + " Помилка: Невірний номер.")
    except ValueError:
        print(Fore.RED + " Помилка: Введіть число.")

def show_stats():
    games = load_data()
    if not games: return
    avg = sum(g['rating'] for g in games) / len(games)
    print(f"\n --- СТАТИСТИКА ---\n Всього ігор: {len(games)}\n Середня оцінка: {avg:.2f}")

def sort_games():
    games = load_data()
    games.sort(key=lambda x: x['rating'], reverse=True)
    print_games(games, "ТОП ІГОР")

def menu():
    while True:
        print("\n=== МЕНЮ КАТАЛОГУ ===")
        print(" 1. Додати гру\n 2. Переглянути всі ігри\n 3. Фільтр за статусом\n 4. Сортувати за оцінкою\n 5. Статистика\n 6. Видалити гру\n 0. Вихід")
        choice = input(" Вибір: ")
        
        if choice == "1": add_game()
        elif choice == "2": print_games(load_data())
        elif choice == "3": 
            valid = ["граю", "пройдено", "відкладено"]
            st = input(f" Статус ({'/'.join(valid)}): ").strip().lower()
            if st in valid:
                print_games([g for g in load_data() if g["status"] == st], "ФІЛЬТР")
            else:
                print(Fore.RED + " Невірний статус!")
        elif choice == "4": sort_games()
        elif choice == "5": show_stats()
        elif choice == "6": delete_game()
        elif choice == "0": break
        else: print(Fore.RED + " Невірний вибір.")

if __name__ == "__main__":
    menu()