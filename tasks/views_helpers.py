from datetime import datetime


class ViewsHelpers:
    @staticmethod
    def calculation_delta(task):
        if task.time_estimated is None:
            return None
        else:
            return (task.time_estimated - datetime.now().date()).days

    @staticmethod
    def request_fields_data(request, task):
        task.priorities = request.POST['priorities']
        task.task_title = request.POST['task_title']
        task.task_description = request.POST['task_description']
        estimated = request.POST['time_estimated']
        if estimated:
            task.time_estimated = datetime.strptime(estimated, '%Y-%m-%d').date()
        else:
            task.time_estimated = estimated
        return task
