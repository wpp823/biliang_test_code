# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Any, List


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


class SupplierGroupListRequestBody(TeaModel):
    def __init__(
        self,
        enable: str = None,
        level: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.enable = enable
        self.level = level
        self.search = search
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.level is not None:
            result['level'] = self.level
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class SupplierGroupListRequest(TeaModel):
    def __init__(
        self,
        body: SupplierGroupListRequestBody = None,
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
            temp_model = SupplierGroupListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SupplierGroupDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        number: str = None,
        parent_id: str = None,
        parent_number: str = None,
        remark: str = None,
    ):
        self.id = id
        self.name = name
        self.number = number
        self.parent_id = parent_id
        self.parent_number = parent_number
        self.remark = remark

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        if self.parent_number is not None:
            result['parent_number'] = self.parent_number
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        if m.get('parent_number') is not None:
            self.parent_number = m.get('parent_number')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class SupplierGroupListResponseData(TeaModel):
    def __init__(
        self,
        rows: List[SupplierGroupDetail] = None,
        totalpage: int = None,
        curpagesize: int = None,
        count: int = None,
        pagesize: int = None,
        page: int = None,
    ):
        self.rows = rows
        self.totalpage = totalpage
        self.curpagesize = curpagesize
        self.count = count
        self.pagesize = pagesize
        self.page = page

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        if self.totalpage is not None:
            result['totalpage'] = self.totalpage
        if self.curpagesize is not None:
            result['curpagesize'] = self.curpagesize
        if self.count is not None:
            result['count'] = self.count
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.page is not None:
            result['page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rows = []
        if m.get('rows') is not None:
            for k in m.get('rows'):
                temp_model = SupplierGroupDetail()
                self.rows.append(temp_model.from_map(k))
        if m.get('totalpage') is not None:
            self.totalpage = m.get('totalpage')
        if m.get('curpagesize') is not None:
            self.curpagesize = m.get('curpagesize')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('page') is not None:
            self.page = m.get('page')
        return self


class SupplierGroupListResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: SupplierGroupListResponseData = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = SupplierGroupListResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class SupplierGroupSaveRequest(TeaModel):
    def __init__(
        self,
        body: SupplierGroupDetail = None,
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
            temp_model = SupplierGroupDetail()
            self.body = temp_model.from_map(m['body'])
        return self

class ErrorInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        msg: str = None,
    ):
        self.id = id
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self

class SaveResponseData(TeaModel):
    def __init__(
        self,
        success_pk_ids: List[str] = None,
        success: bool = None,
        error_info: List[ErrorInfo] = None,
        message: str = None,
        error_level: str = None,
    ):
        self.success_pk_ids = success_pk_ids
        self.success = success
        self.error_info = error_info
        self.message = message
        self.error_level = error_level

    def validate(self):
        if self.error_info:
            for k in self.error_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_pk_ids is not None:
            result['successPkIds'] = self.success_pk_ids
        if self.success is not None:
            result['success'] = self.success
        result['errorInfo'] = []
        if self.error_info is not None:
            for k in self.error_info:
                result['errorInfo'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.error_level is not None:
            result['errorLevel'] = self.error_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('successPkIds') is not None:
            self.success_pk_ids = m.get('successPkIds')
        if m.get('success') is not None:
            self.success = m.get('success')
        self.error_info = []
        if m.get('errorInfo') is not None:
            for k in m.get('errorInfo'):
                temp_model = ErrorInfo()
                self.error_info.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('errorLevel') is not None:
            self.error_level = m.get('errorLevel')
        return self


class SaveResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: SaveResponseData = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = SaveResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self





class SupplierListRequestBody(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        startdate: str = None,
        enddate: str = None,
        begindate: str = None,
        expiredate: str = None,
        starttime: int = None,
        endtime: int = None,
        begintime: int = None,
        expiretime: int = None,
        selectfields: str = None,
        group: List[str] = None,
        is_data_perm: bool = None,
        show_sub_group: bool = None,
        show_debt: bool = None,
        show_contact_detail: bool = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        # 模糊搜索-名称
        self.search = search
        self.startdate = startdate
        self.enddate = enddate
        self.begindate = begindate
        self.expiredate = expiredate
        self.starttime = starttime
        self.endtime = endtime
        self.begintime = begintime
        self.expiretime = expiretime
        # 自定义返回字段（除默认字段外），多个字段用英文逗号隔开，支持的字段见下面解析
        self.selectfields = selectfields
        self.group = group
        # 是否添加数据权限校验，默认false
        self.is_data_perm = is_data_perm
        # 是否查询客户分类下面子类的客户，默认false-不显示，如无特殊情况不要开启改选项，会有性能问题
        self.show_sub_group = show_sub_group
        # 是否显示客户欠款；默认false-不显示
        self.show_debt = show_debt
        # 是否显示客户联系人信息；默认false-不显示
        self.show_contact_detail = show_contact_detail
        self.page = page
        self.pagesize = pagesize
        # 是否分页，1：不分页，其余情况下都分页
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
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
        if self.selectfields is not None:
            result['selectfields'] = self.selectfields
        if self.group is not None:
            result['group'] = self.group
        if self.is_data_perm is not None:
            result['isdataperm'] = self.is_data_perm
        if self.show_sub_group is not None:
            result['showsubgroup'] = self.show_sub_group
        if self.show_debt is not None:
            result['showdebt'] = self.show_debt
        if self.show_contact_detail is not None:
            result['showcontactdetail'] = self.show_contact_detail
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
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
        if m.get('selectfields') is not None:
            self.selectfields = m.get('selectfields')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('isdataperm') is not None:
            self.is_data_perm = m.get('isdataperm')
        if m.get('showsubgroup') is not None:
            self.show_sub_group = m.get('showsubgroup')
        if m.get('showdebt') is not None:
            self.show_debt = m.get('showdebt')
        if m.get('showcontactdetail') is not None:
            self.show_contact_detail = m.get('showcontactdetail')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class SupplierListRequest(TeaModel):
    def __init__(
        self,
        body: SupplierListRequestBody = None,
    ):
        self.body = body
        # 供应商列表

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
            temp_model = SupplierListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SupplierDetailRequestBody(TeaModel):
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


class SupplierDetailRequest(TeaModel):
    def __init__(
        self,
        body: SupplierDetailRequestBody = None,
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
            temp_model = SupplierDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContactPerson(TeaModel):
    def __init__(
        self,
        contact_person: str = None,
        mobile: str = None,
        phone: str = None,
        gender: str = None,
        birthday: str = None,
        qq: str = None,
        wechat: str = None,
        email: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        district: str = None,
        address: str = None,
        is_default_link_man: str = None,
        id: str = None,
    ):
        self.contact_person = contact_person
        self.mobile = mobile
        self.phone = phone
        self.gender = gender
        self.birthday = birthday
        self.qq = qq
        self.wechat = wechat
        self.email = email
        self.country = country
        self.province = province
        self.city = city
        self.district = district
        self.address = address
        self.is_default_link_man = is_default_link_man
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_person is not None:
            result['contactperson'] = self.contact_person
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.phone is not None:
            result['phone'] = self.phone
        if self.gender is not None:
            result['gender'] = self.gender
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.qq is not None:
            result['qq'] = self.qq
        if self.wechat is not None:
            result['wechat'] = self.wechat
        if self.email is not None:
            result['email'] = self.email
        if self.country is not None:
            result['contact_countryid'] = self.country
        if self.province is not None:
            result['contact_provinceid'] = self.province
        if self.city is not None:
            result['contact_cityid'] = self.city
        if self.district is not None:
            result['contact_districtid'] = self.district
        if self.address is not None:
            result['contact_address'] = self.address
        if self.is_default_link_man is not None:
            result['isdefault_linkman'] = self.is_default_link_man
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactperson') is not None:
            self.contact_person = m.get('contactperson')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('qq') is not None:
            self.qq = m.get('qq')
        if m.get('wechat') is not None:
            self.wechat = m.get('wechat')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('contact_countryid') is not None:
            self.country = m.get('contact_countryid')
        if m.get('contact_provinceid') is not None:
            self.province = m.get('contact_provinceid')
        if m.get('contact_cityid') is not None:
            self.city = m.get('contact_cityid')
        if m.get('contact_districtid') is not None:
            self.district = m.get('contact_districtid')
        if m.get('contact_address') is not None:
            self.address = m.get('contact_address')
        if m.get('isdefault_linkman') is not None:
            self.is_default_link_man = m.get('isdefault_linkman')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class SupplierDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        group_id: str = None,
        group_number: str = None,
        sale_dept_id: str = None,
        sale_dept_number: str = None,
        saler_id: str = None,
        saler_number: str = None,
        rate: str = None,
        invoice_name: str = None,
        tax_payer_no: str = None,
        bank_account: str = None,
        bank: str = None,
        account_open_addr: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        district: str = None,
        addr: str = None,
        remark: str = None,
        contact_persons: List[ContactPerson] = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        self.group_id = group_id
        self.group_number = group_number
        self.sale_dept_id = sale_dept_id
        self.sale_dept_number = sale_dept_number
        self.saler_id = saler_id
        self.saler_number = saler_number
        self.rate = rate
        self.invoice_name = invoice_name
        self.tax_payer_no = tax_payer_no
        self.bank_account = bank_account
        self.bank = bank
        self.account_open_addr = account_open_addr
        self.country = country
        self.province = province
        self.city = city
        self.district = district
        self.addr = addr
        self.remark = remark
        # 联系人
        self.contact_persons = contact_persons

    def validate(self):
        if self.contact_persons:
            for k in self.contact_persons:
                if k:
                    k.validate()

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
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_number is not None:
            result['group_number'] = self.group_number
        if self.sale_dept_id is not None:
            result['saledeptid_id'] = self.sale_dept_id
        if self.sale_dept_number is not None:
            result['saledeptid_number'] = self.sale_dept_number
        if self.saler_id is not None:
            result['salerid_id'] = self.saler_id
        if self.saler_number is not None:
            result['salerid_number'] = self.saler_number
        if self.rate is not None:
            result['rate'] = self.rate
        if self.invoice_name is not None:
            result['invoicename'] = self.invoice_name
        if self.tax_payer_no is not None:
            result['taxpayerno'] = self.tax_payer_no
        if self.bank_account is not None:
            result['bankaccount'] = self.bank_account
        if self.bank is not None:
            result['bank'] = self.bank
        if self.account_open_addr is not None:
            result['accountopenaddr'] = self.account_open_addr
        if self.country is not None:
            result['countryid_id'] = self.country
        if self.province is not None:
            result['provinceid_id'] = self.province
        if self.city is not None:
            result['cityid_id'] = self.city
        if self.district is not None:
            result['districtid_id'] = self.district
        if self.addr is not None:
            result['addr'] = self.addr
        if self.remark is not None:
            result['remark'] = self.remark
        result['bomentity'] = []
        if self.contact_persons is not None:
            for k in self.contact_persons:
                result['bomentity'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_number') is not None:
            self.group_number = m.get('group_number')
        if m.get('saledeptid_id') is not None:
            self.sale_dept_id = m.get('saledeptid_id')
        if m.get('saledeptid_number') is not None:
            self.sale_dept_number = m.get('saledeptid_number')
        if m.get('salerid_id') is not None:
            self.saler_id = m.get('salerid_id')
        if m.get('salerid_number') is not None:
            self.saler_number = m.get('salerid_number')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('invoicename') is not None:
            self.invoice_name = m.get('invoicename')
        if m.get('taxpayerno') is not None:
            self.tax_payer_no = m.get('taxpayerno')
        if m.get('bankaccount') is not None:
            self.bank_account = m.get('bankaccount')
        if m.get('bank') is not None:
            self.bank = m.get('bank')
        if m.get('accountopenaddr') is not None:
            self.account_open_addr = m.get('accountopenaddr')
        if m.get('countryid_id') is not None:
            self.country = m.get('countryid_id')
        if m.get('provinceid_id') is not None:
            self.province = m.get('provinceid_id')
        if m.get('cityid_id') is not None:
            self.city = m.get('cityid_id')
        if m.get('districtid_id') is not None:
            self.district = m.get('districtid_id')
        if m.get('addr') is not None:
            self.addr = m.get('addr')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        self.contact_persons = []
        if m.get('bomentity') is not None:
            for k in m.get('bomentity'):
                temp_model = ContactPerson()
                self.contact_persons.append(temp_model.from_map(k))
        return self


class SupplierDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: SupplierDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = SupplierDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class SupplierDetailBatchRequestBodyItems(TeaModel):
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


class SupplierDetailBatchRequestBody(TeaModel):
    def __init__(
        self,
        items: List[SupplierDetailBatchRequestBodyItems] = None,
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
                temp_model = SupplierDetailBatchRequestBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class SupplierDetailBatchRequest(TeaModel):
    def __init__(
        self,
        body: SupplierDetailBatchRequestBody = None,
    ):
        self.body = body
        # 批量查询供应商详情

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
            temp_model = SupplierDetailBatchRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SupplierSaveRequest(TeaModel):
    def __init__(
        self,
        body: SupplierDetail = None,
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
            temp_model = SupplierDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSupplierBatchRequestBody(TeaModel):
    def __init__(
        self,
        items: List[SupplierDetail] = None,
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
                temp_model = SupplierDetail()
                self.items.append(temp_model.from_map(k))
        return self


class SaveSupplierBatchRequest(TeaModel):
    def __init__(
        self,
        body: SaveSupplierBatchRequestBody = None,
    ):
        self.body = body
        # 供应商批量保存

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
            temp_model = SaveSupplierBatchRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomerGroupListRequestBody(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
        name: str = None,
        number: str = None,
        search: str = None,
        parent: List[str] = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.ids = ids
        self.name = name
        self.number = number
        self.search = search
        # 父级类别id
        self.parent = parent
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
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.search is not None:
            result['search'] = self.search
        if self.parent is not None:
            result['parent'] = self.parent
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class CustomerGroupListRequest(TeaModel):
    def __init__(
        self,
        body: CustomerGroupListRequestBody = None,
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
            temp_model = CustomerGroupListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomerGroupDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        number: str = None,
        parent_id: str = None,
        parent_number: str = None,
        remark: str = None,
        level: str = None,
        isleaf: str = None,
    ):
        self.id = id
        self.name = name
        self.number = number
        self.parent_id = parent_id
        self.parent_number = parent_number
        self.remark = remark
        self.level = level
        self.isleaf = isleaf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        if self.parent_number is not None:
            result['parent_number'] = self.parent_number
        if self.remark is not None:
            result['remark'] = self.remark
        if self.level is not None:
            result['level'] = self.level
        if self.isleaf is not None:
            result['isleaf'] = self.isleaf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        if m.get('parent_number') is not None:
            self.parent_number = m.get('parent_number')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('isleaf') is not None:
            self.isleaf = m.get('isleaf')
        return self


class CustomerGroupListResponseData(TeaModel):
    def __init__(
        self,
        rows: List[CustomerGroupDetail] = None,
        totalpage: int = None,
        curpagesize: int = None,
        count: int = None,
        pagesize: int = None,
        page: int = None,
    ):
        self.rows = rows
        self.totalpage = totalpage
        self.curpagesize = curpagesize
        self.count = count
        self.pagesize = pagesize
        self.page = page

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        if self.totalpage is not None:
            result['totalpage'] = self.totalpage
        if self.curpagesize is not None:
            result['curpagesize'] = self.curpagesize
        if self.count is not None:
            result['count'] = self.count
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.page is not None:
            result['page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rows = []
        if m.get('rows') is not None:
            for k in m.get('rows'):
                temp_model = CustomerGroupDetail()
                self.rows.append(temp_model.from_map(k))
        if m.get('totalpage') is not None:
            self.totalpage = m.get('totalpage')
        if m.get('curpagesize') is not None:
            self.curpagesize = m.get('curpagesize')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('page') is not None:
            self.page = m.get('page')
        return self


class CustomerGroupListResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: CustomerGroupListResponseData = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = CustomerGroupListResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class CustomerGroupSaveRequest(TeaModel):
    def __init__(
        self,
        body: CustomerGroupDetail = None,
    ):
        self.body = body
        # 保存客户类别

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
            temp_model = CustomerGroupDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomerListRequestBody(TeaModel):
    def __init__(
        self,
        group: List[str] = None,
        clevel: str = None,
        saler_id: str = None,
        sale_dept_id: str = None,
        main_concact_persion: str = None,
        main_concact_mobile: str = None,
        mul_label: List[str] = None,
        customer_maturity: str = None,
        enable: str = None,
        trace_startdate: str = None,
        trace_enddate: str = None,
        startdate: str = None,
        enddate: str = None,
        begindate: str = None,
        expiredate: str = None,
        starttime: int = None,
        endtime: int = None,
        begintime: int = None,
        expiretime: int = None,
        search: str = None,
        selectfields: str = None,
        orderby: str = None,
        is_data_perm: bool = None,
        show_sub_group: bool = None,
        show_debt: bool = None,
        show_trace_info: bool = None,
        show_unvisit_days: bool = None,
        show_business_time: bool = None,
        show_alarm: bool = None,
        show_contact_detail: bool = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        self.group = group
        self.clevel = clevel
        self.saler_id = saler_id
        self.sale_dept_id = sale_dept_id
        # 主要联系人名称
        self.main_concact_persion = main_concact_persion
        # 主要联系人电话
        self.main_concact_mobile = main_concact_mobile
        # 客户标签，格式：[“xxx”,”xxx”]
        self.mul_label = mul_label
        # 成熟度id
        self.customer_maturity = customer_maturity
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        # 跟进开始时间（格式：“yyyy-MM-dd”）
        self.trace_startdate = trace_startdate
        # 跟进结束时间（格式：“yyyy-MM-dd”）
        self.trace_enddate = trace_enddate
        self.startdate = startdate
        self.enddate = enddate
        self.begindate = begindate
        self.expiredate = expiredate
        self.starttime = starttime
        self.endtime = endtime
        self.begintime = begintime
        self.expiretime = expiretime
        # 按客户名称、客户编码模糊查询
        self.search = search
        # 自定义返回字段（除默认字段外），多个字段用英文逗号隔开，支持的字段见下面解析
        self.selectfields = selectfields
        # 排序；
        self.orderby = orderby
        # 是否添加数据权限校验，默认false
        self.is_data_perm = is_data_perm
        # 是否查询客户分类下面子类的客户，默认false-不显示，如无特殊情况不要开启改选项，会有性能问题
        self.show_sub_group = show_sub_group
        # 是否显示客户欠款；默认false-不显示
        self.show_debt = show_debt
        # 是否显示最近一条跟进记录；默认false-不显示
        self.show_trace_info = show_trace_info
        # 是否显示未拜访天数；默认false-不显示
        self.show_unvisit_days = show_unvisit_days
        # 是否显示最近交易时间；默认false-不显示
        self.show_business_time = show_business_time
        # 是否显示客户预警信息；默认false-不显示
        self.show_alarm = show_alarm
        # 是否显示客户联系人信息；默认false-不显示
        self.show_contact_detail = show_contact_detail
        self.page = page
        self.pagesize = pagesize
        # 是否分页，1：不分页，其余情况下都分页
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.clevel is not None:
            result['clevel'] = self.clevel
        if self.saler_id is not None:
            result['salerid'] = self.saler_id
        if self.sale_dept_id is not None:
            result['saledeptid'] = self.sale_dept_id
        if self.main_concact_persion is not None:
            result['contactperson_main'] = self.main_concact_persion
        if self.main_concact_mobile is not None:
            result['contactperson_main'] = self.main_concact_mobile
        if self.mul_label is not None:
            result['mullabel'] = self.mul_label
        if self.customer_maturity is not None:
            result['customer_maturity'] = self.customer_maturity
        if self.enable is not None:
            result['enable'] = self.enable
        if self.trace_startdate is not None:
            result['traceStartdate'] = self.trace_startdate
        if self.trace_enddate is not None:
            result['traceEnddate'] = self.trace_enddate
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
        if self.search is not None:
            result['search'] = self.search
        if self.selectfields is not None:
            result['selectfields'] = self.selectfields
        if self.orderby is not None:
            result['orderby'] = self.orderby
        if self.is_data_perm is not None:
            result['isdataperm'] = self.is_data_perm
        if self.show_sub_group is not None:
            result['showsubgroup'] = self.show_sub_group
        if self.show_debt is not None:
            result['showdebt'] = self.show_debt
        if self.show_trace_info is not None:
            result['showtraceinfo'] = self.show_trace_info
        if self.show_unvisit_days is not None:
            result['showunvisitdays'] = self.show_unvisit_days
        if self.show_business_time is not None:
            result['showbusinesstime'] = self.show_business_time
        if self.show_alarm is not None:
            result['showalarm'] = self.show_alarm
        if self.show_contact_detail is not None:
            result['showcontactdetail'] = self.show_contact_detail
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('clevel') is not None:
            self.clevel = m.get('clevel')
        if m.get('salerid') is not None:
            self.saler_id = m.get('salerid')
        if m.get('saledeptid') is not None:
            self.sale_dept_id = m.get('saledeptid')
        if m.get('contactperson_main') is not None:
            self.main_concact_persion = m.get('contactperson_main')
        if m.get('contactperson_main') is not None:
            self.main_concact_mobile = m.get('contactperson_main')
        if m.get('mullabel') is not None:
            self.mul_label = m.get('mullabel')
        if m.get('customer_maturity') is not None:
            self.customer_maturity = m.get('customer_maturity')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('traceStartdate') is not None:
            self.trace_startdate = m.get('traceStartdate')
        if m.get('traceEnddate') is not None:
            self.trace_enddate = m.get('traceEnddate')
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
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('selectfields') is not None:
            self.selectfields = m.get('selectfields')
        if m.get('orderby') is not None:
            self.orderby = m.get('orderby')
        if m.get('isdataperm') is not None:
            self.is_data_perm = m.get('isdataperm')
        if m.get('showsubgroup') is not None:
            self.show_sub_group = m.get('showsubgroup')
        if m.get('showdebt') is not None:
            self.show_debt = m.get('showdebt')
        if m.get('showtraceinfo') is not None:
            self.show_trace_info = m.get('showtraceinfo')
        if m.get('showunvisitdays') is not None:
            self.show_unvisit_days = m.get('showunvisitdays')
        if m.get('showbusinesstime') is not None:
            self.show_business_time = m.get('showbusinesstime')
        if m.get('showalarm') is not None:
            self.show_alarm = m.get('showalarm')
        if m.get('showcontactdetail') is not None:
            self.show_contact_detail = m.get('showcontactdetail')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class CustomerListRequest(TeaModel):
    def __init__(
        self,
        body: CustomerListRequestBody = None,
    ):
        self.body = body
        # 查询客户列表

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
            temp_model = CustomerListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomerDetailRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        show_period: bool = None,
        show_unvisit_days: bool = None,
        show_business_time: bool = None,
        show_debt: bool = None,
    ):
        self.id = id
        self.number = number
        # 是否查询周期信息，true-查询，false-不查询；默认为：false
        self.show_period = show_period
        # 是否显示未拜访天数；默认false-不显示
        self.show_unvisit_days = show_unvisit_days
        # 是否查询客户最近交易时间，true-查询，false-不查询；默认为：false
        self.show_business_time = show_business_time
        # 是否查询客户欠款，true-查询，false-不查询；默认为：false
        self.show_debt = show_debt

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        if self.show_period is not None:
            result['showperiod'] = self.show_period
        if self.show_unvisit_days is not None:
            result['showunvisitdays'] = self.show_unvisit_days
        if self.show_business_time is not None:
            result['showbusinesstime'] = self.show_business_time
        if self.show_debt is not None:
            result['showdebt'] = self.show_debt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('showperiod') is not None:
            self.show_period = m.get('showperiod')
        if m.get('showunvisitdays') is not None:
            self.show_unvisit_days = m.get('showunvisitdays')
        if m.get('showbusinesstime') is not None:
            self.show_business_time = m.get('showbusinesstime')
        if m.get('showdebt') is not None:
            self.show_debt = m.get('showdebt')
        return self


class CustomerDetailRequest(TeaModel):
    def __init__(
        self,
        body: CustomerDetailRequestBody = None,
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
            temp_model = CustomerDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomerDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        group_id: str = None,
        group_number: str = None,
        clevel_id: str = None,
        clevel_number: str = None,
        sale_dept_id: str = None,
        sale_dept_number: str = None,
        saler_id: str = None,
        saler_number: str = None,
        mul_label: List[str] = None,
        rate: str = None,
        invoice_name: str = None,
        tax_payer_no: str = None,
        bank_account: str = None,
        bank: str = None,
        account_open_addr: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        district: str = None,
        addr: str = None,
        remark: str = None,
        contact_persons: List[ContactPerson] = None,
        ignore_warn: bool = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        self.group_id = group_id
        self.group_number = group_number
        self.clevel_id = clevel_id
        self.clevel_number = clevel_number
        self.sale_dept_id = sale_dept_id
        self.sale_dept_number = sale_dept_number
        self.saler_id = saler_id
        self.saler_number = saler_number
        self.mul_label = mul_label
        self.rate = rate
        self.invoice_name = invoice_name
        self.tax_payer_no = tax_payer_no
        self.bank_account = bank_account
        self.bank = bank
        self.account_open_addr = account_open_addr
        self.country = country
        self.province = province
        self.city = city
        self.district = district
        self.addr = addr
        self.remark = remark
        # 联系人
        self.contact_persons = contact_persons
        self.ignore_warn = ignore_warn

    def validate(self):
        if self.contact_persons:
            for k in self.contact_persons:
                if k:
                    k.validate()

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
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_number is not None:
            result['group_number'] = self.group_number
        if self.clevel_id is not None:
            result['clevel_id'] = self.clevel_id
        if self.clevel_number is not None:
            result['clevel_number'] = self.clevel_number
        if self.sale_dept_id is not None:
            result['saledeptid_id'] = self.sale_dept_id
        if self.sale_dept_number is not None:
            result['saledeptid_number'] = self.sale_dept_number
        if self.saler_id is not None:
            result['salerid_id'] = self.saler_id
        if self.saler_number is not None:
            result['salerid_number'] = self.saler_number
        if self.mul_label is not None:
            result['mullabel'] = self.mul_label
        if self.rate is not None:
            result['rate'] = self.rate
        if self.invoice_name is not None:
            result['invoicename'] = self.invoice_name
        if self.tax_payer_no is not None:
            result['taxpayerno'] = self.tax_payer_no
        if self.bank_account is not None:
            result['bankaccount'] = self.bank_account
        if self.bank is not None:
            result['bank'] = self.bank
        if self.account_open_addr is not None:
            result['accountopenaddr'] = self.account_open_addr
        if self.country is not None:
            result['countryid_id'] = self.country
        if self.province is not None:
            result['provinceid_id'] = self.province
        if self.city is not None:
            result['cityid_id'] = self.city
        if self.district is not None:
            result['districtid_id'] = self.district
        if self.addr is not None:
            result['addr'] = self.addr
        if self.remark is not None:
            result['remark'] = self.remark
        result['contactpersons'] = []
        if self.contact_persons is not None:
            for k in self.contact_persons:
                result['contactpersons'].append(k.to_map() if k else None)
        if self.ignore_warn is not None:
            result['ignorewarn'] = self.ignore_warn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_number') is not None:
            self.group_number = m.get('group_number')
        if m.get('clevel_id') is not None:
            self.clevel_id = m.get('clevel_id')
        if m.get('clevel_number') is not None:
            self.clevel_number = m.get('clevel_number')
        if m.get('saledeptid_id') is not None:
            self.sale_dept_id = m.get('saledeptid_id')
        if m.get('saledeptid_number') is not None:
            self.sale_dept_number = m.get('saledeptid_number')
        if m.get('salerid_id') is not None:
            self.saler_id = m.get('salerid_id')
        if m.get('salerid_number') is not None:
            self.saler_number = m.get('salerid_number')
        if m.get('mullabel') is not None:
            self.mul_label = m.get('mullabel')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('invoicename') is not None:
            self.invoice_name = m.get('invoicename')
        if m.get('taxpayerno') is not None:
            self.tax_payer_no = m.get('taxpayerno')
        if m.get('bankaccount') is not None:
            self.bank_account = m.get('bankaccount')
        if m.get('bank') is not None:
            self.bank = m.get('bank')
        if m.get('accountopenaddr') is not None:
            self.account_open_addr = m.get('accountopenaddr')
        if m.get('countryid_id') is not None:
            self.country = m.get('countryid_id')
        if m.get('provinceid_id') is not None:
            self.province = m.get('provinceid_id')
        if m.get('cityid_id') is not None:
            self.city = m.get('cityid_id')
        if m.get('districtid_id') is not None:
            self.district = m.get('districtid_id')
        if m.get('addr') is not None:
            self.addr = m.get('addr')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        self.contact_persons = []
        if m.get('contactpersons') is not None:
            for k in m.get('contactpersons'):
                temp_model = ContactPerson()
                self.contact_persons.append(temp_model.from_map(k))
        if m.get('ignorewarn') is not None:
            self.ignore_warn = m.get('ignorewarn')
        return self


class CustomerDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: CustomerDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = CustomerDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class CustomerDetailBatchRequestBodyItems(TeaModel):
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


class CustomerDetailBatchRequestBody(TeaModel):
    def __init__(
        self,
        items: List[CustomerDetailBatchRequestBodyItems] = None,
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
                temp_model = CustomerDetailBatchRequestBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class CustomerDetailBatchRequest(TeaModel):
    def __init__(
        self,
        body: CustomerDetailBatchRequestBody = None,
    ):
        self.body = body
        # 批量查询客户详情

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
            temp_model = CustomerDetailBatchRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomerSaveRequest(TeaModel):
    def __init__(
        self,
        body: CustomerDetail = None,
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
            temp_model = CustomerDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomerBatchSaveRequestBody(TeaModel):
    def __init__(
        self,
        items: List[CustomerDetail] = None,
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
                temp_model = CustomerDetail()
                self.items.append(temp_model.from_map(k))
        return self


class CustomerBatchSaveRequest(TeaModel):
    def __init__(
        self,
        body: CustomerBatchSaveRequestBody = None,
    ):
        self.body = body
        # 客户批量保存

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
            temp_model = CustomerBatchSaveRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DepartmentListRequestBody(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
        parentid: List[str] = None,
        level: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        self.ids = ids
        self.parentid = parentid
        self.level = level
        # 模糊搜索-名称,编码
        self.search = search
        self.page = page
        self.pagesize = pagesize
        # 是否分页，1：不分页，其余情况下都分页
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.parentid is not None:
            result['parentid'] = self.parentid
        if self.level is not None:
            result['level'] = self.level
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('parentid') is not None:
            self.parentid = m.get('parentid')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class DepartmentListRequest(TeaModel):
    def __init__(
        self,
        body: DepartmentListRequestBody = None,
    ):
        self.body = body
        # 查询部门列表

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
            temp_model = DepartmentListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DepartmentDetailRequestBody(TeaModel):
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


class DepartmentDetailRequest(TeaModel):
    def __init__(
        self,
        body: DepartmentDetailRequestBody = None,
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
            temp_model = DepartmentDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DepartmentDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        org_id: str = None,
        org_number: str = None,
        description: str = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        # 上级部门id
        self.org_id = org_id
        # 上级部门编码
        self.org_number = org_number
        # 描述
        self.description = description

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
        if self.name is not None:
            result['name'] = self.name
        if self.org_id is not None:
            result['group_id'] = self.org_id
        if self.org_number is not None:
            result['parentorg_id'] = self.org_number
        if self.description is not None:
            result['fcomment'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('group_id') is not None:
            self.org_id = m.get('group_id')
        if m.get('parentorg_id') is not None:
            self.org_number = m.get('parentorg_id')
        if m.get('fcomment') is not None:
            self.description = m.get('fcomment')
        return self


class DepartmentDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: DepartmentDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = DepartmentDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class DepartmentSaveRequest(TeaModel):
    def __init__(
        self,
        body: DepartmentDetail = None,
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
            temp_model = DepartmentDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class EmployeeListRequestBody(TeaModel):
    def __init__(
        self,
        deptid: List[str] = None,
        enable: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        self.deptid = deptid
        self.enable = enable
        # 模糊搜索-名称,编码
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deptid is not None:
            result['deptid'] = self.deptid
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptid') is not None:
            self.deptid = m.get('deptid')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class EmployeeListRequest(TeaModel):
    def __init__(
        self,
        body: EmployeeListRequestBody = None,
    ):
        self.body = body
        # 查询职员列表

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
            temp_model = EmployeeListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmployeeDetailRequestBody(TeaModel):
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


class EmployeeDetailRequest(TeaModel):
    def __init__(
        self,
        body: EmployeeDetailRequestBody = None,
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
            temp_model = EmployeeDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmployeeDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        gender: str = None,
        mobile: str = None,
        birthday: str = None,
        email: str = None,
        wechat: str = None,
        id_number: str = None,
        hire_date: str = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        self.gender = gender
        self.mobile = mobile
        self.birthday = birthday
        self.email = email
        self.wechat = wechat
        # 身份证号
        self.id_number = id_number
        # 入职日期
        self.hire_date = hire_date

    def validate(self):
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
        if self.gender is not None:
            result['gender'] = self.gender
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.email is not None:
            result['email'] = self.email
        if self.wechat is not None:
            result['wechat'] = self.wechat
        if self.id_number is not None:
            result['idnumber'] = self.id_number
        if self.hire_date is not None:
            result['hiredate'] = self.hire_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('wechat') is not None:
            self.wechat = m.get('wechat')
        if m.get('idnumber') is not None:
            self.id_number = m.get('idnumber')
        if m.get('hiredate') is not None:
            self.hire_date = m.get('hiredate')
        return self


class EmployeeDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: EmployeeDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = EmployeeDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class EmployeeSaveRequest(TeaModel):
    def __init__(
        self,
        body: EmployeeDetail = None,
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
            temp_model = EmployeeDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class SettlingTermListRequestBody(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class SettlingTermListRequest(TeaModel):
    def __init__(
        self,
        body: SettlingTermListRequestBody = None,
    ):
        self.body = body
        # 结算期限列表

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
            temp_model = SettlingTermListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SettlingTermDetailRequestBody(TeaModel):
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


class SettlingTermDetailRequest(TeaModel):
    def __init__(
        self,
        body: SettlingTermDetailRequestBody = None,
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
            temp_model = SettlingTermDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SettlingTermDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
        enable: str = None,
        stand_days: str = None,
        month_pay_day: str = None,
        before_dys: str = None,
        month_check_day: str = None,
    ):
        self.id = id
        self.name = name
        self.type = type
        self.enable = enable
        # 收款期限，type为1时传递
        self.stand_days = stand_days
        # 月结期限每月结算日期，type为2时传递
        self.month_pay_day = month_pay_day
        # 月结期限结算多少天，type为2时传递
        self.before_dys = before_dys
        # 对账日
        self.month_check_day = month_check_day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.stand_days is not None:
            result['standdays'] = self.stand_days
        if self.month_pay_day is not None:
            result['monthpayday'] = self.month_pay_day
        if self.before_dys is not None:
            result['beforedays'] = self.before_dys
        if self.month_check_day is not None:
            result['monthcheckday'] = self.month_check_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('standdays') is not None:
            self.stand_days = m.get('standdays')
        if m.get('monthpayday') is not None:
            self.month_pay_day = m.get('monthpayday')
        if m.get('beforedays') is not None:
            self.before_dys = m.get('beforedays')
        if m.get('monthcheckday') is not None:
            self.month_check_day = m.get('monthcheckday')
        return self


class SettlingTermDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: SettlingTermDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = SettlingTermDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class SettlingTermSaveRequest(TeaModel):
    def __init__(
        self,
        body: SettlingTermDetail = None,
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
            temp_model = SettlingTermDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class SettlementListRequestBody(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class SettlementListRequest(TeaModel):
    def __init__(
        self,
        body: SettlementListRequestBody = None,
    ):
        self.body = body
        # 结算方式列表

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
            temp_model = SettlementListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SettlementDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        is_default: bool = None,
    ):
        self.id = id
        self.name = name
        # 是否默认结算方式
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.is_default is not None:
            result['isdefault'] = self.is_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('isdefault') is not None:
            self.is_default = m.get('isdefault')
        return self


class SettlementSaveRequest(TeaModel):
    def __init__(
        self,
        body: SettlementDetail = None,
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
            temp_model = SettlementDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class StockGroupListRequestBody(TeaModel):
    def __init__(
        self,
        enable: str = None,
        parent_ids: List[str] = None,
        level: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        self.enable = enable
        # 父级id，全部：-1
        self.parent_ids = parent_ids
        self.level = level
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.parent_ids is not None:
            result['parentid_id'] = self.parent_ids
        if self.level is not None:
            result['level'] = self.level
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('parentid_id') is not None:
            self.parent_ids = m.get('parentid_id')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class StockGroupListRequest(TeaModel):
    def __init__(
        self,
        body: StockGroupListRequestBody = None,
    ):
        self.body = body
        # 仓库分类列表

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
            temp_model = StockGroupListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StockGroupDetailRequestBody(TeaModel):
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


class StockGroupDetailRequest(TeaModel):
    def __init__(
        self,
        body: StockGroupDetailRequestBody = None,
    ):
        self.body = body
        # 查询仓库分类详情

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
            temp_model = StockGroupDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StockListRequestBody(TeaModel):
    def __init__(
        self,
        group: List[str] = None,
        enable: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        self.group = group
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        # 按客户名称、客户编码模糊查询
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['groupid'] = self.group
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupid') is not None:
            self.group = m.get('groupid')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class StockListRequest(TeaModel):
    def __init__(
        self,
        body: StockListRequestBody = None,
    ):
        self.body = body
        # 仓库列表

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
            temp_model = StockListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StockDetailRequestBody(TeaModel):
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


class StockDetailRequest(TeaModel):
    def __init__(
        self,
        body: StockDetailRequestBody = None,
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
            temp_model = StockDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StockDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        is_allow_neg: str = None,
        isallowfreight: str = None,
        group_id: str = None,
        store_keeper_id: str = None,
        mobile: str = None,
        phone: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        district: str = None,
        addr: str = None,
        remark: str = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        # 是否允许负库存
        self.is_allow_neg = is_allow_neg
        # 是否启用仓位管理
        self.isallowfreight = isallowfreight
        # 是否启用仓位管理
        self.group_id = group_id
        # 仓管id
        self.store_keeper_id = store_keeper_id
        self.mobile = mobile
        self.phone = phone
        self.country = country
        self.province = province
        self.city = city
        self.district = district
        self.addr = addr
        self.remark = remark

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
        if self.name is not None:
            result['name'] = self.name
        if self.is_allow_neg is not None:
            result['isallowneg'] = self.is_allow_neg
        if self.isallowfreight is not None:
            result['isallowfreight'] = self.isallowfreight
        if self.group_id is not None:
            result['groupid_id'] = self.group_id
        if self.store_keeper_id is not None:
            result['storekeeper_id'] = self.store_keeper_id
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.phone is not None:
            result['phone'] = self.phone
        if self.country is not None:
            result['countryid_id'] = self.country
        if self.province is not None:
            result['provinceid_id'] = self.province
        if self.city is not None:
            result['cityid_id'] = self.city
        if self.district is not None:
            result['districtid_id'] = self.district
        if self.addr is not None:
            result['addr'] = self.addr
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('isallowneg') is not None:
            self.is_allow_neg = m.get('isallowneg')
        if m.get('isallowfreight') is not None:
            self.isallowfreight = m.get('isallowfreight')
        if m.get('groupid_id') is not None:
            self.group_id = m.get('groupid_id')
        if m.get('storekeeper_id') is not None:
            self.store_keeper_id = m.get('storekeeper_id')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('countryid_id') is not None:
            self.country = m.get('countryid_id')
        if m.get('provinceid_id') is not None:
            self.province = m.get('provinceid_id')
        if m.get('cityid_id') is not None:
            self.city = m.get('cityid_id')
        if m.get('districtid_id') is not None:
            self.district = m.get('districtid_id')
        if m.get('addr') is not None:
            self.addr = m.get('addr')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class StockDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: StockDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = StockDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class StockSaveRequest(TeaModel):
    def __init__(
        self,
        body: StockDetail = None,
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
            temp_model = StockDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class StockSpaceListRequestBody(TeaModel):
    def __init__(
        self,
        group: List[str] = None,
        enable: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: int = None,
    ):
        self.group = group
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        # 按客户名称、客户编码模糊查询
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        self.validate_required(self.group, 'group')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['groupid'] = self.group
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupid') is not None:
            self.group = m.get('groupid')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class StockSpaceListRequest(TeaModel):
    def __init__(
        self,
        body: StockSpaceListRequestBody = None,
    ):
        self.body = body
        # 仓位列表

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
            temp_model = StockSpaceListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StockGroupSave(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        parent_id: str = None,
        remark: str = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        # parent_id
        self.parent_id = parent_id
        self.remark = remark

    def validate(self):
        self.validate_required(self.parent_id, 'parent_id')

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
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class StockGroupSaveRequest(TeaModel):
    def __init__(
        self,
        body: StockGroupSave = None,
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
            temp_model = StockGroupSave()
            self.body = temp_model.from_map(m['body'])
        return self


class MeasureUnitListRequestBody(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: str = None,
    ):
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class MeasureUnitListRequest(TeaModel):
    def __init__(
        self,
        body: MeasureUnitListRequestBody = None,
    ):
        self.body = body
        # 计量单位列表

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
            temp_model = MeasureUnitListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MeasureUnitDetailRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class MeasureUnitDetailRequest(TeaModel):
    def __init__(
        self,
        body: MeasureUnitDetailRequestBody = None,
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
            temp_model = MeasureUnitDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LanguageString(TeaModel):
    def __init__(
        self,
        tw: str = None,
        cn: str = None,
    ):
        self.tw = tw
        self.cn = cn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tw is not None:
            result['zh_TW'] = self.tw
        if self.cn is not None:
            result['zh_CN'] = self.cn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('zh_TW') is not None:
            self.tw = m.get('zh_TW')
        if m.get('zh_CN') is not None:
            self.cn = m.get('zh_CN')
        return self


class MeasureUnitDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: LanguageString = None,
        precision: str = None,
    ):
        self.id = id
        self.name = name
        # 数量小数位
        self.precision = precision

    def validate(self):
        if self.name:
            self.name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name.to_map()
        if self.precision is not None:
            result['precision'] = self.precision
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            temp_model = LanguageString()
            self.name = temp_model.from_map(m['name'])
        if m.get('precision') is not None:
            self.precision = m.get('precision')
        return self


class MeasureUnitDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: MeasureUnitDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = MeasureUnitDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class MeasureUnitSaveRequest(TeaModel):
    def __init__(
        self,
        body: MeasureUnitDetail = None,
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
            temp_model = MeasureUnitDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class MaterialMeasureUnitListRequestBody(TeaModel):
    def __init__(
        self,
        material_id: List[str] = None,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: int = None,
    ):
        # 商品ID
        self.material_id = material_id
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_id is not None:
            result['materialid'] = self.material_id
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('materialid') is not None:
            self.material_id = m.get('materialid')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class MaterialMeasureUnitListRequest(TeaModel):
    def __init__(
        self,
        body: MaterialMeasureUnitListRequestBody = None,
    ):
        self.body = body
        # 商品单位列表

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
            temp_model = MaterialMeasureUnitListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MaterialMeasureUnitDetailRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class MaterialMeasureUnitDetailRequest(TeaModel):
    def __init__(
        self,
        body: MaterialMeasureUnitDetailRequestBody = None,
    ):
        self.body = body
        # 商品单位详情

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
            temp_model = MaterialMeasureUnitDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CurrencyListRequestBody(TeaModel):
    def __init__(
        self,
        enable: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: int = None,
    ):
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class CurrencyListRequest(TeaModel):
    def __init__(
        self,
        body: CurrencyListRequestBody = None,
    ):
        self.body = body
        # 币别列表

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
            temp_model = CurrencyListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CurrencyDetailRequestBody(TeaModel):
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


class CurrencyDetailRequest(TeaModel):
    def __init__(
        self,
        body: CurrencyDetailRequestBody = None,
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
            temp_model = CurrencyDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CurrencyDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        price_precision: str = None,
        amt_precision: str = None,
        description: str = None,
        sign: str = None,
        exc_type: str = None,
        rate: str = None,
        convert_mode: str = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        # 单价小数位
        self.price_precision = price_precision
        # 金额小数位
        self.amt_precision = amt_precision
        self.description = description
        self.sign = sign
        # 汇率类型:1-固定汇率，2-浮动汇率
        self.exc_type = exc_type
        self.rate = rate
        # 折算方式，1原币//汇率=本位币，2原币/汇率=本位币
        self.convert_mode = convert_mode

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
        if self.name is not None:
            result['name'] = self.name
        if self.price_precision is not None:
            result['priceprecision'] = self.price_precision
        if self.amt_precision is not None:
            result['amtprecision'] = self.amt_precision
        if self.description is not None:
            result['description'] = self.description
        if self.sign is not None:
            result['sign'] = self.sign
        if self.exc_type is not None:
            result['exctype'] = self.exc_type
        if self.rate is not None:
            result['rate'] = self.rate
        if self.convert_mode is not None:
            result['convertmode'] = self.convert_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('priceprecision') is not None:
            self.price_precision = m.get('priceprecision')
        if m.get('amtprecision') is not None:
            self.amt_precision = m.get('amtprecision')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('sign') is not None:
            self.sign = m.get('sign')
        if m.get('exctype') is not None:
            self.exc_type = m.get('exctype')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('convertmode') is not None:
            self.convert_mode = m.get('convertmode')
        return self


class CurrencyDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: CurrencyDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = CurrencyDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class CurrencySaveRequest(TeaModel):
    def __init__(
        self,
        body: CurrencyDetail = None,
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
            temp_model = CurrencyDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class AttributeGroupListRequestBody(TeaModel):
    def __init__(
        self,
        search: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: int = None,
    ):
        self.search = search
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class AttributeGroupListRequest(TeaModel):
    def __init__(
        self,
        body: AttributeGroupListRequestBody = None,
    ):
        self.body = body
        # 查询辅助属性分类列表

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
            temp_model = AttributeGroupListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttributeGroupSaveRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        number: str = None,
        parent_id: str = None,
    ):
        self.id = id
        self.name = name
        self.number = number
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        return self


class AttributeGroupSaveRequest(TeaModel):
    def __init__(
        self,
        body: AttributeGroupSaveRequestBody = None,
    ):
        self.body = body
        # 保存辅助属性分类

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
            temp_model = AttributeGroupSaveRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttributeListRequestBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: str = None,
        enable: str = None,
        search: str = None,
        group: List[str] = None,
        page: int = None,
        pagesize: int = None,
        unpage: int = None,
    ):
        self.name = name
        self.number = number
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        # 模糊搜索-名称
        self.search = search
        # groupid
        self.group = group
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.group is not None:
            result['group'] = self.group
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class AttributeListRequest(TeaModel):
    def __init__(
        self,
        body: AttributeListRequestBody = None,
    ):
        self.body = body
        # 查询辅助属性列表

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
            temp_model = AttributeListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttributeDetailRequestBody(TeaModel):
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


class AttributeDetailRequest(TeaModel):
    def __init__(
        self,
        body: AttributeDetailRequestBody = None,
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
            temp_model = AttributeDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttributeDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: LanguageString = None,
        group_id: str = None,
        parent_id: str = None,
        description: LanguageString = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        self.group_id = group_id
        self.parent_id = parent_id
        self.description = description

    def validate(self):
        if self.name:
            self.name.validate()
        if self.description:
            self.description.validate()

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
            result['name'] = self.name.to_map()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        if self.description is not None:
            result['description'] = self.description.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            temp_model = LanguageString()
            self.name = temp_model.from_map(m['name'])
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        if m.get('description') is not None:
            temp_model = LanguageString()
            self.description = temp_model.from_map(m['description'])
        return self


class AttributeDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: AttributeDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = AttributeDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class AttributeSaveRequest(TeaModel):
    def __init__(
        self,
        body: AttributeDetail = None,
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
            temp_model = AttributeDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class AuxGroupListRequestBody(TeaModel):
    def __init__(
        self,
        search: str = None,
        parent: List[str] = None,
        page: int = None,
        pagesize: int = None,
        unpage: int = None,
    ):
        self.search = search
        # 父级类别id
        self.parent = parent
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.parent is not None:
            result['parent'] = self.parent
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class AuxGroupListRequest(TeaModel):
    def __init__(
        self,
        body: AuxGroupListRequestBody = None,
    ):
        self.body = body
        # 查询辅助资料分类列表

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
            temp_model = AuxGroupListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuxGroupDetailRequestBody(TeaModel):
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


class AuxGroupDetailRequest(TeaModel):
    def __init__(
        self,
        body: AuxGroupDetailRequestBody = None,
    ):
        self.body = body
        # 查询辅助资料分类

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
            temp_model = AuxGroupDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuxGroupSaveRequestBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.id = id
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        return self


class AuxGroupSaveRequest(TeaModel):
    def __init__(
        self,
        body: AuxGroupSaveRequestBody = None,
    ):
        self.body = body
        # 保存辅助资料分类

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
            temp_model = AuxGroupSaveRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuxListRequestBody(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
        name: str = None,
        number: str = None,
        group: List[str] = None,
        search: str = None,
        enable: str = None,
        page: int = None,
        pagesize: int = None,
        unpage: int = None,
    ):
        self.ids = ids
        self.name = name
        self.number = number
        self.group = group
        # 按客户名称、客户编码模糊查询
        self.search = search
        # 状态(1:启用 0:禁用 -1：不限)
        self.enable = enable
        self.page = page
        self.pagesize = pagesize
        self.unpage = unpage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.group is not None:
            result['group'] = self.group
        if self.search is not None:
            result['search'] = self.search
        if self.enable is not None:
            result['enable'] = self.enable
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        if self.unpage is not None:
            result['unpage'] = self.unpage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        if m.get('unpage') is not None:
            self.unpage = m.get('unpage')
        return self


class AuxListRequest(TeaModel):
    def __init__(
        self,
        body: AuxListRequestBody = None,
    ):
        self.body = body
        # 查询辅助资料列表

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
            temp_model = AuxListRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuxDetailRequestBody(TeaModel):
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


class AuxDetailRequest(TeaModel):
    def __init__(
        self,
        body: AuxDetailRequestBody = None,
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
            temp_model = AuxDetailRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuxDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        name: str = None,
        group_id: str = None,
        remark: str = None,
    ):
        self.id = id
        self.number = number
        self.name = name
        self.group_id = group_id
        self.remark = remark

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
        if self.name is not None:
            result['name'] = self.name
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class AuxDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: AuxDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = AuxDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class AuxSaveRequest(TeaModel):
    def __init__(
        self,
        body: AuxDetail = None,
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
            temp_model = AuxDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class BrandListRequest(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        parent: List[str] = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.enable = enable
        self.search = search
        # 上级品牌ID
        self.parent = parent
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.parent is not None:
            result['parent'] = self.parent
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class BrandSaveRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
        number: str = None,
        parent_id: int = None,
        description: str = None,
    ):
        self.name = name
        self.id = id
        # 商品品牌编码,不传递则由后台生成（不设置有编码规则和更新时必传）
        self.number = number
        self.parent_id = parent_id
        self.description = description

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class MaterialGroupListRequest(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        parent: List[str] = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.enable = enable
        self.search = search
        # 上级品牌ID
        self.parent = parent
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.parent is not None:
            result['parent'] = self.parent
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class MaterialGroupSaveRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
        number: str = None,
        parent_id: int = None,
        parent_number: int = None,
        description: str = None,
    ):
        self.name = name
        self.id = id
        # 商品类别编码,不传递则由后台生成（不设置有编码规则和更新时必传）
        self.number = number
        self.parent_id = parent_id
        self.parent_number = parent_number
        self.description = description

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        if self.parent_number is not None:
            result['parent_number'] = self.parent_number
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        if m.get('parent_number') is not None:
            self.parent_number = m.get('parent_number')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class LabelListRequest(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        parent: List[str] = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.enable = enable
        self.search = search
        # 上级ID
        self.parent = parent
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.parent is not None:
            result['parent'] = self.parent
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class LabelSaveRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
        number: str = None,
        parent_id: int = None,
        description: str = None,
    ):
        self.name = name
        self.id = id
        # 商品标签编码,不传递则由后台生成（不设置有编码规则和更新时必传）
        self.number = number
        self.parent_id = parent_id
        self.description = description

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class MaterialListRequest(TeaModel):
    def __init__(
        self,
        enable: str = None,
        search: str = None,
        parent: List[str] = None,
        is_data_perm: str = None,
        startdate: str = None,
        enddate: str = None,
        begindate: str = None,
        expiredate: str = None,
        starttime: int = None,
        endtime: int = None,
        begintime: int = None,
        expiretime: int = None,
        showunits: bool = None,
        showimages: bool = None,
        selectfields: str = None,
        page: int = None,
        pagesize: int = None,
    ):
        self.enable = enable
        self.search = search
        # 商品类别ID
        self.parent = parent
        # 是否添加数据权限校验，默认false
        self.is_data_perm = is_data_perm
        self.startdate = startdate
        self.enddate = enddate
        self.begindate = begindate
        self.expiredate = expiredate
        self.starttime = starttime
        self.endtime = endtime
        self.begintime = begintime
        self.expiretime = expiretime
        # 是否返回多单位信息，true：返回，默认false
        self.showunits = showunits
        # 是否返回图片信息，true：返回，默认false
        self.showimages = showimages
        # 自定义返回字段（除默认字段外），多个字段用英文逗号隔开,具体看商品元数据的标识
        self.selectfields = selectfields
        self.page = page
        self.pagesize = pagesize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.search is not None:
            result['search'] = self.search
        if self.parent is not None:
            result['parent'] = self.parent
        if self.is_data_perm is not None:
            result['isdataperm'] = self.is_data_perm
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
        if self.showunits is not None:
            result['showunits'] = self.showunits
        if self.showimages is not None:
            result['showimages'] = self.showimages
        if self.selectfields is not None:
            result['selectfields'] = self.selectfields
        if self.page is not None:
            result['page'] = self.page
        if self.pagesize is not None:
            result['pagesize'] = self.pagesize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('parent') is not None:
            self.parent = m.get('parent')
        if m.get('isdataperm') is not None:
            self.is_data_perm = m.get('isdataperm')
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
        if m.get('showunits') is not None:
            self.showunits = m.get('showunits')
        if m.get('showimages') is not None:
            self.showimages = m.get('showimages')
        if m.get('selectfields') is not None:
            self.selectfields = m.get('selectfields')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pagesize') is not None:
            self.pagesize = m.get('pagesize')
        return self


class MaterialDetailRequest(TeaModel):
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


class MaterialMulLabel(TeaModel):
    def __init__(
        self,
        number: str = None,
    ):
        self.number = number
        # 商品保存

    def validate(self):
        self.validate_required(self.number, 'number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class MaterialAuxEntity(TeaModel):
    def __init__(
        self,
        sku_id: str = None,
        sku_number: str = None,
        picture_url: str = None,
        mulpictureurl: str = None,
        aux_1id: str = None,
        aux_1number: str = None,
        aux_1type_id: str = None,
        aux_1type_number: str = None,
        aux_2id: str = None,
        aux_2number: str = None,
        aux_21type_id: str = None,
        aux_2type_number: str = None,
        aux_3id: str = None,
        aux_3number: str = None,
        aux_3type_id: str = None,
        aux_3type_number: str = None,
        aux_4id: str = None,
        aux_4number: str = None,
        aux_4type_id: str = None,
        aux_4type_number: str = None,
        aux_5id: str = None,
        aux_5number: str = None,
        aux_5type_id: str = None,
        aux_5type_number: str = None,
        aux_combin_name: str = None,
        concat_type_id: str = None,
    ):
        # 辅助属性id,传递则更新
        self.sku_id = sku_id
        # SKU编码
        self.sku_number = sku_number
        # 辅助属性主图
        self.picture_url = picture_url
        # 辅助属性图片集合(包含url属性的json对象集合的字符串)
        self.mulpictureurl = mulpictureurl
        # 辅助属性1id
        self.aux_1id = aux_1id
        # 辅助属性1编码
        self.aux_1number = aux_1number
        # 辅助属性类型1 id
        self.aux_1type_id = aux_1type_id
        # 辅助属性类型1编码
        self.aux_1type_number = aux_1type_number
        # 辅助属性2id
        self.aux_2id = aux_2id
        # 辅助属性2编码
        self.aux_2number = aux_2number
        # 辅助属性类型2 id
        self.aux_21type_id = aux_21type_id
        # 辅助属性类型2编码
        self.aux_2type_number = aux_2type_number
        # 辅助属性3id
        self.aux_3id = aux_3id
        # 辅助属性3编码
        self.aux_3number = aux_3number
        # 辅助属性类型3 id
        self.aux_3type_id = aux_3type_id
        # 辅助属性类型3编码
        self.aux_3type_number = aux_3type_number
        # 辅助属性4id
        self.aux_4id = aux_4id
        # 辅助属性4编码
        self.aux_4number = aux_4number
        # 辅助属性类型4 id
        self.aux_4type_id = aux_4type_id
        # 辅助属性类型4编码
        self.aux_4type_number = aux_4type_number
        # 辅助属性5id
        self.aux_5id = aux_5id
        # 辅助属性5编码
        self.aux_5number = aux_5number
        # 辅助属性类型5 id
        self.aux_5type_id = aux_5type_id
        # 辅助属性类型5编码
        self.aux_5type_number = aux_5type_number
        # 辅助属性名称连接,使用/分隔每个属性
        self.aux_combin_name = aux_combin_name
        # 多个辅助属性id连接串,使用英文逗号隔开
        self.concat_type_id = concat_type_id

    def validate(self):
        self.validate_required(self.aux_1id, 'aux_1id')
        self.validate_required(self.aux_1number, 'aux_1number')
        self.validate_required(self.aux_1type_id, 'aux_1type_id')
        self.validate_required(self.aux_1type_number, 'aux_1type_number')
        self.validate_required(self.aux_2id, 'aux_2id')
        self.validate_required(self.aux_2number, 'aux_2number')
        self.validate_required(self.aux_21type_id, 'aux_21type_id')
        self.validate_required(self.aux_2type_number, 'aux_2type_number')
        self.validate_required(self.aux_3id, 'aux_3id')
        self.validate_required(self.aux_3number, 'aux_3number')
        self.validate_required(self.aux_3type_id, 'aux_3type_id')
        self.validate_required(self.aux_3type_number, 'aux_3type_number')
        self.validate_required(self.aux_4id, 'aux_4id')
        self.validate_required(self.aux_4number, 'aux_4number')
        self.validate_required(self.aux_4type_id, 'aux_4type_id')
        self.validate_required(self.aux_4type_number, 'aux_4type_number')
        self.validate_required(self.aux_5id, 'aux_5id')
        self.validate_required(self.aux_5number, 'aux_5number')
        self.validate_required(self.aux_5type_id, 'aux_5type_id')
        self.validate_required(self.aux_5type_number, 'aux_5type_number')
        self.validate_required(self.aux_combin_name, 'aux_combin_name')
        self.validate_required(self.concat_type_id, 'concat_type_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['skuid'] = self.sku_id
        if self.sku_number is not None:
            result['skunumber'] = self.sku_number
        if self.picture_url is not None:
            result['pictureurl'] = self.picture_url
        if self.mulpictureurl is not None:
            result['mulpictureurl'] = self.mulpictureurl
        if self.aux_1id is not None:
            result['auxid1_id'] = self.aux_1id
        if self.aux_1number is not None:
            result['auxid1_number'] = self.aux_1number
        if self.aux_1type_id is not None:
            result['auxtypeid1_id'] = self.aux_1type_id
        if self.aux_1type_number is not None:
            result['auxtypeid1_number'] = self.aux_1type_number
        if self.aux_2id is not None:
            result['auxid2_id'] = self.aux_2id
        if self.aux_2number is not None:
            result['auxid2_number'] = self.aux_2number
        if self.aux_21type_id is not None:
            result['auxtypeid2_id'] = self.aux_21type_id
        if self.aux_2type_number is not None:
            result['auxtypeid2_number'] = self.aux_2type_number
        if self.aux_3id is not None:
            result['auxid3_id'] = self.aux_3id
        if self.aux_3number is not None:
            result['auxid3_number'] = self.aux_3number
        if self.aux_3type_id is not None:
            result['auxtypeid3_id'] = self.aux_3type_id
        if self.aux_3type_number is not None:
            result['auxtypeid3_number'] = self.aux_3type_number
        if self.aux_4id is not None:
            result['auxid4_id'] = self.aux_4id
        if self.aux_4number is not None:
            result['auxid4_number'] = self.aux_4number
        if self.aux_4type_id is not None:
            result['auxtypeid4_id'] = self.aux_4type_id
        if self.aux_4type_number is not None:
            result['auxtypeid4_number'] = self.aux_4type_number
        if self.aux_5id is not None:
            result['auxid5_id'] = self.aux_5id
        if self.aux_5number is not None:
            result['auxid5_number'] = self.aux_5number
        if self.aux_5type_id is not None:
            result['auxtypeid5_id'] = self.aux_5type_id
        if self.aux_5type_number is not None:
            result['auxtypeid5_number'] = self.aux_5type_number
        if self.aux_combin_name is not None:
            result['auxcombinationname'] = self.aux_combin_name
        if self.concat_type_id is not None:
            result['concattypeid'] = self.concat_type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skuid') is not None:
            self.sku_id = m.get('skuid')
        if m.get('skunumber') is not None:
            self.sku_number = m.get('skunumber')
        if m.get('pictureurl') is not None:
            self.picture_url = m.get('pictureurl')
        if m.get('mulpictureurl') is not None:
            self.mulpictureurl = m.get('mulpictureurl')
        if m.get('auxid1_id') is not None:
            self.aux_1id = m.get('auxid1_id')
        if m.get('auxid1_number') is not None:
            self.aux_1number = m.get('auxid1_number')
        if m.get('auxtypeid1_id') is not None:
            self.aux_1type_id = m.get('auxtypeid1_id')
        if m.get('auxtypeid1_number') is not None:
            self.aux_1type_number = m.get('auxtypeid1_number')
        if m.get('auxid2_id') is not None:
            self.aux_2id = m.get('auxid2_id')
        if m.get('auxid2_number') is not None:
            self.aux_2number = m.get('auxid2_number')
        if m.get('auxtypeid2_id') is not None:
            self.aux_21type_id = m.get('auxtypeid2_id')
        if m.get('auxtypeid2_number') is not None:
            self.aux_2type_number = m.get('auxtypeid2_number')
        if m.get('auxid3_id') is not None:
            self.aux_3id = m.get('auxid3_id')
        if m.get('auxid3_number') is not None:
            self.aux_3number = m.get('auxid3_number')
        if m.get('auxtypeid3_id') is not None:
            self.aux_3type_id = m.get('auxtypeid3_id')
        if m.get('auxtypeid3_number') is not None:
            self.aux_3type_number = m.get('auxtypeid3_number')
        if m.get('auxid4_id') is not None:
            self.aux_4id = m.get('auxid4_id')
        if m.get('auxid4_number') is not None:
            self.aux_4number = m.get('auxid4_number')
        if m.get('auxtypeid4_id') is not None:
            self.aux_4type_id = m.get('auxtypeid4_id')
        if m.get('auxtypeid4_number') is not None:
            self.aux_4type_number = m.get('auxtypeid4_number')
        if m.get('auxid5_id') is not None:
            self.aux_5id = m.get('auxid5_id')
        if m.get('auxid5_number') is not None:
            self.aux_5number = m.get('auxid5_number')
        if m.get('auxtypeid5_id') is not None:
            self.aux_5type_id = m.get('auxtypeid5_id')
        if m.get('auxtypeid5_number') is not None:
            self.aux_5type_number = m.get('auxtypeid5_number')
        if m.get('auxcombinationname') is not None:
            self.aux_combin_name = m.get('auxcombinationname')
        if m.get('concattypeid') is not None:
            self.concat_type_id = m.get('concattypeid')
        return self


class MaterialBarCodeEntity(TeaModel):
    def __init__(
        self,
        id: str = None,
        barcode: str = None,
        unit_id: str = None,
    ):
        self.id = id
        # 条形码
        self.barcode = barcode
        # 单位
        self.unit_id = unit_id

    def validate(self):
        self.validate_required(self.barcode, 'barcode')
        self.validate_required(self.unit_id, 'unit_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.barcode is not None:
            result['barcode_barcode'] = self.barcode
        if self.unit_id is not None:
            result['barcode_unitid_id'] = self.unit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('barcode_barcode') is not None:
            self.barcode = m.get('barcode_barcode')
        if m.get('barcode_unitid_id') is not None:
            self.unit_id = m.get('barcode_unitid_id')
        return self


class MaterialPriceEntity(TeaModel):
    def __init__(
        self,
        id: str = None,
        barcode: str = None,
        unit_id: str = None,
        purchase_price: str = None,
        max_purchase_price: str = None,
        cost_price: str = None,
        distribution_price: str = None,
        trade_price: str = None,
        retail_price: str = None,
        min_sales_price: str = None,
        sale_price_1: str = None,
        sale_price_2: str = None,
        sale_price_3: str = None,
        near_sale_price: str = None,
        near_purchase_price: str = None,
        min_purchase_tax_price: str = None,
        min_purchase_cost: str = None,
        near_supplier: str = None,
        near_sale_tax_price: str = None,
        near_purchase_tax_price: str = None,
    ):
        self.id = id
        # 条形码
        self.barcode = barcode
        # 单位
        self.unit_id = unit_id
        # 采购价
        self.purchase_price = purchase_price
        # 最高采购价
        self.max_purchase_price = max_purchase_price
        # 参考成本
        self.cost_price = cost_price
        # 配送价
        self.distribution_price = distribution_price
        # 批发价
        self.trade_price = trade_price
        # 零售价
        self.retail_price = retail_price
        # 最低销售价
        self.min_sales_price = min_sales_price
        # 价格等级1
        self.sale_price_1 = sale_price_1
        # 价格等级2
        self.sale_price_2 = sale_price_2
        # 价格等级3
        self.sale_price_3 = sale_price_3
        # 最近销售单价
        self.near_sale_price = near_sale_price
        # 最近采购单价
        self.near_purchase_price = near_purchase_price
        # 最低含税采购价
        self.min_purchase_tax_price = min_purchase_tax_price
        # 最近采购入库成本
        self.min_purchase_cost = min_purchase_cost
        # 最近成交供应商
        self.near_supplier = near_supplier
        # 最近销售含税单价
        self.near_sale_tax_price = near_sale_tax_price
        # 最近采购含税单价
        self.near_purchase_tax_price = near_purchase_tax_price

    def validate(self):
        self.validate_required(self.barcode, 'barcode')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.purchase_price, 'purchase_price')
        self.validate_required(self.max_purchase_price, 'max_purchase_price')
        self.validate_required(self.cost_price, 'cost_price')
        self.validate_required(self.distribution_price, 'distribution_price')
        self.validate_required(self.trade_price, 'trade_price')
        self.validate_required(self.retail_price, 'retail_price')
        self.validate_required(self.min_sales_price, 'min_sales_price')
        self.validate_required(self.sale_price_1, 'sale_price_1')
        self.validate_required(self.sale_price_2, 'sale_price_2')
        self.validate_required(self.sale_price_3, 'sale_price_3')
        self.validate_required(self.near_sale_price, 'near_sale_price')
        self.validate_required(self.near_purchase_price, 'near_purchase_price')
        self.validate_required(self.min_purchase_tax_price, 'min_purchase_tax_price')
        self.validate_required(self.min_purchase_cost, 'min_purchase_cost')
        self.validate_required(self.near_supplier, 'near_supplier')
        self.validate_required(self.near_sale_tax_price, 'near_sale_tax_price')
        self.validate_required(self.near_purchase_tax_price, 'near_purchase_tax_price')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.barcode is not None:
            result['price_barcode'] = self.barcode
        if self.unit_id is not None:
            result['price_unitid_id'] = self.unit_id
        if self.purchase_price is not None:
            result['price_purchaseprice'] = self.purchase_price
        if self.max_purchase_price is not None:
            result['price_maxpurchaseprice'] = self.max_purchase_price
        if self.cost_price is not None:
            result['price_costprice'] = self.cost_price
        if self.distribution_price is not None:
            result['price_distributionprice'] = self.distribution_price
        if self.trade_price is not None:
            result['price_tradeprice'] = self.trade_price
        if self.retail_price is not None:
            result['price_retailprice'] = self.retail_price
        if self.min_sales_price is not None:
            result['price_minsalesprice'] = self.min_sales_price
        if self.sale_price_1 is not None:
            result['price_saleprice1'] = self.sale_price_1
        if self.sale_price_2 is not None:
            result['price_saleprice2'] = self.sale_price_2
        if self.sale_price_3 is not None:
            result['price_saleprice3'] = self.sale_price_3
        if self.near_sale_price is not None:
            result['price_nearsalprice'] = self.near_sale_price
        if self.near_purchase_price is not None:
            result['price_nearpurprice'] = self.near_purchase_price
        if self.min_purchase_tax_price is not None:
            result['price_minpurtaxprice'] = self.min_purchase_tax_price
        if self.min_purchase_cost is not None:
            result['price_nearpurunitcost'] = self.min_purchase_cost
        if self.near_supplier is not None:
            result['price_nearsupplier'] = self.near_supplier
        if self.near_sale_tax_price is not None:
            result['price_nearsaltaxprice'] = self.near_sale_tax_price
        if self.near_purchase_tax_price is not None:
            result['price_nearpurtaxprice'] = self.near_purchase_tax_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('price_barcode') is not None:
            self.barcode = m.get('price_barcode')
        if m.get('price_unitid_id') is not None:
            self.unit_id = m.get('price_unitid_id')
        if m.get('price_purchaseprice') is not None:
            self.purchase_price = m.get('price_purchaseprice')
        if m.get('price_maxpurchaseprice') is not None:
            self.max_purchase_price = m.get('price_maxpurchaseprice')
        if m.get('price_costprice') is not None:
            self.cost_price = m.get('price_costprice')
        if m.get('price_distributionprice') is not None:
            self.distribution_price = m.get('price_distributionprice')
        if m.get('price_tradeprice') is not None:
            self.trade_price = m.get('price_tradeprice')
        if m.get('price_retailprice') is not None:
            self.retail_price = m.get('price_retailprice')
        if m.get('price_minsalesprice') is not None:
            self.min_sales_price = m.get('price_minsalesprice')
        if m.get('price_saleprice1') is not None:
            self.sale_price_1 = m.get('price_saleprice1')
        if m.get('price_saleprice2') is not None:
            self.sale_price_2 = m.get('price_saleprice2')
        if m.get('price_saleprice3') is not None:
            self.sale_price_3 = m.get('price_saleprice3')
        if m.get('price_nearsalprice') is not None:
            self.near_sale_price = m.get('price_nearsalprice')
        if m.get('price_nearpurprice') is not None:
            self.near_purchase_price = m.get('price_nearpurprice')
        if m.get('price_minpurtaxprice') is not None:
            self.min_purchase_tax_price = m.get('price_minpurtaxprice')
        if m.get('price_nearpurunitcost') is not None:
            self.min_purchase_cost = m.get('price_nearpurunitcost')
        if m.get('price_nearsupplier') is not None:
            self.near_supplier = m.get('price_nearsupplier')
        if m.get('price_nearsaltaxprice') is not None:
            self.near_sale_tax_price = m.get('price_nearsaltaxprice')
        if m.get('price_nearpurtaxprice') is not None:
            self.near_purchase_tax_price = m.get('price_nearpurtaxprice')
        return self


class MaterialDetail(TeaModel):
    def __init__(
        self,
        id: str = None,
        number: str = None,
        check_type: str = None,
        name: str = None,
        base_unit_id: str = None,
        parent_id: str = None,
        parent_number: str = None,
        mul_label: List[MaterialMulLabel] = None,
        bar_code: str = None,
        model: str = None,
        brand_id: str = None,
        brand_number: str = None,
        producingpace: str = None,
        help_code: str = None,
        is_mlti_unit: bool = None,
        fix_unit_1id: str = None,
        coefficient_1: int = None,
        conversion_unit_id_1: str = None,
        fix_unit_2id: str = None,
        coefficient_2: int = None,
        conversion_unit_id_2: str = None,
        fix_unit_3id: str = None,
        coefficient_3: int = None,
        conversion_unit_id_3: str = None,
        purchase_unit_id: str = None,
        sale_unit_id: str = None,
        store_unit_id: str = None,
        aux_unit_id: str = None,
        is_weight: bool = None,
        is_serial: bool = None,
        is_batch: bool = None,
        is_sale: bool = None,
        is_purchase: bool = None,
        is_subpart: bool = None,
        is_assembly: bool = None,
        is_kf_period: bool = None,
        kfperiodtype: str = None,
        kf_period: str = None,
        alarm_day: str = None,
        is_asst_attr: bool = None,
        aux_entity: List[MaterialAuxEntity] = None,
        bar_code_entity: List[MaterialBarCodeEntity] = None,
        price_entity: List[MaterialPriceEntity] = None,
        inventory_manage_type: str = None,
        min_inventory: str = None,
        max_inventory: str = None,
        security_inventory: str = None,
        cost_method: str = None,
        tax_category: str = None,
        tax_rate: str = None,
        stock_id: str = None,
        stock_number: str = None,
        space_id: str = None,
        space_number: str = None,
        vender_id: str = None,
        vender_number: str = None,
        purchase_id: str = None,
        purchase_number: str = None,
        registration_number: str = None,
        pro_license: str = None,
        gross_weight: str = None,
        net_weight: str = None,
        weight_unit: str = None,
        length: str = None,
        wide: str = None,
        high: str = None,
        volume: str = None,
        volume_unit: str = None,
        images: List[str] = None,
        remove_images: List[str] = None,
        ignore_warn: bool = None,
    ):
        self.id = id
        self.number = number
        # 商品类型，普通：1、套装：2、服务：3
        self.check_type = check_type
        self.name = name
        # 计量单位id
        self.base_unit_id = base_unit_id
        # 商品类别id
        self.parent_id = parent_id
        # 商品类别编码
        self.parent_number = parent_number
        # 商品标签
        self.mul_label = mul_label
        # 主条形码
        self.bar_code = bar_code
        self.model = model
        # 品牌id
        self.brand_id = brand_id
        # 品牌编码
        self.brand_number = brand_number
        # 产地
        self.producingpace = producingpace
        # 助记码
        self.help_code = help_code
        # 是否启用多单位,默认false，不启用
        self.is_mlti_unit = is_mlti_unit
        # 辅助单位1id,启动多单位，才需要传递
        self.fix_unit_1id = fix_unit_1id
        # 换算率1
        self.coefficient_1 = coefficient_1
        # 换算单位1
        self.conversion_unit_id_1 = conversion_unit_id_1
        # 辅助单位2id,启动多单位，才需要传递
        self.fix_unit_2id = fix_unit_2id
        # 换算率2
        self.coefficient_2 = coefficient_2
        # 换算单位2
        self.conversion_unit_id_2 = conversion_unit_id_2
        # 辅助单位3id,启动多单位，才需要传递
        self.fix_unit_3id = fix_unit_3id
        # 换算率3
        self.coefficient_3 = coefficient_3
        # 换算单位3
        self.conversion_unit_id_3 = conversion_unit_id_3
        # 采购单位,单单位时传递计量单位id
        self.purchase_unit_id = purchase_unit_id
        # 销售单位,单单位时传递计量单位id
        self.sale_unit_id = sale_unit_id
        # 库存单位,单单位时传递计量单位id
        self.store_unit_id = store_unit_id
        # 报表辅助单位,单单位时传递计量单位id
        self.aux_unit_id = aux_unit_id
        # 是否启用称重,默认false
        self.is_weight = is_weight
        # 是否启用序列号管理,默认false
        self.is_serial = is_serial
        # 是否启用批次管理,默认false
        self.is_batch = is_batch
        # 是否可销售,默认true
        self.is_sale = is_sale
        # 是否可采购,默认true
        self.is_purchase = is_purchase
        # 是否可为子件,默认true
        self.is_subpart = is_subpart
        # 是否可为组件,默认true
        self.is_assembly = is_assembly
        # 是否启用保质期,默认false
        self.is_kf_period = is_kf_period
        # 保质期单位，1：天，2：月，3：年
        self.kfperiodtype = kfperiodtype
        # 保质期
        self.kf_period = kf_period
        # 预警天数
        self.alarm_day = alarm_day
        # 是否启用辅助属性,默认false
        self.is_asst_attr = is_asst_attr
        # 辅助属性
        self.aux_entity = aux_entity
        # 商品条码
        self.bar_code_entity = bar_code_entity
        # 商品价格
        self.price_entity = price_entity
        # 库存管理方式,0：统一库存，1：分仓库存,默认统一库存
        self.inventory_manage_type = inventory_manage_type
        # 最低库存
        self.min_inventory = min_inventory
        # 最高库存
        self.max_inventory = max_inventory
        # 预警库存
        self.security_inventory = security_inventory
        # 成本计算方法,默认为移动平均法,1：移动平均法，2：加权平均法，3：先进先出法
        self.cost_method = cost_method
        # 税收分类编码
        self.tax_category = tax_category
        # 税率
        self.tax_rate = tax_rate
        # 默认仓库id
        self.stock_id = stock_id
        # 默认仓库编码
        self.stock_number = stock_number
        # 默认仓位id
        self.space_id = space_id
        # 默认仓位编码
        self.space_number = space_number
        # 默认供应商id
        self.vender_id = vender_id
        # 默认供应商编码
        self.vender_number = vender_number
        # 采购员id
        self.purchase_id = purchase_id
        # 采购员编码
        self.purchase_number = purchase_number
        # 注册证号
        self.registration_number = registration_number
        # 生产许可证
        self.pro_license = pro_license
        # 毛重
        self.gross_weight = gross_weight
        # 净重
        self.net_weight = net_weight
        # 重量单位
        self.weight_unit = weight_unit
        # 长
        self.length = length
        # 宽
        self.wide = wide
        # 高
        self.high = high
        # 体积
        self.volume = volume
        # 体积单位
        self.volume_unit = volume_unit
        # 商品图片,商品图片服务器连接(上传图片接口的返回值)的集合，多个用英文逗号分隔
        self.images = images
        # 商品图片,商品图片服务器连接(上传图片接口的返回值)的集合，多个用英文逗号分隔
        self.remove_images = remove_images
        # 是否忽略告警信息
        self.ignore_warn = ignore_warn

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.base_unit_id, 'base_unit_id')
        if self.mul_label:
            for k in self.mul_label:
                if k:
                    k.validate()
        self.validate_required(self.purchase_unit_id, 'purchase_unit_id')
        self.validate_required(self.sale_unit_id, 'sale_unit_id')
        self.validate_required(self.store_unit_id, 'store_unit_id')
        self.validate_required(self.aux_unit_id, 'aux_unit_id')
        if self.aux_entity:
            for k in self.aux_entity:
                if k:
                    k.validate()
        if self.bar_code_entity:
            for k in self.bar_code_entity:
                if k:
                    k.validate()
        if self.price_entity:
            for k in self.price_entity:
                if k:
                    k.validate()
        self.validate_required(self.cost_method, 'cost_method')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        if self.check_type is not None:
            result['checktype'] = self.check_type
        if self.name is not None:
            result['name'] = self.name
        if self.base_unit_id is not None:
            result['baseunitid_id'] = self.base_unit_id
        if self.parent_id is not None:
            result['parent_id'] = self.parent_id
        if self.parent_number is not None:
            result['parent_number'] = self.parent_number
        result['mullabel'] = []
        if self.mul_label is not None:
            for k in self.mul_label:
                result['mullabel'].append(k.to_map() if k else None)
        if self.bar_code is not None:
            result['barcode'] = self.bar_code
        if self.model is not None:
            result['model'] = self.model
        if self.brand_id is not None:
            result['brandid_id'] = self.brand_id
        if self.brand_number is not None:
            result['brandid_number'] = self.brand_number
        if self.producingpace is not None:
            result['producingpace'] = self.producingpace
        if self.help_code is not None:
            result['helpcode'] = self.help_code
        if self.is_mlti_unit is not None:
            result['ismulti_unit'] = self.is_mlti_unit
        if self.fix_unit_1id is not None:
            result['fixunit1_id'] = self.fix_unit_1id
        if self.coefficient_1 is not None:
            result['coefficient1'] = self.coefficient_1
        if self.conversion_unit_id_1 is not None:
            result['conversionunitid1_id'] = self.conversion_unit_id_1
        if self.fix_unit_2id is not None:
            result['fixunit2_id'] = self.fix_unit_2id
        if self.coefficient_2 is not None:
            result['coefficient2'] = self.coefficient_2
        if self.conversion_unit_id_2 is not None:
            result['conversionunitid2_id'] = self.conversion_unit_id_2
        if self.fix_unit_3id is not None:
            result['fixunit3_id'] = self.fix_unit_3id
        if self.coefficient_3 is not None:
            result['coefficient3'] = self.coefficient_3
        if self.conversion_unit_id_3 is not None:
            result['conversionunitid3_id'] = self.conversion_unit_id_3
        if self.purchase_unit_id is not None:
            result['purchaseunitid_id'] = self.purchase_unit_id
        if self.sale_unit_id is not None:
            result['saleunitid_id'] = self.sale_unit_id
        if self.store_unit_id is not None:
            result['storeunitid_id'] = self.store_unit_id
        if self.aux_unit_id is not None:
            result['auxunitid_id'] = self.aux_unit_id
        if self.is_weight is not None:
            result['isweight'] = self.is_weight
        if self.is_serial is not None:
            result['isserial'] = self.is_serial
        if self.is_batch is not None:
            result['isbatch'] = self.is_batch
        if self.is_sale is not None:
            result['issale'] = self.is_sale
        if self.is_purchase is not None:
            result['ispurchase'] = self.is_purchase
        if self.is_subpart is not None:
            result['issubpart'] = self.is_subpart
        if self.is_assembly is not None:
            result['isassembly'] = self.is_assembly
        if self.is_kf_period is not None:
            result['iskfperiod'] = self.is_kf_period
        if self.kfperiodtype is not None:
            result['kfperiodtype'] = self.kfperiodtype
        if self.kf_period is not None:
            result['kfperiod'] = self.kf_period
        if self.alarm_day is not None:
            result['alarmday'] = self.alarm_day
        if self.is_asst_attr is not None:
            result['isasstattr'] = self.is_asst_attr
        result['auxentity'] = []
        if self.aux_entity is not None:
            for k in self.aux_entity:
                result['auxentity'].append(k.to_map() if k else None)
        result['barcodeentity'] = []
        if self.bar_code_entity is not None:
            for k in self.bar_code_entity:
                result['barcodeentity'].append(k.to_map() if k else None)
        result['priceentity'] = []
        if self.price_entity is not None:
            for k in self.price_entity:
                result['priceentity'].append(k.to_map() if k else None)
        if self.inventory_manage_type is not None:
            result['inv_mgr_type'] = self.inventory_manage_type
        if self.min_inventory is not None:
            result['mininventoryqty'] = self.min_inventory
        if self.max_inventory is not None:
            result['maxinventoryqty'] = self.max_inventory
        if self.security_inventory is not None:
            result['secinventoryqty'] = self.security_inventory
        if self.cost_method is not None:
            result['costmethod'] = self.cost_method
        if self.tax_category is not None:
            result['fetchcategoryid_id'] = self.tax_category
        if self.tax_rate is not None:
            result['taxrate'] = self.tax_rate
        if self.stock_id is not None:
            result['stockid_id'] = self.stock_id
        if self.stock_number is not None:
            result['stockid_number'] = self.stock_number
        if self.space_id is not None:
            result['spaceid_id'] = self.space_id
        if self.space_number is not None:
            result['spaceid_number'] = self.space_number
        if self.vender_id is not None:
            result['venderid_id'] = self.vender_id
        if self.vender_number is not None:
            result['venderid_number'] = self.vender_number
        if self.purchase_id is not None:
            result['purchaseid_id'] = self.purchase_id
        if self.purchase_number is not None:
            result['purchaseid_number'] = self.purchase_number
        if self.registration_number is not None:
            result['refistrationnumber'] = self.registration_number
        if self.pro_license is not None:
            result['prolicense'] = self.pro_license
        if self.gross_weight is not None:
            result['gross_weight'] = self.gross_weight
        if self.net_weight is not None:
            result['net_weight'] = self.net_weight
        if self.weight_unit is not None:
            result['weight_unit_id'] = self.weight_unit
        if self.length is not None:
            result['length'] = self.length
        if self.wide is not None:
            result['wide'] = self.wide
        if self.high is not None:
            result['high'] = self.high
        if self.volume is not None:
            result['volume'] = self.volume
        if self.volume_unit is not None:
            result['volume_unit_id'] = self.volume_unit
        if self.images is not None:
            result['images'] = self.images
        if self.remove_images is not None:
            result['removeimages'] = self.remove_images
        if self.ignore_warn is not None:
            result['ignoreWarn'] = self.ignore_warn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('checktype') is not None:
            self.check_type = m.get('checktype')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('baseunitid_id') is not None:
            self.base_unit_id = m.get('baseunitid_id')
        if m.get('parent_id') is not None:
            self.parent_id = m.get('parent_id')
        if m.get('parent_number') is not None:
            self.parent_number = m.get('parent_number')
        self.mul_label = []
        if m.get('mullabel') is not None:
            for k in m.get('mullabel'):
                temp_model = MaterialMulLabel()
                self.mul_label.append(temp_model.from_map(k))
        if m.get('barcode') is not None:
            self.bar_code = m.get('barcode')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('brandid_id') is not None:
            self.brand_id = m.get('brandid_id')
        if m.get('brandid_number') is not None:
            self.brand_number = m.get('brandid_number')
        if m.get('producingpace') is not None:
            self.producingpace = m.get('producingpace')
        if m.get('helpcode') is not None:
            self.help_code = m.get('helpcode')
        if m.get('ismulti_unit') is not None:
            self.is_mlti_unit = m.get('ismulti_unit')
        if m.get('fixunit1_id') is not None:
            self.fix_unit_1id = m.get('fixunit1_id')
        if m.get('coefficient1') is not None:
            self.coefficient_1 = m.get('coefficient1')
        if m.get('conversionunitid1_id') is not None:
            self.conversion_unit_id_1 = m.get('conversionunitid1_id')
        if m.get('fixunit2_id') is not None:
            self.fix_unit_2id = m.get('fixunit2_id')
        if m.get('coefficient2') is not None:
            self.coefficient_2 = m.get('coefficient2')
        if m.get('conversionunitid2_id') is not None:
            self.conversion_unit_id_2 = m.get('conversionunitid2_id')
        if m.get('fixunit3_id') is not None:
            self.fix_unit_3id = m.get('fixunit3_id')
        if m.get('coefficient3') is not None:
            self.coefficient_3 = m.get('coefficient3')
        if m.get('conversionunitid3_id') is not None:
            self.conversion_unit_id_3 = m.get('conversionunitid3_id')
        if m.get('purchaseunitid_id') is not None:
            self.purchase_unit_id = m.get('purchaseunitid_id')
        if m.get('saleunitid_id') is not None:
            self.sale_unit_id = m.get('saleunitid_id')
        if m.get('storeunitid_id') is not None:
            self.store_unit_id = m.get('storeunitid_id')
        if m.get('auxunitid_id') is not None:
            self.aux_unit_id = m.get('auxunitid_id')
        if m.get('isweight') is not None:
            self.is_weight = m.get('isweight')
        if m.get('isserial') is not None:
            self.is_serial = m.get('isserial')
        if m.get('isbatch') is not None:
            self.is_batch = m.get('isbatch')
        if m.get('issale') is not None:
            self.is_sale = m.get('issale')
        if m.get('ispurchase') is not None:
            self.is_purchase = m.get('ispurchase')
        if m.get('issubpart') is not None:
            self.is_subpart = m.get('issubpart')
        if m.get('isassembly') is not None:
            self.is_assembly = m.get('isassembly')
        if m.get('iskfperiod') is not None:
            self.is_kf_period = m.get('iskfperiod')
        if m.get('kfperiodtype') is not None:
            self.kfperiodtype = m.get('kfperiodtype')
        if m.get('kfperiod') is not None:
            self.kf_period = m.get('kfperiod')
        if m.get('alarmday') is not None:
            self.alarm_day = m.get('alarmday')
        if m.get('isasstattr') is not None:
            self.is_asst_attr = m.get('isasstattr')
        self.aux_entity = []
        if m.get('auxentity') is not None:
            for k in m.get('auxentity'):
                temp_model = MaterialAuxEntity()
                self.aux_entity.append(temp_model.from_map(k))
        self.bar_code_entity = []
        if m.get('barcodeentity') is not None:
            for k in m.get('barcodeentity'):
                temp_model = MaterialBarCodeEntity()
                self.bar_code_entity.append(temp_model.from_map(k))
        self.price_entity = []
        if m.get('priceentity') is not None:
            for k in m.get('priceentity'):
                temp_model = MaterialPriceEntity()
                self.price_entity.append(temp_model.from_map(k))
        if m.get('inv_mgr_type') is not None:
            self.inventory_manage_type = m.get('inv_mgr_type')
        if m.get('mininventoryqty') is not None:
            self.min_inventory = m.get('mininventoryqty')
        if m.get('maxinventoryqty') is not None:
            self.max_inventory = m.get('maxinventoryqty')
        if m.get('secinventoryqty') is not None:
            self.security_inventory = m.get('secinventoryqty')
        if m.get('costmethod') is not None:
            self.cost_method = m.get('costmethod')
        if m.get('fetchcategoryid_id') is not None:
            self.tax_category = m.get('fetchcategoryid_id')
        if m.get('taxrate') is not None:
            self.tax_rate = m.get('taxrate')
        if m.get('stockid_id') is not None:
            self.stock_id = m.get('stockid_id')
        if m.get('stockid_number') is not None:
            self.stock_number = m.get('stockid_number')
        if m.get('spaceid_id') is not None:
            self.space_id = m.get('spaceid_id')
        if m.get('spaceid_number') is not None:
            self.space_number = m.get('spaceid_number')
        if m.get('venderid_id') is not None:
            self.vender_id = m.get('venderid_id')
        if m.get('venderid_number') is not None:
            self.vender_number = m.get('venderid_number')
        if m.get('purchaseid_id') is not None:
            self.purchase_id = m.get('purchaseid_id')
        if m.get('purchaseid_number') is not None:
            self.purchase_number = m.get('purchaseid_number')
        if m.get('refistrationnumber') is not None:
            self.registration_number = m.get('refistrationnumber')
        if m.get('prolicense') is not None:
            self.pro_license = m.get('prolicense')
        if m.get('gross_weight') is not None:
            self.gross_weight = m.get('gross_weight')
        if m.get('net_weight') is not None:
            self.net_weight = m.get('net_weight')
        if m.get('weight_unit_id') is not None:
            self.weight_unit = m.get('weight_unit_id')
        if m.get('length') is not None:
            self.length = m.get('length')
        if m.get('wide') is not None:
            self.wide = m.get('wide')
        if m.get('high') is not None:
            self.high = m.get('high')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        if m.get('volume_unit_id') is not None:
            self.volume_unit = m.get('volume_unit_id')
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('removeimages') is not None:
            self.remove_images = m.get('removeimages')
        if m.get('ignoreWarn') is not None:
            self.ignore_warn = m.get('ignoreWarn')
        return self


class MaterialDetailResponse(TeaModel):
    def __init__(
        self,
        success: bool = None,
        message: str = None,
        data: MaterialDetail = None,
        error_code: str = None,
    ):
        self.success = success
        self.message = message
        self.data = data
        self.error_code = error_code

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.error_code, 'error_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = MaterialDetail()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class MaterialSaveRequest(TeaModel):
    def __init__(
        self,
        body: MaterialDetail = None,
    ):
        self.body = body
        # 商品价格

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
            temp_model = MaterialDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageUploadRequest(TeaModel):
    def __init__(
        self,
        savetemp: str = None,
        filename: str = None,
        basestring: str = None,
    ):
        # 是否上传到临时服务器，默认为true
        self.savetemp = savetemp
        self.filename = filename
        # base64字符串，包含头部data信息
        self.basestring = basestring

    def validate(self):
        self.validate_required(self.filename, 'filename')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.savetemp is not None:
            result['savetemp'] = self.savetemp
        if self.filename is not None:
            result['filename'] = self.filename
        if self.basestring is not None:
            result['basestring'] = self.basestring
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('savetemp') is not None:
            self.savetemp = m.get('savetemp')
        if m.get('filename') is not None:
            self.filename = m.get('filename')
        if m.get('basestring') is not None:
            self.basestring = m.get('basestring')
        return self


class ImageDeleteRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url
        # 商品图片删除

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CustomerMaterialPriceRequest(TeaModel):
    def __init__(
        self,
        material_id: str = None,
        unit_id: List[str] = None,
        bill_type_id: str = None,
        bill_date: str = None,
        aux_prop_id: List[str] = None,
        qty: List[str] = None,
        customer_id: str = None,
        supplier_id: str = None,
    ):
        # 商品ID
        self.material_id = material_id
        # 单位ID，格式：[“”,””,””]
        self.unit_id = unit_id
        # 单据类型
        self.bill_type_id = bill_type_id
        # 单据日期，格式：2019-0-01
        self.bill_date = bill_date
        # 商品辅助属性ID，格式：[“”,””,””]
        self.aux_prop_id = aux_prop_id
        # 商品辅助属性ID，格式：[“”,””,””]
        self.qty = qty
        # 客户ID（销售类单据必填）
        self.customer_id = customer_id
        # 供应商ID（采购类单据必填）
        self.supplier_id = supplier_id

    def validate(self):
        self.validate_required(self.material_id, 'material_id')
        self.validate_required(self.unit_id, 'unit_id')
        self.validate_required(self.bill_type_id, 'bill_type_id')
        self.validate_required(self.bill_date, 'bill_date')
        self.validate_required(self.aux_prop_id, 'aux_prop_id')
        self.validate_required(self.qty, 'qty')
        self.validate_required(self.customer_id, 'customer_id')
        self.validate_required(self.supplier_id, 'supplier_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_id is not None:
            result['materialid'] = self.material_id
        if self.unit_id is not None:
            result['unitid'] = self.unit_id
        if self.bill_type_id is not None:
            result['billtypeid'] = self.bill_type_id
        if self.bill_date is not None:
            result['billdate'] = self.bill_date
        if self.aux_prop_id is not None:
            result['auxpropid'] = self.aux_prop_id
        if self.qty is not None:
            result['qty'] = self.qty
        if self.customer_id is not None:
            result['customerid'] = self.customer_id
        if self.supplier_id is not None:
            result['supplierid'] = self.supplier_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('materialid') is not None:
            self.material_id = m.get('materialid')
        if m.get('unitid') is not None:
            self.unit_id = m.get('unitid')
        if m.get('billtypeid') is not None:
            self.bill_type_id = m.get('billtypeid')
        if m.get('billdate') is not None:
            self.bill_date = m.get('billdate')
        if m.get('auxpropid') is not None:
            self.aux_prop_id = m.get('auxpropid')
        if m.get('qty') is not None:
            self.qty = m.get('qty')
        if m.get('customerid') is not None:
            self.customer_id = m.get('customerid')
        if m.get('supplierid') is not None:
            self.supplier_id = m.get('supplierid')
        return self


class BatchMaterial(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 类别id
        self.id = id

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class MaterialDetailBatchRequest(TeaModel):
    def __init__(
        self,
        items: List[BatchMaterial] = None,
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
                temp_model = BatchMaterial()
                self.items.append(temp_model.from_map(k))
        return self


class MaterialBatchSaveRequest(TeaModel):
    def __init__(
        self,
        items: List[MaterialDetail] = None,
    ):
        self.items = items
        # 商品批量保存

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
                temp_model = MaterialDetail()
                self.items.append(temp_model.from_map(k))
        return self


