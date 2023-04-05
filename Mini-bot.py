slova={1:['а','в','и','н','о','р','с','т','е'], 2:['д','к','л','м','п','у'], 3:['б','г','ё','ь','я'], 4:['ы','й'], 5:['ж','з','х','ц','ч'], 8:['ш','э','ю'], 10:['ф','щ','ъ']}

def scrabl():
    ball=0
    slovo_1=list(input('Введите слово: ').lower())
    for i in slovo_1:
        for k,v in slova.items():
            if i in v:
                ball+=k
    print(ball, 'Баллов!')

def game():
    vibor_game = int(input("1-Скрабл | 2-Уникальные символы | 3-Анаграммы\n"))
    if vibor_game == 1:
        scrabl()
    if vibor_game == 2:
        game()
    if vibor_game == 3:
        "Пока 👋 "
    else:
        game()


def main(interests):
    for i in (people):
        result1 = interests & (set(people[i][1]))
        result2 = interests.union(set(people[i][1]))
        result = len(result1)/len(result2) *100
        if round(result) > 15:
            print(people[i][0], round(result))
            print(people[i][1]-interests)
  
def menu():
    vibor = int(input("1-Найти друга | 2-Играть | 3-Выйти\n"))
    if vibor == 1:
        main(interests)
    if vibor == 2:
        game()
    if vibor == 3:
        "Пока 👋 "
    else:
        menu()

people = {1: ['Иван', {'фантастика', 'комикс', 'детектив', 'роман'}], 2: ['Марина', {'комикс', 'фэнтези', 'детектив', 'комедия'}], 3: ['Тим', {'фантастика', 'ужасы', 'детектив', 'драма'}], 4: ['Никита', {'фэнтези', 'комедия', 'мистика', 'комикс'}], 5: ['Владимир', {'комикс', 'роман', 'комедия', 'драма'}]}
name = input("Введи имя: ")
interests = set(input("Введите 4 любимых жанра 🎦 : ").split(" "))
print(interests)
menu()