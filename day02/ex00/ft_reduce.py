def ft_reduce(function_to_apply, list_of_inputs):
    ret = function_to_apply(list_of_inputs[0], list_of_inputs[1])
    for ele in list_of_inputs[2:]:
        ret = function_to_apply(ret, ele)
    return ret
