# Generated by Django 5.1.6 on 2025-03-18 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='SAMLConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sso_url', models.URLField(help_text='Sign-in URL')),
                ('slo_url', models.URLField(help_text='Sign-out URL')),
                ('sp_metadata_url', models.URLField(help_text='https://host/saml/metadata')),
                ('idp_id', models.URLField(help_text='Identity Provider ID')),
                ('idp_cert', models.TextField(help_text='x509cert')),
                ('uid', models.CharField(help_text='eg eduPersonPrincipalName', max_length=100)),
                ('name', models.CharField(blank=True, help_text='eg displayName', max_length=100, null=True)),
                ('email', models.CharField(blank=True, help_text='eg mail', max_length=100, null=True)),
                ('groups', models.CharField(blank=True, help_text='eg isMemberOf', max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, help_text='eg gn', max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, help_text='eg sn', max_length=100, null=True)),
                ('user_logo', models.CharField(blank=True, help_text='eg jpegPhoto', max_length=100, null=True)),
                ('role', models.CharField(blank=True, help_text='eduPersonPrimaryAffiliation', max_length=100, null=True)),
                ('verified_email', models.BooleanField(default=False, help_text='Mark email as verified')),
                ('email_authentication', models.BooleanField(default=False, help_text='Use email authentication too')),
                ('remove_from_groups', models.BooleanField(default=False, help_text='Automatically remove from groups')),
                ('save_saml_response_logs', models.BooleanField(default=True)),
                ('social_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saml_configurations', to='socialaccount.socialapp')),
            ],
            options={
                'verbose_name': 'SAML Configuration',
                'verbose_name_plural': 'SAML Configurations',
                'unique_together': {('social_app', 'idp_id')},
            },
        ),
    ]
