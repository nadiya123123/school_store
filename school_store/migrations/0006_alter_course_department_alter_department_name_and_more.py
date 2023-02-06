# Generated by Django 4.1.6 on 2023-02-05 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_store', '0005_alter_formdata_course_alter_formdata_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_store.department'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_store.course'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_store.department'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='materials',
            field=models.ManyToManyField(to='school_store.material'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='purpose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_store.purpose'),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purpose',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
