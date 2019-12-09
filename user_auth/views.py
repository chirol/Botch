from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import Recruitment
from .forms import RecruitmentForm
from django.urls import reverse_lazy
import twitter
from django.conf import settings
from django.contrib.auth import login

from social_django.utils import psa

"""
@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    return render(request, 'user_auth/top.html', {'user': user})
"""

class RecruitCreateView(CreateView):
    model = Recruitment
    form_class = RecruitmentForm
    template_name = "user_auth/create_form.html"
    success_url = reverse_lazy('user_auth:top_r')
     
    def user_auth(request):
        self.user = UserSocialAuth.objects.get(user_id=self.request.user.id)
        return render(request, 'user_auth/create_form.html', {'user': self.user})

    def get_initial(self):
        self.user = UserSocialAuth.objects.get(user_id=self.request.user.id)
        self.initial_form = {'username': self.user, 'userid': self.user.id}
        return self.initial_form

"""
    def get_initial(self):
        self.twitter_api = twitter.Api(
            consumer_key=settings.SOCIAL_AUTH_TWITTER_KEY,
            consumer_secret=settings.SOCIAL_AUTH_TWITTER_SECRET,
            access_token_key=settings.SOCIAL_AUTH_TWITTER_ACCESS_TOKEN,
            access_token_secret=settings.SOCIAL_AUTH_TWITTER_ACCESS_TOKEN_SECRET,
        )
        self.user = UserSocialAuth.objects.get(user_id=self.request.user.id) #ログインユーザのtwitter表示名
        self.user_info = self.twitter_api.GetUser(screen_name=self.user) #表示名からtwitter情報取得
        self.initial_form = {'username': self.user, 'userid': self.user_info.id} #twitter情報からユーザid（一意)をフォームの初期値に
        return self.initial_form
"""



class RecruitmentDatailView(DetailView):
    """
    募集の詳細ページ
    """
    model = Recruitment
    template_name = "user_auth/recruitment_detail.html"

"""
    def user_auth(request):
        self.user = UserSocialAuth.objects.get(user_id=self.request.user.id)
        return render(request, 'user_auth/create_form.html', {'user': self.user})
"""

class RecruitmentUpdateView(UpdateView):
    """
    募集の更新ページ
    """
    model = Recruitment
    template_name = "user_auth/recruitment_update.html"

    def user_auth(request):
        self.user = UserSocialAuth.objects.get(user_id=self.request.user.id)
        return render(request, 'user_auth/create_form.html', {'user': self.user})


class RecruitmentListView(ListView):
    """
    募集をリスト表示する
    """
    model = Recruitment
    template_name = "user_auth/top.html"

    def user_auth(request):
        self.user = UserSocialAuth.objects.get(user_id=self.request.user.id)
        return render(request, 'user_auth/top.html', {'user': self.user})

"""
class RecruitmentDeleteView(DeleteView):
    model = Recruitment
    # 削除はまずはなしの方針で、要望があれば追加
"""

    