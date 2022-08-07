from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from forms import UserLogInForm
from django.contrib.auth.views import LoginView
from test_task.api import Keitaro
from config.config import api_key, url_clicks, url_conversions

# Create your views here.


class LogInUser(LoginView):
    form = UserLogInForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


@login_required
def home(request):

    total_clicks = Keitaro(api_key, url_clicks, limit=10).get_exact()
    total_conversions = Keitaro(api_key, url_conversions, limit=10).get_exact()

    sub_id = Keitaro(api_key=api_key,
                     url=url_clicks, limit=10).get_sub()

    context = {'clicks': total_clicks[0], 'conversions': total_conversions, 'sub_id_6': sub_id}
    return render(request, 'home.html', context)
