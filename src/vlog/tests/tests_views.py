from django.test import TestCase, override_settings
from django.test import Client
from vlog import views
from vlog.models import Category, Article, Tag, Comment
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class ViewsTest(TestCase):
    fixtures = ['db.json', ]

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            password='qwerty123'
        )

        self.client.login(
            username='vlog',
            password='vlogvlog'
        )
    @override_settings(DEBUG=True)
    def test_index_view(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.login(
            username='vlog',
            password='vlogvlog'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:index'))
        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertQuerysetEqual(
            context['categories'],
            [
                '<Category: Происшествия>',
                '<Category: Спорт>',
                '<Category: Наука>'
            ]
        )

        self.assertQuerysetEqual(
            context['articles'],
            [
                '<Article: Из-за тату с ошибкой мама сменила>',
                '<Article: Фамилия довела футболиста до красной карточки>',
                '<Article: Британский свиновод потребовал запретить оскорблять'
                ' свиней>',
                '<Article: Китаец целый год бесплатно обедал в ресторане по'
                ' одному авиабилету>',
                '<Article: Пьяная за рулем>',
                '<Article: Посреди поля погиб пастух>',
                '<Article: Как избавиться от жены? Сделать из неё террористку!>'
            ]
        )

        self.assertQuerysetEqual(
            context['tags'],
            [
                '<Tag: Смешное>',
                '<Tag: Фигасе>',
                '<Tag: На заметку>',
                '<Tag: Огого>',
                '<Tag: Мужское>'
            ]
        )

        # response = self.client.get(reverse('vlog:categories'))
        # context = response.context
        # import ipdb
        # ipdb.set_trace()



    @override_settings(DEBUG=True)
    def test_categories_view(self):
        response = self.client.get(reverse('vlog:categories'))
        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertQuerysetEqual(
            context['categories'],
            [
                '<Category: Происшествия>',
                '<Category: Спорт>',
                '<Category: Наука>',
                '<Category: Политика>'
            ]
        )

    @override_settings(DEBUG=True)
    def test_category_view(self):
        response = self.client.get(
            reverse(
                'vlog:category',
                args=['proisshestvija']
            )
        )
        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertQuerysetEqual(
            context['top_2_articles'],
            [
                '<Article: Из-за тату с ошибкой мама сменила>',
                '<Article: Пьяная за рулем>'
            ]
        )

        self.assertQuerysetEqual(
            context['articles'],
            [
                '<Article: Из-за тату с ошибкой мама сменила>',
                '<Article: Пьяная за рулем>',
                '<Article: Китаец целый год бесплатно обедал в ресторане по'
                ' одному авиабилету>',
                '<Article: Как избавиться от жены? Сделать из неё террористку!>',
                '<Article: Посреди поля погиб пастух>'
            ]
        )

    @override_settings(DEBUG=True)
    def test_articles_view(self):
        response = self.client.get(reverse('vlog:articles'))
        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertQuerysetEqual(
            context['articles'],
            [
                '<Article: Из-за тату с ошибкой мама сменила>',
                '<Article: Фамилия довела футболиста до красной карточки>',
                '<Article: Британский свиновод потребовал запретить оскорблять'
                ' свиней>',
                '<Article: Китаец целый год бесплатно обедал в ресторане по'
                ' одному авиабилету>',
                '<Article: Пьяная за рулем>',
                '<Article: Посреди поля погиб пастух>',
                '<Article: Как избавиться от жены? Сделать из неё террористку!>'
            ]
        )

    @override_settings(DEBUG=True)
    def test_article_view(self):
        response = self.client.get(
            reverse(
                'vlog:article',
                args=['iz-za-tatu-с-oshibkoj-mama-smenila']
            )
        )
        self.assertEquals(response.status_code, 200)

    @override_settings(DEBUG=True)
    def test_tags_view(self):
        response = self.client.get(reverse('vlog:tags'))
        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertQuerysetEqual(
            context['tags'],
            [
                '<Tag: Смешное>',
                '<Tag: Фигасе>',
                '<Tag: На заметку>',
                '<Tag: Огого>',
                '<Tag: Мужское>'
            ]
        )

        tags_articles = context['articles_by_tag']
        i = 0
        for ta in tags_articles:
            if ta['tags'] == 4:
                i = i + 1

        self.assertEqual(i, 4)

    @override_settings(DEBUG=True)
    def test_tag_view(self):
        response = self.client.get(reverse('vlog:tag', args=['smeshnoe']))
        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertQuerysetEqual(
            context['articles'],
            [
                '<Article: Из-за тату с ошибкой мама сменила>',
                '<Article: Британский свиновод потребовал запретить оскорблять'
                ' свиней>',
                '<Article: Фамилия довела футболиста до красной карточки>',
                '<Article: Китаец целый год бесплатно обедал в ресторане по'
                ' одному авиабилету>'
            ]
        )
