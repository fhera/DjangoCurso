from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy

from beers.models import Beer, Company

# Create your tests here.


# class CompanyListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         """Se ejecuta al comienzo de la ejecución del test
#         """
#         Company.objects.create(name="comp1", tax_number=1)
#         Company.objects.create(name="comp2", tax_number=2)
#         Company.objects.create(name="comp3", tax_number=3)
#         User.objects.create(username='pepe')

#     def test_view_url_exists(self):
#         url = "/beers/company/list/"
#         self.client.force_login(User.objects.first())
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)

#     def test_views_return_all_entries(self):
#         url = "/beers/company/list/"
#         self.client.force_login(User.objects.first())
#         resp = self.client.get(url)

#         self.assertEqual(resp.context['object_list'].count(), 3)

#     def test_views_template(self):
#         self.client.force_login(User.objects.first())
#         resp = self.client.get(reverse('company-list-view'))

#         self.assertTemplateUsed(resp, 'beers/company_list.html')

#     def test_login(self):
#         resp = self.client.get(reverse('company-list-view'))

#         self.assertEqual(resp.status_code, 302)


class CompanyListViewMommyTest(TestCase):
    def setUp(self):
        self.companies = mommy.make(Company, _quantity=12)
        self. user = mommy.make(User)

    def test_view_url_exists(self):
        url = "/beers/company/list/"
        self.client.force_login(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_views_return_all_entries(self):
        url = "/beers/company/list/"
        self.client.force_login(self.user)
        resp = self.client.get(url)

        self.assertEqual(
            resp.context['object_list'].count(),
            Company.objects.all().count()
        )

    def test_views_template(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('company-list-view'))

        self.assertTemplateUsed(resp, 'beers/company_list.html')

    def test_login(self):
        resp = self.client.get(reverse('company-list-view'))

        self.assertEqual(resp.status_code, 302)
