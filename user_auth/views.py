from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.views.generic import CreateView, ListView
from .models import Recruitment
from .forms import RecruitmentForm
from django.urls import reverse_lazy


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)

    return render(request, 'user_auth/top.html', {'user': user})


class RecruitCreateView(CreateView):
    model = Recruitment
    form_class = RecruitmentForm
    template_name = "user_auth/create_form.html"
    success_url = reverse_lazy('user_auth:top_r')
    user = UserSocialAuth.objects.get(user_id= self.request.user.id)
    
    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        
        form_kwargs['initial'] = {'userid': self.user}
        return form_kwargs
