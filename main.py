import first_task as scrabble
import second_task as song

if __name__ == '__main__':

    task_number = int(input('Enter task number: '))

    while task_number < 1 or task_number > 2:
        print('Try again\n')
        task_number = int(input('Enter task number: '))

    if task_number == 1:
        print(f'{scrabble.Scrabble(input("Enter ur word: ")).count_score()}')
    else:
        song.Song().show_song()  # TF is going on there
