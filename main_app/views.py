from django.shortcuts import render

# parrots = [
#     {'name': 'Minnie', 'breed': 'Cockatoo', 'description': 'All white with a yellow feather on top', 'age': 7},
#     {'name': 'Paulie', 'breed': 'Macaw', 'description': 'Mainly red with blue feathers', 'age': 5},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def parrots_index(request):
    return render(request, 'parrots/index.html', {
        'parrots': parrots
    })