# Generated by Django 4.1.11 on 2023-09-20 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('texnoApp', '0004_authorimage_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/')),
                ('alt_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='full_text',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author_images',
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('all', 'ALL'), ('software', 'Software'), ('hardware', 'Hardware'), ('biology', 'Biology')], default='all', max_length=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='AuthorImage',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='texnoApp.project'),
        ),
    ]
