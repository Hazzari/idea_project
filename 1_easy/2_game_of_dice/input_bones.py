#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_bones():
    while True:
        born_count = input('Сколько бросить кубиков? ( не больше 10 ) \n >>> ')
        try:
            if 0 < int(born_count) <= 10:
                born_count = int(born_count)
                break
        except ValueError:
            print('Не число')
        except IndexError:
            print("Не верное количество")

    return born_count
