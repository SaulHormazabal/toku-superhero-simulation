from django.urls import include, path
from django.views.generic import RedirectView

from simulation.config.urls import urlpatterns


urlpatterns += [
    path('', RedirectView.as_view(url='/api/', permanent=True)),
    path('__debug__/', include('debug_toolbar.urls')),
]
