# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'djangoapp'
urlpatterns = [
    path(route='about',view=views.aboutus,name='about'),
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route="logout",view=views.logout_request,name='logout'),
    path(route='register',view=views.registration,name='register'),
    path(route='getcars',view=views.get_cars,name='get_cars'),
    
    # path for dealer reviews view
    path(route='getdealers/', view=views.get_dealerships,name='get_dealer'),
    path(route='getdealers/<str:state>', view=views.get_dealerships,name='get_dealer'),
    path(route='getdealer/<int:dealer_id>', view=views.get_dealer_details,name='get_dealer'),
    path(route='getreview/dealer/<int:dealer_id>', view=views.get_dealer_reviews,name='get_review'),
    path(route='postreview',view=views.add_review,name='post_review')
    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
