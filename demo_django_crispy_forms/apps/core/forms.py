from django import forms
from .models import Registration
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from captcha.fields import CaptchaField


class RegistrationForm(forms.ModelForm):
    """
    Formulaire d'inscription
    """

    # Ici, tu vas rajouter les champs supplémentaires au modèle
    # Tu définis le captcha
    captcha = CaptchaField()
    # Tu ajoutes un mail de confirmation
    confirmation_mail = forms.EmailField(label="Mail de confirmation")

    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu modifies le label de la date de naissance pour rajouter le format
        self.fields['birth_date'].label = "%s (JJ/MM/AAAA)" % "Date de naissance"
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'registration-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crée l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Identité',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'civility',
                    'birth_name',
                    'last_name',
                    'first_name',
                    'birth_date',
                    'birth_place',
                    'birth_country',
                    # Tu rajoute un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Suivant",
                        type='button',
                        css_class='btn-default col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 2 - Adresse',
                    # Liste des champs à afficher
                    'street_number',
                    'street_type',
                    'street',
                    'comp_1',
                    'comp_2',
                    'city',
                    'zip_code',
                    'country',
                    'phone',
                    # Tu rajoute des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 3 - Validation',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'mail',
                    'confirmation_mail',
                    'comments',
                    'captcha',
                    # Tu rajoute des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Précédent",
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valider",
                        type='submit',
                        css_class='btn-default col-md-offset-8'
                    )
                ),
            ),
        )

    def clean_confirmation_mail(self):
        """
        Méthode pour vérifier que le mail correspond bien au
        mail de confirmation lors de la validation du formulaire
        """
        confirmation_mail = self.cleaned_data['confirmation_mail']
        mail = self.cleaned_data['mail']
        if mail != confirmation_mail:
            raise forms.ValidationError(
                "Le mail et le mail de confirmation ne sont pas identiques")
        return confirmation_mail

    class Meta:
        # Tu définis le modèle utilisé
        model = Registration
        exclude = []
        # Tu customise le champ date de naissance pour ajouter le date picker
        widgets = {
            'birth_date': DateTimePicker(
                options={"format": "DD/MM/YYYY", "pickTime": False,
                         "useStrict": True, "viewMode": "years",
                         "startDate": "01/01/1900"},
                attrs={'placeholder': 'ex: 05/11/1975'}
            )
        }
