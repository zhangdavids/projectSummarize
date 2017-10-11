from django.conf.urls import include, url
from django.contrib import admin

from books_app.api import UsersList
import books_app.views
import rest_framework_swagger


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^$', books_app.views.home, name='home'),
    url(r'^auth/', books_app.views.auth, name='auth'),   
    url(r'^sign_out/', books_app.views.sign_out, name='sign_out'),
    url(r'^rate_movie/', books_app.views.rate_movie, name='rate_movie'),
    url(r'^movies_recs/', books_app.views.movies_recs, name='movies_recs'),
    url(r'^users_list/', UsersList.as_view(), name='users_list')
]
