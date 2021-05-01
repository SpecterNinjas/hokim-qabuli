from django.db import models
from django.utils.translation import ugettext_lazy as _


class Mahalla(models.Model):
    title = models.CharField(_("Mahalla nomi"), max_length=256, null=True)
    region = models.CharField(verbose_name='Tuman', max_length=255, null=True)
    title_uz = models.CharField(max_length=255, null=True)
    title_ru = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=1024, null=True)
    location = models.CharField(_("Manzil"), max_length=256, null=True)
    phone = models.CharField(_("Telefon"), max_length=13, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Mahalla')
        verbose_name_plural = _('Mahallalar')


class Muammo(models.Model):
    title = models.CharField(_("Muammo nomi"), max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Muammo nomi")
        verbose_name_plural = _('Muammolar')


class SubMuammo(models.Model):
    title = models.ForeignKey(Muammo, on_delete=models.CASCADE, default='')
    category = models.CharField(_("Kategoriya"), max_length=64)

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
    telegram_id = models.PositiveBigIntegerField(_("Telegram ID"), null=True)
    fullname = models.CharField(_("Ism Sharifi"), max_length=256, null=True)
    last_name = models.CharField(_("Ism Sharifi"), max_length=256, null=True)
    middle_name = models.CharField(_("Ism Sharifi"), max_length=256, null=True)
    year_of_birth = models.CharField(_("Tug'ilgan yil"), max_length=256, null=True)
    month_of_birth = models.CharField(_("Tug'ilgan oy"), max_length=256, null=True)
    day_of_birth = models.CharField(_("Tug'ilgan kun"), max_length=256, null=True)
    gender = models.PositiveBigIntegerField(_("Gender"), choices=GENDER, null=True)
    username = models.CharField(_("Username"), max_length=32, null=True)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE, null=True)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, null=True)
    murojat_turi = models.CharField(max_length=16, choices=MUROJAT_TURI, default=2, null=True)
    muammo = models.ForeignKey(Muammo, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(SubMuammo, on_delete=models.CASCADE, null=True)
    media = models.FileField(_("Media"), upload_to='muammo_media/', blank=True, null=True)
    location = models.CharField(_("Manzil"), max_length=300, blank=True, null=True)
    description = models.TextField(_("Murojat Matni"), null=True)
    phone = models.CharField(_("Telefon"), max_length=13, null=True)
    reply_message = models.TextField(_("Javob Matni"), default=_("Javob berilmagan"), null=True)
    created = models.DateField(_("Murojat Sanasi"), auto_now_add=True, null=True)
    updated = models.DateField(_("O'zgartish Kiritilgan Sana"), auto_now_add=True, null=True)
    status = models.CharField(_("Murojatchi Statusi"), max_length=32, choices=MUROJATCHI_STATUSI,
                              default=MUROJATCHI_STATUSI[0][0], null=True)

    def __str__(self):
        return f"{self.fullname}"

    class Meta:
        verbose_name = _('Murojatchi')
        verbose_name_plural = _('Murojatchilar')
