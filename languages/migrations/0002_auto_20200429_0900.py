# Generated by Django 3.0.5 on 2020-04-29 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradigm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('languages', models.ManyToManyField(to='languages.Language')),
            ],
        ),
        migrations.AlterField(
            model_name='language',
            name='paradigm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Paradigm'),
        ),
    ]
