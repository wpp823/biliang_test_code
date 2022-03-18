# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Any


class AccountListRequestBody(TeaModel):
    def __init__(
        self,
        search: str = None,
        enable: str = None,
    ):
        self.search = search
        self.enable = enable

    def validate(self):
        self.validate_required(self.search, 'search')
        self.validate_required(self.enable, 'enable')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class AccountListRequest(TeaModel):
    def __init__(
        self,
        body: AccountListRequestBody = None,
    ):
        self.body = body
        # 获取财务基础资料 科目列表（所有科目） 信息

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AccountListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AccountTypeListRequestBody(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AccountTypeListRequest(TeaModel):
    def __init__(
        self,
        body: AccountTypeListRequestBody = None,
    ):
        self.body = body
        # 科目类别列表

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AccountTypeListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SujectDetailRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
    ):
        self.id = id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class SujectDetailRequest(TeaModel):
    def __init__(
        self,
        body: SujectDetailRequestBody = None,
    ):
        self.body = body
        # 科目详情接口批量查询

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SujectDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckItemEntry(TeaModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
        aux_type: str = None,
        is_require: bool = None,
    ):
        self.id = id
        self.type = type
        self.aux_type = aux_type
        self.is_require = is_require

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.aux_type, 'aux_type')
        self.validate_required(self.is_require, 'is_require')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.type is not None:
            result['type'] = self.type
        if self.aux_type is not None:
            result['bd_auxinfo_type_id'] = self.aux_type
        if self.is_require is not None:
            result['isrequire'] = self.is_require
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('bd_auxinfo_type_id') is not None:
            self.aux_type = m.get('bd_auxinfo_type_id')
        if m.get('isrequire') is not None:
            self.is_require = m.get('isrequire')
        return self


class AccountInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        level: str = None,
        number: str = None,
        account_type: str = None,
        help_code: str = None,
        dc: str = None,
        enable: str = None,
        parent: str = None,
        isbank: bool = None,
        is_cash: bool = None,
        is_cash_equivalent: bool = None,
        isqty: bool = None,
        iscurrency: bool = None,
        rdbtnall: bool = None,
        currencys: str = None,
        is_change_currency: bool = None,
        is_assist: bool = None,
        checkitementry: List[CheckItemEntry] = None,
    ):
        self.id = id
        self.name = name
        self.level = level
        self.number = number
        self.account_type = account_type
        self.help_code = help_code
        self.dc = dc
        self.enable = enable
        self.parent = parent
        self.isbank = isbank
        self.is_cash = is_cash
        self.is_cash_equivalent = is_cash_equivalent
        self.isqty = isqty
        self.iscurrency = iscurrency
        self.rdbtnall = rdbtnall
        self.currencys = currencys
        self.is_change_currency = is_change_currency
        self.is_assist = is_assist
        self.checkitementry = checkitementry

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.level, 'level')
        self.validate_required(self.number, 'number')
        self.validate_required(self.account_type, 'account_type')
        self.validate_required(self.checkitementry, 'checkitementry')
        if self.checkitementry:
            for k in self.checkitementry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.level is not None:
            result['level'] = self.level
        if self.number is not None:
            result['number'] = self.number
        if self.account_type is not None:
            result['accounttype_id'] = self.account_type
        if self.help_code is not None:
            result['helpcode'] = self.help_code
        if self.dc is not None:
            result['dc'] = self.dc
        if self.enable is not None:
            result['enable'] = self.enable
        if self.parent is not None:
            result['parent_id'] = self.parent
        if self.isbank is not None:
            result['isbank'] = self.isbank
        if self.is_cash is not None:
            result['iscash'] = self.is_cash
        if self.is_cash_equivalent is not None:
            result['iscashequivalent'] = self.is_cash_equivalent
        if self.isqty is not None:
            result['isqty'] = self.isqty
        if self.iscurrency is not None:
            result['iscurrency'] = self.iscurrency
        if self.rdbtnall is not None:
            result['rdbtnall'] = self.rdbtnall
        if self.currencys is not None:
            result['currencys'] = self.currencys
        if self.is_change_currency is not None:
            result['ischangecurrency'] = self.is_change_currency
        if self.is_assist is not None:
            result['isassist'] = self.is_assist
        result['checkitementry'] = []
        if self.checkitementry is not None:
            for k in self.checkitementry:
                result['checkitementry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('accounttype_id') is not None:
            self.account_type = m.get('accounttype_id')
        if m.get('helpcode') is not None:
            self.help_code = m.get('helpcode')
        if m.get('dc') is not None:
            self.dc = m.get('dc')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('parent_id') is not None:
            self.parent = m.get('parent_id')
        if m.get('isbank') is not None:
            self.isbank = m.get('isbank')
        if m.get('iscash') is not None:
            self.is_cash = m.get('iscash')
        if m.get('iscashequivalent') is not None:
            self.is_cash_equivalent = m.get('iscashequivalent')
        if m.get('isqty') is not None:
            self.isqty = m.get('isqty')
        if m.get('iscurrency') is not None:
            self.iscurrency = m.get('iscurrency')
        if m.get('rdbtnall') is not None:
            self.rdbtnall = m.get('rdbtnall')
        if m.get('currencys') is not None:
            self.currencys = m.get('currencys')
        if m.get('ischangecurrency') is not None:
            self.is_change_currency = m.get('ischangecurrency')
        if m.get('isassist') is not None:
            self.is_assist = m.get('isassist')
        self.checkitementry = []
        if m.get('checkitementry') is not None:
            for k in m.get('checkitementry'):
                temp_model = CheckItemEntry()
                self.checkitementry.append(temp_model.from_map(k))
        return self


class AccountSaveRequestBody(TeaModel):
    def __init__(
        self,
        items: List[AccountInfo] = None,
    ):
        self.items = items

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AccountInfo()
                self.items.append(temp_model.from_map(k))
        return self


class AccountSaveRequest(TeaModel):
    def __init__(
        self,
        body: AccountSaveRequestBody = None,
    ):
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AccountSaveRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CABalanceHomeRequestBody(TeaModel):
    def __init__(
        self,
        query_type: str = None,
    ):
        # 查询类型:”1”-本月 “2”-上月 “3”-本季度 “4”-本年
        self.query_type = query_type

    def validate(self):
        self.validate_required(self.query_type, 'query_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_type is not None:
            result['queryType'] = self.query_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        return self


class CABalanceHomeRequest(TeaModel):
    def __init__(
        self,
        body: CABalanceHomeRequestBody = None,
    ):
        self.body = body
        # 出纳资金余额

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CABalanceHomeRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CAAccountBalanceRequestBody(TeaModel):
    def __init__(
        self,
        currency_id: str = None,
    ):
        self.currency_id = currency_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency_id is not None:
            result['currencyId'] = self.currency_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currencyId') is not None:
            self.currency_id = m.get('currencyId')
        return self


class CAAccountBalanceRequest(TeaModel):
    def __init__(
        self,
        body: CAAccountBalanceRequestBody = None,
    ):
        self.body = body
        # 出纳资金余额

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CAAccountBalanceRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CABalanceTrendRequestBody(TeaModel):
    def __init__(
        self,
        currency_id: str = None,
    ):
        self.currency_id = currency_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency_id is not None:
            result['currencyId'] = self.currency_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currencyId') is not None:
            self.currency_id = m.get('currencyId')
        return self


class CABalanceTrendRequest(TeaModel):
    def __init__(
        self,
        body: CABalanceTrendRequestBody = None,
    ):
        self.body = body
        # 出纳资金收支趋势接口

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CABalanceTrendRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebitAndCreditTrendRequestBody(TeaModel):
    def __init__(
        self,
        income_type: str = None,
        trend_type: str = None,
    ):
        # 收支类型， “1”-收入趋势，”2”-支出趋势
        self.income_type = income_type
        # 趋势类型，”1”-最近一周，”2”-最近30天，”3”-最近一年
        self.trend_type = trend_type

    def validate(self):
        self.validate_required(self.income_type, 'income_type')
        self.validate_required(self.trend_type, 'trend_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.income_type is not None:
            result['incomeType'] = self.income_type
        if self.trend_type is not None:
            result['trendType'] = self.trend_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('incomeType') is not None:
            self.income_type = m.get('incomeType')
        if m.get('trendType') is not None:
            self.trend_type = m.get('trendType')
        return self


class DebitAndCreditTrendRequest(TeaModel):
    def __init__(
        self,
        body: DebitAndCreditTrendRequestBody = None,
    ):
        self.body = body
        # 出纳资金流水明细接口

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DebitAndCreditTrendRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AccountDetailRequestBody(TeaModel):
    def __init__(
        self,
        query_type: str = None,
        param_date_from: str = None,
        param_date_to: str = None,
        param_start_period: str = None,
        param_end_period: str = None,
        account_ids: str = None,
        currency_ids: str = None,
        page: str = None,
    ):
        # 查询类型:”date”-按照日期查询 “period”-按照期间查询
        self.query_type = query_type
        # 开始时间 （当queryType=”date”时必填）， 格式如：”2021-03-01”
        self.param_date_from = param_date_from
        # 结束时间 （当queryType=”date”时必填）， 格式如：”2021-03-15”
        self.param_date_to = param_date_to
        # 开始期间（当queryType=”period”时必填）， 格式：”202103”
        self.param_start_period = param_start_period
        # 结束期间（当queryType=”period”时必填），格式：”202103”
        self.param_end_period = param_end_period
        # 账户ID（暂不支持多个） 如：”1020775979343210496”
        self.account_ids = account_ids
        # 币别ID（暂不支持多个）, 如：”1020775979343210496”
        self.currency_ids = currency_ids
        self.page = page

    def validate(self):
        self.validate_required(self.query_type, 'query_type')
        self.validate_required(self.param_date_from, 'param_date_from')
        self.validate_required(self.param_date_to, 'param_date_to')
        self.validate_required(self.param_start_period, 'param_start_period')
        self.validate_required(self.param_end_period, 'param_end_period')
        self.validate_required(self.account_ids, 'account_ids')
        self.validate_required(self.currency_ids, 'currency_ids')
        self.validate_required(self.page, 'page')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.param_date_from is not None:
            result['paramdatefrom'] = self.param_date_from
        if self.param_date_to is not None:
            result['paramdateto'] = self.param_date_to
        if self.param_start_period is not None:
            result['paramstartperiod'] = self.param_start_period
        if self.param_end_period is not None:
            result['paramendperiod'] = self.param_end_period
        if self.account_ids is not None:
            result['accountIds'] = self.account_ids
        if self.currency_ids is not None:
            result['currencyIds'] = self.currency_ids
        if self.page is not None:
            result['page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('paramdatefrom') is not None:
            self.param_date_from = m.get('paramdatefrom')
        if m.get('paramdateto') is not None:
            self.param_date_to = m.get('paramdateto')
        if m.get('paramstartperiod') is not None:
            self.param_start_period = m.get('paramstartperiod')
        if m.get('paramendperiod') is not None:
            self.param_end_period = m.get('paramendperiod')
        if m.get('accountIds') is not None:
            self.account_ids = m.get('accountIds')
        if m.get('currencyIds') is not None:
            self.currency_ids = m.get('currencyIds')
        if m.get('page') is not None:
            self.page = m.get('page')
        return self


class AccountDetailRequest(TeaModel):
    def __init__(
        self,
        body: AccountDetailRequestBody = None,
    ):
        self.body = body
        # 日记账详情

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AccountDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JournalDetailRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
    ):
        self.id = id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class JournalDetailRequest(TeaModel):
    def __init__(
        self,
        body: JournalDetailRequestBody = None,
    ):
        self.body = body
        # 日记账列表

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = JournalDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JournalListRequestBody(TeaModel):
    def __init__(
        self,
        period: str = None,
        startdate: str = None,
        enddate: str = None,
        begindate: str = None,
        expiredate: str = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.period = period
        self.startdate = startdate
        self.enddate = enddate
        self.begindate = begindate
        self.expiredate = expiredate
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        self.validate_required(self.period, 'period')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['period'] = self.period
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.begindate is not None:
            result['begindate'] = self.begindate
        if self.expiredate is not None:
            result['expiredate'] = self.expiredate
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('begindate') is not None:
            self.begindate = m.get('begindate')
        if m.get('expiredate') is not None:
            self.expiredate = m.get('expiredate')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class JournalListRequest(TeaModel):
    def __init__(
        self,
        body: JournalListRequestBody = None,
    ):
        self.body = body
        # 日记账保存

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = JournalListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveJournalRequestBody(TeaModel):
    def __init__(
        self,
        number: str = None,
        account_number: str = None,
        account_name: str = None,
        account_id: str = None,
        currency_id: str = None,
        date: str = None,
        explanation: str = None,
        source_type: str = None,
        debitfor: str = None,
        creditfor: str = None,
        checktime: str = None,
        isinit: int = None,
        bill_entry_id: str = None,
        operator: str = None,
        supplier: str = None,
        credit: str = None,
        period: str = None,
        account_2: str = None,
        billno: str = None,
        exchangerate: str = None,
        remark: str = None,
        number_1: str = None,
        settle_no: str = None,
        voucher_no: str = None,
        is_check: str = None,
        bill_type: str = None,
        bill_id: str = None,
        account_no_2: str = None,
        debit: str = None,
        bizdate: str = None,
        voucherid: str = None,
        id_1: str = None,
        bill_entry_type: str = None,
        customer: str = None,
    ):
        self.number = number
        self.account_number = account_number
        self.account_name = account_name
        self.account_id = account_id
        # 币别id
        self.currency_id = currency_id
        self.date = date
        self.explanation = explanation
        # 数据来源：manual：手工 voucher：凭证 bill：单据 account：关联账户
        self.source_type = source_type
        self.debitfor = debitfor
        self.creditfor = creditfor
        self.checktime = checktime
        self.isinit = isinit
        # 单据分录id
        self.bill_entry_id = bill_entry_id
        self.operator = operator
        self.supplier = supplier
        self.credit = credit
        self.period = period
        self.account_2 = account_2
        # 源单编号
        self.billno = billno
        self.exchangerate = exchangerate
        self.remark = remark
        # 关联日记账编码
        self.number_1 = number_1
        # 结算号
        self.settle_no = settle_no
        # 凭证字号
        self.voucher_no = voucher_no
        # 是否勾对（1：是，0：否）
        self.is_check = is_check
        # 源单类型
        self.bill_type = bill_type
        # 源单id
        self.bill_id = bill_id
        # 往来账户
        self.account_no_2 = account_no_2
        # 借方金额本位币
        self.debit = debit
        # 业务日期
        self.bizdate = bizdate
        # 凭证id
        self.voucherid = voucherid
        # 关联账户id
        self.id_1 = id_1
        # 资金转账单分录
        self.bill_entry_type = bill_entry_type
        # 客户
        self.customer = customer

    def validate(self):
        self.validate_required(self.number, 'number')
        self.validate_required(self.currency_id, 'currency_id')
        self.validate_required(self.date, 'date')
        self.validate_required(self.explanation, 'explanation')
        self.validate_required(self.source_type, 'source_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['number'] = self.number
        if self.account_number is not None:
            result['account_number'] = self.account_number
        if self.account_name is not None:
            result['account_name'] = self.account_name
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.currency_id is not None:
            result['currency_id'] = self.currency_id
        if self.date is not None:
            result['date'] = self.date
        if self.explanation is not None:
            result['explanation'] = self.explanation
        if self.source_type is not None:
            result['sourcetype'] = self.source_type
        if self.debitfor is not None:
            result['debitfor'] = self.debitfor
        if self.creditfor is not None:
            result['creditfor'] = self.creditfor
        if self.checktime is not None:
            result['checktime'] = self.checktime
        if self.isinit is not None:
            result['isinit'] = self.isinit
        if self.bill_entry_id is not None:
            result['billentryid'] = self.bill_entry_id
        if self.operator is not None:
            result['operator'] = self.operator
        if self.supplier is not None:
            result['supplier'] = self.supplier
        if self.credit is not None:
            result['credit'] = self.credit
        if self.period is not None:
            result['period'] = self.period
        if self.account_2 is not None:
            result['account2'] = self.account_2
        if self.billno is not None:
            result['billno'] = self.billno
        if self.exchangerate is not None:
            result['exchangerate'] = self.exchangerate
        if self.remark is not None:
            result['remark'] = self.remark
        if self.number_1 is not None:
            result['number1'] = self.number_1
        if self.settle_no is not None:
            result['settleno'] = self.settle_no
        if self.voucher_no is not None:
            result['voucherno'] = self.voucher_no
        if self.is_check is not None:
            result['ischeck'] = self.is_check
        if self.bill_type is not None:
            result['billtype'] = self.bill_type
        if self.bill_id is not None:
            result['billid'] = self.bill_id
        if self.account_no_2 is not None:
            result['accountno2'] = self.account_no_2
        if self.debit is not None:
            result['debit'] = self.debit
        if self.bizdate is not None:
            result['bizdate'] = self.bizdate
        if self.voucherid is not None:
            result['voucherid'] = self.voucherid
        if self.id_1 is not None:
            result['id1'] = self.id_1
        if self.bill_entry_type is not None:
            result['billentrytype'] = self.bill_entry_type
        if self.customer is not None:
            result['customer'] = self.customer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('account_number') is not None:
            self.account_number = m.get('account_number')
        if m.get('account_name') is not None:
            self.account_name = m.get('account_name')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('currency_id') is not None:
            self.currency_id = m.get('currency_id')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('explanation') is not None:
            self.explanation = m.get('explanation')
        if m.get('sourcetype') is not None:
            self.source_type = m.get('sourcetype')
        if m.get('debitfor') is not None:
            self.debitfor = m.get('debitfor')
        if m.get('creditfor') is not None:
            self.creditfor = m.get('creditfor')
        if m.get('checktime') is not None:
            self.checktime = m.get('checktime')
        if m.get('isinit') is not None:
            self.isinit = m.get('isinit')
        if m.get('billentryid') is not None:
            self.bill_entry_id = m.get('billentryid')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')
        if m.get('credit') is not None:
            self.credit = m.get('credit')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('account2') is not None:
            self.account_2 = m.get('account2')
        if m.get('billno') is not None:
            self.billno = m.get('billno')
        if m.get('exchangerate') is not None:
            self.exchangerate = m.get('exchangerate')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('number1') is not None:
            self.number_1 = m.get('number1')
        if m.get('settleno') is not None:
            self.settle_no = m.get('settleno')
        if m.get('voucherno') is not None:
            self.voucher_no = m.get('voucherno')
        if m.get('ischeck') is not None:
            self.is_check = m.get('ischeck')
        if m.get('billtype') is not None:
            self.bill_type = m.get('billtype')
        if m.get('billid') is not None:
            self.bill_id = m.get('billid')
        if m.get('accountno2') is not None:
            self.account_no_2 = m.get('accountno2')
        if m.get('debit') is not None:
            self.debit = m.get('debit')
        if m.get('bizdate') is not None:
            self.bizdate = m.get('bizdate')
        if m.get('voucherid') is not None:
            self.voucherid = m.get('voucherid')
        if m.get('id1') is not None:
            self.id_1 = m.get('id1')
        if m.get('billentrytype') is not None:
            self.bill_entry_type = m.get('billentrytype')
        if m.get('customer') is not None:
            self.customer = m.get('customer')
        return self


class SaveJournalRequest(TeaModel):
    def __init__(
        self,
        body: SaveJournalRequestBody = None,
    ):
        self.body = body
        # 科目余额表查询

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SaveJournalRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AcctBalanceRequestBody(TeaModel):
    def __init__(
        self,
        search: str = None,
        start_period: str = None,
        end_period: str = None,
        show_expand_item: str = None,
        show_sum_acct_type: str = None,
        currency_id: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.search = search
        self.start_period = start_period
        self.end_period = end_period
        self.show_expand_item = show_expand_item
        self.show_sum_acct_type = show_sum_acct_type
        self.currency_id = currency_id
        self.page = page
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.start_period, 'start_period')
        self.validate_required(self.end_period, 'end_period')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.start_period is not None:
            result['startperiod'] = self.start_period
        if self.end_period is not None:
            result['endperiod'] = self.end_period
        if self.show_expand_item is not None:
            result['showExpandItem'] = self.show_expand_item
        if self.show_sum_acct_type is not None:
            result['showSumAcctType'] = self.show_sum_acct_type
        if self.currency_id is not None:
            result['currencyID'] = self.currency_id
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pagesize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('startperiod') is not None:
            self.start_period = m.get('startperiod')
        if m.get('endperiod') is not None:
            self.end_period = m.get('endperiod')
        if m.get('showExpandItem') is not None:
            self.show_expand_item = m.get('showExpandItem')
        if m.get('showSumAcctType') is not None:
            self.show_sum_acct_type = m.get('showSumAcctType')
        if m.get('currencyID') is not None:
            self.currency_id = m.get('currencyID')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.page_size = m.get('pagesize')
        return self


class AcctBalanceRequest(TeaModel):
    def __init__(
        self,
        body: AcctBalanceRequestBody = None,
    ):
        self.body = body
        # 明细账查询

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AcctBalanceRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubLedgerRequestBody(TeaModel):
    def __init__(
        self,
        acct_id: str = None,
        start_period: str = None,
        end_period: str = None,
        currency_id: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.acct_id = acct_id
        self.start_period = start_period
        self.end_period = end_period
        self.currency_id = currency_id
        self.page = page
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.acct_id, 'acct_id')
        self.validate_required(self.start_period, 'start_period')
        self.validate_required(self.end_period, 'end_period')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acct_id is not None:
            result['acctid'] = self.acct_id
        if self.start_period is not None:
            result['startperiod'] = self.start_period
        if self.end_period is not None:
            result['endperiod'] = self.end_period
        if self.currency_id is not None:
            result['currencyID'] = self.currency_id
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pagesize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acctid') is not None:
            self.acct_id = m.get('acctid')
        if m.get('startperiod') is not None:
            self.start_period = m.get('startperiod')
        if m.get('endperiod') is not None:
            self.end_period = m.get('endperiod')
        if m.get('currencyID') is not None:
            self.currency_id = m.get('currencyID')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.page_size = m.get('pagesize')
        return self


class SubLedgerRequest(TeaModel):
    def __init__(
        self,
        body: SubLedgerRequestBody = None,
    ):
        self.body = body
        # 利润表

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SubLedgerRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProfitSheetRequestBody(TeaModel):
    def __init__(
        self,
        period: str = None,
    ):
        self.period = period

    def validate(self):
        self.validate_required(self.period, 'period')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('period') is not None:
            self.period = m.get('period')
        return self


class ProfitSheetRequest(TeaModel):
    def __init__(
        self,
        body: ProfitSheetRequestBody = None,
    ):
        self.body = body
        # 数量金额总账

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ProfitSheetRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QtySumReportRequestBody(TeaModel):
    def __init__(
        self,
        start_period: str = None,
        end_period: str = None,
        account_id: List[int] = None,
        levelfrom: str = None,
        levelto: str = None,
        qty_scale: str = None,
        price_scale: str = None,
        currency_id: str = None,
        show_expand_item: str = None,
        expend_all: str = None,
        show_only_leaf: str = None,
        hide_balance_zero: str = None,
        hide_no_happen: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.start_period = start_period
        self.end_period = end_period
        self.account_id = account_id
        self.levelfrom = levelfrom
        self.levelto = levelto
        self.qty_scale = qty_scale
        self.price_scale = price_scale
        self.currency_id = currency_id
        self.show_expand_item = show_expand_item
        self.expend_all = expend_all
        self.show_only_leaf = show_only_leaf
        self.hide_balance_zero = hide_balance_zero
        self.hide_no_happen = hide_no_happen
        self.page = page
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.start_period, 'start_period')
        self.validate_required(self.end_period, 'end_period')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_period is not None:
            result['startperiod'] = self.start_period
        if self.end_period is not None:
            result['endperiod'] = self.end_period
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.levelfrom is not None:
            result['levelfrom'] = self.levelfrom
        if self.levelto is not None:
            result['levelto'] = self.levelto
        if self.qty_scale is not None:
            result['qtyscale'] = self.qty_scale
        if self.price_scale is not None:
            result['pricescale'] = self.price_scale
        if self.currency_id is not None:
            result['currencyId'] = self.currency_id
        if self.show_expand_item is not None:
            result['showExpandItem'] = self.show_expand_item
        if self.expend_all is not None:
            result['expendall'] = self.expend_all
        if self.show_only_leaf is not None:
            result['showonlyleaf'] = self.show_only_leaf
        if self.hide_balance_zero is not None:
            result['hidebalancezero'] = self.hide_balance_zero
        if self.hide_no_happen is not None:
            result['hidenohappen'] = self.hide_no_happen
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pagesize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startperiod') is not None:
            self.start_period = m.get('startperiod')
        if m.get('endperiod') is not None:
            self.end_period = m.get('endperiod')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('levelfrom') is not None:
            self.levelfrom = m.get('levelfrom')
        if m.get('levelto') is not None:
            self.levelto = m.get('levelto')
        if m.get('qtyscale') is not None:
            self.qty_scale = m.get('qtyscale')
        if m.get('pricescale') is not None:
            self.price_scale = m.get('pricescale')
        if m.get('currencyId') is not None:
            self.currency_id = m.get('currencyId')
        if m.get('showExpandItem') is not None:
            self.show_expand_item = m.get('showExpandItem')
        if m.get('expendall') is not None:
            self.expend_all = m.get('expendall')
        if m.get('showonlyleaf') is not None:
            self.show_only_leaf = m.get('showonlyleaf')
        if m.get('hidebalancezero') is not None:
            self.hide_balance_zero = m.get('hidebalancezero')
        if m.get('hidenohappen') is not None:
            self.hide_no_happen = m.get('hidenohappen')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.page_size = m.get('pagesize')
        return self


class QtySumReportRequest(TeaModel):
    def __init__(
        self,
        body: QtySumReportRequestBody = None,
    ):
        self.body = body
        # 外部单据分类列表

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = QtySumReportRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VirtualBillTypeRequestBody(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
        number: str = None,
        name: int = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.ids = ids
        self.number = number
        self.name = name
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.number is not None:
            result['number'] = self.number
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class VirtualBillTypeRequest(TeaModel):
    def __init__(
        self,
        body: VirtualBillTypeRequestBody = None,
    ):
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = VirtualBillTypeRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApiResponse(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
        success: bool = None,
        data: Any = None,
    ):
        self.error_code = error_code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class VirtualBillType(TeaModel):
    def __init__(
        self,
        id: int = None,
        number: str = None,
        name: str = None,
    ):
        self.id = id
        self.number = number
        self.name = name

    def validate(self):
        self.validate_required(self.number, 'number')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class SaveVirtualBillTypeRequestBody(TeaModel):
    def __init__(
        self,
        items: List[VirtualBillType] = None,
    ):
        self.items = items

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = VirtualBillType()
                self.items.append(temp_model.from_map(k))
        return self


class SaveVirtualBillTypeRequest(TeaModel):
    def __init__(
        self,
        body: SaveVirtualBillTypeRequestBody = None,
    ):
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SaveVirtualBillTypeRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VirtualBillListRequestBody(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
        group_id: List[str] = None,
        billno: str = None,
        billstatus: str = None,
        startbilldate: str = None,
        endbilldate: str = None,
        startdate: str = None,
        enddate: str = None,
        begindate: str = None,
        expiredate: str = None,
        starttime: int = None,
        endtime: int = None,
        begintime: int = None,
        expiretime: int = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.ids = ids
        # 分类ID(来自外部基础资料分类)
        self.group_id = group_id
        self.billno = billno
        self.billstatus = billstatus
        self.startbilldate = startbilldate
        self.endbilldate = endbilldate
        self.startdate = startdate
        self.enddate = enddate
        self.begindate = begindate
        self.expiredate = expiredate
        self.starttime = starttime
        self.endtime = endtime
        self.begintime = begintime
        self.expiretime = expiretime
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.billno is not None:
            result['billno'] = self.billno
        if self.billstatus is not None:
            result['billstatus'] = self.billstatus
        if self.startbilldate is not None:
            result['startbilldate'] = self.startbilldate
        if self.endbilldate is not None:
            result['endbilldate'] = self.endbilldate
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.begindate is not None:
            result['begindate'] = self.begindate
        if self.expiredate is not None:
            result['expiredate'] = self.expiredate
        if self.starttime is not None:
            result['starttime'] = self.starttime
        if self.endtime is not None:
            result['endtime'] = self.endtime
        if self.begintime is not None:
            result['begintime'] = self.begintime
        if self.expiretime is not None:
            result['expiretime'] = self.expiretime
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('billno') is not None:
            self.billno = m.get('billno')
        if m.get('billstatus') is not None:
            self.billstatus = m.get('billstatus')
        if m.get('startbilldate') is not None:
            self.startbilldate = m.get('startbilldate')
        if m.get('endbilldate') is not None:
            self.endbilldate = m.get('endbilldate')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('begindate') is not None:
            self.begindate = m.get('begindate')
        if m.get('expiredate') is not None:
            self.expiredate = m.get('expiredate')
        if m.get('starttime') is not None:
            self.starttime = m.get('starttime')
        if m.get('endtime') is not None:
            self.endtime = m.get('endtime')
        if m.get('begintime') is not None:
            self.begintime = m.get('begintime')
        if m.get('expiretime') is not None:
            self.expiretime = m.get('expiretime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class VirtualBillListRequest(TeaModel):
    def __init__(
        self,
        body: VirtualBillListRequestBody = None,
    ):
        self.body = body
        # 外部单据详情

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = VirtualBillListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VirtualBillDetailRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        billno: str = None,
    ):
        self.id = id
        self.billno = billno

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.billno is not None:
            result['billno'] = self.billno
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('billno') is not None:
            self.billno = m.get('billno')
        return self


class VirtualBillDetailRequest(TeaModel):
    def __init__(
        self,
        body: VirtualBillDetailRequestBody = None,
    ):
        self.body = body
        # 保存外部单据(支持批量)

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = VirtualBillDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VirtualBillEntry(TeaModel):
    def __init__(
        self,
        id: int = None,
        material_id: str = None,
        material_number: str = None,
        qty: str = None,
        price: str = None,
        amount: str = None,
        amountfor: str = None,
        taxamount: str = None,
        taxamountfor: str = None,
        disamount: str = None,
        disamountfor: str = None,
        unit_id: str = None,
        unit_number: str = None,
        stock_id: str = None,
        stock_number: str = None,
        bank_id: str = None,
        bank_number: str = None,
        pacct_type_id: str = None,
        pacct_type_number: str = None,
        pay_out_type_id: str = None,
        pay_out_type_number: str = None,
        comment: str = None,
        entry_custom_amount_1: str = None,
        entry_custom_amount_for_1: str = None,
        entry_custom_amount_2: str = None,
        entry_custom_amount_for_2: str = None,
        entry_custom_amount_3: str = None,
        entry_custom_amount_for_3: str = None,
        entry_custom_amount_4: str = None,
        entry_custom_amount_for_4: str = None,
        entry_custom_amount_5: str = None,
        entry_custom_amount_for_5: str = None,
        custom_item_id_1: str = None,
        custom_item_number_1: str = None,
        custom_item_id_2: str = None,
        custom_item_number_2: str = None,
        custom_item_id_3: str = None,
        custom_item_number_3: str = None,
        custom_item_id_4: str = None,
        custom_item_number_4: str = None,
        custom_item_id_5: str = None,
        custom_item_number_5: str = None,
        custom_item_id_6: str = None,
        custom_item_number_6: str = None,
        custom_item_id_7: str = None,
        custom_item_number_7: str = None,
        custom_item_id_8: str = None,
        custom_item_number_8: str = None,
        custom_item_id_9: str = None,
        custom_item_number_9: str = None,
        custom_item_id_10: str = None,
        custom_item_number_10: str = None,
        entry_custom_text_1: str = None,
        entry_custom_text_2: str = None,
        entry_custom_text_3: str = None,
        entry_custom_text_4: str = None,
        entry_custom_text_5: str = None,
    ):
        self.id = id
        self.material_id = material_id
        self.material_number = material_number
        self.qty = qty
        self.price = price
        self.amount = amount
        self.amountfor = amountfor
        self.taxamount = taxamount
        self.taxamountfor = taxamountfor
        self.disamount = disamount
        self.disamountfor = disamountfor
        # 单位id
        self.unit_id = unit_id
        # 单位编码
        self.unit_number = unit_number
        # 仓库id
        self.stock_id = stock_id
        # 仓库编码
        self.stock_number = stock_number
        # 银行账户id
        self.bank_id = bank_id
        # 银行账户编码
        self.bank_number = bank_number
        # 收入类别id
        self.pacct_type_id = pacct_type_id
        # 收入类别编码
        self.pacct_type_number = pacct_type_number
        # 支出类别id
        self.pay_out_type_id = pay_out_type_id
        # 支出类别编码
        self.pay_out_type_number = pay_out_type_number
        # 分录备注
        self.comment = comment
        self.entry_custom_amount_1 = entry_custom_amount_1
        self.entry_custom_amount_for_1 = entry_custom_amount_for_1
        self.entry_custom_amount_2 = entry_custom_amount_2
        self.entry_custom_amount_for_2 = entry_custom_amount_for_2
        self.entry_custom_amount_3 = entry_custom_amount_3
        self.entry_custom_amount_for_3 = entry_custom_amount_for_3
        self.entry_custom_amount_4 = entry_custom_amount_4
        self.entry_custom_amount_for_4 = entry_custom_amount_for_4
        self.entry_custom_amount_5 = entry_custom_amount_5
        self.entry_custom_amount_for_5 = entry_custom_amount_for_5
        self.custom_item_id_1 = custom_item_id_1
        self.custom_item_number_1 = custom_item_number_1
        self.custom_item_id_2 = custom_item_id_2
        self.custom_item_number_2 = custom_item_number_2
        self.custom_item_id_3 = custom_item_id_3
        self.custom_item_number_3 = custom_item_number_3
        self.custom_item_id_4 = custom_item_id_4
        self.custom_item_number_4 = custom_item_number_4
        self.custom_item_id_5 = custom_item_id_5
        self.custom_item_number_5 = custom_item_number_5
        self.custom_item_id_6 = custom_item_id_6
        self.custom_item_number_6 = custom_item_number_6
        self.custom_item_id_7 = custom_item_id_7
        self.custom_item_number_7 = custom_item_number_7
        self.custom_item_id_8 = custom_item_id_8
        self.custom_item_number_8 = custom_item_number_8
        self.custom_item_id_9 = custom_item_id_9
        self.custom_item_number_9 = custom_item_number_9
        self.custom_item_id_10 = custom_item_id_10
        self.custom_item_number_10 = custom_item_number_10
        self.entry_custom_text_1 = entry_custom_text_1
        self.entry_custom_text_2 = entry_custom_text_2
        self.entry_custom_text_3 = entry_custom_text_3
        self.entry_custom_text_4 = entry_custom_text_4
        self.entry_custom_text_5 = entry_custom_text_5

    def validate(self):
        self.validate_required(self.material_id, 'material_id')
        self.validate_required(self.material_number, 'material_number')
        self.validate_required(self.qty, 'qty')
        self.validate_required(self.price, 'price')
        self.validate_required(self.amount, 'amount')
        self.validate_required(self.amountfor, 'amountfor')
        self.validate_required(self.taxamount, 'taxamount')
        self.validate_required(self.taxamountfor, 'taxamountfor')
        self.validate_required(self.disamount, 'disamount')
        self.validate_required(self.disamountfor, 'disamountfor')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.unit_number, 'unit_number')
        self.validate_required(self.stock_id, 'stock_id')
        self.validate_required(self.stock_number, 'stock_number')
        self.validate_required(self.bank_id, 'bank_id')
        self.validate_required(self.bank_number, 'bank_number')
        self.validate_required(self.pacct_type_id, 'pacct_type_id')
        self.validate_required(self.pacct_type_number, 'pacct_type_number')
        self.validate_required(self.pay_out_type_id, 'pay_out_type_id')
        self.validate_required(self.pay_out_type_number, 'pay_out_type_number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.material_id is not None:
            result['materialid_id'] = self.material_id
        if self.material_number is not None:
            result['materialid_number'] = self.material_number
        if self.qty is not None:
            result['qty'] = self.qty
        if self.price is not None:
            result['price'] = self.price
        if self.amount is not None:
            result['amount'] = self.amount
        if self.amountfor is not None:
            result['amountfor'] = self.amountfor
        if self.taxamount is not None:
            result['taxamount'] = self.taxamount
        if self.taxamountfor is not None:
            result['taxamountfor'] = self.taxamountfor
        if self.disamount is not None:
            result['disamount'] = self.disamount
        if self.disamountfor is not None:
            result['disamountfor'] = self.disamountfor
        if self.unit_id is not None:
            result['unit_id'] = self.unit_id
        if self.unit_number is not None:
            result['unit_number'] = self.unit_number
        if self.stock_id is not None:
            result['stockid_id'] = self.stock_id
        if self.stock_number is not None:
            result['stockid_number'] = self.stock_number
        if self.bank_id is not None:
            result['bank_id'] = self.bank_id
        if self.bank_number is not None:
            result['bank_number'] = self.bank_number
        if self.pacct_type_id is not None:
            result['paccttype_id'] = self.pacct_type_id
        if self.pacct_type_number is not None:
            result['paccttype_number'] = self.pacct_type_number
        if self.pay_out_type_id is not None:
            result['payouttype_id'] = self.pay_out_type_id
        if self.pay_out_type_number is not None:
            result['payouttype_number'] = self.pay_out_type_number
        if self.comment is not None:
            result['comment'] = self.comment
        if self.entry_custom_amount_1 is not None:
            result['entrycustomamount1'] = self.entry_custom_amount_1
        if self.entry_custom_amount_for_1 is not None:
            result['entrycustomamountfor1'] = self.entry_custom_amount_for_1
        if self.entry_custom_amount_2 is not None:
            result['entrycustomamount2'] = self.entry_custom_amount_2
        if self.entry_custom_amount_for_2 is not None:
            result['entrycustomamountfor2'] = self.entry_custom_amount_for_2
        if self.entry_custom_amount_3 is not None:
            result['entrycustomamount3'] = self.entry_custom_amount_3
        if self.entry_custom_amount_for_3 is not None:
            result['entrycustomamountfor3'] = self.entry_custom_amount_for_3
        if self.entry_custom_amount_4 is not None:
            result['entrycustomamount4'] = self.entry_custom_amount_4
        if self.entry_custom_amount_for_4 is not None:
            result['entrycustomamountfor4'] = self.entry_custom_amount_for_4
        if self.entry_custom_amount_5 is not None:
            result['entrycustomamount5'] = self.entry_custom_amount_5
        if self.entry_custom_amount_for_5 is not None:
            result['entrycustomamountfor5'] = self.entry_custom_amount_for_5
        if self.custom_item_id_1 is not None:
            result['customitem1_id'] = self.custom_item_id_1
        if self.custom_item_number_1 is not None:
            result['customitem1_number'] = self.custom_item_number_1
        if self.custom_item_id_2 is not None:
            result['customitem2_id'] = self.custom_item_id_2
        if self.custom_item_number_2 is not None:
            result['customitem2_number'] = self.custom_item_number_2
        if self.custom_item_id_3 is not None:
            result['customitem3_id'] = self.custom_item_id_3
        if self.custom_item_number_3 is not None:
            result['customitem3_number'] = self.custom_item_number_3
        if self.custom_item_id_4 is not None:
            result['customitem4_id'] = self.custom_item_id_4
        if self.custom_item_number_4 is not None:
            result['customitem4_number'] = self.custom_item_number_4
        if self.custom_item_id_5 is not None:
            result['customitem5_id'] = self.custom_item_id_5
        if self.custom_item_number_5 is not None:
            result['customitem5_number'] = self.custom_item_number_5
        if self.custom_item_id_6 is not None:
            result['customitem6_id'] = self.custom_item_id_6
        if self.custom_item_number_6 is not None:
            result['customitem6_number'] = self.custom_item_number_6
        if self.custom_item_id_7 is not None:
            result['customitem7_id'] = self.custom_item_id_7
        if self.custom_item_number_7 is not None:
            result['customitem7_number'] = self.custom_item_number_7
        if self.custom_item_id_8 is not None:
            result['customitem8_id'] = self.custom_item_id_8
        if self.custom_item_number_8 is not None:
            result['customitem8_number'] = self.custom_item_number_8
        if self.custom_item_id_9 is not None:
            result['customitem9_id'] = self.custom_item_id_9
        if self.custom_item_number_9 is not None:
            result['customitem9_number'] = self.custom_item_number_9
        if self.custom_item_id_10 is not None:
            result['customitem10_id'] = self.custom_item_id_10
        if self.custom_item_number_10 is not None:
            result['customitem10_number'] = self.custom_item_number_10
        if self.entry_custom_text_1 is not None:
            result['entrycustomtext1'] = self.entry_custom_text_1
        if self.entry_custom_text_2 is not None:
            result['entrycustomtext2'] = self.entry_custom_text_2
        if self.entry_custom_text_3 is not None:
            result['entrycustomtext3'] = self.entry_custom_text_3
        if self.entry_custom_text_4 is not None:
            result['entrycustomtext4'] = self.entry_custom_text_4
        if self.entry_custom_text_5 is not None:
            result['entrycustomtext5'] = self.entry_custom_text_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('materialid_id') is not None:
            self.material_id = m.get('materialid_id')
        if m.get('materialid_number') is not None:
            self.material_number = m.get('materialid_number')
        if m.get('qty') is not None:
            self.qty = m.get('qty')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('amountfor') is not None:
            self.amountfor = m.get('amountfor')
        if m.get('taxamount') is not None:
            self.taxamount = m.get('taxamount')
        if m.get('taxamountfor') is not None:
            self.taxamountfor = m.get('taxamountfor')
        if m.get('disamount') is not None:
            self.disamount = m.get('disamount')
        if m.get('disamountfor') is not None:
            self.disamountfor = m.get('disamountfor')
        if m.get('unit_id') is not None:
            self.unit_id = m.get('unit_id')
        if m.get('unit_number') is not None:
            self.unit_number = m.get('unit_number')
        if m.get('stockid_id') is not None:
            self.stock_id = m.get('stockid_id')
        if m.get('stockid_number') is not None:
            self.stock_number = m.get('stockid_number')
        if m.get('bank_id') is not None:
            self.bank_id = m.get('bank_id')
        if m.get('bank_number') is not None:
            self.bank_number = m.get('bank_number')
        if m.get('paccttype_id') is not None:
            self.pacct_type_id = m.get('paccttype_id')
        if m.get('paccttype_number') is not None:
            self.pacct_type_number = m.get('paccttype_number')
        if m.get('payouttype_id') is not None:
            self.pay_out_type_id = m.get('payouttype_id')
        if m.get('payouttype_number') is not None:
            self.pay_out_type_number = m.get('payouttype_number')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('entrycustomamount1') is not None:
            self.entry_custom_amount_1 = m.get('entrycustomamount1')
        if m.get('entrycustomamountfor1') is not None:
            self.entry_custom_amount_for_1 = m.get('entrycustomamountfor1')
        if m.get('entrycustomamount2') is not None:
            self.entry_custom_amount_2 = m.get('entrycustomamount2')
        if m.get('entrycustomamountfor2') is not None:
            self.entry_custom_amount_for_2 = m.get('entrycustomamountfor2')
        if m.get('entrycustomamount3') is not None:
            self.entry_custom_amount_3 = m.get('entrycustomamount3')
        if m.get('entrycustomamountfor3') is not None:
            self.entry_custom_amount_for_3 = m.get('entrycustomamountfor3')
        if m.get('entrycustomamount4') is not None:
            self.entry_custom_amount_4 = m.get('entrycustomamount4')
        if m.get('entrycustomamountfor4') is not None:
            self.entry_custom_amount_for_4 = m.get('entrycustomamountfor4')
        if m.get('entrycustomamount5') is not None:
            self.entry_custom_amount_5 = m.get('entrycustomamount5')
        if m.get('entrycustomamountfor5') is not None:
            self.entry_custom_amount_for_5 = m.get('entrycustomamountfor5')
        if m.get('customitem1_id') is not None:
            self.custom_item_id_1 = m.get('customitem1_id')
        if m.get('customitem1_number') is not None:
            self.custom_item_number_1 = m.get('customitem1_number')
        if m.get('customitem2_id') is not None:
            self.custom_item_id_2 = m.get('customitem2_id')
        if m.get('customitem2_number') is not None:
            self.custom_item_number_2 = m.get('customitem2_number')
        if m.get('customitem3_id') is not None:
            self.custom_item_id_3 = m.get('customitem3_id')
        if m.get('customitem3_number') is not None:
            self.custom_item_number_3 = m.get('customitem3_number')
        if m.get('customitem4_id') is not None:
            self.custom_item_id_4 = m.get('customitem4_id')
        if m.get('customitem4_number') is not None:
            self.custom_item_number_4 = m.get('customitem4_number')
        if m.get('customitem5_id') is not None:
            self.custom_item_id_5 = m.get('customitem5_id')
        if m.get('customitem5_number') is not None:
            self.custom_item_number_5 = m.get('customitem5_number')
        if m.get('customitem6_id') is not None:
            self.custom_item_id_6 = m.get('customitem6_id')
        if m.get('customitem6_number') is not None:
            self.custom_item_number_6 = m.get('customitem6_number')
        if m.get('customitem7_id') is not None:
            self.custom_item_id_7 = m.get('customitem7_id')
        if m.get('customitem7_number') is not None:
            self.custom_item_number_7 = m.get('customitem7_number')
        if m.get('customitem8_id') is not None:
            self.custom_item_id_8 = m.get('customitem8_id')
        if m.get('customitem8_number') is not None:
            self.custom_item_number_8 = m.get('customitem8_number')
        if m.get('customitem9_id') is not None:
            self.custom_item_id_9 = m.get('customitem9_id')
        if m.get('customitem9_number') is not None:
            self.custom_item_number_9 = m.get('customitem9_number')
        if m.get('customitem10_id') is not None:
            self.custom_item_id_10 = m.get('customitem10_id')
        if m.get('customitem10_number') is not None:
            self.custom_item_number_10 = m.get('customitem10_number')
        if m.get('entrycustomtext1') is not None:
            self.entry_custom_text_1 = m.get('entrycustomtext1')
        if m.get('entrycustomtext2') is not None:
            self.entry_custom_text_2 = m.get('entrycustomtext2')
        if m.get('entrycustomtext3') is not None:
            self.entry_custom_text_3 = m.get('entrycustomtext3')
        if m.get('entrycustomtext4') is not None:
            self.entry_custom_text_4 = m.get('entrycustomtext4')
        if m.get('entrycustomtext5') is not None:
            self.entry_custom_text_5 = m.get('entrycustomtext5')
        return self


class VirtualBillHead(TeaModel):
    def __init__(
        self,
        id: int = None,
        billno: str = None,
        billdate: str = None,
        group_id: str = None,
        group_number: str = None,
        emp_id: str = None,
        emp_number: str = None,
        dept_id: str = None,
        dept_number: str = None,
        supplier_id: str = None,
        supplier_number: str = None,
        customer_id: str = None,
        customer_number: str = None,
        currency_id: str = None,
        currency_number: str = None,
        bill_amount: str = None,
        bill_amount_for: str = None,
        exchangerate: str = None,
        remark: str = None,
        bill_custom_amount_1: str = None,
        bill_custom_amountfor_1: str = None,
        bill_custom_amount_2: str = None,
        bill_custom_amountfor_2: str = None,
        bill_custom_amount_3: str = None,
        bill_custom_amountfor_3: str = None,
        bill_custom_amount_4: str = None,
        bill_custom_amountfor_4: str = None,
        bill_custom_amount_5: str = None,
        bill_custom_amountfor_5: str = None,
        bill_custom_text_1: str = None,
        bill_custom_text_2: str = None,
        bill_custom_text_3: str = None,
        bill_custom_text_4: str = None,
        bill_custom_text_5: str = None,
        bill_entries: List[VirtualBillEntry] = None,
    ):
        self.id = id
        self.billno = billno
        self.billdate = billdate
        self.group_id = group_id
        self.group_number = group_number
        self.emp_id = emp_id
        self.emp_number = emp_number
        self.dept_id = dept_id
        self.dept_number = dept_number
        self.supplier_id = supplier_id
        self.supplier_number = supplier_number
        self.customer_id = customer_id
        self.customer_number = customer_number
        self.currency_id = currency_id
        self.currency_number = currency_number
        self.bill_amount = bill_amount
        self.bill_amount_for = bill_amount_for
        self.exchangerate = exchangerate
        self.remark = remark
        self.bill_custom_amount_1 = bill_custom_amount_1
        self.bill_custom_amountfor_1 = bill_custom_amountfor_1
        self.bill_custom_amount_2 = bill_custom_amount_2
        self.bill_custom_amountfor_2 = bill_custom_amountfor_2
        self.bill_custom_amount_3 = bill_custom_amount_3
        self.bill_custom_amountfor_3 = bill_custom_amountfor_3
        self.bill_custom_amount_4 = bill_custom_amount_4
        self.bill_custom_amountfor_4 = bill_custom_amountfor_4
        self.bill_custom_amount_5 = bill_custom_amount_5
        self.bill_custom_amountfor_5 = bill_custom_amountfor_5
        self.bill_custom_text_1 = bill_custom_text_1
        self.bill_custom_text_2 = bill_custom_text_2
        self.bill_custom_text_3 = bill_custom_text_3
        self.bill_custom_text_4 = bill_custom_text_4
        self.bill_custom_text_5 = bill_custom_text_5
        self.bill_entries = bill_entries

    def validate(self):
        self.validate_required(self.billno, 'billno')
        self.validate_required(self.billdate, 'billdate')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_number, 'group_number')
        self.validate_required(self.bill_entries, 'bill_entries')
        if self.bill_entries:
            for k in self.bill_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.billno is not None:
            result['billno'] = self.billno
        if self.billdate is not None:
            result['billdate'] = self.billdate
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_number is not None:
            result['group_number'] = self.group_number
        if self.emp_id is not None:
            result['empid_id'] = self.emp_id
        if self.emp_number is not None:
            result['empid_number'] = self.emp_number
        if self.dept_id is not None:
            result['deptid_id'] = self.dept_id
        if self.dept_number is not None:
            result['deptid_number'] = self.dept_number
        if self.supplier_id is not None:
            result['supplierid_id'] = self.supplier_id
        if self.supplier_number is not None:
            result['supplierid_number'] = self.supplier_number
        if self.customer_id is not None:
            result['customerid_id'] = self.customer_id
        if self.customer_number is not None:
            result['customerid_number'] = self.customer_number
        if self.currency_id is not None:
            result['currencyid_id'] = self.currency_id
        if self.currency_number is not None:
            result['currencyid_number'] = self.currency_number
        if self.bill_amount is not None:
            result['billamount'] = self.bill_amount
        if self.bill_amount_for is not None:
            result['billamountfor'] = self.bill_amount_for
        if self.exchangerate is not None:
            result['exchangerate'] = self.exchangerate
        if self.remark is not None:
            result['remark'] = self.remark
        if self.bill_custom_amount_1 is not None:
            result['billcustomamount1'] = self.bill_custom_amount_1
        if self.bill_custom_amountfor_1 is not None:
            result['billcustomamountfor1'] = self.bill_custom_amountfor_1
        if self.bill_custom_amount_2 is not None:
            result['billcustomamount2'] = self.bill_custom_amount_2
        if self.bill_custom_amountfor_2 is not None:
            result['billcustomamountfor2'] = self.bill_custom_amountfor_2
        if self.bill_custom_amount_3 is not None:
            result['billcustomamount3'] = self.bill_custom_amount_3
        if self.bill_custom_amountfor_3 is not None:
            result['billcustomamountfor3'] = self.bill_custom_amountfor_3
        if self.bill_custom_amount_4 is not None:
            result['billcustomamount4'] = self.bill_custom_amount_4
        if self.bill_custom_amountfor_4 is not None:
            result['billcustomamountfor4'] = self.bill_custom_amountfor_4
        if self.bill_custom_amount_5 is not None:
            result['billcustomamount5'] = self.bill_custom_amount_5
        if self.bill_custom_amountfor_5 is not None:
            result['billcustomamountfor5'] = self.bill_custom_amountfor_5
        if self.bill_custom_text_1 is not None:
            result['billcustomtext1'] = self.bill_custom_text_1
        if self.bill_custom_text_2 is not None:
            result['billcustomtext2'] = self.bill_custom_text_2
        if self.bill_custom_text_3 is not None:
            result['billcustomtext3'] = self.bill_custom_text_3
        if self.bill_custom_text_4 is not None:
            result['billcustomtext4'] = self.bill_custom_text_4
        if self.bill_custom_text_5 is not None:
            result['billcustomtext5'] = self.bill_custom_text_5
        result['entryentity'] = []
        if self.bill_entries is not None:
            for k in self.bill_entries:
                result['entryentity'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('billno') is not None:
            self.billno = m.get('billno')
        if m.get('billdate') is not None:
            self.billdate = m.get('billdate')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_number') is not None:
            self.group_number = m.get('group_number')
        if m.get('empid_id') is not None:
            self.emp_id = m.get('empid_id')
        if m.get('empid_number') is not None:
            self.emp_number = m.get('empid_number')
        if m.get('deptid_id') is not None:
            self.dept_id = m.get('deptid_id')
        if m.get('deptid_number') is not None:
            self.dept_number = m.get('deptid_number')
        if m.get('supplierid_id') is not None:
            self.supplier_id = m.get('supplierid_id')
        if m.get('supplierid_number') is not None:
            self.supplier_number = m.get('supplierid_number')
        if m.get('customerid_id') is not None:
            self.customer_id = m.get('customerid_id')
        if m.get('customerid_number') is not None:
            self.customer_number = m.get('customerid_number')
        if m.get('currencyid_id') is not None:
            self.currency_id = m.get('currencyid_id')
        if m.get('currencyid_number') is not None:
            self.currency_number = m.get('currencyid_number')
        if m.get('billamount') is not None:
            self.bill_amount = m.get('billamount')
        if m.get('billamountfor') is not None:
            self.bill_amount_for = m.get('billamountfor')
        if m.get('exchangerate') is not None:
            self.exchangerate = m.get('exchangerate')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('billcustomamount1') is not None:
            self.bill_custom_amount_1 = m.get('billcustomamount1')
        if m.get('billcustomamountfor1') is not None:
            self.bill_custom_amountfor_1 = m.get('billcustomamountfor1')
        if m.get('billcustomamount2') is not None:
            self.bill_custom_amount_2 = m.get('billcustomamount2')
        if m.get('billcustomamountfor2') is not None:
            self.bill_custom_amountfor_2 = m.get('billcustomamountfor2')
        if m.get('billcustomamount3') is not None:
            self.bill_custom_amount_3 = m.get('billcustomamount3')
        if m.get('billcustomamountfor3') is not None:
            self.bill_custom_amountfor_3 = m.get('billcustomamountfor3')
        if m.get('billcustomamount4') is not None:
            self.bill_custom_amount_4 = m.get('billcustomamount4')
        if m.get('billcustomamountfor4') is not None:
            self.bill_custom_amountfor_4 = m.get('billcustomamountfor4')
        if m.get('billcustomamount5') is not None:
            self.bill_custom_amount_5 = m.get('billcustomamount5')
        if m.get('billcustomamountfor5') is not None:
            self.bill_custom_amountfor_5 = m.get('billcustomamountfor5')
        if m.get('billcustomtext1') is not None:
            self.bill_custom_text_1 = m.get('billcustomtext1')
        if m.get('billcustomtext2') is not None:
            self.bill_custom_text_2 = m.get('billcustomtext2')
        if m.get('billcustomtext3') is not None:
            self.bill_custom_text_3 = m.get('billcustomtext3')
        if m.get('billcustomtext4') is not None:
            self.bill_custom_text_4 = m.get('billcustomtext4')
        if m.get('billcustomtext5') is not None:
            self.bill_custom_text_5 = m.get('billcustomtext5')
        self.bill_entries = []
        if m.get('entryentity') is not None:
            for k in m.get('entryentity'):
                temp_model = VirtualBillEntry()
                self.bill_entries.append(temp_model.from_map(k))
        return self


class SaveVirtualBillRequestBody(TeaModel):
    def __init__(
        self,
        items: List[VirtualBillHead] = None,
    ):
        self.items = items

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = VirtualBillHead()
                self.items.append(temp_model.from_map(k))
        return self


class SaveVirtualBillRequest(TeaModel):
    def __init__(
        self,
        body: SaveVirtualBillRequestBody = None,
    ):
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SaveVirtualBillRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


