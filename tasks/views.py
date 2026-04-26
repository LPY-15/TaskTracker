from django.shortcuts import render
from . import models
from . import forms

def main(request):
    all_members = models.Member.objects.all
    member_form = forms.MemberForm()
    if request.method == 'POST':
        form = forms.MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'main.html', {'members': all_members, 'member_form': member_form})
        
    else: 
        return render(request, 'main.html', {'members': all_members, 'member_form': member_form})