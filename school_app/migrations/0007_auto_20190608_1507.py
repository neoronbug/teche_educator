# Generated by Django 2.1.7 on 2019-06-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0006_auto_20190608_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile_info',
            name='edu_awards',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='edu_services',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac2_dsg',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac2_name',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac2_prlf',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac2_qlf',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac3_dsg',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac3_name',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac3_prlf',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac3_qlf',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac4_dsg',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac4_name',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac4_prlf',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac4_qlf',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac5_dsg',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac5_name',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac5_prlf',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac5_qlf',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac6_dsg',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac6_name',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac6_prlf',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='fac6_qlf',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='portfolio_site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='principal_image',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='principal_message',
            field=models.CharField(default='name', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='sch_featured_img1',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='sch_featured_img2',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='sch_featured_img3',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile_info',
            name='school_logo',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]