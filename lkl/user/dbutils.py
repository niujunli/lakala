# -*- coding: utf-8 -*-
import time
from collections import defaultdict
from decimal import Decimal
from django.db import transaction
from . import models


def add_userrmb_rmb(user, rmb, is_child=False):
    with transaction.atomic():
        obj, created = models.UserRMB.objects.select_for_update().get_or_create(user=user, defaults={"rmb": 0})
        if is_child:
            obj.child_rmb += rmb
        else:
            obj.rmb += rmb
        obj.save()


def sub_userrmb_rmb(user, rmb, is_child=False):
    with transaction.atomic():
        obj, created = models.UserRMB.objects.select_for_update().get_or_create(user=user, defaults={"rmb": 0})
        if is_child:
            obj.child_rmb -= rmb
        else:
            obj.rmb -= rmb
        obj.save()


def get_userrmb_num(user):
    with transaction.atomic():
        obj, created = models.UserRMB.objects.select_for_update().get_or_create(user=user, defaults={"rmb": 0})
    return obj.rmb, obj.child_rmb


def get_user_by_terminal(terminal):
    """
    通过终端号获取用户
    """
    try:
        obj = models.UserPos.objects.get(code=terminal)
        user = obj.user
    except Exception:
        user = None
    return user


def get_user_by_mcode(mcode):
    """
    通过商户号获取用户
    """
    objs = models.LKLTerminal.objects.filter(merchant_code=mcode)
    if len(objs) == 0:
        return None
    elif len(objs) > 1:
        return "multi"
    else:
        pos = objs[0].terminal
        return get_user_by_terminal(pos)


def get_user_pos(user):
    """
    获取用户终端号
    """
    poses = models.UserPos.objects.filter(user=user).values_list("code", flat=True)
    return list(poses)


def get_user_mcode(user):
    """
    获取用户商户号
    """
    mcode_list = []
    pos_list = get_user_pos(user)
    mcode_dict = defaultdict(list)
    objs = models.LKLTerminal.objects.filter(terminal__in=pos_list)
    for obj in objs:
        mcode_dict[obj.merchant_code].append(obj.terminal)
    for mcode, poses in mcode_dict.iteritems():
        if len(poses) == 1:
            mcode_list.append(mcode)
        else:
            ok_list = [pos in pos_list for pos in poses]
            if all(ok_list):
                mcode_list.append(mcode)
    return mcode_list


def get_user_d0_num(user):
    """
    获取用户D0笔数
    """
    mcode_list = get_user_mcode(user)
    objs = models.LKLD0.objects.filter(merchant_code__in=mcode_list).filter(fee_rmb="2").filter(trans_type=u"正交易").filter(trans_status=u"成功")
    return len(objs)


def get_user_d1_total(user):
    """
    获取用户D1刷卡总额
    """
    trans_total = Decimal(0)
    pos_list = get_user_pos(user)
    objs = models.LKLD1.objects.filter(terminal__in=pos_list)
    for obj in objs:
        if obj.card_type == u"贷记卡":
            month = obj.pay_date[:7]
            if month == "2018-01":
                continue
            # 100以下交易不计算
            if Decimal(obj.draw_rmb) < 100:
                continue
            trans_total += Decimal(obj.draw_rmb)
    return str(trans_total)