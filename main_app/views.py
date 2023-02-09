from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Parrot
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'parrots/detail.html', {
        'parrot': parrot, 'feeding_form': feeding_form
    })

def add_feeding(request, parrot_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.parrot_id = parrot_id
        new_feeding.save()
    return redirect('detail', parrot_id=parrot_id)

    

class ParrotCreate(CreateView):
    model = Parrot
    fields = '__all__'

class ParrotUpdate(UpdateView):
    model = Parrot
    fields = ['breed', 'description', 'age']

class ParrotDelete(DeleteView):
    model = Parrot
    success_url = '/parrots'
