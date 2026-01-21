# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimeter=','):
    list1 = group1.split(delimeter)
    list2 = group2.split(delimeter)
    common_set = set(list1).intersection(set(list2))
    return sorted(list(common_set))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, delimeter=',')

print(f"Общие участники: {common}")