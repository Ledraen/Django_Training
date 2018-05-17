from django.conf.urls import url
from . import views #note the . searches current package

app_name = 'blog'
urlpatterns = [
    # 1st URLpattern doesnt take any args and is mapped to the post list view.
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^$', views.PostListView.as_view(), name='post_list'),
    #2nd pattern takes the 4 arguments and is mapped to the post detail view.
    #the reg. expressions listed require the following numbers of digits:
    #Year = {4}, Month = {2}, Day = {2}, Post =can be composed by words & hyphens
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]
