# Generated by Django 2.2.6 on 2019-10-05 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Department', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('Date_of_Birth', models.DateTimeField()),
                ('Gender', models.CharField(max_length=10)),
                ('Postion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='YearlySaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateTimeField()),
                ('TotalAmount', models.IntegerField()),
                ('YearlyDifference', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='YearlyExpenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateTimeField()),
                ('TotalAmount', models.IntegerField()),
                ('YearlyDifference', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlySaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.DateTimeField()),
                ('TotalSaved', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.DateTimeField()),
                ('TotalAmount', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobName', models.CharField(blank=True, max_length=40)),
                ('Income', models.IntegerField()),
                ('Increment', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Employee')),
            ],
        ),
    ]
