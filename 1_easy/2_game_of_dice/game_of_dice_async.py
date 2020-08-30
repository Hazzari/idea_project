#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2. Симулятор игры в кости в Python

Идея проекта. Симулятор игры в кости будет имитировать
бросание костей в реальной жизни. С помощью него пользователь
сможет снова и снова «выбрасывать» случайным образом генерируемое число,
до тех пор пока не захочет выйти из программы.

в асинхронном режиме
"""

from dataclasses import dataclass

import asyncio
from pprint import pprint
from random import randint



@dataclass
class Bone:
    __number: int

    async def roll_the_bones(self):
        print(f'Кидаем {self.__number} кубик...')
        await asyncio.sleep(randint(1, 3))

    async def bones_are_rolling(self, ):
        print(f'...кубик {self.__number} катится по игровому полю...')
        await asyncio.sleep(randint(1, 3))

    async def bones_show_the_result(self):
        print(f'Кубик {self.__number} остановился и выпало {randint(1, 6)}')
        await asyncio.sleep(randint(1, 3))

    async def main(self):
        await self.roll_the_bones()
        await self.bones_are_rolling()
        await self.bones_show_the_result()


def __get_bones():
    while True:
        born_count = input('Сколько бросить кубиков? ( не больше 10 ) \n >>> ')
        try:
            if (0 < int(born_count) < 10):
                born_count = int(born_count)
                break

        except ValueError:
            print('Не число')
        except IndexError:
            print("Не верное количество")

    return born_count


def app():
    while True:
        loop = asyncio.get_event_loop()

        bones_count = __get_bones()
        bones = [Bone(task).main() for task in range(1, int(bones_count) + 1)]

        task_count = [loop.create_task(task) for task in bones]

        tasks = asyncio.wait(task_count)

        loop.run_until_complete(tasks)
        loop.close()
        end_game = input("Играем?\n.... q для выхода\n>>> ")
        app()
        if end_game == ('q' and 'й'):
            print('Спасибо за игру!')
            break


if __name__ == '__main__':
    app()

# TODO 2020-08-31, пн, 2:1 aleksan: После перого прогона выдает ошибку:
        # RuntimeError: Event loop is closed
        # sys:1: RuntimeWarning: coroutine 'Bone.main' was never awaited