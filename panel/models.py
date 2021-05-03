from django.db import models
from django.utils.translation import ugettext_lazy as _


class Mahalla(models.Model):
    title = models.CharField(_("Mahalla nomi"), max_length=256, null=True)
    region = models.CharField(verbose_name='Tuman', max_length=255, null=True)

    title_ru = models.CharField(_("Mahalla nomi_ru"), max_length=256, null=True)
    title_uz = models.CharField(_("Mahalla nomi_uz"), max_length=256, null=True)


    token = models.CharField(max_length=1024, null=True)
    location = models.CharField(_("Manzil"), max_length=256, null=True)
    phone = models.CharField(_("Telefon"), max_length=13, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Mahalla')
        verbose_name_plural = _('Mahallalar')


class MuammoManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Muammo(models.Model):
    title = models.CharField(_("Muammo nomi"), max_length=300)

    objects = MuammoManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Muammo nomi")
        verbose_name_plural = _('Muammolar')

    def natural_key(self):
        return self.title


class SubMuammo(models.Model):
    title = models.ForeignKey(Muammo, on_delete=models.CASCADE, default='')
    category = models.CharField(_("Kategoriya"), max_length=64, default="Default")

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = _("Kategoriya nomi")
        verbose_name_plural = _('Kategoriyalar')


class Hudud(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(_("Hudud"), max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Hudud")
        verbose_name_plural = _('Hudud')


class Murojatchi(models.Model):
    MUROJATCHI_STATUSI = (
        ("ko'rib chiqilmagan", _("ko'rib chiqilmagan")),
        ("ko'rib chiqilmoqda", _("ko'rib chiqilmoqda")),
        ("ko'rib chiqildi", _("ko'rib chiqildi")),
        ("qabulga chaqirildi", _("qabulga chaqirildi")),
        ("rad etildi", _("rad etildi")),
    )
    MUROJAT_TURI = (
        ("Taklif", _("Taklif")),
        ("Murojat", _("Murojat")),
        ("Qabul", _("Qabul")),
    )

    GENDER = (
        (1, _("Erkak")),
        (2, _("Ayol")),
    )

    id = models.BigAutoField(primary_key=True)
    telegram_id = models.PositiveBigIntegerField(_("Telegram ID"), blank=True, null=True)
    fullname = models.CharField(_("Ism Sharifi"), max_length=256, blank=True, null=True)
    username = models.CharField(_("Username"), max_length=32, blank=True, null=True)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE, blank=True, null=True)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, blank=True, null=True)
    murojat_turi = models.CharField(max_length=16, choices=MUROJAT_TURI, blank=True, null=True)
    muammo = models.ForeignKey(Muammo, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(SubMuammo, on_delete=models.CASCADE, blank=True, null=True)
    media = models.FileField(_("Media"), upload_to='muammo_media/', blank=True, null=True)
    location = models.CharField(_("Manzil"), max_length=300, blank=True, null=True)
    description = models.TextField(_("Murojat Matni"), null=True, blank=True)
    phone = models.CharField(_("Telefon"), max_length=13, blank=True, null=True)
    accepted = models.BooleanField(_("Qabulga Chaqirildi"), default=False)

    reply_message = models.TextField(_("Javob Matni"), default=_("Javob berilmagan"), blank=True, null=True)
    created = models.DateField(_("Murojat Sanasi"), auto_now_add=True, null=True, blank=True)
    updated = models.DateField(_("O'zgartish Kiritilgan Sana"), auto_now_add=True, null=True, blank=True)
    status = models.CharField(_("Murojatchi Statusi"), max_length=32, choices=MUROJATCHI_STATUSI,
                              default=MUROJATCHI_STATUSI[0][0], null=True, blank=True)

    year_of_birth = models.CharField(_("Tug'ilgan yil"), max_length=256, null=True, blank=True)
    month_of_birth = models.CharField(_("Tug'ilgan oy"), max_length=256, null=True, blank=True)
    day_of_birth = models.CharField(_("Tug'ilgan kun"), max_length=256, null=True, blank=True)
    gender = models.PositiveBigIntegerField(_("Gender"), choices=GENDER, null=True, blank=True)

    def __str__(self):
        return f"{str(self.telegram_id)}"

    class Meta:
        verbose_name = _('Murojatchi')
        verbose_name_plural = _('Murojatchilar')


class Reception(models.Model):
    title = models.CharField(_("Qabul Nomi"), max_length=256)
    telegram_id = models.ForeignKey(Murojatchi, on_delete=models.CASCADE, default=True, null=True)
    appointment = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Qabul')
        verbose_name_plural = _('Qabullar')
