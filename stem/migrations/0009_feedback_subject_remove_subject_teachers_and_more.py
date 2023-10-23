# Generated by Django 4.1.2 on 2022-11-23 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stem", "0008_alter_teacherprofile_department"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stem.sessionsubject",
            ),
        ),
        migrations.RemoveField(
            model_name="subject",
            name="teachers",
        ),
        migrations.AddField(
            model_name="subject",
            name="teachers",
            field=models.ManyToManyField(
                blank=True, null=True, to="stem.teacherprofile"
            ),
        ),
    ]
