
from django.test import TestCase
from django.urls import reverse

from rango.models import Category

def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


class CategoryMethodTests(TestCase):
    def test_ensure_views_are__positive(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()

        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):
        cat = Category(name='Random CAtegory String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')


class IndexViewTest(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['categories'], [])
        self.assertContains(response, "There are no categories present.")

    def test_index_view_with_categories(self):
        for i in ('test', 'ttest', 'temp', 'endtest'):
            add_cat(i, 1, 1)

        response =self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "endtest")

        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)
