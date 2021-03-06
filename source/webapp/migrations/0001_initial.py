# Generated by Django 3.1.7 on 2021-03-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mail', models.EmailField(default='ali@mail.com', max_length=254)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'книга',
                'db_table': 'books',
            },
        ),
    ]
