"""
Идея проекта.

У пользователя будет несколько шансов,
причем при каждой неправильной попытке он будет получать
подсказку от компьютера, сообщающую о том,
в какую сторону (большую или меньшую) он ошибся.

"""
from random import randint
from dataclasses import dataclass
from time import sleep


@dataclass
class Game:

    __random_number: int = 0
    _status_hidden_number: bool = False
    _number_of_attempts: int = 0

    def default_settings(self):
        self.__random_number: int = 0
        self._status_hidden_number = False
        self._number_of_attempts = 0

    def get_level(self, level):
        if level == '3':
            self._number_of_attempts = 5
        elif level == '2':
            self._number_of_attempts = 15
        elif level == '1':
            self._number_of_attempts = 20
        else:
            raise ValueError

    @staticmethod
    def get_number_from_user():
        while True:
            number_from_user = input('Ваше число: ')
            try:
                conversion_result = int(number_from_user)
                if int(conversion_result) in range(1, 99):
                    return conversion_result
                else:
                    print(f'{conversion_result} < -- не правильное число')
            except ValueError:
                print(f'{number_from_user} < -- это не число')

    @property
    def number_of_attempts(self):
        return self._number_of_attempts

    @staticmethod
    def get_random_number():
        random_number = randint(0, 100)
        return random_number

    def main(self):
        # Настраиваем игру
        while True:
            # Выбираем уровень:
            level = input('Выберите уровень сложности:\n'
                          '3 - hard\n'
                          '2 - medium\n'
                          '1 - easy\n'
                          '--> ')
            try:
                self.get_level(level=level)
                break
            except ValueError:
                print('Не верно выбран уровень\n*')

        while self._number_of_attempts:

            # Если число не загаданно то
            if not self._status_hidden_number:
                # Загадываем число
                print('Задумался...')
                sleep(1)
                self.__random_number = self.get_random_number()
                self._status_hidden_number = True
                print('...число загадано.'.rjust(30))
                sleep(1)
                print('Игра начинается!')
                for _ in range(3):
                    sleep(0.4)
                    print('.')
                print('\n')
                sleep(1)

            # приглашение ввести число
            number_from_player = self.get_number_from_user()
            if number_from_player == self.__random_number:
                print('Вы отгадали число')
                self.default_settings()
                break
            elif number_from_player > self.__random_number:
                print(f'{number_from_player} больше загаданного числа')
            else:
                print(f'{number_from_player} меньше загаданного числа')

            self._number_of_attempts -= 1
            print(f'У вас осталось {self._number_of_attempts} попыток!')
            if not self._number_of_attempts:
                print(f'Компьютер загадал {self.__random_number}')


if __name__ == '__main__':
    game = Game()
    while True:
        game.main()
        print('Хотите еще раз сыграть?')
        print('Для продолжения игры нажмите любую клавишу')
        print('Для выхода нажмите "q"')

        result = input(">>> ")
        if result == ('q' and 'й'):
            print('Спасибо за игру!')
            break
