from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Author, Blog

# Create your tests here.
class BlogPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/secondapp/about/')
        self.assertEqual(response.status_code, 200)

    # def test_url_exists_at_correct_name(self):
    #     response = self.client.get(reverse('about'))
    #     self.assertEqual(response.status_code, 200)

    # def test_correct_template_used(self):
    #     respose = self.client.get(reverse('about'))
    #     self.assertTemplateUsed(respose, 'sec_app/about.html')

    # def test_template_content_is_correct(self):
    #     response = self.client.get(reverse('about'))
    #     self.assertContains(response, 'information about the website.')

    def test_blog_page_tests(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sec_app/about.html')
        self.assertContains(response, 'information about the website.')

class AuthorTestPage(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author1 = Author.objects.create(name = "Test Author1",
                                           genre = "Fiction",
                                           email = "tester@gmail.com")
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/secondapp/author_detail/')
        self.assertEqual(response.status_code, 200)
    def test_url_exists_at_correct_name(self):
        response = self.client.get(reverse('author_detail'))
        self.assertEqual(response.status_code, 200)
    def test_correct_template_used(self):
        respose = self.client.get(reverse('author_detail'))
        self.assertTemplateUsed(respose, 'sec_app/author.html')
    def test_template_content_is_correct(self):
        response = self.client.get(reverse('author_detail'))
        self.assertContains(response, 'Test Author1')

class HomePageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name = "Test Author2",
                                           genre = "Fiction",
                                           email = "tester@gmail.com")
        cls.blog1 = Blog.objects.create(title = "Blog Post One",
                                        author = HomePageTest.author,
                                        blog_text = "This is the first blog")
        cls.blog2 = Blog.objects.create(title = "Blog Post Two",
                                        author = HomePageTest.author,
                                        blog_text = "second blog")
    def test_home_by_url(self):
        response = self.client.get('/secondapp/')
        self.assertEqual(response.status_code, 200)
    # def test_author_page_in_home_page(self):
    #     response = self.client.get(reverse('author_detail'))
    #     self.assertContains(response, 'Test Author1')
    def test_blog_page_tests(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sec_app/home.html')
        self.assertContains(response, 'Test Author2')
        self.assertContains(response, 'Blog Post One')
        self.assertContains(response, 'Blog Post Two')
    def test_blog_detail_view(self):
        response = self.client.get(reverse('detailed_blog', kwargs={'pk':self.blog1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sec_app/detailed_blog.html')
        self.assertContains(response, 'Test Author2')
        self.assertContains(response, 'Blog Post One')
    def test_author_blog_page(self):
        response = self.client.get(reverse('author_blog', kwargs={'id': self.author.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sec_app/author_blog.html')
        self.assertContains(response, 'Test Author2')
        self.assertContains(response, 'tester@gmail.com')
        self.assertContains(response, 'Blog Post One')
        self.assertContains(response, 'Blog Post Two')

        