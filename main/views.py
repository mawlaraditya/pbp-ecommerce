from django.shortcuts import render
from django.http import HttpResponse
from .models import Hat
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import AddNewHatForm
from main.models import Hat
from django.http import HttpResponse
from django.core import serializers


def home (request) :
    hat = Hat.objects.all()
    return render(request, 'home.html', {'hat' : hat})


def add_new_hat(request):
    form = AddNewHatForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:home')

    context = {'form': form}
    return render(request, "add_new_hat.html", context)


# def show_xml(request):
#     data = Hat.objects.all()


# def show_xml(request):
#     data = Hat.objects.all()
#     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


# def show_json(request):
#     data = Hat.objects.all()
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# def show_xml_by_id (request, id):
#     data = Hat.objects.filter(pk=id)
#     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# def show_json_by_id(request, id):
#     data = Hat.objects.filter(pk=id)
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json")

