# Generated by Django 4.1.1 on 2022-09-11 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_consumeruser_alter_transportuser_contact_number'),
        ('transport', '0005_updatetransportprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateStudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('batch', models.IntegerField()),
                ('section', models.CharField(max_length=100)),
                ('user_consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.consumeruser')),
            ],
        ),
    ]
