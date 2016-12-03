import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page
import django.utils.timezone as timezone

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


def add_page(cat, title, url, views=0, last_visit=timezone.now(), first_visit= timezone.now()):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.last_visit = last_visit
    p.first_visit = first_visit
    p.save()
    return p
def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 20},
        {"title": "How to think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 23},
        {"title": "Learn python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorial/python/",
         "views": 56}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "http://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 0},
        {"title": "Django Rocks",
         "url": "http:/www.djangorocks.com/",
         "views": 31},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 32}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 33},
        {"title": "Flask",
         "url": "http://flask.pocoo.org/",
         "views": 34}]

    cats = {"Python": {"pages": python_pages, "likes":64, "views":128},
            "Django":{"pages": django_pages, "likes":32, "views":64},
            "Other Frameworks": {"pages": other_pages,"likes":16, "views":32} }

    for cat, cat_data in cats.items():
        c = add_cat(cat, views = cat_data["views"], likes= cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], views = p["views"])
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()



