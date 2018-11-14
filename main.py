from base_prepary import PlayingField

b = 0
move = 1 #хранится информация о том чей ход: 1- синие, 2- красные

a = PlayingField()
a.create_pf()
# вывод игровового поля в первый раз
a.show_playing_field()

while b < 99:
    if move == 1:
        print('Ход синих')
    else:
        print('Ход красных')
    # определяем тип хода: новая шестерня или переносим стареую на новое место
    step_type = int(input('введите тип хода (1 - новая шестерня, 2- переставить существующую'))
    if step_type == 1:
        # ввести значения координат для установки новой шестерни
        new_x = int(input('введите X'))
        new_y = int(input('Введите Y'))
        a.new_gear(move, new_x, new_y)
    else:
        old_x = int(input('введите старое значение X'))
        old_y = int(input('Введите старое значение Y'))
        new_x = int(input('введите новое значение X'))
        new_y = int(input('Введите новое значение Y'))
        a.move_gear(move, old_x, old_y, new_x, new_y)
        #ввести значения координаты текущей шестерни и потом новые координаты


    # проверяем корректно ли ввели коорединаны. если корректно, то идем дальше
    if a.result == 'ok':
        # обновление игрового поля
        a.show_playing_field()
        # проверка закончилась игра или нет
        a.check_who_win()
        # смена игрока
        a.change_plaer(move)
        move = a.new_player
    else:
        print('координаты не корректны')






