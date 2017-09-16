from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.galleryView.as_view(), name='gallery'),
	url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name="detail"),
	url(r'gallery/add/$', views.galleryCreate.as_view(), name="gallery-add"),
	url(r'gallery/(?P<pk>[0-9]+)/$', views.galleryUpdate.as_view(), name="gallery-update"),
	url(r'gallery/(?P<pk>[0-9]+)/delete/$', views.galleryDelete.as_view(), name="gallery-delete"),
	]