from django.shortcuts import render, resolve_url, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import login as auth_login


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             #  로그인 처리 여기서 해주면 됨
#             auth_login(request, user)
#             next_url = request.GET.get("next") or "profile"
#             # or; 앞이 거짓이면 뒤의 값 사용.
#             return redirect(next_url)
#     else:
#         form = SignupForm()
#     return render(
#         request,
#         "accounts/signup.html",
#         {
#             "form": form,
#         },
#     )


##first CBV
# signup = CreateView.as_view(
#     model=User,
#     form_class=SignupForm,
#     template_name="accounts/signup.html",
#     success_url=settings.LOGIN_URL,
# )


##new CBV
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "accounts/signup.html"

    def get_success_url(self):
        next_url = self.request.GET.get("next") or "profile"
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())


signup = SignupView.as_view()