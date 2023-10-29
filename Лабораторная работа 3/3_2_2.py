participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(part1, part2, spl="|"):
    group1 = set(part1.split(spl))
    group2 = set(part2.split(spl))
    same_part = list(group1.intersection(group2))  # Ищем идентичные объекты
    return same_part

common_participants = find_common_participants(participants_first_group, participants_second_group)
common_participants.sort()
print("Список общих участников: ", common_participants)

