# TODO Напишите функцию find_common_participants

def find_common_participants (first_group, second_group, split_ch = ','):
    return sorted (list (set(first_group.split (split_ch)).intersection (set (second_group.split (split_ch)))))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print (find_common_participants(participants_first_group, participants_second_group, '|'))