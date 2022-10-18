# Generated by Django 4.1 on 2022-10-13 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Brend_logo', models.CharField(max_length=50)),
                ('Brend_country', models.CharField(max_length=50)),
                ('Brend_rating', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Tel', models.CharField(max_length=50)),
                ('Card_date_valid', models.CharField(max_length=50)),
                ('Shop_cart', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('Create_date', models.CharField(max_length=50)),
                ('Validity_date', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Color', models.CharField(max_length=50)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.brend')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.category')),
                ('Image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.image')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=50)),
                ('shop_logo', models.CharField(max_length=50)),
                ('shop_adress', models.CharField(max_length=50)),
                ('shop_contact', models.CharField(max_length=50)),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.boss')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shopping_date', models.DateTimeField(auto_now_add=True)),
                ('Price_sum', models.CharField(max_length=50)),
                ('Card_number', models.CharField(max_length=50)),
                ('Brend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.brend')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.customer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.product')),
                ('Shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.shop')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.shop'),
        ),
        migrations.AddField(
            model_name='product',
            name='Size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.size'),
        ),
        migrations.CreateModel(
            name='Payment_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.customer')),
                ('Shopping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.shopping')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.customer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsosiyApp.product')),
            ],
        ),
    ]
