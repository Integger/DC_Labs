# TODO  Напишите функцию count_letters
from itertools import count


def count_letters (text):
    counter_ret = {}

    for character in text.lower ():
        if character.isalpha ():
            if counter_ret.get(character) is None:
                counter_ret[character] = 1
            else:
                counter_ret[character] += 1

    return counter_ret

# TODO Напишите функцию calculate_frequency
def calculate_frequency (counter_, len_):
    frequencies = {}

    for character, count_ in counter_.items ():
        frequencies [character] = round (count_ / len_, 2)

    return frequencies

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
counter = count_letters (main_str)

length = 0

for count in counter.values ():
    length += count

for character, count_ in calculate_frequency (counter, length).items ():
    print (f"{character}: {count_:.2f}")