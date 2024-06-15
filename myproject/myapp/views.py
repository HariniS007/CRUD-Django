from django.shortcuts import render, get_object_or_404, redirect
from bson import ObjectId
from .forms import PersonForm
from .models import Person

# Read and List all persons
def index(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})

# Create a new person
def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

# Update an existing person
def edit_person(request, pk):
    try:
        person_id = ObjectId(pk)
    except Exception as e:
        # Handle invalid ObjectId format
        return render(request, '404.html', {'error': 'Invalid ID format'})
    
    person = get_object_or_404(Person, _id=person_id)
    
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to your index page or another appropriate view
    else:
        form = PersonForm(instance=person)
    
    return render(request, 'edit_person.html', {'form': form})


# Delete an existing person
def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('index')
    return render(request, 'delete_person.html', {'person': person})
