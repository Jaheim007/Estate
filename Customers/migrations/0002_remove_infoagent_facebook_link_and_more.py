# Generated by Django 4.0.5 on 2022-06-17 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoagent',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='infoagent',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='infoagent',
            name='linkedin_link',
        ),
        migrations.RemoveField(
            model_name='infoagent',
            name='skype_link',
        ),
        migrations.RemoveField(
            model_name='infoagent',
            name='twitter_link',
        ),
        migrations.RemoveField(
            model_name='infoagent',
            name='whatsapp_number',
        ),
        migrations.CreateModel(
            name='SocialAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=255)),
                ('social_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_agent_social_agent', to='Customers.infoagent')),
            ],
        ),
    ]
