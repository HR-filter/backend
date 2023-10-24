# Generated by Django 3.2.3 on 2023-10-23 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('education_level', models.CharField(blank=True, choices=[('school', 'Среднее образование'), ('college', 'Средне-специальное образование'), ('university', 'Высшее образование'), ('postgrad', 'Ученая степень')], max_length=100, null=True, verbose_name='Уровень образования')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('work_experience', models.CharField(blank=True, max_length=100, null=True, verbose_name='Опыт работы')),
                ('grade', models.CharField(blank=True, choices=[('junior', 'Junior'), ('middle', 'Middle')], max_length=100, null=True, verbose_name='Грэйд')),
                ('description', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='student_photos/', verbose_name='Фото')),
                ('resume', models.FileField(blank=True, null=True, upload_to='student_resumes/', verbose_name='Резюме')),
                ('academic_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.academicstatus', verbose_name='Учебный статус')),
                ('contact_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.contactinfo', verbose_name='Контактная информация')),
                ('employment_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.employmentstatus', verbose_name='Статус трудоустройства')),
                ('skills', models.ManyToManyField(blank=True, related_name='students', to='students.Skill', verbose_name='Навыки')),
                ('training_status', models.ManyToManyField(blank=True, through='students.StudentPosition', to='students.Position', verbose_name='Предпочтительные должности')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorited_resumes', to='students.studentresume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='studentposition',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_positions', to='students.studentresume', verbose_name='Студент'),
        ),
        migrations.DeleteModel(
            name='StudentUser',
        ),
        migrations.AddConstraint(
            model_name='favoriteresume',
            constraint=models.UniqueConstraint(fields=('user', 'resume'), name='unique_user_resume'),
        ),
    ]