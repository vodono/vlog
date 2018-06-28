from django.contrib.auth import get_user_model
from django.test import TestCase
from vlog import models
from vlog import forms
import datetime

class ModelsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user', password='qwerty123'
        )
        self.test_time = datetime.datetime.now()

        self.cat = models.Category.objects.create(
            title='Спорт',
            description='Все о спорте.',
            author=self.user,
        )
        self.cat.slug = forms.transliterate(self.cat.title)
        self.cat.save()

        self.art = models.Article.objects.create(
            title='Статья',
            description='Описание статьи',
            content='Содержание',
            author=self.user,
            category=self.cat
        )
        self.art.slug = forms.transliterate(self.art.title)
        self.art.save()

        self.tag = models.Tag.objects.create(
            title='Тег',
        )
        self.tag.slug = forms.transliterate(self.tag.title)
        self.tag.save()

        self.tag.articles.add(self.art)
        self.tag.save()
        self.art.tags.add(self.tag)
        self.art.save()

        self.com = models.Comment.objects.create(
            text='Текст',
            author=self.user,
            article=self.art
        )

    def test_category(self):
        category = models.Category.objects.get(title="Спорт")
        self.assertEqual(category.description, 'Все о спорте.')
        self.assertEqual(category.title, 'Спорт')
        self.assertEqual(category.slug, 'sport')
        self.assertEqual(str(category), 'Спорт')
        # self.assertEqual(category.created, self.test_time)

    def test_article(self):
        article = models.Article.objects.get(title='Статья')
        self.assertEqual(article.description, 'Описание статьи')
        self.assertEqual(article.title, 'Статья')
        self.assertEqual(article.content, 'Содержание')
        self.assertEqual(article.category.title, 'Спорт')
        self.assertEqual(
            article.tags.get(title='Тег').title,
            'Тег'
        )
        # self.assertEqual(self.art.created, self.test_time)

    def test_tag(self):
        tag = models.Tag.objects.get(title='Тег')
        self.assertEqual(tag.title, 'Тег')
        # self.assertEqual(self.tag.created, self.test_time)
        self.assertEqual(
            tag.articles.get(title='Статья').title,
            'Статья'
        )

    def test_comment(self):
        comment = models.Comment.objects.get(text='Текст')
        self.assertEqual(comment.text, 'Текст')
        self.assertEqual(comment.article.title, 'Статья')
        self.assertEqual(str(comment), 'user [Статья]')
