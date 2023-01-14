def time_transform(start, end, monthly_total):
    start_sep = start.split(':')
    start_hour = int(start_sep[0])
    start_min = int(start_sep[1])


    end_sep = end.split(':')
    end_hour = int(end_sep[0])
    end_min = int(end_sep[1])

    time_calculation(start_hour, start_min, end_hour, end_min, monthly_total)


def time_calculation(start_hour, start_min, end_hour, end_min, monthly_total):
    total_minuts = (end_min - start_min)
    if total_minuts < 0:
        total_minuts  = total_minuts * -1
    total_hours = end_hour - start_hour
    calc_comb = (total_hours * 60) + total_minuts
    calc_total = calc_comb / 60

    monthly_total.append(calc_total)


def time_split(hour_group):
    join_hour_group = ','.join(hour_group)
    split_group = join_hour_group.split(',')
    split_start = split_group[0]
    split_end = split_group[1]

    time_transform(split_start, split_end, monthly_total)




def loop_test():
    list_one = ['1', '2', '3', '4', '5']
    list_two = ['1', '2', '3', '4', '5']
    combo_list = []

    for first, second in zip(list_one, list_two):
        math_list = first + ',' + second
        combo_list.append(math_list)

    return combo_list


def loop_split(combo_list):
    combo_solution = []
    for combo in combo_list:
        list_sep = combo.split(',')
        start_sep = int(list_sep[0])
        end_sep = int(list_sep[1])

        calc_together = start_sep + end_sep

        combo_solution.append(calc_together)

    return combo_solution


loop_test()
loop_test_result = loop_test()
print(loop_split(loop_test_result))

# monthly_total = []
# time_split(['15:00','16:00'])
# print(monthly_total)





























































# from datetime import datetime

# # time_str = '13:55'
# # time_object = datetime.strptime(time_str, '%H:%M').time()
# # print(time_object)

# this_list = ['13:55', '17:00']

# start_time_pull = [this_list[0]]
# end_time_pull = [this_list[1]]

# start_time = ''.join(start_time_pull)
# end_time = ''.join(end_time_pull)


# start_time_object = datetime.strptime(start_time, '%H:%M').time()
# end_time_object = datetime.strptime(end_time, '%H:%M').time()
# print(start_time_object)
# print(end_time_object)
# print(end_time_object - start_time_object)
