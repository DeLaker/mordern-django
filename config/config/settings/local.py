from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRETE_KEY', default='x0(6llyh92h2j8^h&hhx!8#^#l%kiak52g1^u+99n_(2eqed0q')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)