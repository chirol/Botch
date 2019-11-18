from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.views.generic import CreateView, ListView
from .models import Recruitment
from .forms import RecruitmentForm
from django.urls import reverse_lazy


@login_required
def top_page(request):
    user_id = UserSocialAuth.objects.get(user_id=request.user.id)

    return render(request, 'user_auth/top.html', {'user': user_id})


class RecruitCreateView(CreateView):
    model = Recruitment
    form_class = RecruitmentForm
    template_name = "user_auth/create_form.html"
    success_url = reverse_lazy('user_auth:top_r')

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

    def form_init(self, request):
        user_id = UserSocialAuth.objects.get(user_id=self.request.user.id)
        initial_dict = {
            'userid': user_id
        }
        formset = RecruitmentForm(request.POST or None, initial=initial_dict)
        return render(request, 'create_form.html', {'form': formset})
