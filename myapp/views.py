
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from . import models

class IndexView(TemplateView):
    template_name = 'myapp/index.html'


# ログイン状態や権限の有無により、テンプレートの表示内容を変更
class ArticleView(DetailView):
    model = models.Article
    template_name = 'myapp/article.html'


# LoginRequiredMixinを使って、ログインした場合のみテンプレートを表示
class LoginRequiredView(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/login_required.html'
# 未ログインの場合、403ページを表示する版
class LoginRequiredWith403View(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/login_required.html'
    # raise_exception=Trueにすると、リダイレクトの代わりに403を表示
    # 自作403ページは、テンプレートフォルダのルートに置く
    # https://docs.djangoproject.com/en/1.9/ref/views/#django.views.defaults.permission_denied
    raise_exception = True


# UserPassesTestMixinを使って、test_func()の条件を満たしたユーザのみテンプレートを表示
class LimitedUserRequiredView(UserPassesTestMixin, TemplateView):
    template_name = 'myapp/limited_user_required.html'
    
    def test_func(self):
        # ログインしていない場合はAnonymousUserになるが、その場合は、email属性を持っていないので、そのままではエラーが発生する
        # [django.contrib.auth | Django documentation | Django](https://docs.djangoproject.com/en/1.9/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser)
        # 'AnonymousUser' object has no attribute 'email'
        if not hasattr(self.request.user, 'email'):
            return False
        
        return self.request.user.email and self.request.user.email.startswith('perm')
# 未ログインの場合、403ページを表示する版
class LimitedUserRequiredWith403View(UserPassesTestMixin, TemplateView):
    template_name = 'myapp/limited_user_required.html'
    raise_exception = True
    
    def test_func(self):
        if not hasattr(self.request.user, 'email'):
            return False
        
        return self.request.user.email.startswith('perm')


# PermissionRequiredMixinを使って、ユーザが権限を持っている場合のみテンプレートを表示
class PermissionRequiredView(PermissionRequiredMixin, TemplateView):
    template_name = 'myapp/permission_required.html'
    permission_required = ('myapp.can_view',)
# 未ログインの場合、403ページを表示する版
class PermissionRequiredWith403View(PermissionRequiredMixin, TemplateView):
    template_name = 'myapp/permission_required.html'
    permission_required = ('myapp.can_view',)
    raise_exception=True