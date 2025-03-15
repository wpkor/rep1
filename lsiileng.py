from datetime import datetime
formats = {
    "The Moscow Times": "%A, %B %d, %Y",  # Wednesday, October 2, 2002
    "The Guardian": "%A, %d.%m.%y",  # Friday, 11.10.13
    "Daily News": "%A, %d %B %Y"  # Thursday, 18 August 1977
}

def parse_date(date_string):
    for newspaper, date_format in formats.items():
        try:

            return datetime.strptime(date_string, date_format)
        except ValueError:

            continue

    print(f"Некорректный формат даты: {date_string}")
    return None


def main():
    while True:

        date_input = input("Введите дату (или 'exit' для выхода): ")


        if date_input.lower() == 'exit':
            print("Завершение программы.")
            break


        parsed_date = parse_date(date_input)

        if parsed_date:
            print(f"Преобразованная дата: {parsed_date}")
        else:
            print("Попробуйте ввести дату в другом формате.")

main()