#rom django.db import models
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class FlowTable(models.Model):
    flow_id = models.IntegerField(db_column='Flow.id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action = models.CharField(db_column='Action', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rule_table_rule_id = models.ForeignKey('RuleTable', db_column='Rule_table_Rule.id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stats_table_stats_id = models.ForeignKey('StatsTable', db_column='Stats_table_Stats.id')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Flow_table'


class FlowTableHasStatsTable(models.Model):
    flow_table_flow_id = models.ForeignKey(FlowTable, db_column='Flow_table_Flow.id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stats_table_stats_id = models.ForeignKey('StatsTable', db_column='Stats_table_Stats.id')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Flow_table_has_Stats_table'
        unique_together = (('Flow_table_Flow.id', 'Stats_table_Stats.id'),)


class RuleTable(models.Model):
    rule_id = models.AutoField(db_column='Rule.id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    switchport = models.CharField(db_column='SwitchPort', max_length=45)  # Field name made lowercase.
    mac_src = models.CharField(db_column='MAC_src', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mac_dst = models.CharField(db_column='MAC_dst', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_src = models.CharField(db_column='IP_src', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_dst = models.CharField(db_column='IP_dst', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s_port = models.CharField(db_column='S_port', max_length=45, blank=True, null=True)  # Field name made lowercase.
    d_port = models.CharField(db_column='D_port', max_length=45, blank=True, null=True)  # Field name made lowercase.
    flow_table_flow_id = models.IntegerField(db_column='Flow_table_Flow.id')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Rule_table'


class StatsTable(models.Model):
    stats_id = models.AutoField(db_column='Stats.id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    packet_counter = models.FloatField(db_column='Packet_counter', blank=True, null=True)  # Field name made lowercase.
    byte_counter = models.FloatField(db_column='Byte_counter', blank=True, null=True)  # Field name made lowercase.
    flow_table_flow_id = models.IntegerField(db_column='Flow_table_Flow.id')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Stats_table'


class TemporaryFlow(models.Model):
    flow_id = models.AutoField(db_column='Flow.id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    switchport = models.CharField(db_column='SwitchPort', max_length=45)  # Field name made lowercase.
    mac_src = models.CharField(db_column='MAC_src', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mac_dst = models.CharField(db_column='MAC_dst', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_src = models.CharField(db_column='IP_src', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_dst = models.CharField(db_column='IP_dst', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s_port = models.CharField(db_column='S_port', max_length=45, blank=True, null=True)  # Field name made lowercase.
    d_port = models.CharField(db_column='D_port', max_length=45, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tomeout_time = models.CharField(db_column='Tomeout_time', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temporary_Flow'


class UsageTable(models.Model):
    srv_id = models.AutoField(db_column='Srv.id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    servername = models.CharField(db_column='Servername', max_length=45)  # Field name made lowercase.
    cpu_usage = models.FloatField(db_column='Cpu_usage', blank=True, null=True)  # Field name made lowercase.
    input_traffic = models.FloatField(db_column='Input_traffic', blank=True, null=True)  # Field name made lowercase.
    output_traffic = models.FloatField(db_column='Output_traffic', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='Timestamp', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usage_table'

