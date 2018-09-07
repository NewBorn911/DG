from django.shortcuts import render, redirect
from django.db.models import Count, F, Value, FloatField
from django.db.models.functions import Cast
from django.views import View
from .models import TruckModel, Truck


def index(request):
    m = request.GET.get("ml", "")
    print(m)
    # traks = Truck.objects.all().annotate(percent=(Cast(F('loaded'), FloatField()) / Cast(F('model__tonnage'), FloatField())) * 100)
    models = TruckModel.objects.all()
    traks = Truck.objects.all()
    if m != "":
        traks = traks.filter(model__name=m)

    traks = traks.annotate(percent=(Cast(F('loaded'), FloatField()) / Cast(F('model__tonnage'), FloatField())) * 100)
    context = {
        "traks": traks,
        "models": models
    }

    return render(request, 'index.html', context)


class Models(View):
    def get(self, request):
        models = TruckModel.objects.all()
        return render(request, 'models.html', {"models": models})

    def post(self, request):
        name = request.POST['name']
        tonnage = request.POST['tonnage']
        print(name, tonnage)
        TruckModel(name=name, tonnage=tonnage).save()
        return redirect('models')

class Trucks(View):
    def get(self, request):
        trucks = Truck.objects.all()
        models = TruckModel.objects.all()
        return render(request, 'truck.html', {"models": models, "trucks": trucks})

    def post(self, request):
        number = request.POST['number']
        model_id = request.POST['model_id']
        loaded = request.POST['loaded']

        Truck(number=number, loaded=loaded, model=TruckModel.objects.get(pk=model_id)).save()
        return redirect('trucks')
