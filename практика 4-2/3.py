note_book = {
    "Маша": {
        'tel': '+7922123561',
        'vk': 'vk.com/masha321',
        'youtube': 'youtube.com/masha321',
        'telegram': 't.me/masha321'
    },
    "Паша": {
        'tel': '+79151234567',
        'vk': 'vk.com/pasha123',
        'youtube': 'youtube.com/pasha123',
        'telegram': 't.me/pasha123'
    },
    "Даша": {
        'tel': '+79031112233',
        'vk': 'vk.com/dasha456',
        'youtube': 'youtube.com/dasha456',
        'telegram': 't.me/dasha456'
    }
}

user_search = input("Введите имя из списка контактов: ").capitalize()

if user_search in note_book:
    print(f"\nДанные контакта {user_search}:")
    print(f"Телефон: {note_book[user_search]['tel']}")
    print(f"ВКонтакте: {note_book[user_search]['vk']}")
    print(f"YouTube: {note_book[user_search]['youtube']}")
    print(f"Telegram: {note_book[user_search]['telegram']}")
else:
    print("Контакт не найден!")