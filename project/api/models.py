# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id = models.BigAutoField(primary_key=True)
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


class Food(models.Model):
    category = models.CharField(max_length=60, blank=True, null=True)
    elaboration_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    food_state = models.IntegerField(blank=True, null=True)
    food_name = models.CharField(max_length=60, blank=True, null=True)
    food_price = models.IntegerField(blank=True, null=True)
    img_src = models.CharField(max_length=200)
    food_amount = models.IntegerField(blank=True, null=True)
    consumed = models.IntegerField(blank=True, null=True)
    possible_expiration_date = models.DateField(blank=True, null=True)
    food_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserData', models.DO_NOTHING)
    discard_date = models.DateField(blank=True, null=True)
    food_amount_g = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class Inbox(models.Model):
    inbox_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('UserData', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inbox'


class NutritionalInfo(models.Model):
    nutrit_info_id = models.IntegerField(primary_key=True)
    food = models.ForeignKey(Food, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'nutritional_info'


class PossibleShop(models.Model):
    poss_shop_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=60)
    food_categoty = models.CharField(max_length=60)
    details = models.CharField(max_length=100)
    possbile_price = models.IntegerField()
    user = models.ForeignKey('UserData', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'possible_shop'


class Publication(models.Model):
    publ_price = models.IntegerField()
    publ_descp = models.CharField(max_length=800)
    publ_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('UserData', models.DO_NOTHING)
    food = models.ForeignKey(Food, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'publication'


class UserData(models.Model):
    intolerance_allergies = models.CharField(max_length=80)
    home_size = models.IntegerField()
    name_user = models.CharField(max_length=80)
    age = models.IntegerField()
    month_budget = models.IntegerField()
    user_id = models.IntegerField(primary_key=True)
    type_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_data'
