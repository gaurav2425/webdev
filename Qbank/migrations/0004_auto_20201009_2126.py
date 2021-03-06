# Generated by Django 3.1.2 on 2020-10-09 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Qbank', '0003_auto_20200918_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='last_updated',
        ),
        migrations.AlterField(
            model_name='topic',
            name='QbankModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Qbank.qbankmodel'),
        ),
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopicname', models.CharField(max_length=255)),
                ('Topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Qbank.topic')),
            ],
        ),
    ]
