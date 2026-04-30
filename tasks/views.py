from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import TaskForm
from django.http import JsonResponse

def main(request):
    task_list = models.task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save()

        if 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(models.task, id=task_id)
            task.delete()
            return redirect('main')

    return render(request, 'main.html', {'task_list': task_list, 'form': form})


###task_list = models.task.objects.all

    form = forms.TaskForm()

    if request.method == 'POST':

        form = forms.TaskForm(request.POST)

        if form.is_valid():

            form.save()

        return render(request, 'main.html', {'task_list': task_list, 'form': form})
        
    else: 

        return render(request, 'main.html', {'task_list': task_list, 'form': form})###