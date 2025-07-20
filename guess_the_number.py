import random

def print_instructions():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100.")
    print("Попробуйте угадать его. У вас будет 10 попыток.")
    print("После каждой попытки я скажу, больше или меньше ваше число.")
    print("Введите 'выход', чтобы выйти из игры в любой момент.\n")

def get_user_guess():
    while True:
        guess = input("Введите ваше предположение: ").strip()
        if guess.lower() == "выход":
            return "exit"
        if not guess.isdigit():
            print("Ошибка: пожалуйста, введите целое число от 1 до 100.")
            continue
        guess = int(guess)
        if 1 <= guess <= 100:
            return guess
        else:
            print("Ошибка: число должно быть в диапазоне от 1 до 100.")

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        print(f"\nПопытка {attempts + 1} из {max_attempts}")
        user_guess = get_user_guess()

        if user_guess == "exit":
            print("Вы вышли из игры. До свидания!")
            return

        attempts += 1

        if user_guess < secret_number:
            print("Слишком маленькое число.")
        elif user_guess > secret_number:
            print("Слишком большое число.")
        else:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток.\n")
            break
    else:
        print(f"\nВы проиграли. Загаданное число было: {secret_number}\n")

def main():
    while True:
        print_instructions()
        play_game()
        retry = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
        if retry != "да":
            print("Спасибо за игру! До встречи!")
            break

if __name__ == "__main__":
    main()
