# Generated by Django 4.0.2 on 2022-03-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlistings',
            name='category',
            field=models.CharField(choices=[('C', 'Clothing'), ('F', 'Furniture'), ('H', 'Household Items'), ('E', 'Electronic Items')], default='blank', max_length=1),
            preserve_default=False,
        ),
    ]
