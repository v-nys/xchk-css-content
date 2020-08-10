from django.urls import path

from . import contentviews

urlpatterns = [
    path('xchk_css_content_demo', contentviews.DemoCSSView.as_view(), name=f'{contentviews.DemoCSSView.uid}_view'),
]
