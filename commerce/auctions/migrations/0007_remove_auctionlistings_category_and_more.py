# Generated by Django 4.0.2 on 2022-03-08 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auctionlistings_seller_comments_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlistings',
            name='category',
        ),
        migrations.RemoveField(
            model_name='auctionlistings',
            name='seller',
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='buyer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='categories',
            field=models.CharField(choices=[('C', 'Clothing'), ('F', 'Furniture'), ('H', 'Household Items'), ('E', 'Electronic Items')], default='No category', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlistings'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlistings')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.DecimalField(decimal_places=2, max_digits=99)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlistings')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
