def get_dict(task):
    to_list = list(task.result.values())                    # dict -> list 
    to_str = ' '.join(to_list)                              # list -> string
    lists = to_str.split()                                  # string -> list
    dict = {string:i for i, string in enumerate(lists)}     # confidence별로 dict의 value값 지정 (낮을수록 높은 confidence)    
    return dict
