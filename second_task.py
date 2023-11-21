class Song:

    def __init__(self):
        self.__second_const_string = 'my true love sent to me:\n'
        self.__last_const_string = 'And a partridge in a pear tree.'
        self.__days_dict = {
            1: 'first',
            2: 'second',
            3: 'third',
            4: 'fourth',
            5: 'fifth',
            6: 'sixth',
            7: 'seventh',
            8: 'eighth',
            9: 'ninth',
            10: 'tenth',
            11: 'eleventh',
            12: 'twelfth'
        }
        self.__gifts_counter_dict = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve'
        }
        self.__song_parts_list = self.get_default_part(1)

    def create_part_of_song(self, day: int):
        self.__song_parts_list.insert(day + 1, self.__gifts_counter_dict.get(day) + 'something')

    def get_default_part(self, day) -> list:
        return [
            f'On the {self.__days_dict.get(day)} of Christmas\n',
            self.__second_const_string,
            self.__last_const_string + '\n'
        ]

    def __show_part(self):
        for string in self.__song_parts_list:
            print(string)

    def show_song(self):
        for part in range(2, 13):
            self.create_part_of_song(part)
            self.__show_part()
