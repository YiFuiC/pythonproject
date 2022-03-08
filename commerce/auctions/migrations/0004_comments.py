# Generated by Django 4.0.2 on 2022-03-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_product_name_auctionlistings_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review', models.CharField(max_length=10000000000)),
                ('ratings', models.CharField(choices=[('1', 'Terrible'), ('2', 'Bad'), ('3', 'Average'), ('4', 'Good'), ('5', 'Excellent')], max_length=1)),
            ],
        ),
    ]