def find_common_participants(participants_first_group, participants_second_group, sep=','):
    first_group = set(participants_first_group.split(sep))
    second_group = set(participants_second_group.split(sep))
    common_participants = sorted(first_group.intersection(second_group))

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, '!')
print(common_participants)

common_participants = find_common_participants(participants_first_group, participants_second_group, ',')
print(common_participants)

participants_first_group_v2 = "Иванов|Петров|Сидоров"
participants_second_group_v2 = "Иванов|Петров|Смирнов"
common_participants = find_common_participants(participants_first_group_v2, participants_second_group_v2)
print(common_participants)
