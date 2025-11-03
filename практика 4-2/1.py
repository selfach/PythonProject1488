def is_cyrillic(text):
    for char in text.upper():
        if 'А' <= char <= 'Я' or char == 'Ё':
            return True
    return False


points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}


def calculate_score(word):
    word = word.upper()
    points_dict = points_ru if is_cyrillic(word) else points_en
    score = 0
    for letter in word:
        for points, letters in points_dict.items():
            if letter in letters:
                score += points
                break
    return score


def multiplayer_game():
    players = int(input("Количество игроков: "))
    rounds = int(input("Количество раундов: "))
    scores = [0] * players

    for round in range(1, rounds + 1):
        print(f"\nРаунд {round}")
        for player in range(players):
            word = input(f"Игрок {player + 1}, введите слово: ")
            round_score = calculate_score(word)
            scores[player] += round_score
            print(f"+{round_score} очков. Всего: {scores[player]}")

    print("\nРезультаты:")
    max_score = max(scores)
    for i, score in enumerate(scores):
        print(f"Игрок {i + 1}: {score} очков")

    winners = [i + 1 for i, score in enumerate(scores) if score == max_score]
    if len(winners) == 1:
        print(f"Победил игрок {winners[0]}!")
    else:
        print(f"Ничья! Победители: {winners}")


multiplayer_game()