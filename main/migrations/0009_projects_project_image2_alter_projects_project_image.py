# Generated by Django 4.1.7 on 2023-04-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_socials_alter_review_reviewer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_image2',
            field=models.ImageField(blank=True, default='product_img/placeholder.png', null=True, upload_to='project_img'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_image',
            field=models.ImageField(blank=True, default='product_img/placeholder.png', null=True, upload_to='project_img'),
        ),
    ]