# Vivek Kumar Yadav, Django notes
# Citation: freeCodeCamp.org

#_________________________________________Terminal commands_________________________________________________
'''

Product.objects.create() -> creates new objects
Product.objects.all() -> prints all existing objects
python manage.py createsuperuser -> to create account
python manage.py startapp pages -> creates a new app called "pages" which is added in to settings' "INSTALLED_APPS"
from products.models import Product -> to import Product objects/class from models.py of products folder/app
Product.objects.get(id=1) -> to get object with id=1(assigned automatically by django)
dir(object) -> to get all the directory info of the object

'''
#______________________________Project 0_____________________________________________________________________
# creates new objects from command line
 Product.objects.create(title='New product 2', description='another one', price = '19312'
, summary = 'sweet')

# Prints all existing objects
Product.objects.all()

# models.py
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool!')

# _____________________________________New Model Fields_______________________________________________________________
# models.py
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    #price = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()

#________________________________________Change a Model________________________________________________________________
#python manage.py createsuperuser -- to create account
#models.py
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    #price = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False) #blank: for fields (required or not required), null: for database (active or inactive)
    #blank: (True: can leave blank and isn't strictly required, False: cannot leave blank and is required)
    #null= (True: active means can be left null so so available to edit, False: inactive means can't be left null so uavailable to edit) : informal understanding as a beginner
    featured = models.BooleanField() # null=True, default=True


#_____________________________________Default homepage to custom homepage________________________________________________
# python manage.py startapp pages - creates a new app called pages which is added in to settings' "INSTALLED_APPS"

#views.py (Path: Pages/views.py)
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Hello World</h1>") # strings of HTML code

# urls.py (path: trydjango/urls.py)
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
]
#____________________________for no confusion above code segment is better with________________________________
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]

#___________________________Url routing and requests______________________________________________
#views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Hello World</h1>") # strings of HTML code

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")

def about_view(*args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")

def social_view(*args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")
#____________________we can directly prints the requests or info in the terminal as given in the extened version of above code below
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return HttpResponse("<h1>Hello World</h1>") # strings of HTML code

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

#__________________________________________________Django templates______________________________________________________________
#templates folder creataed in src folder home.html file creataed

#home.HTML-----------------------------------
<h1>Hello world</h1>
<p>This is a template</p>

# contact.html------------------------------
<h1>Contact</h1>
<p>This is a template</p>

# about.html-----------------------------------
<h1>About</h1>
<p>This is a template</p>

#views.py---------------------------------
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # strings of HTML code
    return render(request, "home.html",{}) #line added to take request and return html file

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")


#settings.py--------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['/Users/Vivek Kumar Yadav/Dev/trydjango/src/templates/'], #changes made here: path to templates provided

        # 'DIRS': ['/Users/Vivek Kumar Yadav/Dev/trydjango/src/templates/'],
        'DIRS': [os.path.join(BASE_DIR, "templates")], #adding this line makes it os independent which means works on other pc as well

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#___________________________________________________Django Templating Engine Basics___________________________________________

# inheritance from different html pages using base html pages

#base.html-----------------------
<!doctype html>
<html>
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
<h1>This is a navbar</h1>
    {% block content %}
      replace me             #replaces this segment with the data pulled from another html file
    {% endblock %}
</body>
</html>

#home.html-------------------------
{% extends 'base.html' %} #follows the base.html and provides the requested data

{% block content %}
    <h1>Hello world</h1>
    <p>This is a template</p>
{% endblock %}

#about.html--------------------------
{% extends 'base.html' %}

{% block content %}
    <h1>About</h1>
    <p>This is a template</p>
{% endblock %}

#contact.html-------------------------
{% extends 'base.html' %}

{% block content %}
    <h1>Contact</h1>
    <p>This is a template</p>
{% endblock %}

#__________________________________________________Include Template Tag___________________________________________________
#navbar.html in templates folder-----------------
<nav>
    <ul>
        <li>Brand</li>
        <li>Contact</li>
        <li>About</li>
    </ul>
</nav>

#base.html------------------------------------
<!doctype html>
<html>
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
{% include 'navbar.html' %} #similar but not same to <h1>This is a navbar</h1>

    {% block content %}
      replace me
    {% endblock %}
</body>
</html>

#views.py same as above and settings.py same as above

#_______________________________________Rendering Context into a Template______________________________________________________________

#views.py of pages folder-----------------------------------------
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # strings of HTML code
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {                                    # context added
        "my_text": "This is about us",                # request and contexts are rendered out together here
        "my_number": 123,
        "my_list": [123, 4242, 123123]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

# about.HTML of templates folder-------------------------------------------------
{% extends 'base.html' %}

{% block content %}
    <h1>About</h1>
    <p>This is a template</p>

#adding contexts
<p>
    {{ my_text }}, {{ my_number }},
    {{ my_list }}
</p>

{% endblock %}


#Output: ----------------------------------------
Brand
Contact
About
About
This is a template

This is about us, 123, [123, 4242, 123123]

#____________________________________________________For Loop in a Template______________________________________________________________

#views.py ----------------------------
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # strings of HTML code
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 123123, "Abc"]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

#about.html----------------------------------------------
{% extends 'base.html' %}

{% block content %}
    <h1>About</h1>
    <p>This is a template</p>

<p>
    {{ my_text }}, {{ my_number }},
    {{ my_list }}
</p>

<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<ul>
    {% for my_sub_item in my_list %}
    <li>{{forloop.counter }} - {{ my_sub_item }}</li>
    {% endfor %}
</ul>

{% endblock %}

#output:------------------------------------
Brand
Contact
About
About
This is a template

This is about us, 123, [123, 4242, 123123, 'Abc']

Item 1
Item 2
1 - 123
2 - 4242
3 - 123123
4 - Abc

#__________________________________________________________Using Conditions in a Template______________________________________________________________

#views.py --------------------------------------
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # strings of HTML code
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

# about.html---------------------------------------------
{% extends 'base.html' %}

{% block content %}
    <h1>About</h1>
    <p>This is a template</p>

<p>
    {{ my_text }}, {{ my_number }},
    {{ my_list }}
</p>

<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<ul>
    {% for abc in my_list %}
        {% if abc == 321 %}
            <li>{{ forloop.counter }} - {{ abc|add:22 }}</li>
        {% elif abc == "Abc" %}
            <li>This is not the network</li>
        {% else %}
            <li>{{forloop.counter }} - {{ abc }}</li>
        {% endif %}
    {% endfor %}
</ul>

{% endblock %}

#_______________________________________________Template Tags and Filters____________________________________________
#views.py ---------------------------
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # strings of HTML code
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "title": "ABC This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

#about.html--------------------------------------------------------------
{% extends 'base.html' %}

{% block content %}
    <h1>About</h1>

    <h3>{{ title|capfirst|title }}</h3> #filters added
    <p>This is a template</p>

    {{ my_html|striptags|slugify }} #comment: {{my_html|safe}} remove this comment while running it


<p>
    , {{ my_number }},
    {{ my_list }}
</p>

<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<ul>
    {% for abc in my_list %}
        {% if abc == 321 %}
            <li>{{ forloop.counter }} - {{ abc|add:22 }}</li>
        {% elif abc == "Abc" %}
            <li>This is not the network</li>
        {% else %}
            <li>{{forloop.counter }} - {{ abc }}</li>
        {% endif %}
    {% endfor %}
</ul>

{% endblock %}


#_____________________________________Rendering data from the Database with a Model____________________________________

#New: Product, for this all the files are below

#products/models.py -------------------------------
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField() # null=True, default=True

#products/views.py -----------------------------------
from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=3)
    context = {
        'title': obj.title,
        'description': obj.description
    }
    return render(request, "product/detail.html", context)

#templates/product/detail.html-----------------------------
{% extends 'base.html' %}

{% block content %}
<h1>Item</h1>
{% endblock %}

#trydjango/urls.py-------------------------updated
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import product_detail_view #<---------------------imported for products

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('product/', product_detail_view), #<-----------------------path added new
    path('social/', social_view),
    path('admin/', admin.site.urls),
]

#output:----------------------------------------------------------------
Brand
Contact
About
Item

#updated #templates/product/detail.html-----------------------------
{% extends 'base.html' %}

{% block content %}
<h1>{{ title }}</h1>

<p>{% if description != None and description != '' %}{{ description }}{% else %} Description Coming Soon{% endif %}</p>

{% endblock %}

#new output: -----------------------------------------------------
Brand
Contact
About
New Product
new description

##products/views.py -----------------------------------updated so that won't have to match and update context everytime with object's features
from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=3)

   # context = {
   #     'title': obj.title,
   #     'description': obj.description
   #}

    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)

#updated #templates/product/detail.html-----------------------------updated too
{% extends 'base.html' %}

{% block content %}
<h1>{{ object.title }}</h1>

<p>{% if object.description != None and object.description != '' %}{{ object.description }}{% else %} Description Coming Soon{% endif %}</p>

{{ object.price }}

{% endblock %}

#______________________________________________________________How Django templates Load with Apps___________________________________________________________________
#New "templates" folder creataed in "products" app and again "products" folder created inside "products/templates/" and again product_detail.html created inheritance
#purpose is to keep the templates within the app i.e app specific content within app folder
#Note: previously we were using path sr/templates/product/detail.html for "products" app


#products/templates/products/product_detail.HTML---------------code here
{% extends 'base.html' %}

{% block content %}
<h1>In App template: {{ object.title }}</h1>

<p>{% if object.description != None and object.description != '' %}{{ object.description }}{% else %} Description Coming Soon{% endif %}</p>

{{ object.price }}

{% endblock %}

#products/views.py---------------------------updated
from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=3)

   # context = {
   #     'title': obj.title,
   #     'description': obj.description
   #}

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context) #update available here

#_____________________________________________Django Model Forms_____________________________________________________________
#Fresh new form created that prompts user to enter data in the url and adds objects in the backend
#files are below:

#products[it is an app]/models.py---------------------------------------------
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False) # null=True, default=True

#products[it is an app]/forms.py -------------------------------
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

#products[it is an app]/views.py-----------------------------------
from django.shortcuts import render

from .forms import ProductForm

from .models import Product

# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=3)

   # context = {
   #     'title': obj.title,
   #     'description': obj.description
   #}

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

#products/templates/products/product_create.html-------------------------------
{% extends 'base.html' %}

{% block content %}
<form method='POST'> {% csrf_token %}
<form>
    {{ form.as_p }}
    <input type='submit' value='Save' />
</form>
{% endblock %}

#trydjango/urls.py--------------------------------------------------------
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('create/', product_create_view),
    path('product/', product_detail_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
]

#____________________________________________________________________RAW HTML Forms_____________________________________________________________
#views.py-------------------------------------
from django.shortcuts import render

from .forms import ProductForm

from .models import Product

# Create your views here.

def product_create_view(request):
    context = {}
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     form = ProductForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=3)

   # context = {
   #     'title': obj.title,
   #     'description': obj.description
   #}

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

#product_create.html----------------------------------------------------
{% extends 'base.html' %}

{% block content %}
<form action='http://www.google.com/search' method='GET'> #performs the google search if method=GET ->gives output on the page i.e getting information
# method='POST' -> saves data in the backend
# Also action changes the url too that's why when using google.com it goes to google.com to perform the action
    <input type='text' name='q' placeholder="Your search"/>
    <input type='submit' value='Save' />
</form>
{% endblock %}

#code segment of product_create.html just for info---
def product_create_view(request):
    print(request.GET['title'])
    print(request.POST)
    context = {}
    return render(request, "products/product_create.html", context)

#------------------------------this is important for saving the data entered or using it for different purposes-----------------------
#views.py -------------------------although this may be a bad way of saving data due to lack of checking validation if the data saved is good or not
from django.shortcuts import render

from .forms import ProductForm

from .models import Product

# Create your views here.

def product_create_view(request):
    # print(request.GET)
    # print(request.POST)
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)
        # Product.objects.create(title=my_new_title)
    context = {}
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     form = ProductForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=3)

   # context = {
   #     'title': obj.title,
   #     'description': obj.description
   #}

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

#product_create .html for above code----------------
{% extends 'base.html' %}

{% block content %}
<form action='.' method='POST'> {% csrf_token %}
    <input type='text' name='title' placeholder="Your title"/>
    <input type='submit' value='Save' />
</form>
{% endblock %}

#_____________________________________________________Pure Django Form_____________________________________________________________________
#saved data using some raw django forms along with validation that forms did which saving the data
#product_create.html-------------------------------------
{% extends 'base.html' %}

{% block content %}
<form action='.' method='POST'> {% csrf_token %}
    {{ form.as_p }}
    <input type='submit' value='Save' />
</form>
{% endblock %}

#forms.py----------------------------------------------
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

# views.py-----------------------------------------------------
from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     form = ProductForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=3)

   # context = {
   #     'title': obj.title,
   #     'description': obj.description
   #}

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
#____________________________________________Form Widgets________________________________________________________________
#forms.py----------------------------------------
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial=199.99)

#________________________________________________Form Validation Methods__________________________________________________
#forms.py-----------------------------------------------
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        title = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(

        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial=199.99)


#___________________________________________________Initial Values for Forms_______________________________________________________
#views.py --------------------------------
from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.
def render_initial_data(request):    #added fn-------------to added initial data or edit data 'instance' not supported needs to be fixed
    initial_data = {
        'title': "My this awesome title"
    }
   # obj = Product.objects.get(id=3)
    form = RawProductForm(request.POST or None, initial=initial_data) # instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     form = ProductForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=3)

   # context = {
   #     'title': obj.title,
   #     'description': obj.description
   #}

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

    #urls.py-----------------------------------------------------------
    """trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import product_detail_view, product_create_view, render_initial_data

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('create/', product_create_view),
    path('initial/', render_initial_data), #added path-------------------------------------------
    path('product/', product_detail_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
]

#______________________________________________________Dynamic Url Routing_______________________________________________________
#views.py ------------------------function added for dynamic lookup view
def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

#product_detail.html-------------------------updated
{% extends 'base.html' %}

{% block content %}
<h1>{{ object.title }}</h1>
<p>{{ object.description }}</p>
<p>{{ object.price }}</p>
{% endblock %}

#urls.py------------------------new path added for /products/
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    dynamic_lookup_view   #added
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('create/', product_create_view),
    path('initial/', render_initial_data),
    path('product/', product_detail_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
    path('products/<int:my_id>/', dynamic_lookup_view, name='product') #added
]

#__________________________________________________________Handle Doesnot Exist________________________________________________
# views.py------------------------one method to handle exception with 404 error
from django.shortcuts import render, get_object_or_404 #added----------

def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

#views.py -------------------------another way to handle exception with 404 error using try and except
from django.http import Http404 #added
from django.shortcuts import render, get_object_or_404 #added

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.

def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product, id=id)

    #''' added '''
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

#_______________________________________________Delete and Confirm__________________________________________________________________________
#product_delete.html-----------------------new file added
{% extends 'base.html' %}

{% block content %}

<form action='.' method='POST'>{% csrf_token %}
    <h1>Do yo want to delete the product "{{ object.title }}"</h1> #prompts to ask is user wants to delete file
    <p><input type='submit' value='Yes' /> <a href='../'>Cancel</a></p>
</form>

{% endblock %}

#views.py ------------------------------------ to perform deletion of object
from django.http import Http404
from django.shortcuts import render, get_object_or_404,  redirect #redirect added---------------

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
    # confirming delete
        obj.delete() #deletes the object
        return redirect('../../') # brings 2 locations back after deletion
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

#urls.py--------------------------------------------------------------------
"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    product_delete_view #added--------------------------
    #dynamic_lookup_view
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('create/', product_create_view),
    path('initial/', render_initial_data),
    path('product/', product_detail_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
    #path('products/<int:id>/', dynamic_lookup_view, name='product')
    path('products/<int:id>/delete/', product_delete_view, name='product-delete') #added------------------------
]

#_________________________________________________View of a list of database objects________________________________________________________________________________________
#product_list.html-------------------------------
{% extends 'base.html' %}

{% block content %}

{{ object_list }}

{% for instance in object_list %}
<p>{{ instance.id }} - {{ instance.title }}</p>

{% endfor %}

{% endblock %}

#;views.py-------------------including code segments in views.py above-----------------
from django.http import Http404
from django.shortcuts import render, get_object_or_404,  redirect

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.
def product_list_view(request):
    queryset = Product.objects.all()  #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

#urls.py---------------------------------------------------
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    product_delete_view,
    product_list_view
    #dynamic_lookup_view
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('create/', product_create_view),
    path('initial/', render_initial_data),
    path('product/', product_detail_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
    #path('products/<int:id>/', dynamic_lookup_view, name='product')
    #path('products/<int:id>/delete/', product_delete_view, name='product-delete')
    path('products/', product_list_view, name='product-list')
]

#NOTE for third parameter in path() : https://docs.djangoproject.com/en/3.0/topics/http/urls/
# URLconfs have a hook that lets you pass extra arguments to your view functions, as a Python dictionary.
#
# The path() function can take an optional third argument which should be a dictionary of extra keyword arguments to pass to the view function.
#
# For example:
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
# ]
# In this example, for a request to /blog/2005/, Django will call views.year_archive(request, year=2005, foo='bar').
#
# This technique is used in the syndication framework to pass metadata and options to views.
#
# Dealing with conflicts
#
# It’s possible to have a URL pattern which captures named keyword arguments, and also passes arguments with the same names in its dictionary of extra arguments. When this happens, the arguments in the dictionary will be used instead of the arguments captured in the URL.


#base.html-----------------------------------------------------
<!doctype html>
<html>
<head>
    <title>Coding for Entrepreneurs is doing Try Django</title>
</head>
<body>
{% include 'navbar.html' %}

    {% block content %}
      replace me
    {% endblock %}
</body>
</html>

#________________________________________________Dynamic Linking of Urls_________________________________________________________________________________________________________________________
# it links the objects's title to its data and helps navigate back and forth
#models.py ----------------------------------------------------
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False) # null=True, default=True

    def get_absolute_url(self): #added--------------
        return f"/products/{self.id}/" #added--------------

#product_list.html---------------------------------------------
{% extends 'base.html' %}

{% block content %}

{{ object_list }}

{% for instance in object_list %}
    <p>{{ instance.id }} - <a href='{{ instance.get_absolute_url }}'>{{ instance.title }}</a>
    </p>
{% endfor %}

{% endblock %}

#urls.py--------------------------------------
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    product_delete_view,
    product_list_view,
    dynamic_lookup_view
    )

urlpatterns = [
    # path('', home_view, name='home'),
    # path('contact/', contact_view),
    # path('about/', about_view),
    # path('create/', product_create_view),
    # path('initial/', render_initial_data),
    # path('product/', product_detail_view),
    # path('social/', social_view),
    # path('admin/', admin.site.urls),
    path('products/', product_list_view, name='product-list'),
    path('products/<int:id>/', dynamic_lookup_view, name='product'),
    path('products/<int:id>/delete/', product_delete_view, name='product-delete')
]

#___________________________________________Django Urls reverse_______________________________________________________________________________________________________
#urls.py--------------------------
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    product_delete_view,
    product_list_view,
    dynamic_lookup_view
    )

urlpatterns = [
    # path('', home_view, name='home'),
    # path('contact/', contact_view),
    # path('about/', about_view),
    # path('create/', product_create_view),
    # path('initial/', render_initial_data),
    # path('product/', product_detail_view),
    # path('social/', social_view),
    # path('admin/', admin.site.urls),
    path('products/', product_list_view, name='product-list'),
    path('p/<int:id>/', dynamic_lookup_view, name='product-detail'), #goes with third parameter of path and updates to 'p' on url dynamically for example as for p here
    path('products/<int:id>/delete/', product_delete_view, name='product-delete')
]

#models.py ------------------------------------updated
from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False) # null=True, default=True

    def get_absolute_url(self):
        #return f"/products/{self.id}/"
        return reverse("product-detail", kwargs={"id": self.id})

# this is recommended as previous one  is like hardcoded this one works for dynamic paths
# we can define similarily for other remailing paths as well for example for delete:
# it can be:     path('productsdel/<int:id>/delete/', product_delete_view, name='product-delete')
# and return reverse("product-delete", kwargs={"id": self.id})

#_________________________________________________________________In App Urls and Namespacing______________________________________________________________________________________________________________
