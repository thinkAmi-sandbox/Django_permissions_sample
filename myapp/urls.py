from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from . import views

urlpatterns = [
    # ログイン
    url(r'^login/$', 
        auth_views.login, 
        {
            'template_name': 'myapp/login.html'
        },
        name='login'
    ),
    
    # ログアウト後にindexへリダイレクト
    url(r'^logout/$', 
        auth_views.logout,
        {
            'next_page': reverse_lazy('my:index'),
        },
        name='logout_with_redirect'
    ),
    
    # Index
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # ログイン状態や権限の有無により、表示内容を変更
    url(r'^article/(?P<pk>[0-9]+)$', views.ArticleView.as_view(), name='detail'),
    
    # 表示するのに、ログインする必要あり(未ログインはリダイレクト)
    url(r'^login-required$', views.LoginRequiredView.as_view(), name='login_required'),
    # 403ページを表示する板
    url(r'^login-required-with-403$', views.LoginRequiredWith403View.as_view(), name='login_required_403'),
    
    # 表示するのに、ログイン&特定のユーザである必要あり(条件を満たさない場合はリダイレクト)
    url(r'^limited-user-required$', views.LimitedUserRequiredView.as_view(), name='limited_user_required'),
    # 403ページを表示する板
    url(r'^limited-user-required-with-403$', views.LimitedUserRequiredWith403View.as_view(), name='limited_user_required_403'),
    
    # 表示するのに、パーミッションが必要(パーミッションがない場合はリダイレクト)
    url(r'^permission-required$', views.PermissionRequiredView.as_view(), name='permission_required'),
    # 403ページを表示する板
    url(r'^permission-required-with-403$', views.PermissionRequiredWith403View.as_view(), name='permission_required_403'),
]