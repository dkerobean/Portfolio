# Generated by Django 4.1.7 on 2023-04-04 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('phone_2', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_link', models.CharField(blank=True, max_length=200, null=True)),
                ('project_description', models.CharField(blank=True, max_length=250, null=True)),
                ('project_category', models.CharField(choices=[('IT', 'IT'), ('MARKETING', 'Marketing')], max_length=150)),
                ('project_image', models.ImageField(blank=True, default='avatar.svg', null=True, upload_to='project_img')),
                ('project_date', models.CharField(max_length=150)),
                ('project_industry', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=150)),
                ('reviewer_position', models.CharField(max_length=150)),
                ('reviewer_message', models.TextField()),
                ('reviewer_image', models.ImageField(blank=True, default='avatar.svg', null=True, upload_to='project_img')),
            ],
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
