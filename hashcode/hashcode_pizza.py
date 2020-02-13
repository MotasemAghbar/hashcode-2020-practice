import collections
srcs = ['a_example', 'b_small', 'c_medium', 'd_quite_big', 'e_also_big']

def cal_slices(sorted_dict):
    answer = []
    num_slice_taken = 0
    for pizza_type in sorted_dict:
        slices = sorted_dict[pizza_type]
        if len(answer) >= len(sorted_dict) or num_slice_taken + slices > max_slice:
            continue
        num_slice_taken += slices
        answer.append(pizza_type)
    return answer, num_slice_taken


for src in srcs:
    in_file = open('src/' + src + '.in', 'r')
    max_slice, num_types = map(lambda x: int(x), in_file.next().split(' '))
    types_list = map(lambda x: int(x), in_file.next().split(' '))
    types_dict = {i: types_list[i] for i in range(0, len(types_list))}
    sorted_dict = collections.OrderedDict(sorted(types_dict.items(), key=lambda kv: kv[1], reverse=True))
    best_answer = []
    best_slice_taken = 0
    for i in range(len(sorted_dict.keys())):
        temp_answer, temp_slices = cal_slices(sorted_dict)
        if temp_slices > best_slice_taken:
            best_answer = temp_answer
            best_slice_taken = temp_slices
        del sorted_dict[temp_answer[-1]]

    print('score:' + str(best_slice_taken))
    print('losted slices: ' + str(max_slice - best_slice_taken))

    open('out/' + src + '.out', 'w+').write(str(len(best_answer)) + '\n' + ' '.join(map(str, best_answer)))
