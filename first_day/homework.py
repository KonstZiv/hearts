# написати функцію якам приймає рядок і повертає словник у якому
# ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні
# вірогідності зустріти цей символ в цьому рядку.
# № код повинен бути структурований за допомогою конструкції if __name__ == "__main__":,
# всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації


# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over"


# встановити git  зареєструватись на gitlab

from collections import Counter


def get_symbols_frequency(text):
    result_dict = {}
    texts_len = len(text)
    for symbol in set(text):
        result_dict[symbol] = text.count(symbol) / texts_len
    return result_dict


def get_symbols_frequency_with_counter(text):
    texts_len = len(text)
    return {key: value / texts_len for key, value in Counter(text).items()}


def get_ternary(x, y):
    return str(
        x + y if (x < y) else
        x - y if (x > y) else
        "game over" if (x == 0 and y == 0) else
        0
    )


if __name__ == "__main__":
    ternary_causes = (
        (1, 2, "3"),
        (1, 1, "0"),
        (2, 1, "1"),
        (0, 0, "game over"),
    )

    for x, y, result in ternary_causes:
        assert get_ternary(x, y) == result, f"get_ternary({x}, {y}) == {get_ternary(x, y)}, but expected: {result}"

    print(get_symbols_frequency_with_counter("123"))
