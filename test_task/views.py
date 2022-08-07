from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from forms import UserLogInForm
from django.contrib.auth.views import LoginView
from api import Keitaro


# Create your views here.


class LogInUser(LoginView):
    form = UserLogInForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


@login_required
def home(request):
    api_key = '7b88e90dfad2f86bf250b0ac388176ec'
    url_clicks = 'http://136.244.93.168/admin_api/v1/clicks/log'
    url_conversions = 'http://136.244.93.168/admin_api/v1/conversions/log'

    total_clicks = Keitaro(api_key, url_clicks, limit=10).get_exact()
    total_conversions = Keitaro(api_key, url_conversions, limit=10).get_exact()

    sub_id = Keitaro(api_key=api_key,
                     url='http://136.244.93.168/admin_api/v1/clicks/log', limit=10).get_sub()

    context = {'clicks': total_clicks[0], 'conversions': total_conversions, 'sub_id_6': sub_id}
    return render(request, 'home.html', context)
