from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.views.generic import CreateView, ListView
from .models import Recruitment
from .forms import RecruitmentForm
from django.urls import reverse_lazy
import twitter
from django.conf import settings


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)

    return render(request, 'user_auth/top.html', {'user': user})


class RecruitCreateView(CreateView):
    model = Recruitment
    form_class = RecruitmentForm
    template_name = "user_auth/create_form.html"
    success_url = reverse_lazy('user_auth:top_r')

    def get_initial(self):
        self.twitter_api = twitter.Api(
            consumer_key=settings.SOCIAL_AUTH_TWITTER_KEY,
            consumer_secret=settings.SOCIAL_AUTH_TWITTER_SECRET,
            access_token_key=settings.SOCIAL_AUTH_TWITTER_ACCESS_TOKEN,
            access_token_secret=settings.SOCIAL_AUTH_TWITTER_ACCESS_TOKEN_SECRET,
        )
        self.user = UserSocialAuth.objects.get(user_id=self.request.user.id)
        self.user_info = self.twitter_api.GetUser(screen_name=self.user)


        self.initial_form = {'userid': self.user_info.id}
        return self.initial_form
        # user_idをcharfieldにしたほうがいいかも

    """
    def get_form_kwargs(self, *args, **kwargs):
        user_id = UserSocialAuth.objects.get(user_id=self.request.user.id)
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['initial'] = {'userid': user}
        return form_kwargs
        initial_dict = {
            'userid' = user_id
        }
        form = RecruitmentForm()
    """
    """
    def form_init(self, request):
        user_id = UserSocialAuth.objects.get(user_id=self.request.user.id)
        initial_dict = {
            'userid': user_id
        }
        formset = RecruitmentForm(request.POST or None, initial=initial_dict)
        return render(request, 'create_form.html', {'form': formset})
    """
