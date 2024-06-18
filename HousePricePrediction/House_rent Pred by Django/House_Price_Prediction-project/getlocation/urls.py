from django.urls import path
from . import views
from House_Price_Prediction.views import predict as predict_views
app_name='getlocation'
urlpatterns = [
    path('dependantfield/', views.dependantfield, name='dependantfield'),
    # Add other URLs specific to the 'getlocation' app here if needed
    
]

