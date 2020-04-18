def ft_filter(function_to_apply, list_of_inputs):
    for ele in list_of_inputs:
        if function_to_apply(ele):
            yield ele
