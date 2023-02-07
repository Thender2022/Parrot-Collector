from django.shortcuts import render
from .models import Parrot

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def parrots_index(request):
    parrots = Parrot.objects.all()
    return render(request, 'parrots/index.html', {
        'parrots': parrots
    })

def parrots_detail(request, parrot_id):
    parrot = Parrot.objects.get(id=parrot_id)
    return render(request, 'parrots/detail.html', { 'parrot': parrot })
