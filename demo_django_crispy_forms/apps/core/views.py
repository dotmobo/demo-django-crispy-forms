from django.views.generic.edit import CreateView
from .models import Registration
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .forms import RegistrationForm


class RegistrationCreate(CreateView):
    """
    Affichage du formulaire
    """
    model = Registration
    form_class = RegistrationForm
    success_url = reverse_lazy('core:success')


def registration_success(request):
    """
    Message de confirmation
    """
    return render(request, 'core/registration_success.html')
