from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from cotizantes.models import Cotizantes
from user.models import Avatar

class CotizantesListView(ListView):
    model = Cotizantes
    template_name = "cotizantes_list.html"

class CotizantesDetailView(DetailView):
    model = Cotizantes
    template_name = "cotizantes_detail.html"
    fields = ['ente', 'periodo', 'ficha','nombre', 'dni', 'cuil','repa', 'loca', 'importe', 'detalle', 'afiliado']

class CotizantesDetailView1(DetailView):
    model = Cotizantes
    template_name = "cotizantes_detail1.html"
    fields = ['ente', 'periodo', 'ficha','nombre', 'dni', 'cuil','repa', 'loca', 'importe', 'detalle', 'afiliado']

class CotizantesCreateView(LoginRequiredMixin, CreateView):
    model = Cotizantes
    template_name = "cotizantes_add.html"
    success_url = reverse_lazy('cotizantes:cotizantes-list')
    fields = ['ente', 'periodo', 'ficha','nombre', 'dni', 'cuil','repa', 'loca', 'importe', 'detalle', 'afiliado']


class CotizantesUpdateView(LoginRequiredMixin, UpdateView):
    model = Cotizantes
    template_name = "cotizantes_form.html"
    success_url = reverse_lazy('cotizantes:cotizantes-list')
    fields = ['ente', 'periodo', 'ficha','nombre', 'dni', 'cuil','repa', 'loca', 'importe', 'detalle', 'afiliado']


class CotizantesDeleteView(LoginRequiredMixin, DeleteView):
    model = Cotizantes
    template_name = "cotizantes_confirm_delete.html"
    success_url = reverse_lazy('cotizantes:cotizantes-list')