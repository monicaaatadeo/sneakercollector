from django.shortcuts import render, redirect

 # Class-Based Views 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Interaction with Sneaker & Box Models
from .models import Sneaker, Box
from .forms import SneakerForm, WearingForm



# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def sneakers_index(request):
	sneakers = Sneaker.objects.all()
	return render(request, 'sneakers/index.html', {'sneakers': sneakers})

def sneakers_detail(request, sneaker_id):
	sneaker = Sneaker.objects.get(id = sneaker_id)
	boxes_sneaker_doesnt_have = Box.objects.exclude(id__in = sneaker.boxes.all().values_list('id'))

	# create an instance from WearingForm
	wearing_form = WearingForm()
	# create dictionalty to send to template
	context = {
	'sneaker': sneaker,
	'wearing_form': wearing_form,
	'boxes': boxes_sneaker_doesnt_have
	}
	return render(request, 'sneakers/detail.html', context)

def add_wearing(request, sneaker_id):
	# create instance of model using ModelForm and POST data
	form = WearingForm(request.POST)
	# validate form 
	if form.is_valid():

		new_wearing = form.save(commit=False)
		new_wearing.sneaker_id = sneaker_id
		new_wearing.save()

	return redirect('detail', sneaker_id = sneaker_id)


def assoc_box(request, sneaker_id, box_id):
	Sneaker.objects.get(id=sneaker_id).boxes.add(box_id)
	return redirect ('detail', sneaker_id = sneaker_id)


def new_sneaker(request):

	if request.method == 'POST':

		form = SneakerForm(request.POST)
		if form.is_valid():

			sneaker = form.save()
			print(sneaker.id)
			return redirect('detail', sneaker.id)
	else:
		form = SneakerForm()
	context = {'form': form}

	return render(request, 'sneakers/sneaker_form.html', context)


def sneakers_update(request,sneaker_id):
	sneaker = Sneaker.objects.get(id=sneaker_id)

	if request.method == 'POST':
		form = SneakerForm(request.POST, instance=sneaker)
		if form.is_valid():
			sneaker=form.save()
			return redirect('detail', sneaker.id)

	else:
		form = SneakerForm(instance=sneaker)
		return render(request, 'sneakers/sneaker_form.html', {'form': form})

def sneakers_delete(request, sneaker_id):
	Sneaker.objects.get(id=sneaker_id).delete()

	return redirect('index')



# CLASS-BASED VIEWS for BOX MODEL

class BoxList(ListView):
	model = Box

class BoxDetail(DetailView):
	model = Box

class BoxCreate(CreateView):
	model = Box
	fields = '__all__'

class BoxUpdate(UpdateView):
	model = Box
	fields = ['color']

class BoxDelete(DeleteView):
	model = Box

	success_url = '/boxes/'
































	