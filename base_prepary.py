
class PlayingField:


    def __init__(self):
        self.varr = None

    def create_pf(self): #создание игорового поля
        self.max_value_y = 19
        self.max_value_x = 10
        x = 0
        y = 0
        value_zero = 0
        value_one = 1
        value_two = 2
        self.varr = []

        self.varr = [0]*self.max_value_x
        for y in range(0,self.max_value_x):
            self.varr[y] = [0]*self.max_value_y

        count = 0

        for x in range(0,self.max_value_x):
            y = 0
            begin_value = x
            end_value = self.max_value_y-x
            for y in range(begin_value, end_value):
                if (x%2) == 0:
                    if (y%2) == 0:
                        self.varr[x][y] = 1
                    else:
                        self.varr[x][y] = 0
                else:
                    if (y%2) == 0:
                        self.varr[x][y] = 0
                    else:
                        self.varr[x][y] = 1
                self.varr[0][0]=2
                self.varr[0][18]=3
        return self.varr

    def new_gear(self, player, x, y):
        #проверка на корректность координат
        if self.varr[x][y] == 1:
            if player == 1:
                self.varr[x][y] = 2
            else:
                self.varr[x][y] = 3
            self.result = 'ok'
        else:
            self.result = 'err'
        return self.result, self.varr

    def move_gear(self, player, x_before, y_before, x_after, y_after):
        # проверяем наша ли шестерня на данной точке
        if player == 1:
            if self.varr[x_before][y_before] == 2:
                self.varr[x_before][y_before] = 1
                self.result = 'ok'
            else:
                self.result = 'err'
        else:
            if self.varr[x_before][y_before] == 3:
                self.varr[x_before][y_before] = 1
                self.result = 'ok'
            else:
                self.result = 'err'

        # установка новых координат
        # проверка на корректность координат
        if self.varr[x_after][y_after] == 1:
            if player == 1:
                self.varr[x_after][y_after] = 2
            else:
                self.varr[x_after][y_after] = 3
                self.result = 'ok'
        else:
            self.result = 'err'
        return self.varr, self.result

        return self.varr, self.result

    def show_playing_field(self):
        for y in range(0, 10):
            print(str(y) + '-' + str(self.varr[y]))
        return

    def change_plaer(self, current_plaer):
        if current_plaer == 1:
            self.new_player = 2
        else:
            self.new_player = 1

        return self.new_player

    def check_who_win(self):
        pass
        # проверяет кто выиграл
        return
