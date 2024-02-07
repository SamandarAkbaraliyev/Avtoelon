from django.db.models import TextChoices


class Kuzov(TextChoices):
    SEDAN = 'Sedan'
    HATCHBACK = 'Hatchback'
    YOLTANLAMAS = "Yo'ltanlamas"
    UNIVERSAL = 'Universal'
    KABRIOLET = 'Kabriolet'
    KROSSOVER = 'Krossover'
    KUPE = 'Kupe'
    LIMUZIN = 'Limuzin'
    MIKROAVTOBUS = 'Mikroavtobus'
    MINIVAN = 'Minivan'
    MIKROVEN = 'Mikroven'
    PIKUP = 'Pikup'
    RODSTER = 'Rodster'
    FURGON = 'Furgon'


class FuelType(TextChoices):
    BENZIN = 'Benzin'
    GAZ_BENZIN = 'Gaz-benzin'
    DIZEL = 'Dizel'
    ELEKTR = 'Elektr'
    GIBRID = 'Gibrid'
    GAZ = 'Gaz'


class Gearbox(TextChoices):
    MEXANIKA = 'Mexanika'
    AVTOMAT = 'Avtomat'
    TIPTRONIK = 'Tiptronik'
    VARIATOR = 'Variator'
    ROBOT = 'Robot'


class Color(TextChoices):
    OQ = 'Oq'
    QAYMOQ = 'Qaymoq rang'
    DELFIN = 'Delfin'
    MOKRIY = 'Mokriy asfalt'
    QORA = 'Qora'
    KUMUSH = 'Kumush rang'
    SAXARA = 'Saxara (qum rang)'
    SADAF = 'Sadaf-jigarrang'
    SA_YA = 'Sariq-yashil rang'
    KO_HA = "Ko'k-havo rang"
    OLCHA = 'Olcha'
    KOK = "Ko'k"
    QIZIL = 'Qizil'
    KULRANG = 'Kulrang'
    JIGARRANG = 'Jigarrang'
    BRONZA = 'Bronza'
    XAMELEON = 'Xameleon'
    MOVIY = 'Moviy'
    SARIQ = 'Sariq'
    YASHIL = 'Yashil'


class ColorCondition(TextChoices):
    TOZA = 'Kraska toza'
    BOR = 'Kraska bor'
    PYATNO = 'Pyatno bor'
    KRASKA = "To'liq kraskalangan"


class Gear(TextChoices):
    OLDI = 'Oldi'
    ORQA = 'Orqa'
    TOLIQ = "To'liq"


class Outer(TextChoices):
    YENGIL = 'Yengil qotishmali disklar'
    TONIROVKA = 'Tonirovka'
    LYUK = 'Lyuk'
    TOM = 'Tom qopqog\'i'
    KENGURYATNIK = 'Kenguryatnik'
    SPOYLER = 'Spoyler'
    KUZOV = 'Kuzov to\'plami'
    LEBYO = 'Lebyodka'
    SHAMOL = 'Shamolto\'sgichlar'
    DUGA = 'Duga'
    YUKXONA = 'Yukxona'
    FARKOP = 'Farkop'


class Optika(TextChoices):
    KSE = 'Ksenon'
    BIK = 'Biksenon'
    XRU = 'Xrustal optika'
    LIN = 'Linzali optika'
    TAS = 'Tashqi chiroq proborlari'
    TUM = 'Tumanga qarshi chiroqlar'
    FAR = 'Faralarni yuvish uskunasi'
    KOR = 'Faralar korrektori'
    OYN = 'Oyna isitgich'


class Salon(TextChoices):
    VEL = 'Velyur'
    CHA = 'Charm'
    YOG = "Yog'och"
    ALK = 'Alkantara'
    KOM = 'Kombinatsiyalangan'
    PAR = 'Pardachalar'


class Media(TextChoices):
    AUD = 'Audiosistema'
    TEL = 'O\'rnatma telefon'
    BLU = 'Bluetooth'
    CD = 'CD'
    ALM = 'CD-almashtirgich'
    MP3 = 'MP3'
    USB = 'USB'
    DVD = 'DVD'
    DVA = 'DVD-almashtirgich'
    SAB = 'Sabvufer'


class AdditionalFeatures(TextChoices):
    GID = 'Gidravlikali rul'
    ABS = 'ABS'
    XAF = 'Xavfsizlik yostiqchalari'
    QIR = 'Qishgi rejim'
    SPO = 'Sport rejimi'
    TUR = 'Turbo gurillash'
    TAY = 'Turbotaymer'
    SIG = 'Signalizatsiya'
    AVT = 'Avtomatik ishga tushish'
    IMO = 'Immobilayzer'
    KAL = 'Kalitsiz kirish'
    BUT = 'Butun elektr paketi'
    MAR = 'Markaziy qulf'
    KON = 'Konditsioner'
    IQL = 'Iqlim nazorati'
    KRU = 'Kruiz nazorat'
    BOR = 'Bort kompyuteri'
    NAV = 'Navigatsiya tizimi'
    MUL = 'Multirul'
    RUL = 'Rulni qizdirgich'
    ORN = "O'rindiq isitgich"
    ORQ = "Orqa o'rindiq qizdirgichi"
    VEN = "O'rindiq ventilyatsiyasi"
    XOT = "O'rindiqlar xotirasi"
    RUX = 'Rul xotirasi'
    PAR = 'Parktroniklar'
    KAM = 'Orqa ko\'rinish kamerasi'
    DAT = 'Datchik chiroqi'
    YOM = 'Yomg\'ir datchigi'
    SHIN = 'Shinalardagi bosim datchigi'
    PNEV = 'Pnevmatik ilgak'
    KLIR = 'O\'zgartiriluvchi klirens'
