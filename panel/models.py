from django.db import models
from django.utils.translation import ugettext_lazy as _


class Mahalla(models.Model):
    title = models.CharField(_("Mahalla nomi"), max_length=256)
    location = models.CharField(_("Manzil"), max_length=256)
    phone = models.CharField(_("Telefon"), max_length=13)

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
        ('yopiq', _('yopiq')),
        ('ochiq', _('ochiq')),
    )
    id = models.AutoField(primary_key=True)
    telegram_id = models.PositiveBigIntegerField(_("Telegram ID"))
    fullname = models.CharField(_("Ism Sharifi"), max_length=256)
    username = models.CharField(_("Username"), max_length=32)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE, default=0)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    muammo = models.ForeignKey(Muammo, on_delete=models.CASCADE)
    category = models.ForeignKey(SubMuammo, on_delete=models.CASCADE, null=True, blank=True, default=_('Boshqa'))
    media = models.FileField(_("Media"), upload_to='muammo_media/', blank=True, null=True)
    location = models.CharField(_("Manzil"), max_length=300, blank=True, null=True)
    description = models.TextField(_("Qisqacha Ma'lumot"))
    phone = models.CharField(_("Telefon"), max_length=13)
    status = models.CharField(_("Murojatchi Statusi"), max_length=32, choices=MUROJATCHI_STATUSI)
    created = models.DateField(_("Murojat Sanasi"), auto_now_add=True)
    updated = models.DateField(_("O'zgartish Kiritilgan Sana"), auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('Murojatchi')
        verbose_name_plural = _('Murojatchilar')
