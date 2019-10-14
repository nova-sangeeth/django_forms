from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForms,SnippetForms
# Create your views here.
def contact(request):
    if request.method =='POST':
        form = contactForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email =form.cleaned_data['email']
            print(name,email)


    form = contactForms()

    return render(request,'form.html',{'form': form})
    return HttpResponse ('contact view')


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForms(request.POST)
        if form.is_valid():
            print('VALID')
            form.save()

    form = SnippetForms()

    return render(request, 'form.html', {'form': form})
    return HttpResponse('contact view')

