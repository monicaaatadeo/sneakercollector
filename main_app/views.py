from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Sneaker, Box
from .forms import SneakerForm, WearingForm


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

	wearing_form = WearingForm()
	context = {
	'sneaker': sneaker,
	'wearing_form': wearing_form,
	'boxes': boxes_sneaker_doesnt_have
	}
	return render(request, 'sneakers/detail.html', context)

def add_wearing(request, sneaker_id):
	form = WearingForm(request.POST)
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


