from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class ParrotCreate(CreateView):
    model = Parrot
    fields = '__all__'

class ParrotUpdate(UpdateView):
    model = Parrot
    fields = ['breed', 'description', 'age']

class ParrotDelete(DeleteView):
    model = Parrot
    success_url = '/parrots'
