# Generated by Django 3.0.4 on 2020-04-14 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_sport_beauty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('type', models.IntegerField(choices=[(0, 'Sport'), (1, 'Beauty')], default=0)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=15)),
                ('slug', models.SlugField(max_length=200)),
                ('price', models.DecimalField(decimal_places=3, max_digits=100)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='form_sport_beauty.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
