# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.template.loader import render_to_string
from easy_select2 import select2_modelform
from suit.admin import SortableTabularInline
from . import models
from . import forms as fms


def is_superuser(request):
    if request.user.is_active and request.user.is_superuser:
        return True
    else:
        return False


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "fatherx", "phone", "sex", "fenrun", "code", "max_num", "create_time"]
    fields = ["user", "phone", "name", "sex", "is_vip", "father", "max_num"]
    search_fields = ["name", "phone"]
    all_fields = [f.name for f in models.UserProfile._meta.get_fields()]
    all_fields.remove("max_num")
    readonly_fields = all_fields

    def get_readonly_fields(self, request, obj=None):
        if is_superuser(request):
            return []
        else:
            return super(UserProfileAdmin, self).get_readonly_fields(request, obj)

    def fatherx(self, obj):
        if obj.father and hasattr(obj.user, "userprofile"):
            return '<a href="/admin/user/userprofile/?father__id__exact=%s" target="_blank">%s</a>' % (obj.father.id, obj.father.userprofile.name)
        else:
            return u"五彩神石"
    fatherx.allow_tags = True
    fatherx.short_description = u'导师'

    def fenrun(self, obj):
        if hasattr(obj.user, "userfenrun"):
            return "%s__%s" % (obj.user.userfenrun.point, obj.user.userfenrun.rmb)
        else:
            return u"未设置"
    fenrun.allow_tags = True
    fenrun.short_description = u'分润'


admin.site.register(models.UserProfile, UserProfileAdmin)


class LKLTrade01ileAdmin(admin.ModelAdmin):
    list_display = [
        "merchantCode", "maintainOrg", "transId",
        "cardType", "transCode", "termNo", "payAmt",
        "cardNo", "feeAmt", "sid", "merchantName",
        "transType", "transAmt", "trade_date"]
    fields = list_display
    list_filter = ["cardType", "transType"]
    search_fields = ["termNo", "merchantCode", "transId", "trade_date"]


admin.site.register(models.LKLTrade01, LKLTrade01ileAdmin)


class UserPosAdmin(admin.ModelAdmin):
    form = fms.UserPosAdminForm
    list_display = ["user", "userx", "code", "pos_d1", "create_time"]
    fields = ["user", "code"]
    search_fields = ["user__username", "code"]

    def userx(self, obj):
        if obj.user and hasattr(obj.user, "userprofile"):
            return obj.user.userprofile.name
        else:
            return obj.user
    userx.allow_tags = True
    userx.short_description = u'用户姓名'

    def pos_d1(self, obj):
        return u'<a href="/admin/user/lkld1/?q=%s" target="_blank">查看</a>' % obj.code
    pos_d1.allow_tags = True
    pos_d1.short_description = u'D1交易'


admin.site.register(models.UserPos, UserPosAdmin)


class UserFenRunAdmin(admin.ModelAdmin):
    form = fms.UserFenRunFrom
    list_display = ["user", "point", "rmb", "message", "create_time", "update_time"]
    fields = ["user", "point", "rmb", "message"]
    list_filter = ["point", "rmb"]
    search_fields = ["user__username"]


class UserAlipayAdmin(admin.ModelAdmin):
    list_display = ["user", "account", "name", "create_time", "update_time"]
    fields = ["user", "account", "name"]
    search_fields = ["user__username"]


admin.site.register(models.UserFenRun, UserFenRunAdmin)
admin.site.register(models.UserAlipay, UserAlipayAdmin)


class LKLTerminalAdmin(admin.ModelAdmin):
    list_display = ["merchant_code", "merchant_name", "maintain", "terminal", "category", "terminal_type", "open_date", "close_date", "is_give", "is_ok", "ok_date"]
    fields = list_display
    list_filter = ["is_give", "is_ok"]
    search_fields = ["terminal", "merchant_code"]


class LKLD0Admin(admin.ModelAdmin):
    list_display = ["merchant_code", "merchant_name", "maintain", "maintain_code", "trans_id", "category", "draw_date", "draw_rmb", "fee_rmb", "real_rmb", "trans_type", "trans_status"]
    fields = list_display
    search_fields = ["merchant_code"]


class LKLD1Admin(admin.ModelAdmin):
    list_display = ["agent", "merchant_code", "merchant_name", "maintain", "maintain_code", "trans_id", "terminal_num", "draw_date", "draw_rmb", "fee_rmb", "card_type", "pay_date", "pos_type", "terminal"]
    fields = list_display
    search_fields = ["terminal", "merchant_code"]


admin.site.register(models.LKLTerminal, LKLTerminalAdmin)
admin.site.register(models.LKLD0, LKLD0Admin)
admin.site.register(models.LKLD1, LKLD1Admin)


class UserRMBAdmin(admin.ModelAdmin):
    list_display = ["user", "rmb", "child_rmb", "create_time", "update_time"]
    fields = ["user", "rmb", "child_rmb"]
    search_fields = ["user__username"]


class ProfitD1Admin(admin.ModelAdmin):
    list_display = ["user", "trans_id", "fenrun_point", "fenrun_rmb", "rmb", "merchant_code", "draw_date", "draw_rmb", "fee_rmb", "card_type", "pay_date", "terminal", "status", "create_time", "pay_time"]
    fields = ["user", "trans_id", "fenrun_point", "fenrun_rmb", "rmb", "merchant_code", "draw_date", "draw_rmb", "fee_rmb", "card_type", "pay_date", "terminal", "status", "pay_time"]
    search_fields = ["user__username", "terminal", "merchant_code"]
    list_filter = ["status"]


class ProfitD0Admin(admin.ModelAdmin):
    list_display = ["user", "trans_id", "fenrun_point", "fenrun_rmb", "rmb", "merchant_code", "draw_date", "draw_rmb", "fee_rmb", "real_rmb", "trans_type", "trans_status", "status", "create_time", "pay_time"]
    fields = ["user", "trans_id", "fenrun_point", "fenrun_rmb", "rmb", "merchant_code", "draw_date", "draw_rmb", "fee_rmb", "real_rmb", "trans_type", "trans_status", "status", "pay_time"]
    search_fields = ["user__username", "merchant_code"]
    list_filter = ["status"]


class TiXianOrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "user", "rmb", "fee", "status", "create_time", "pay_time"]
    fields = ["user", "rmb", "fee", "status", "order_id", "pay_time"]
    search_fields = ["user__username"]
    list_filter = ["status"]


admin.site.register(models.UserRMB, UserRMBAdmin)
admin.site.register(models.ProfitD1, ProfitD1Admin)
admin.site.register(models.ProfitD0, ProfitD0Admin)
admin.site.register(models.TiXianOrder, TiXianOrderAdmin)
