#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2. Симулятор игры в кости на Python

Идея проекта. Симулятор игры в кости будет имитировать
бросание костей в реальной жизни. С помощью него пользователь
сможет снова и снова «выбрасывать» случайным образом генерируемое число,
до тех пор пока не захочет выйти из программы.

в асинхронном режиме
"""
import time
from dataclasses import dataclass

import asyncio
from random import randint

from input_bones import get_bones


@dataclass
class Bone:
    __number: int

    async def roll_the_bones(self):
        print(f'Кидаем {self.__number} кубик...')
        await asyncio.sleep(randint(0, 1))

    async def bones_are_rolling(self, ):
        print(f'...кубик {self.__number} катится по игровому полю...')
        await asyncio.sleep(randint(1, 6))

    async def bones_show_the_result(self):
        print(f'Кубик {self.__number} остановился и выпало ---->>>> "{randint(1, 6)}"')
        await asyncio.sleep(randint(1, 5))

    async def main(self):
        await self.roll_the_bones()
        await self.bones_are_rolling()
        await self.bones_show_the_result()


def app():
    while True:
        bones_count = get_bones()

        bones = [Bone(c) for c in range(1, bones_count + 1)]

        coros = [c.main() for c in bones]
        coro = asyncio.wait(coros)
        asyncio.run(coro)

        time.sleep(1)
        end_game = input("Играем?\n.... q для выхода\n>>> ")

        if end_game == ('й' and 'q'):
            print('Спасибо за игру!')
            break


if __name__ == '__main__':
    app()
