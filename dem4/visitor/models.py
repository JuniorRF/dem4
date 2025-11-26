from django.db import models


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="IP-адрес")
    user_agent = models.CharField(max_length=255, blank=True, null=True, verbose_name="User-Agent")
    path = models.CharField(max_length=255, verbose_name="Посещенная страница")
    referer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Реферер")
    visit_time = models.DateTimeField(auto_now_add=True, verbose_name="Время посещения")
    user = models.CharField(max_length=255, default="неавторизованный", verbose_name="Пользователь")

    def __str__(self):
        return f"{self.user} посетил {self.path} в {self.visit_time} с {self.ip_address}"

    class Meta:
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"
