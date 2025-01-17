from datetime import datetime

def Lab(date_str):

    try:
        
        date = datetime.strptime(date_str, '%Y-%m-%d')
        month = date.month

        
        if 1 <= month <= 3:
            return 1
        elif 4 <= month <= 6:
            return 2
        elif 7 <= month <= 9:
            return 3
        elif 10 <= month <= 12:
            return 4
    except ValueError:
        return "Невірний формат дати. Введіть дату у форматі 'YYYY-MM-DD'."


if __name__ == "__main__":
    date_input = input("Введіть дату у форматі YYYY-MM-DD: ")
    result = Lab(date_input)
    print(f"Квартал: {result}")
