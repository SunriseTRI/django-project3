# Generated by Django 4.2.2 on 2023-07-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_order_comment_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(max_length=255, null=True),
        ),
    ]