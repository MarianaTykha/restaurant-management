# Generated by Django 5.1.4 on 2025-01-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chef",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="chef",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="dish",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="dishes/"),
        ),
        migrations.AddField(
            model_name="dish",
            name="servings",
            field=models.IntegerField(default=1),
        ),
    ]
