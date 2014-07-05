django-modernizr
===============

[Modernizr web site](http://modernizr.com/)

## Usage

* To install package run python setup.py install in your virtualenv
* Add django\_modernizr into your INSTALLED_APPS

### Installation using pip
* To install package directly from github using pip command run in terminal:

```bash
pip install -e git+https://github.com/ITrex/django-modernizr.git@2.8.3#egg=django_modernizr
```

```python
INSTALLED_APPS=[
# ...
    'django_colorbox',
# ...
]
```
* Load javascript in your template
```html

<link rel="stylesheet" href="{% static 'django_colorbox/css/colorbox.css' %}"/>
<script type="text/javascript" src="{% static 'django_colorbox/js/jquery.colorbox-min.js' %}"></script>
```
