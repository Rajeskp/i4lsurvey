from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Items, opt

def myview(request):
    all_items_objects = Items.objects.all()
    return render(request, 'index.html',
            {'all_items': all_items_objects})

def ques_data(request):
    all_items_objects = Items.objects.all()
    all_data_items = opt.objects.all
    return render(request, 'admin.html',
            {'all_items': all_items_objects, 'data_items': all_data_items})

def addData(request):
    new_data = Items(content = request.POST['content'])
    new_data.save()
    return HttpResponseRedirect('/data/')

def delData(request, todo_id):
    del_item = Items.objects.get(id=todo_id)
    del_item.delete()
    return HttpResponseRedirect('/data/')

def addOpt(request):
    for key,value in request.POST.items():
        if 'rating' in key:
            ques_data = key.split("-",1)[1]
            new_data = opt(team = key)
            new_data.save()
            new_data = opt(ans = value)
            new_data.save()
            new_data = opt(ques = ques_data)
            new_data.save()

    return render(request, 'test.html')
        
    