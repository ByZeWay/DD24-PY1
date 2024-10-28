def count_letters(text):
    dict_letter_cnt = {}

    for char in text:
        lowercase_ch = char.lower()
        if lowercase_ch.isalpha():
            if lowercase_ch in dict_letter_cnt:
                dict_letter_cnt[lowercase_ch] += 1
            else:
                dict_letter_cnt[lowercase_ch] = 1

    return dict_letter_cnt


def calculate_frequency(dict_letter_cnt):
    dict_frequency = {}
    total_letters_cnt = sum(dict_letter_cnt.values())

    for letter, cnt in dict_letter_cnt.items():
        dict_frequency[letter] = ("%.2f" % (cnt / total_letters_cnt))

    return dict_frequency


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


frequencies = calculate_frequency(count_letters(main_str))

for letter, frequency in frequencies.items():
    print(f"{letter}: {frequency}")