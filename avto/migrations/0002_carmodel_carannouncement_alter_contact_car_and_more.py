# Generated by Django 4.2.7 on 2024-02-07 06:55

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_delete_leasing"),
        ("avto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
                (
                    "manufacturer",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="common.manufacturer"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CarAnnouncement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "kuzov",
                    models.CharField(
                        choices=[
                            ("Sedan", "Sedan"),
                            ("Hatchback", "Hatchback"),
                            ("Yo'ltanlamas", "Yoltanlamas"),
                            ("Universal", "Universal"),
                            ("Kabriolet", "Kabriolet"),
                            ("Krossover", "Krossover"),
                            ("Kupe", "Kupe"),
                            ("Limuzin", "Limuzin"),
                            ("Mikroavtobus", "Mikroavtobus"),
                            ("Minivan", "Minivan"),
                            ("Mikroven", "Mikroven"),
                            ("Pikup", "Pikup"),
                            ("Rodster", "Rodster"),
                            ("Furgon", "Furgon"),
                        ],
                        default="Sedan",
                        max_length=32,
                    ),
                ),
                ("price", models.IntegerField(default=0)),
                ("views", models.IntegerField(default=0)),
                ("manufactured_year", models.DateField()),
                ("has_bargain", models.BooleanField(default=False)),
                ("has_leasing", models.BooleanField(default=False)),
                ("engine_capacity", models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                (
                    "fuel_type",
                    models.CharField(
                        choices=[
                            ("Benzin", "Benzin"),
                            ("Gaz-benzin", "Gaz Benzin"),
                            ("Dizel", "Dizel"),
                            ("Elektr", "Elektr"),
                            ("Gibrid", "Gibrid"),
                            ("Gaz", "Gaz"),
                        ],
                        max_length=16,
                    ),
                ),
                (
                    "gearbox",
                    models.CharField(
                        choices=[
                            ("Mexanika", "Mexanika"),
                            ("Avtomat", "Avtomat"),
                            ("Tiptronik", "Tiptronik"),
                            ("Variator", "Variator"),
                            ("Robot", "Robot"),
                        ],
                        max_length=16,
                    ),
                ),
                ("kilometers", models.DecimalField(blank=True, decimal_places=3, max_digits=16, null=True)),
                (
                    "color",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Oq", "Oq"),
                            ("Qaymoq rang", "Qaymoq"),
                            ("Delfin", "Delfin"),
                            ("Mokriy asfalt", "Mokriy"),
                            ("Qora", "Qora"),
                            ("Kumush rang", "Kumush"),
                            ("Saxara (qum rang)", "Saxara"),
                            ("Sadaf-jigarrang", "Sadaf"),
                            ("Sariq-yashil rang", "Sa Ya"),
                            ("Ko'k-havo rang", "Ko Ha"),
                            ("Olcha", "Olcha"),
                            ("Ko'k", "Kok"),
                            ("Qizil", "Qizil"),
                            ("Kulrang", "Kulrang"),
                            ("Jigarrang", "Jigarrang"),
                            ("Bronza", "Bronza"),
                            ("Xameleon", "Xameleon"),
                            ("Moviy", "Moviy"),
                            ("Sariq", "Sariq"),
                            ("Yashil", "Yashil"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "color_condition",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Kraska toza", "Toza"),
                            ("Kraska bor", "Bor"),
                            ("Pyatno bor", "Pyatno"),
                            ("To'liq kraskalangan", "Kraska"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "gear",
                    models.CharField(
                        blank=True,
                        choices=[("Oldi", "Oldi"), ("Orqa", "Orqa"), ("To'liq", "Toliq")],
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "outer_side",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
                            ("Yengil qotishmali disklar", "Yengil"),
                            ("Tonirovka", "Tonirovka"),
                            ("Lyuk", "Lyuk"),
                            ("Tom qopqog'i", "Tom"),
                            ("Kenguryatnik", "Kenguryatnik"),
                            ("Spoyler", "Spoyler"),
                            ("Kuzov to'plami", "Kuzov"),
                            ("Lebyodka", "Lebyo"),
                            ("Shamolto'sgichlar", "Shamol"),
                            ("Duga", "Duga"),
                            ("Yukxona", "Yukxona"),
                            ("Farkop", "Farkop"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "optika",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
                            ("Ksenon", "Kse"),
                            ("Biksenon", "Bik"),
                            ("Xrustal optika", "Xru"),
                            ("Linzali optika", "Lin"),
                            ("Tashqi chiroq proborlari", "Tas"),
                            ("Tumanga qarshi chiroqlar", "Tum"),
                            ("Faralarni yuvish uskunasi", "Far"),
                            ("Faralar korrektori", "Kor"),
                            ("Oyna isitgich", "Oyn"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "salon",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
                            ("Velyur", "Vel"),
                            ("Charm", "Cha"),
                            ("Yog'och", "Yog"),
                            ("Alkantara", "Alk"),
                            ("Kombinatsiyalangan", "Kom"),
                            ("Pardachalar", "Par"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "additional_features",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
                            ("Gidravlikali rul", "Gid"),
                            ("ABS", "Abs"),
                            ("Xavfsizlik yostiqchalari", "Xaf"),
                            ("Qishgi rejim", "Qir"),
                            ("Sport rejimi", "Spo"),
                            ("Turbo gurillash", "Tur"),
                            ("Turbotaymer", "Tay"),
                            ("Signalizatsiya", "Sig"),
                            ("Avtomatik ishga tushish", "Avt"),
                            ("Immobilayzer", "Imo"),
                            ("Kalitsiz kirish", "Kal"),
                            ("Butun elektr paketi", "But"),
                            ("Markaziy qulf", "Mar"),
                            ("Konditsioner", "Kon"),
                            ("Iqlim nazorati", "Iql"),
                            ("Kruiz nazorat", "Kru"),
                            ("Bort kompyuteri", "Bor"),
                            ("Navigatsiya tizimi", "Nav"),
                            ("Multirul", "Mul"),
                            ("Rulni qizdirgich", "Rul"),
                            ("O'rindiq isitgich", "Orn"),
                            ("Orqa o'rindiq qizdirgichi", "Orq"),
                            ("O'rindiq ventilyatsiyasi", "Ven"),
                            ("O'rindiqlar xotirasi", "Xot"),
                            ("Rul xotirasi", "Rux"),
                            ("Parktroniklar", "Par"),
                            ("Orqa ko'rinish kamerasi", "Kam"),
                            ("Datchik chiroqi", "Dat"),
                            ("Yomg'ir datchigi", "Yom"),
                            ("Shinalardagi bosim datchigi", "Shin"),
                            ("Pnevmatik ilgak", "Pnev"),
                            ("O'zgartiriluvchi klirens", "Klir"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                ("additional_info", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="avto/")),
                ("model_of_car", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="avto.carmodel")),
                (
                    "subcategory",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="common.subcategory"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="contact",
            name="car",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="avto.carannouncement"),
        ),
        migrations.AlterField(
            model_name="leasing",
            name="car",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="avto.carannouncement"),
        ),
        migrations.DeleteModel(
            name="Car",
        ),
    ]
