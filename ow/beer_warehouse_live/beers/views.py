from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import UpdateView

from beers.mixins import AddMyBirthdayToContextMixin

from .forms import CompanyForm, CompanyFormOld
from .models import Beer, Company


class BeerListView(ListView):
    model = Beer


class BeerDetailView(DetailView):
    model = Beer


class CompanyDetailView(DetailView):
    model = Company


class CompanyListView(ListView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')

class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form,
    }
    return render(request, 'company/company_form.html', context)


def company_edit_old(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyFormOld(request.POST)
        if form.is_valid():
            company.name = form.cleaned_data['name']
            company.tax_number = form.cleaned_data['tax_number']
            company.save()
    else:
        form = CompanyForm(initial={
            'name': company.name,
            'tax_number': company.tax_number,
        })

    context = {
        'form': form,
    }
    return render(request, 'company/company_form.html', context)


# def beer_list_view(request):
#     beer_list = Beer.objects.all()
# beer_list_counter = Beer.objects.count()
# print(beer_list_counter)
# print ("exist?", beer_list.filter(id=1).exists())

# Crear objetos
# company = Company.objects.create(name="co", tax_number="4")
# Beer.objects.create(name="broma", company=company)

# print(beer_list.order_by('name'))
# Filtrar por compañia
# company = Company.objects.get(id=1)
# print(beer_list.filter(company=company))
# # Filtrar por comañía y por abv
# print(beer_list.filter(company__name__startswith="com", abv__gte=5))
# # Filtrar por comañía o por abv
# print(beer_list.filter(Q(company__name__startswith="com") | Q(abv__gte=5)))

# Borrar objetos
# print(Beer.objects.filter(pk=4).first().delete())

# Que cervezas tiene una compañia
# print(company.beers.all())
# for beer in company.beers.all():
#     print(beer)
#     if "Cruzcampo" in beer.name:
#         beer.abv = 4.81
#         beer.save()

# Añadir un specialIngredients a una cerveza
# sp = SpecialIngredients(name="romero")
# sp.save()
# beer = Beer.objects.filter(pk__in=[1,3]).first()
# sp = SpecialIngredients.objects.get(pk=1)
# beer.special_ingredients.add(sp)

# print(beer.special_ingredients.all())

# context = {
#     'beer_list': beer_list
# }

# return render(request, 'beer_list.html', context)


# @login_required
# def beer_list_view(request):
#     if request.method == 'GET':
#         return render(request, 'beer_list.html', {
#             'beer_list': Beer.objects.all()
#         })


# class BeerListView(LoginRequiredMixin, View):
#     def get(self, request):
#         return render(request, 'beer_list.html', {
#             'beer_list': Beer.objects.all()
#         })


# def beer_detail_view(request, pk):
#     print("user", request.user)
#     print("GET", request.GET)
#     print("is_ajax", request.is_ajax)
#     context = {
#         'beer': Beer.objects.get(pk=pk)
#     }

#     return render(request, 'beer_detail.html', context)

# class BeerListViewAlt(AddMyBirthdayToContextMixin, ListView):
#     model = Beer

#     # def get_queryset(self):
#     #     qs = super().get_queryset()
#     #     return qs.filter(pk=3)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["company"] = context['beer_list'].first().company
#         print(context)
#         return context
