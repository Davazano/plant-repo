from django.shortcuts import render, get_object_or_404
from .models import Plant, PlantImage

def index(request):
    plants = Plant.objects.filter(is_visible = True)
    return render(request, 'library/index.html', {
        'plants': plants
    })

def index2(request):
    plants = Plant.objects.filter(is_visible = True)
    return render(request, 'library/index2.html', {
        'plants': plants
    })

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, pk = plant_id)
    plant_images = PlantImage.objects.filter(plant = plant)
    return render(request, 'library/detail.html', {'plant': plant, 'plant_images': plant_images})