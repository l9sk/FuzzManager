# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-04 19:51
from __future__ import unicode_literals

from django.db import migrations


def add_permissions(apps, schema_editor):
    # add all permissions to existing users, which was the pre-migrate state
    User = apps.get_model('crashmanager', 'User')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')

    content_type = ContentType.objects.get_for_model(User)
    for user in User.objects.all():
        perms = user.user.user_permissions
        perms.add(Permission.objects.get(content_type=content_type, codename='view_covmanager'))
        perms.add(Permission.objects.get(content_type=content_type, codename='view_crashmanager'))
        perms.add(Permission.objects.get(content_type=content_type, codename='view_ec2spotmanager'))


class Migration(migrations.Migration):

    dependencies = [
        ('crashmanager', '0019_bucket_optimizedsignature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('view_crashmanager', 'Can see CrashManager app'),
                                     ('view_covmanager', 'Can see CovManager app'),
                                     ('view_ec2spotmanager', 'Can see EC2SpotManager app'))},
        ),
        migrations.RunPython(add_permissions, migrations.RunPython.noop),
    ]
