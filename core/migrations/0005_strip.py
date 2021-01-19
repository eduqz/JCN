# Generated by Django 3.1.5 on 2021-01-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoj_1', models.ImageField(upload_to='strip/1/', verbose_name='Primeiro emoticon')),
                ('title_1', models.CharField(max_length=12, verbose_name='Primeiro título')),
                ('text_1', models.TextField(max_length=100, verbose_name='Primeiro texto')),
                ('emoj_2', models.ImageField(upload_to='strip/2/', verbose_name='Segundo emoticon')),
                ('title_2', models.CharField(max_length=12, verbose_name='Segundo título')),
                ('text_2', models.TextField(max_length=100, verbose_name='Segundo texto')),
                ('emoj_3', models.ImageField(upload_to='strip/3/', verbose_name='Terceiro emoticon')),
                ('title_3', models.CharField(max_length=12, verbose_name='Terceiro título')),
                ('text_3', models.TextField(max_length=100, verbose_name='Terceiro texto')),
                ('emoj_4', models.ImageField(upload_to='strip/4/', verbose_name='Quarto emoticon')),
                ('title_4', models.CharField(max_length=12, verbose_name='Quarto título')),
                ('text_4', models.TextField(max_length=100, verbose_name='Quarto texto')),
            ],
            options={
                'verbose_name': 'Faixa de informações',
            },
        ),
    ]
