from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import TaskForm
from django.http import JsonResponse

def main(request):
    task_list = models.task.objects.all()
    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            print('ajax worked')

            if request.POST.get('action') == 'create-task':
                
                if form.is_valid():
                    task = form.save()

                    return JsonResponse({
                        'id': task.id,
                        'task_name': task.task_name
                    })
                else:
                    return JsonResponse({'errors': form.errors}, status=400)

            elif request.POST.get('action') == 'delete-task':

                task_id = request.POST.get('task_id')
                task = get_object_or_404(task_list, id=task_id)
                task.delete()

            else:
                print('action is not in request')
        else:
            print('ajax not worked')

    return render(request, 'main.html', {'task_list': task_list, 'form': form})
