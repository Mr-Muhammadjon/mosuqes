# Generated by Django 3.1.5 on 2021-03-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210322_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='F,I,SH')),
                ('email', models.EmailField(max_length=100, verbose_name='Elektron pochta')),
                ('phone', models.CharField(max_length=20, verbose_name='Telfon raqami')),
                ('message', models.TextField(verbose_name='Xabari')),
            ],
            options={
                'verbose_name': 'Aloqa',
                'verbose_name_plural': 'Aloqalar',
            },
        ),
    ]
