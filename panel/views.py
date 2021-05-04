from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from .forms import *
from .models import *


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
    paginate_by = 10


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


class HududView(LoginRequiredMixin, ListView):
    template_name = 'panel/hudud/index.html'
    context_object_name = 'hudud_list'
    queryset = Hudud.objects.all()
    form = HududForm
    paginate_by = 10


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


class HududCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'panel/hudud/create.html')

    def post(self, request):
        form = HududForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel:hudud')
        else:
            return render(request, 'panel/hudud/create.html', {'form': form})


class MuammoUpdateView(LoginRequiredMixin, UpdateView):
    model = Muammo
    template_name = "panel/muammo/update.html"
    context_object_name = 'muammo'
    form_class = MuammoForm
    success_url = reverse_lazy("panel:muammo")


class HududUpdateView(LoginRequiredMixin, UpdateView):
    model = Hudud
    template_name = "panel/hudud/update.html"
    context_object_name = 'hudud'
    form_class = HududForm
    success_url = reverse_lazy("panel:hudud")


class MuammoDeleteView(LoginRequiredMixin, DeleteView):
    model = Muammo
    success_url = reverse_lazy("panel:muammo")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class HududDeleteView(LoginRequiredMixin, DeleteView):
    model = Hudud
    success_url = reverse_lazy("panel:hudud")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


""" End Muammo Part """

""" Murojatchi Part """


class MurojatchiView(LoginRequiredMixin, ListView):
    template_name = 'panel/murojatchi/index.html'
    context_object_name = 'murojatchi_list'
    queryset = Murojatchi.objects.all()
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(MurojatchiView, self).get_context_data(**kwargs)
        context['mahallalar'] = Mahalla.objects.all()
        context['muammolar'] = Muammo.objects.all()
        context['hududlar'] = Hudud.objects.all()

        return context


class MurojatchiSearchView(LoginRequiredMixin, ListView):
    template_name = 'panel/murojatchi/search.html'
    model = Murojatchi

    def get_queryset(self):
        queryset = Murojatchi.objects.all()
        if self.request.GET.get('fullname') != '':
            fullname = self.request.GET.get('fullname')
            queryset = self.model.objects.filter(fullname__icontains=fullname)
        if self.request.GET.get('phone') != '':
            phone = self.request.GET.get('phone')
            queryset &= self.model.objects.filter(phone__icontains=phone)
        if self.request.GET.get('mahalla') != '':
            mahalla = self.request.GET.get('mahalla')
            queryset &= self.model.objects.filter(mahalla_id=mahalla)
        if self.request.GET.get('murojat_turi') != '':
            murojat_turi = self.request.GET.get('murojat_turi')
            queryset &= self.model.objects.filter(murojat_turi=murojat_turi)
        if self.request.GET.get('hudud') != '':
            hudud = self.request.GET.get('hudud')
            queryset &= self.model.objects.filter(hudud_id=hudud)
        if self.request.GET.get('muammo') != '':
            muammo = self.request.GET.get('muammo')
            queryset &= self.model.objects.filter(muammo_id=muammo)
        if self.request.GET.get('status') != '':
            status = self.request.GET.get('status')
            queryset &= self.model.objects.filter(status=status)
        return queryset


class MurojatchiDetailView(DetailView):
    model = Murojatchi
    context_object_name = 'murojatchi'
    queryset = Murojatchi.objects.all()
    template_name = 'panel/murojatchi/see.html'


class StatisticsView(LoginRequiredMixin, ListView):
    queryset = Murojatchi.objects.all()
    template_name = 'panel/statistics/statistics.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data(**kwargs)
        context['muammolar'] = Muammo.objects.all()
        context['a'] = Murojatchi.objects.all()
        return context


class FoydalanuvchiDetailView(LoginRequiredMixin, DetailView):
    model = Murojatchi
    context_object_name = 'murojatchi'
    queryset = Murojatchi.objects.all()
    template_name = 'panel/foydalanuvchi/see.html'

    def get_context_data(self, **kwargs):
        context = super(FoydalanuvchiDetailView, self).get_context_data(**kwargs)
        context['hududlar'] = Hudud.objects.all()
        context['mahallalar'] = Mahalla.objects.all()
        context['murojatlar'] = Murojatchi.objects.all()
        return context


class FoydalanuvchiSearchView(LoginRequiredMixin, ListView):
    template_name = 'panel/foydalanuvchi/search.html'
    model = Murojatchi

    def get_queryset(self):
        queryset = Murojatchi.objects.all()
        if self.request.GET.get('telegram_id') != '':
            telegram_id = self.request.GET.get('telegram_id')
            queryset = self.model.objects.filter(telegram_id__icontains=telegram_id)
        if self.request.GET.get('fullname') != '':
            fullname = self.request.GET.get('fullname')
            queryset &= self.model.objects.filter(fullname__icontains=fullname)
        if self.request.GET.get('username') != '':
            username = self.request.GET.get('username')
            queryset &= self.model.objects.filter(username__icontains=username)
        return queryset


# class MurojatchiUpdateView(LoginRequiredMixin, UpdateView):
#     model = Murojatchi
#     template_name = "panel/murojatchi/update.html"
#     context_object_name = 'murojatchi'
#     form_class = MurojatchiForm
#     success_url = reverse_lazy("panel:murojatchi")


class MurojatchiReplyMessageView(LoginRequiredMixin, UpdateView):
    model = Murojatchi
    template_name = "panel/murojatchi/reply.html"
    context_object_name = 'murojatchi'
    form_class = MurojatchiReplyMessageForm
    success_url = reverse_lazy("panel:murojatchi")



class MurojatchiDeleteView(LoginRequiredMixin, DeleteView):
    model = Murojatchi
    success_url = reverse_lazy("panel:murojatchi")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AcceptedDetailView(LoginRequiredMixin, DetailView):
    model = Reception
    context_object_name = 'reception'
    queryset = Reception.objects.all()
    template_name = 'panel/accepted_applicants/see.html'


class KategoriyaView(LoginRequiredMixin, ListView):
    template_name = 'panel/kategoriya/index.html'
    context_object_name = 'kategoriya_list'
    queryset = SubMuammo.objects.all()
    paginate_by = 10


class FoydalanuvchiView(LoginRequiredMixin, ListView):
    template_name = 'panel/foydalanuvchi/index.html'
    context_object_name = 'foydalanuvchi_list'
    queryset = Murojatchi.objects.all()
    paginate_by = 15


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


class FoydalanuvchiUpdateView(LoginRequiredMixin, UpdateView):
    model = Murojatchi
    template_name = "panel/foydalanuvchi/update.html"
    context_object_name = 'murojatchi'
    form_class = FoydalanuvchiForm
    success_url = reverse_lazy("panel:foydalanuvchi")


class AcceptedUpdateView(LoginRequiredMixin, UpdateView):
    model = Reception
    template_name = "panel/accepted_applicants/update.html"
    context_object_name = 'reception'
    form_class = ReceptionForm
    success_url = reverse_lazy("panel:accepted")

    def get_context_data(self, **kwargs):
        context = super(AcceptedUpdateView, self).get_context_data(**kwargs)
        context['mahallalar'] = Mahalla.objects.all()
        context['muammolar'] = Muammo.objects.all()
        context['kategoriyalar'] = SubMuammo.objects.all()
        return context




class QabulView(LoginRequiredMixin, ListView):
    template_name = 'panel/qabul/index.html'
    context_object_name = 'object_list'
    form_class = MurojatchiForm
    model = Murojatchi
    queryset = Mahalla.objects.all()

    @csrf_exempt
    def get_context_data(self, **kwargs):
        context = super(QabulView, self).get_context_data(**kwargs)
        context['muammolar'] = Muammo.objects.all()
        context['mahallalar'] = Mahalla.objects.all()
        context['kategoriyalar'] = SubMuammo.objects.all()
        context['murojatchilar'] = Murojatchi.objects.all()
        return context

    def post(self, request):
        form1 = ReceptionForm(request.POST)

        if form1.is_valid():

            form1.save()

            return redirect('panel:accepted')
        else:

            return render(request, 'panel/qabul/index.html', {'form1': form1})


@csrf_exempt
def ajax_mahalla(request):
    if request.is_ajax() and request.method == 'GET':

        mahallar, query, add, add2, json_add = [], [], [], [], {}

        for key, val in request.GET.items():
            mahallar.append(key[8:-1])
        checked_mahallar = mahallar[:-1]

        for mahalla in checked_mahallar:
            query_item = Murojatchi.objects.filter(mahalla__title=mahalla)
            add.extend(query_item)

        muammo = Muammo.objects.all()

        json_add = serializers.serialize("json", add,

                                         use_natural_foreign_keys=True, use_natural_primary_keys=True)
        json_add2 = serializers.serialize("json", muammo, fields=['pk', 'title'])

        data = {
            'query': json_add,
            'query2': json_add2
        }

    else:
        data = {
            'query': [],
            'query2': []
        }

    return JsonResponse(data, safe=False)


@csrf_exempt
def ajaxfilter(request):
    if request.is_ajax() and request.method == 'GET':

        muammolar, query, add, queryset_users, json_add = [], [], [], [], {}

        for key, val in request.GET.items():
            muammolar.append(key[8:-1])
        checked_muammolar = muammolar[:-1]

        for muammo in checked_muammolar:
            query_item = SubMuammo.objects.filter(title__title=muammo)
            if Murojatchi.objects.filter(muammo__title__in=checked_muammolar):
                query_users = Murojatchi.objects.filter(
                    Q(muammo__title=muammo) & Q(mahalla__title__in=checked_muammolar))
            else:
                query_users = Murojatchi.objects.filter(mahalla__title__in=checked_muammolar)

            add.extend(query_item)
            queryset_users.extend(query_users)

            queryset_users = list(set(queryset_users))

        for i in add:
            user_count = Murojatchi.objects.filter(
                Q(category__category=str(i)) & Q(mahalla__title__in=checked_muammolar)).count()
            if user_count:
                json_add[str(i)] = user_count

        json_users = serializers.serialize("json", queryset_users, fields=['fullname', 'telegram_id', 'created', ])

        data = {
            'query': json_add,
            'users': json_users
        }

    else:
        data = {
            'query': []
        }

    return JsonResponse(data, safe=False)


@csrf_exempt
def ajax_filter_category(request):
    if request.is_ajax() and request.method == 'GET':

        categories, query, add, json_add = [], [], [], {}

        for key, val in request.GET.items():
            categories.append(key[8:-1])
        checked_categories = categories[:-1]

        if not Murojatchi.objects.filter(category__category__in=checked_categories):

            if Murojatchi.objects.filter(muammo__title__in=checked_categories):
                for category in checked_categories:
                    query_item = Murojatchi.objects.filter(
                        Q(muammo__title=category) & Q(mahalla__title__in=checked_categories))
                    add.extend(query_item)

        for category in checked_categories:
            query_item = Murojatchi.objects.filter(
                Q(category__category=category) & Q(mahalla__title__in=checked_categories))
            add.extend(query_item)

        json_add = serializers.serialize("json", add,
                                         use_natural_foreign_keys=True, use_natural_primary_keys=True)
        data = {
            'query': json_add,

        }

    else:
        data = {
            'query': [],
        }

    return JsonResponse(data, safe=False)


class AcceptedView(LoginRequiredMixin, ListView):
    template_name = 'panel/accepted_applicants/index.html'
    context_object_name = 'accepted_list'
    queryset = Reception.objects.all().order_by('-created')
    paginate_by = 15

    # def get_context_data(self, **kwargs):
    #     context = super(AcceptedView, self).get_context_data(**kwargs)
    #     context['mahallalar'] = Mahalla.objects.all()
    #     context['muammolar'] = Muammo.objects.all()
    #     context['hududlar'] = Hudud.objects.all()
    #
    #     return context


class AcceptedSearchView(LoginRequiredMixin, ListView):
    template_name = 'panel/accepted_applicants/search.html'
    model = Reception

    def get_queryset(self):
        queryset = Reception.objects.all()
        if self.request.GET.get('title') != '':
            title = self.request.GET.get('title')
            queryset = self.model.objects.filter(title__icontains=title)
        if self.request.GET.get('appointment') != '':
            appointment = self.request.GET.get('appointment')
            queryset &= self.model.objects.filter(appointment=appointment)
        if self.request.GET.get('status') != '':
            status = self.request.GET.get('status')
            queryset &= self.model.objects.filter(status=status)
        return queryset


def murojatchi_filter(request):
    pass



