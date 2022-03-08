# Generated by Django 4.0.2 on 2022-03-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_auctionlistings_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='categories',
            field=models.CharField(choices=[('C', 'Clothing'), ('F', 'Furniture'), ('H', 'Household Items'), ('E', 'Electronic Items'), ('T', 'Toys')], max_length=1),
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='product',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='product',
            field=models.ManyToManyField(to='auctions.AuctionListings'),
        ),
    ]
