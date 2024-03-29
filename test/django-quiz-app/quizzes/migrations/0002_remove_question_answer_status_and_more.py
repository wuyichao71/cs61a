# Generated by Django 4.1.1 on 2022-09-15 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="answer_status",
        ),
        migrations.AlterField(
            model_name="freetextanswer",
            name="question",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="quizzes.question"
            ),
        ),
        migrations.AlterField(
            model_name="multiplechoiceanswer",
            name="question",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="quizzes.question"
            ),
        ),
    ]
