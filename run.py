monthly_total = []

def hour_combine(monthly_total):
    list_one = ['15:00', '15:00', '15:00', '15:00', '15:00']
    list_two = ['20:00', '20:00', '20:00', '20:00', '20:00']
    combo_list = []

    for first, second in zip(list_one, list_two):
        math_list = first + ',' + second
        combo_list.append(math_list)
    

    return combo_list


# def time_split(hour_group, monthly_total):
#     for group in hour_group:
#         split_group = group.split(',')
#         split_start = split_group[0]
#         split_end = split_group[1]
#         return split_start, split_end

    # time_transform(split_start, split_end, monthly_total)


def time_transform(start, end, monthly_total):
    start_sep = start.split(':')
    start_hour = int(start_sep[0])
    start_min = int(start_sep[1])


    end_sep = end.split(':')
    end_hour = int(end_sep[0])
    end_min = int(end_sep[1])

    return start_hour, start_min, end_hour, end_min, monthly_total


def time_calculation(start_hour, start_min, end_hour, end_min, monthly_total):
    total_minuts = (end_min - start_min)
    if total_minuts < 0:
        total_minuts  = total_minuts * -1
    total_hours = end_hour - start_hour
    calc_comb = (total_hours * 60) + total_minuts
    calc_total = calc_comb / 60

    monthly_total.append(calc_total)
# START BACK HERE

list_data = hour_combine(monthly_total)


def loop_split(combo_list, round, monthly_total):
    list_sep = combo_list[round].split(',')
    start_sep = list_sep[0]
    end_sep = list_sep[1]

    return start_sep, end_sep, monthly_total


# # print(loop_split(list, monthly_total))
# loop_split(list, monthly_total)
# print(monthly_total)

# loop_test()
# print(loop_test(monthly_total))
# loop_test_result = loop_test()
# print(time_split(loop_test_result))
# loop_test_result = loop_test()
# print(loop_split(loop_test_result))

# monthly_total = []
# time_split(['15:00','16:00'])
# print(monthly_total)

# split each item
# split each part of item
# calculate time

def run_this(list_data, monthly_total):
    rotation = -1
    for pair in list_data:
        rotation += 1
        res_one, res_two, res_three = loop_split(list_data, rotation, monthly_total)
        res_four, res_five, res_six, res_seven, res_eight = time_transform(res_one, res_two, res_three)
        time_calculation(res_four, res_five, res_six, res_seven, res_eight)
        
    print(sum(monthly_total))

run_this(list_data, monthly_total)







# loop_split(list_data, monthly_total)

# def add_one(num1, num2):
#     num3 = num1 + num2
#     num6 = num1 - num1
#     return num3, num6

# def add_two(num3, num6):
#     num4 = num3 + 2
#     return num4

# def add_three(num4):
#     num5 = num4 + 2
#     return num5


# def all_add(num1, num2):
#     result_one, result_four = add_one(num1, num2)
#     result_two = add_two(result_one, result_four)
#     result_three = add_three(result_two)
#     return result_three

# print(all_add(1, 2))






































# combo_list(['15:00,20:00'])


# def loop_split(combo_list):
#     combo_solution = []
#     for combo in combo_list:
#         list_sep = combo.split(',')
#         start_sep = list_sep[0]
#         end_sep = list_sep[1]

   

#     return combo_solution












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
