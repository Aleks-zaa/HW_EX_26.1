# Generated by Django 5.0.7 on 2024-08-02 15:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Donation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="укажите сумму",
                        verbose_name="Сумма пожертвования",
                    ),
                ),
                (
                    "session_id",
                    models.CharField(
                        blank=True,
                        help_text="укажите id сессии",
                        max_length=250,
                        null=True,
                        verbose_name="id сессии",
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        help_text="укажите ссылку на оплату",
                        max_length=400,
                        null=True,
                        verbose_name="ссылка на оплату",
                    ),
                ),
                (
                    "user_d",
                    models.ForeignKey(
                        blank=True,
                        help_text="укажите пользователя",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пожертвование",
                "verbose_name_plural": "Пожертвования",
            },
        ),
    ]