def task_result(status,result=None):
    if result is not None:
        task_result = {
            'status' : status,
            'result' : result
        }
        return task_result
    else: 
        task_result = {
            'status' : status
        }
        return task_result