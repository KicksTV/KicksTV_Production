from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Gallery

# Create your views here.
class galleryView(generic.ListView):
	template_name = 'gallery/gallery.html'
	context_object_name = 'all_gallery'

	def get_queryset(self):
		return Gallery.objects.all()

class detailView(generic.DetailView):
	model = Gallery
	template_name = 'gallery/detail.html'

class galleryCreate(CreateView):
	model = Gallery
	fields = ['gallery_title', 'gallery_date', 'gallery_image', 'gallery_description']

class galleryUpdate(UpdateView):
	model = Gallery
	fields = ['gallery_title', 'gallery_date', 'gallery_image', 'gallery_description']

class galleryDelete(DeleteView):
	model = Gallery
	success_url = reverse_lazy('gallery')
	items_to_delete = []