# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BpcsEch(models.Model):
    hord = models.CharField(db_column='HORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hedte = models.DateField(db_column='HEDTE', blank=True, null=True)  # Field name made lowercase.
    hcust = models.CharField(db_column='HCUST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hcpo = models.CharField(db_column='HCPO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hsdte = models.DateField(db_column='HSDTE', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(blank=True, null=True)
    hwhse = models.CharField(db_column='HWHSE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPCS_ECH'


class BpcsEchSettings(models.Model):
    lastorderid = models.IntegerField(db_column='lastOrderID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPCS_ECH_SETTINGS'


class BpcsEcl(models.Model):
    lord = models.CharField(db_column='LORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lline = models.DecimalField(db_column='LLINE', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lprod = models.CharField(db_column='LPROD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lqord = models.DecimalField(db_column='LQORD', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lwhs = models.CharField(db_column='LWHS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPCS_ECL'


class BpcsExport(models.Model):
    salesorder = models.CharField(db_column='salesOrder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uniqueident = models.CharField(db_column='uniqueIdent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    messagecode = models.CharField(db_column='messageCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    messagename = models.CharField(db_column='messageName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    confirmationdate = models.DateTimeField(db_column='confirmationDate', blank=True, null=True)  # Field name made lowercase.
    errorcode = models.CharField(db_column='errorCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errormessage = models.TextField(db_column='errorMessage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lineid = models.CharField(db_column='lineId', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPCS_EXPORT'


class BpcsMmExport(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    mmdate = models.DateField(db_column='MMdate', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(max_length=50, blank=True, null=True)
    lastpreparedate = models.DateField(db_column='lastPrepareDate', blank=True, null=True)  # Field name made lowercase.
    lastsenddate = models.DateField(db_column='lastSendDate', blank=True, null=True)  # Field name made lowercase.
    sendqty = models.IntegerField(db_column='sendQty', blank=True, null=True)  # Field name made lowercase.
    prepareqty = models.IntegerField(db_column='prepareQty', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BPCS_MM_EXPORT'


class BpcsMmExportDetails(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    mmdate = models.DateField(db_column='MMDate', blank=True, null=True)  # Field name made lowercase.
    warehousecode = models.CharField(db_column='warehouseCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    namebpcs = models.CharField(db_column='nameBPCS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    idmovement = models.CharField(db_column='idMovement', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contcode = models.CharField(db_column='contCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(blank=True, null=True)
    filename = models.CharField(db_column='fileName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPCS_MM_EXPORT_DETAILS'


class BpcsMmExportSettings(models.Model):
    lastid = models.BigIntegerField(db_column='lastID')  # Field name made lowercase.
    qtytransactionperfile = models.IntegerField(db_column='qtyTransactionPerFile')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPCS_MM_EXPORT_SETTINGS'


class Aaaa(models.Model):
    imie = models.CharField(max_length=50, blank=True, null=True)
    nazwisko = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_aaaa'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Box(models.Model):
    idpallet = models.ForeignKey('Pallet', models.DO_NOTHING, db_column='idPallet')  # Field name made lowercase.
    boxcode = models.CharField(db_column='BoxCode', max_length=50)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status')  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate')  # Field name made lowercase.
    creationoperator = models.IntegerField(db_column='CreationOperator')  # Field name made lowercase.
    idmachine = models.IntegerField(db_column='idMachine', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'box'


class Config(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    activeyear = models.IntegerField(db_column='activeYear')  # Field name made lowercase.
    forcelot = models.BooleanField(db_column='forceLot')  # Field name made lowercase.
    forcefifo = models.BooleanField(db_column='forceFifo')  # Field name made lowercase.
    forcewarehouse = models.IntegerField(db_column='forceWarehouse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'config'


class Connection(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    server = models.CharField(max_length=50)
    port = models.IntegerField()
    used = models.BooleanField()
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connection'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Packaging(models.Model):
    idbox = models.ForeignKey(Box, models.DO_NOTHING, db_column='idBox')  # Field name made lowercase.
    slot = models.CharField(db_column='sLot', max_length=50)  # Field name made lowercase.
    sserial1 = models.CharField(db_column='sSerial1', unique=True, max_length=50)  # Field name made lowercase.
    sserial2 = models.CharField(db_column='sSerial2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField()
    idoperator = models.IntegerField(db_column='idOperator', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    idmachine = models.IntegerField(db_column='idMachine', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packaging'


class Pallet(models.Model):
    idprod = models.IntegerField(db_column='idProd')  # Field name made lowercase.
    palletcode = models.CharField(db_column='PalletCode', max_length=50)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status')  # Field name made lowercase.
    exported = models.BooleanField(db_column='Exported')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    creationoperator = models.IntegerField(db_column='CreationOperator')  # Field name made lowercase.
    exporteddate = models.DateTimeField(db_column='ExportedDate', blank=True, null=True)  # Field name made lowercase.
    exportedoperator = models.IntegerField(db_column='ExportedOperator', blank=True, null=True)  # Field name made lowercase.
    idwarehouse = models.IntegerField(db_column='idWarehouse')  # Field name made lowercase.
    imptodcp = models.BooleanField(db_column='impToDCP')  # Field name made lowercase.
    idline = models.IntegerField(db_column='idLine', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pallet'


class Pattern(models.Model):
    serial = models.CharField(max_length=50, blank=True, null=True)
    lot = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    filename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pattern'


class Productsdata(models.Model):
    type = models.CharField(max_length=50)
    qinbox = models.IntegerField()
    qboxonpallet = models.IntegerField()
    twoscans = models.BooleanField()
    imported = models.BooleanField()
    palletno = models.IntegerField(db_column='palletNo')  # Field name made lowercase.
    boxno = models.IntegerField(db_column='boxNo')  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField()
    unitdescription = models.CharField(db_column='unitDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    surowiec = models.IntegerField(blank=True, null=True)
    nameen = models.CharField(db_column='nameEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idprodline = models.IntegerField(db_column='idProdLine', blank=True, null=True)  # Field name made lowercase.
    valuecreation = models.DecimalField(db_column='valueCreation', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valuecreationcurrency = models.CharField(db_column='valueCreationCurrency', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productweight = models.FloatField(db_column='productWeight', blank=True, null=True)  # Field name made lowercase.
    palletweight = models.FloatField(db_column='palletWeight', blank=True, null=True)  # Field name made lowercase.
    palletdimwidth = models.IntegerField(db_column='palletDimWidth', blank=True, null=True)  # Field name made lowercase.
    palletdimlength = models.IntegerField(db_column='palletDimLength', blank=True, null=True)  # Field name made lowercase.
    palletdimheight = models.IntegerField(db_column='palletDimHeight', blank=True, null=True)  # Field name made lowercase.
    productweightgross = models.FloatField(db_column='productWeightGross', blank=True, null=True)  # Field name made lowercase.
    namebpcs = models.CharField(db_column='nameBPCS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lblpalletlastnumber = models.IntegerField(db_column='lblPalletLastNumber', blank=True, null=True)  # Field name made lowercase.
    lblpalletmaxnumber = models.IntegerField(db_column='lblPalletMaxNumber', blank=True, null=True)  # Field name made lowercase.
    minqty = models.IntegerField(db_column='minQty', blank=True, null=True)  # Field name made lowercase.
    warningqty = models.IntegerField(db_column='warningQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productsData'


class Role(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    role = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'role'


class Rwreason(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    product = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    qty = models.IntegerField()
    barcode = models.CharField(max_length=50)
    reason = models.TextField()  # This field type is a guess.
    operator = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rwreason'


class Scans(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    pallet = models.CharField(max_length=50, blank=True, null=True)
    lot = models.CharField(max_length=50, blank=True, null=True)
    box = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    warehouse = models.CharField(max_length=3, blank=True, null=True)
    exported = models.DateTimeField(blank=True, null=True)
    verified = models.CharField(max_length=10, blank=True, null=True)
    number = models.DecimalField(db_column='NUMBER', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    barcode2 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scans'


class Session(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    pallet = models.CharField(max_length=50, blank=True, null=True)
    box = models.CharField(max_length=50, blank=True, null=True)
    lot = models.CharField(max_length=20, blank=True, null=True)
    exported = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tbommaterials(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    idbom = models.IntegerField(db_column='idBom')  # Field name made lowercase.
    idmaterial = models.IntegerField(db_column='idMaterial')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tBomMaterials'


class Tbomproducts(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    idbom = models.IntegerField(db_column='idBom')  # Field name made lowercase.
    idproduct = models.IntegerField(db_column='idProduct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tBomProducts'


class Tboms(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tBoms'


class Tboxlabelcounter(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tBoxLabelCounter'


class Tcardboardstockmovements(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    productid = models.IntegerField(db_column='productId')  # Field name made lowercase.
    quantity = models.DecimalField(max_digits=18, decimal_places=2)
    timestamp = models.DateTimeField(db_column='timeStamp')  # Field name made lowercase.
    movecode = models.CharField(db_column='moveCode', max_length=16)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tCardboardStockMovements'


class Tcardboardstocks(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    productid = models.IntegerField(db_column='productId')  # Field name made lowercase.
    quantity = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tCardboardStocks'


class Tcompany(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    shortname = models.CharField(db_column='shortName', max_length=100)  # Field name made lowercase.
    longname1 = models.CharField(db_column='longName1', max_length=50)  # Field name made lowercase.
    longname2 = models.CharField(db_column='longName2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    nip = models.CharField(max_length=50, blank=True, null=True)
    regon = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=50, blank=True, null=True)
    bankaccount = models.CharField(db_column='bankAccount', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tCompany'


class Tcontainer(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    kod = models.CharField(unique=True, max_length=50)
    zawartosc = models.IntegerField()
    ilosc = models.DecimalField(max_digits=9, decimal_places=4)
    magazyn = models.IntegerField()
    datautworzenia = models.DateTimeField(db_column='dataUtworzenia')  # Field name made lowercase.
    blokada = models.IntegerField()
    komentarz = models.TextField(blank=True, null=True)
    lot = models.CharField(max_length=50, blank=True, null=True)
    dostawa = models.BigIntegerField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deliverystatus = models.BooleanField(db_column='deliveryStatus', blank=True, null=True)  # Field name made lowercase.
    newlot = models.BooleanField(db_column='newLot', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    invstatus = models.IntegerField(db_column='invStatus', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    pallet = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tContainer'
        unique_together = (('blokada', 'id', 'kod', 'zawartosc', 'ilosc', 'magazyn', 'lot', 'userid', 'invstatus', 'price', 'currency'), ('id', 'magazyn', 'blokada'),)


class Tcontainerhistory(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    moveid = models.IntegerField(db_column='moveId', blank=True, null=True)  # Field name made lowercase.
    containerid = models.CharField(db_column='containerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    warehousefromid = models.IntegerField(db_column='warehouseFromId', blank=True, null=True)  # Field name made lowercase.
    warehousetoid = models.IntegerField(db_column='warehouseToId', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    deliverynote = models.CharField(db_column='deliveryNote', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tContainerHistory'


class Tcontainerwashing(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    partnumber = models.CharField(db_column='partNumber', max_length=50)  # Field name made lowercase.
    partname = models.CharField(db_column='partName', max_length=50)  # Field name made lowercase.
    lotnumber = models.CharField(db_column='lotNumber', max_length=50)  # Field name made lowercase.
    containerid = models.BigIntegerField(db_column='containerId')  # Field name made lowercase.
    quantity = models.IntegerField()
    warehouseid = models.IntegerField(db_column='warehouseId')  # Field name made lowercase.
    washingdate = models.DateTimeField(db_column='washingDate')  # Field name made lowercase.
    washingstation = models.CharField(db_column='washingStation', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tContainerWashing'


class Tcontracts(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    active = models.BooleanField()
    deleted = models.BooleanField()
    idsupp = models.IntegerField(db_column='idSupp')  # Field name made lowercase.
    idprod = models.IntegerField(db_column='idProd')  # Field name made lowercase.
    price = models.DecimalField(max_digits=19, decimal_places=4)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    contractid = models.CharField(db_column='contractId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tContracts'


class Tcountryoforigin(models.Model):
    country = models.CharField(db_column='Country', max_length=50)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tCountryOfOrigin'


class Tcurrency(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tCurrency'


class Tcustomers(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    custcode = models.CharField(db_column='custCode', max_length=50)  # Field name made lowercase.
    custname = models.CharField(db_column='custName', max_length=50)  # Field name made lowercase.
    custaddress1 = models.CharField(db_column='custAddress1', max_length=50)  # Field name made lowercase.
    custaddress2 = models.CharField(db_column='custAddress2', max_length=50)  # Field name made lowercase.
    custaddress3 = models.CharField(db_column='custAddress3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custcountry = models.CharField(db_column='custCountry', max_length=50)  # Field name made lowercase.
    custvatcode = models.CharField(db_column='custVatCode', max_length=50)  # Field name made lowercase.
    custcurrency = models.CharField(db_column='custCurrency', max_length=50)  # Field name made lowercase.
    custcontactperson = models.CharField(db_column='custContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custcontactemail = models.CharField(db_column='custContactEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custcontactphone = models.CharField(db_column='custContactPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custactive = models.BooleanField(db_column='custActive')  # Field name made lowercase.
    custcreationdate = models.DateField(db_column='custCreationDate')  # Field name made lowercase.
    custcreatedoperator = models.IntegerField(db_column='custCreatedOperator')  # Field name made lowercase.
    custcomment = models.TextField(db_column='custComment')  # Field name made lowercase.
    ourid = models.CharField(db_column='ourID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ouridupdate = models.CharField(db_column='ourIDUpdate', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tCustomers'


class Tdailyinventory(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    emptylocations = models.IntegerField(db_column='EmptyLocations', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    completedat = models.DateTimeField(db_column='CompletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDailyInventory'


class Tdailyinventoryconfirmations(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    dailyinventoryid = models.IntegerField(db_column='DailyInventoryId')  # Field name made lowercase.
    locationcode = models.CharField(db_column='LocationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    palletcode = models.CharField(db_column='PalletCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmedpalletcode = models.CharField(db_column='ConfirmedPalletCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    boxcode = models.CharField(db_column='BoxCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmedboxcode = models.CharField(db_column='ConfirmedBoxCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    confirmedat = models.DateTimeField(db_column='ConfirmedAt', blank=True, null=True)  # Field name made lowercase.
    confirmedby = models.IntegerField(db_column='ConfirmedBy', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDailyInventoryConfirmations'


class Tdashboardminstock(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    iduser = models.IntegerField(db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    idpart = models.IntegerField(db_column='idPart', blank=True, null=True)  # Field name made lowercase.
    minvalue = models.IntegerField(db_column='minValue', blank=True, null=True)  # Field name made lowercase.
    warninglvl = models.IntegerField(db_column='warningLvl', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDashboardMinStock'


class Tdelivery(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    delcode = models.CharField(db_column='delCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deldate = models.DateTimeField(db_column='delDate', blank=True, null=True)  # Field name made lowercase.
    deluser = models.IntegerField(db_column='delUser', blank=True, null=True)  # Field name made lowercase.
    delsupp = models.IntegerField(db_column='delSupp', blank=True, null=True)  # Field name made lowercase.
    delblocked = models.IntegerField(db_column='delBlocked', blank=True, null=True)  # Field name made lowercase.
    delqualityblocked = models.IntegerField(db_column='delQualityBlocked', blank=True, null=True)  # Field name made lowercase.
    delorderid = models.IntegerField(db_column='delOrderId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDelivery'


class Tdeliveryratingparams(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    paramname = models.CharField(db_column='paramName', max_length=50)  # Field name made lowercase.
    description = models.CharField(max_length=50)
    maxvalue = models.IntegerField(db_column='maxValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tDeliveryRatingParams'


class Tdeliveryratings(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    idsupp = models.IntegerField(db_column='idSupp')  # Field name made lowercase.
    iddelivery = models.BigIntegerField(db_column='idDelivery')  # Field name made lowercase.
    total = models.IntegerField()
    description = models.CharField(max_length=150, blank=True, null=True)
    par1 = models.IntegerField(blank=True, null=True)
    par2 = models.IntegerField(blank=True, null=True)
    par3 = models.IntegerField(blank=True, null=True)
    par4 = models.IntegerField(blank=True, null=True)
    par5 = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tDeliveryRatings'


class Tdeliverystatus(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tDeliveryStatus'


class Tinvboxstatus(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    status = models.IntegerField()
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tInvBoxStatus'


class Tinvheader(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    invcode = models.CharField(db_column='invCode', max_length=50)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='warehouseId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    opendatetime = models.DateTimeField(db_column='openDateTime')  # Field name made lowercase.
    closedatetime = models.DateTimeField(db_column='closeDateTime', blank=True, null=True)  # Field name made lowercase.
    invdescription = models.CharField(db_column='invDescription', max_length=150)  # Field name made lowercase.
    userid2 = models.IntegerField(db_column='userId2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tInvHeader'


class Tinvvolume(models.Model):
    warehouseid = models.IntegerField(db_column='warehouseId')  # Field name made lowercase.
    invcode = models.CharField(db_column='invCode', max_length=50)  # Field name made lowercase.
    partid = models.IntegerField(db_column='partId')  # Field name made lowercase.
    qtybefore = models.DecimalField(db_column='qtyBefore', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtyafter = models.DecimalField(db_column='qtyAfter', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tInvVolume'


class Tkioskmessage(models.Model):
    message = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tKioskMessage'


class Tlocations(models.Model):
    locationid = models.AutoField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='warehouseID')  # Field name made lowercase.
    single = models.BooleanField()
    description = models.CharField(max_length=150)
    isfull = models.BooleanField(db_column='isFull')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tLocations'


class Tlocationscontent(models.Model):
    locationcontentid = models.AutoField(db_column='locationContentID', primary_key=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    containercode = models.CharField(db_column='containerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    containertype = models.IntegerField(db_column='containerType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tLocationsContent'


class Tmovecode(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    code = models.IntegerField()
    description = models.CharField(max_length=50)
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tMoveCode'


class Tmovementhistory(models.Model):
    result = models.BooleanField(blank=True, null=True)
    contcode = models.CharField(db_column='contCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastmessage = models.CharField(db_column='lastMessage', max_length=150, blank=True, null=True)  # Field name made lowercase.
    moveto = models.CharField(db_column='moveTo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tMovementHistory'


class Torderstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tOrderStatus'


class Tordersdetail(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    idorder = models.IntegerField(db_column='idOrder')  # Field name made lowercase.
    idcontract = models.BigIntegerField(db_column='idContract', blank=True, null=True)  # Field name made lowercase.
    cena = models.DecimalField(max_digits=19, decimal_places=4)
    ilosc = models.DecimalField(max_digits=14, decimal_places=4)
    iloscdostarczona = models.DecimalField(db_column='iloscDostarczona', max_digits=14, decimal_places=4)  # Field name made lowercase.
    datautworzenia = models.DateTimeField(db_column='dataUtworzenia')  # Field name made lowercase.
    datamodyfikacji = models.DateTimeField(db_column='dataModyfikacji')  # Field name made lowercase.
    closed = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tOrdersDetail'


class Tordersheader(models.Model):
    ponumber = models.CharField(db_column='poNumber', max_length=50)  # Field name made lowercase.
    idsupp = models.IntegerField(db_column='idSupp')  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    shippedid = models.IntegerField(db_column='shippedId')  # Field name made lowercase.
    tradetermsid = models.IntegerField(db_column='tradeTermsId')  # Field name made lowercase.
    deliverydate = models.DateField(db_column='deliveryDate')  # Field name made lowercase.
    status = models.IntegerField()
    revision = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    additionaltexts = models.TextField(db_column='additionalTexts', blank=True, null=True)  # Field name made lowercase.
    creatorid = models.IntegerField(db_column='creatorId', blank=True, null=True)  # Field name made lowercase.
    approvalid = models.IntegerField(db_column='approvalId', blank=True, null=True)  # Field name made lowercase.
    removerid = models.IntegerField(db_column='removerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tOrdersHeader'


class Tpalletinbound(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    palletcode = models.CharField(db_column='PalletCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    statuscode = models.IntegerField(db_column='StatusCode', blank=True, null=True)  # Field name made lowercase.
    statusdescription = models.CharField(db_column='StatusDescription', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tPalletInbound'


class Tprodcustcode(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    idcust = models.IntegerField(db_column='idCust')  # Field name made lowercase.
    idprod = models.IntegerField(db_column='idProd')  # Field name made lowercase.
    prodcustnumber = models.CharField(db_column='prodCustNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updateinformation = models.CharField(db_column='updateInformation', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProdCustCode'
        unique_together = (('idcust', 'idprod'),)


class Tprodlines(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tProdLines'


class Tproductionordercontainers(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    orderid = models.BigIntegerField(db_column='orderId')  # Field name made lowercase.
    containerid = models.BigIntegerField(db_column='containerId')  # Field name made lowercase.
    containerquantity = models.DecimalField(db_column='containerQuantity', max_digits=9, decimal_places=4)  # Field name made lowercase.
    containerconfirmedquantity = models.DecimalField(db_column='containerConfirmedQuantity', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50)
    takenat = models.DateTimeField(db_column='takenAt', blank=True, null=True)  # Field name made lowercase.
    takenby = models.CharField(db_column='takenBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    takercomment = models.TextField(db_column='takerComment', blank=True, null=True)  # Field name made lowercase.
    confirmedat = models.DateTimeField(db_column='confirmedAt', blank=True, null=True)  # Field name made lowercase.
    confirmedby = models.CharField(db_column='confirmedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confirmercomment = models.TextField(db_column='confirmerComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProductionOrderContainers'


class Tproductionordercontainersreturns(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    containerid = models.BigIntegerField(db_column='containerId')  # Field name made lowercase.
    containerquantity = models.DecimalField(db_column='containerQuantity', max_digits=9, decimal_places=4)  # Field name made lowercase.
    status = models.CharField(max_length=50)
    returnedat = models.DateTimeField(db_column='returnedAt')  # Field name made lowercase.
    returnedby = models.CharField(db_column='returnedBy', max_length=255)  # Field name made lowercase.
    confirmedat = models.DateTimeField(db_column='confirmedAt', blank=True, null=True)  # Field name made lowercase.
    confirmedby = models.CharField(db_column='confirmedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tProductionOrderContainersReturns'


class Tproductionorders(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    instructionid = models.IntegerField(db_column='instructionId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    createdby = models.CharField(db_column='createdBy', max_length=255)  # Field name made lowercase.
    line = models.CharField(max_length=50)
    partnumber = models.CharField(db_column='partNumber', max_length=255)  # Field name made lowercase.
    partlot = models.CharField(db_column='partLot', max_length=255)  # Field name made lowercase.
    orderquantity = models.IntegerField(db_column='orderQuantity')  # Field name made lowercase.
    orderweight = models.FloatField(db_column='orderWeight')  # Field name made lowercase.
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tProductionOrders'


class Treportrawmaterialpartsbo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    idpart = models.IntegerField(db_column='idPart', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    invdate = models.DateField(db_column='invDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tReportRawMaterialPartsBO'


class Treportrawmaterialpartsmonths(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    description = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    spreadsheetname = models.CharField(db_column='spreadsheetName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tReportRawMaterialPartsMonths'
        unique_together = (('year', 'month'),)


class Treportrawmaterialpartsqty(models.Model):
    idpart = models.IntegerField(db_column='idPart', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    qtyin = models.IntegerField(db_column='qtyIN', blank=True, null=True)  # Field name made lowercase.
    qtyout = models.IntegerField(db_column='qtyOUT', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tReportRawMaterialPartsQty'


class Treportrawmaterialpartswatch(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    sequence = models.IntegerField()
    idprod = models.IntegerField(db_column='idProd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tReportRawMaterialPartsWatch'


class Tsalesorders(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    salesorder = models.CharField(db_column='SalesOrder', max_length=50)  # Field name made lowercase.
    dnnumber = models.CharField(db_column='DNnumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custcode = models.CharField(db_column='CustCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.IntegerField(db_column='OrderStatus')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    shippingdate = models.DateField(db_column='ShippingDate', blank=True, null=True)  # Field name made lowercase.
    operator = models.IntegerField(blank=True, null=True)
    custponumber = models.CharField(db_column='CustPONumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    realshippingdate = models.DateField(db_column='realShippingDate', blank=True, null=True)  # Field name made lowercase.
    files = models.BooleanField(blank=True, null=True)
    exported = models.BooleanField(blank=True, null=True)
    result = models.SmallIntegerField(blank=True, null=True)
    uniqueident = models.CharField(db_column='uniqueIdent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deliveryconditions = models.CharField(db_column='deliveryConditions', max_length=100, blank=True, null=True)  # Field name made lowercase.
    specialtext = models.TextField(db_column='specialText', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hwhse = models.CharField(db_column='HWHSE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bpcsstatus = models.SmallIntegerField(db_column='BPCSStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tSalesOrders'


class Tsalesordersdetails(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    salesorder = models.CharField(db_column='SalesOrder', max_length=50)  # Field name made lowercase.
    prodid = models.IntegerField(db_column='prodID')  # Field name made lowercase.
    qty = models.DecimalField(max_digits=18, decimal_places=0)
    lineid = models.IntegerField(db_column='lineId', blank=True, null=True)  # Field name made lowercase.
    lwhs = models.CharField(db_column='LWHS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tSalesOrdersDetails'


class Tsalesordersstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tSalesOrdersStatus'


class Tsettings(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    computername = models.CharField(db_column='computerName', max_length=50)  # Field name made lowercase.
    machineid = models.IntegerField(db_column='machineId', blank=True, null=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='machineName', max_length=31, blank=True, null=True)  # Field name made lowercase.
    reserveboxeswhenaddingpallet = models.BooleanField(db_column='reserveBoxesWhenAddingPallet', blank=True, null=True)  # Field name made lowercase.
    chooseoldestincompletebox = models.BooleanField(db_column='chooseOldestIncompleteBox', blank=True, null=True)  # Field name made lowercase.
    automaticcreatepallet = models.BooleanField(db_column='automaticCreatePallet', blank=True, null=True)  # Field name made lowercase.
    currentboxid = models.IntegerField(db_column='currentBoxId', blank=True, null=True)  # Field name made lowercase.
    images_sourcepath = models.CharField(db_column='images_sourcePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    images_destinationpath = models.CharField(db_column='images_destinationPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    images_username = models.CharField(max_length=50, blank=True, null=True)
    images_password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tSettings'


class Tshipmentdetails(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    salesorder = models.CharField(db_column='salesOrder', max_length=50)  # Field name made lowercase.
    palletnumber = models.CharField(db_column='palletNumber', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tShipmentDetails'


class Tshipped(models.Model):
    shipped = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tShipped'


class Tsupplier(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    shortname = models.CharField(db_column='shortName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='longName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    creationdate = models.DateField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateField(db_column='deletedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tSupplier'


class Ttradeterms(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    tradeterms = models.CharField(db_column='tradeTerms', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tTradeTerms'


class Tunits(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tUnits'


class Twashingstations(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=50)
    printerpath = models.CharField(db_column='printerPath', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tWashingStations'


class Tweight(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    barcode = models.CharField(max_length=50)
    weighthost = models.FloatField(db_column='weightHost', blank=True, null=True)  # Field name made lowercase.
    weightreal = models.FloatField(db_column='weightReal', blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    workstation = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tWeight'


class Testweight(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    barcode = models.CharField(max_length=50)
    weighthost = models.FloatField(db_column='weightHost', blank=True, null=True)  # Field name made lowercase.
    weightreal = models.FloatField(db_column='weightReal', blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    workstation = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testWeight'


class Unscannedserials(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    idbox = models.IntegerField(db_column='idBox')  # Field name made lowercase.
    slot = models.CharField(db_column='sLot', max_length=50)  # Field name made lowercase.
    sserial1 = models.CharField(db_column='sSerial1', max_length=50)  # Field name made lowercase.
    sserial2 = models.CharField(db_column='sSerial2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField()
    idoperator = models.IntegerField(db_column='idOperator', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    idmachine = models.IntegerField(db_column='idMachine', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unscannedSerials'


class Users(models.Model):
    login = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField()
    role = models.SmallIntegerField()
    skin = models.CharField(max_length=50, blank=True, null=True)
    sidebar = models.BooleanField(blank=True, null=True)
    navpanemaxvisiblegroup = models.IntegerField(db_column='navPaneMaxVisibleGroup')  # Field name made lowercase.
    navbartype = models.IntegerField(db_column='navBarType')  # Field name made lowercase.
    accesshash = models.TextField(db_column='accessHash', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class Warehousevolume(models.Model):
    warehouseid = models.IntegerField(db_column='warehouseId')  # Field name made lowercase.
    partid = models.IntegerField(db_column='partId')  # Field name made lowercase.
    quantity = models.DecimalField(max_digits=14, decimal_places=4)
    lastactivity = models.DateTimeField(db_column='lastActivity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warehouseVolume'


class Warehouses(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    active = models.BooleanField()
    bpcscode = models.CharField(db_column='bpcsCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'warehouses'
