import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}'
        send_mail(
            subject="Подтверждение почты",
            message=f"Для подтверждения почты перейди по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))

'''class ResetPasswordView(View):
    def get(self, request):
        form = PasswordResetForm()
        return render(request, 'password_reset_form.html', {'form': form})

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = secrets.token_hex(8)
            user.password = make_password(new_password)
            user.save()
            send_mail(
                subject="Смена пароля",
                message=f"Ваш новый пароль: {new_password}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
            )
            return render(request, 'password_reset_confirm.html')
        except:
            return render(request, 'password_reset_error.html')'''