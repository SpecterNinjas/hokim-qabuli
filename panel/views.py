import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .forms import *
from .models import Murojatchi


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')

                data = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                result = r.json()
                ''' End reCAPTCHA validation '''

                if result['success']:
                    login(request, user)
                    return redirect('panel:mahalla')
                else:
                    messages.error(request, 'Yaroqsiz reCAPTCHA kiritildi')
                    return redirect('panel:login')
            else:
                messages.error(request, "Sizning akkountingiz bloklangan")
                return redirect('panel:login')
        else:
            messages.error(request, "Noto'g'ri kirish tafsilotlari berildi")
            return redirect('panel:login')

    elif request.method == 'GET':
        return render(request, 'panel/AdminLogin/index.html')


class MainView(LoginRequiredMixin, ListView):
    queryset = Mahalla.objects.all()
    template_name = 'panel/main/index.html'


""" Mahalla Part """


class MahallaView(LoginRequiredMixin, ListView):
    template_name = 'panel/mahalla/index.html'
    context_object_name = 'mahalla_list'
    queryset = Mahalla.objects.all()


class MahallaCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'panel/mahalla/create.html')

    def post(self, request):
        form = MahallaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel:mahalla')
        else:
            return render(request, 'panel/mahalla/create.html', {'form': form})


class MahallaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mahalla
    template_name = "panel/mahalla/update.html"
    context_object_name = 'mahalla'
    form_class = MahallaForm
    success_url = reverse_lazy("panel:mahalla")


class MahallaDeleteView(LoginRequiredMixin, DeleteView):
    model = Mahalla
    success_url = reverse_lazy("panel:mahalla")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


""" End Mahalla Part """

""" Muammo Part """


class MuammoView(LoginRequiredMixin, ListView):
    template_name = 'panel/muammo/index.html'
    context_object_name = 'muammo_list'
    queryset = Muammo.objects.all()
    form = MuammoForm


class MuammoCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'panel/muammo/create.html')

    def post(self, request):
        form = MuammoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel:muammo')
        else:
            return render(request, 'panel/muammo/create.html', {'form': form})


class MuammoUpdateView(LoginRequiredMixin, UpdateView):
    model = Muammo
    template_name = "panel/muammo/update.html"
    context_object_name = 'muammo'
    form_class = MuammoForm
    success_url = reverse_lazy("panel:muammo")


class MuammoDeleteView(LoginRequiredMixin, DeleteView):
    model = Muammo
    success_url = reverse_lazy("panel:muammo")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def ajaxfilter(request):
    if request.is_ajax() and request.method == 'GET':

        muammolar, query, add, json_add = [], [], [], {}

        for key, val in request.GET.items():
            muammolar.append(key[8:-1])
        checked_muammolar = muammolar[:-1]

        for muammo in checked_muammolar:
            query_item = SubMuammo.objects.filter(title__title=muammo)
            add.extend(query_item)

        for muammo in checked_muammolar:
            query_item = SubMuammo.objects.filter(title__title=muammo)
            add.extend(query_item)

        for i in add:
            json_add[str(i)] = Murojatchi.objects.filter(category__category=str(i)).count()

        print(json_add)
        data = {
            'query': json_add
        }

    else:
        data = {
            'query': []
        }

    return JsonResponse(data, safe=False)


""" End Muammo Part """

""" Murojatchi Part """


class MurojatchiView(LoginRequiredMixin, ListView):
    template_name = 'panel/murojatchi/index.html'
    context_object_name = 'murojatchi_list'
    queryset = Murojatchi.objects.all()


class MurojatchiUpdateView(LoginRequiredMixin, UpdateView):
    model = Murojatchi
    template_name = "panel/murojatchi/update.html"
    context_object_name = 'murojatchi'
    form_class = MurojatchiForm
    success_url = reverse_lazy("panel:murojatchi")

    def get_context_data(self, **kwargs):
        mahallalar = Mahalla.objects.all()
        muammolar = Muammo.objects.all()
        kategoriyalar = SubMuammo.objects.all()
        context = super(MurojatchiUpdateView, self).get_context_data(**kwargs)
        context['mahallalar'] = mahallalar
        context['muammolar'] = muammolar
        context['kategoriyalar'] = kategoriyalar
        return context


class MurojatchiDeleteView(LoginRequiredMixin, DeleteView):
    model = Murojatchi
    success_url = reverse_lazy("panel:murojatchi")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


""" End Murojatchi Part """


class KategoriyaView(LoginRequiredMixin, ListView):
    template_name = 'panel/kategoriya/index.html'
    context_object_name = 'kategoriya_list'
    queryset = SubMuammo.objects.all()


class KategoriyaCreateView(LoginRequiredMixin, CreateView):
    model = SubMuammo
    template_name = 'panel/kategoriya/create.html'
    form_class = KategoriyaForm
    context_object_name = 'kategoriya'
    success_url = reverse_lazy('panel:kategoriya')

    def get_context_data(self, **kwargs):
        muammolar = Muammo.objects.all()
        context = super(KategoriyaCreateView, self).get_context_data(**kwargs)
        context['muammolar'] = muammolar
        return context


class KategoriyaUpdateView(LoginRequiredMixin, UpdateView):
    model = SubMuammo
    template_name = "panel/kategoriya/update.html"
    context_object_name = 'kategoriya'
    form_class = KategoriyaForm
    success_url = reverse_lazy("panel:kategoriya")


class KategoriyaDeleteView(LoginRequiredMixin, DeleteView):
    model = SubMuammo
    success_url = reverse_lazy("panel:kategoriya")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class QabulView(LoginRequiredMixin, ListView):
    template_name = 'panel/qabul/index.html'
    context_object_name = 'mahallalar'
    queryset = Mahalla.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QabulView, self).get_context_data(**kwargs)
        context['muammolar'] = Muammo.objects.all()
        context['kategoriyalar'] = SubMuammo.objects.all()
        context['murojatchilar'] = Murojatchi.objects.all()

        return context


def ajax_mahalla(request):
    if request.is_ajax() and request.method == 'GET':

        mahallar, query, add, json_add = [], [], [], {}

        for key, val in request.GET.items():
            mahallar.append(key[8:-1])
        checked_mahallar = mahallar[:-1]

        for mahalla in checked_mahallar:
            query_item = Murojatchi.objects.filter(mahalla__title=mahalla)
            add.extend(query_item)

        json_add = serializers.serialize("json", add, fields=['fullname', 'phone', 'created'])

        data = {
            'query': json_add
        }

    else:
        data = {
            'query': []
        }

    return JsonResponse(data, safe=False)


def murojatchi_filter(request):
    pass
