# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from kingdeejdy_kernel.kingdeejdy_kernel.kingdeejdy_kernel import KingdeejdyKernel

from business.fi.kingdeejdy_fi import models as kingdeejdy_fi_models


class KingdeejdyFi:
    _kernel: KingdeejdyKernel = None

    def __init__(
        self, 
        kernel: KingdeejdyKernel,
    ):
        self._kernel = kernel

    def get_account_list(
        self,
        request: kingdeejdy_fi_models.AccountListRequest,
    ) -> dict:
        """
        获取财务基础资料 科目列表（所有科目） 信息
        """
        return self._kernel.post('/jdy/gl/account_list', request.body)

    async def get_account_list_async(
        self,
        request: kingdeejdy_fi_models.AccountListRequest,
    ) -> dict:
        """
        获取财务基础资料 科目列表（所有科目） 信息
        """
        return await self._kernel.post_async('/jdy/gl/account_list', request.body)

    def get_account_type_list(
        self,
        request: kingdeejdy_fi_models.AccountTypeListRequest,
    ) -> dict:
        """
        科目类别列表
        """
        return self._kernel.post('/jdy/gl/account_type_list', request.body)

    async def get_account_type_list_async(
        self,
        request: kingdeejdy_fi_models.AccountTypeListRequest,
    ) -> dict:
        """
        科目类别列表
        """
        return await self._kernel.post_async('/jdy/gl/account_type_list', request.body)

    def get_suject_detail(
        self,
        request: kingdeejdy_fi_models.SujectDetailRequest,
    ) -> dict:
        """
        科目详情接口批量查询
        """
        return self._kernel.post('/jdy/gl/account_detail', request.body)

    async def get_suject_detail_async(
        self,
        request: kingdeejdy_fi_models.SujectDetailRequest,
    ) -> dict:
        """
        科目详情接口批量查询
        """
        return await self._kernel.post_async('/jdy/gl/account_detail', request.body)

    def save_account(
        self,
        request: kingdeejdy_fi_models.AccountSaveRequest,
    ) -> dict:
        """
        保存科目(支持批量)
        """
        return self._kernel.post('/jdy/gl/account_save', request.body)

    async def save_account_async(
        self,
        request: kingdeejdy_fi_models.AccountSaveRequest,
    ) -> dict:
        """
        保存科目(支持批量)
        """
        return await self._kernel.post_async('/jdy/gl/account_save', request.body)

    def get_ca_balance_home_page(
        self,
        request: kingdeejdy_fi_models.CABalanceHomeRequest,
    ) -> dict:
        """
        出纳资金余额首页
        """
        return self._kernel.post('/jdy/ca/ca_balance_home_page', request.body)

    async def get_ca_balance_home_page_async(
        self,
        request: kingdeejdy_fi_models.CABalanceHomeRequest,
    ) -> dict:
        """
        出纳资金余额首页
        """
        return await self._kernel.post_async('/jdy/ca/ca_balance_home_page', request.body)

    def get_ca_account_balance(
        self,
        request: kingdeejdy_fi_models.CAAccountBalanceRequest,
    ) -> dict:
        """
        出纳资金余额
        """
        return self._kernel.post('/jdy/ca/ca_account_balance', request.body)

    async def get_ca_account_balance_async(
        self,
        request: kingdeejdy_fi_models.CAAccountBalanceRequest,
    ) -> dict:
        """
        出纳资金余额
        """
        return await self._kernel.post_async('/jdy/ca/ca_account_balance', request.body)

    def get_balance_trend(
        self,
        request: kingdeejdy_fi_models.CABalanceTrendRequest,
    ) -> dict:
        """
        出纳资金余额
        """
        return self._kernel.post('/jdy/ca/ca_balance_trend', request.body)

    async def get_balance_trend_async(
        self,
        request: kingdeejdy_fi_models.CABalanceTrendRequest,
    ) -> dict:
        """
        出纳资金余额
        """
        return await self._kernel.post_async('/jdy/ca/ca_balance_trend', request.body)

    def get_trend_for_debit_and_credit(
        self,
        request: kingdeejdy_fi_models.DebitAndCreditTrendRequest,
    ) -> dict:
        """
        出纳资金收支趋势接口
        """
        return self._kernel.post('/jdy/ca/ca_debit_and_credit_trend', request.body)

    async def get_trend_for_debit_and_credit_async(
        self,
        request: kingdeejdy_fi_models.DebitAndCreditTrendRequest,
    ) -> dict:
        """
        出纳资金收支趋势接口
        """
        return await self._kernel.post_async('/jdy/ca/ca_debit_and_credit_trend', request.body)

    def get_account_detail(
        self,
        request: kingdeejdy_fi_models.AccountDetailRequest,
    ) -> dict:
        """
        出纳资金流水明细接口
        """
        return self._kernel.post('/jdy/ca/ca_account_details', request.body)

    async def get_account_detail_async(
        self,
        request: kingdeejdy_fi_models.AccountDetailRequest,
    ) -> dict:
        """
        出纳资金流水明细接口
        """
        return await self._kernel.post_async('/jdy/ca/ca_account_details', request.body)

    def get_journal_detail(
        self,
        request: kingdeejdy_fi_models.JournalDetailRequest,
    ) -> dict:
        """
        日记账详情
        """
        return self._kernel.post('/jdy/ca/journal_detail', request.body)

    async def get_journal_detail_async(
        self,
        request: kingdeejdy_fi_models.JournalDetailRequest,
    ) -> dict:
        """
        日记账详情
        """
        return await self._kernel.post_async('/jdy/ca/journal_detail', request.body)

    def get_journal_list(
        self,
        request: kingdeejdy_fi_models.JournalListRequest,
    ) -> dict:
        """
        日记账列表
        """
        return self._kernel.post('/jdy/ca/journal_list', request.body)

    async def get_journal_list_async(
        self,
        request: kingdeejdy_fi_models.JournalListRequest,
    ) -> dict:
        """
        日记账列表
        """
        return await self._kernel.post_async('/jdy/ca/journal_list', request.body)

    def save_journal(
        self,
        request: kingdeejdy_fi_models.SaveJournalRequest,
    ) -> dict:
        """
        日记账保存
        """
        return self._kernel.post('/jdy/ca/journal_save', request.body)

    async def save_journal_async(
        self,
        request: kingdeejdy_fi_models.SaveJournalRequest,
    ) -> dict:
        """
        日记账保存
        """
        return await self._kernel.post_async('/jdy/ca/journal_save', request.body)

    def get_acct_balance(
        self,
        request: kingdeejdy_fi_models.AcctBalanceRequest,
    ) -> dict:
        """
        科目余额表查询
        """
        return self._kernel.post('/jdy/gl/acctbalance_report', request.body)

    async def get_acct_balance_async(
        self,
        request: kingdeejdy_fi_models.AcctBalanceRequest,
    ) -> dict:
        """
        科目余额表查询
        """
        return await self._kernel.post_async('/jdy/gl/acctbalance_report', request.body)

    def get_sub_ledger(
        self,
        request: kingdeejdy_fi_models.SubLedgerRequest,
    ) -> dict:
        """
        明细账查询
        """
        return self._kernel.post('/jdy/gl/subledger_report', request.body)

    async def get_sub_ledger_async(
        self,
        request: kingdeejdy_fi_models.SubLedgerRequest,
    ) -> dict:
        """
        明细账查询
        """
        return await self._kernel.post_async('/jdy/gl/subledger_report', request.body)

    def get_profitsheet(
        self,
        request: kingdeejdy_fi_models.ProfitSheetRequest,
    ) -> dict:
        """
        利润表
        """
        return self._kernel.post('/jdy/gl/profitsheet', request.body)

    async def get_profitsheet_async(
        self,
        request: kingdeejdy_fi_models.ProfitSheetRequest,
    ) -> dict:
        """
        利润表
        """
        return await self._kernel.post_async('/jdy/gl/profitsheet', request.body)

    def get_qty_sum_report(
        self,
        request: kingdeejdy_fi_models.QtySumReportRequest,
    ) -> dict:
        """
        数量金额总账
        """
        return self._kernel.post('/jdy/gl/qtysum_report', request.body)

    async def get_qty_sum_report_async(
        self,
        request: kingdeejdy_fi_models.QtySumReportRequest,
    ) -> dict:
        """
        数量金额总账
        """
        return await self._kernel.post_async('/jdy/gl/qtysum_report', request.body)

    def get_virtual_bill_type_list(
        self,
        request: kingdeejdy_fi_models.VirtualBillTypeRequest,
    ) -> dict:
        """
        外部单据分类列表
        """
        return self._kernel.post('/jdy/iac/virtual_basetype_list', request.body)

    async def get_virtual_bill_type_list_async(
        self,
        request: kingdeejdy_fi_models.VirtualBillTypeRequest,
    ) -> dict:
        """
        外部单据分类列表
        """
        return await self._kernel.post_async('/jdy/iac/virtual_basetype_list', request.body)

    def save_virtual_bill_type(
        self,
        request: kingdeejdy_fi_models.SaveVirtualBillTypeRequest,
    ) -> dict:
        """
        保存外部单据分类
        """
        return self._kernel.post('/jdy/iac/virtual_basetype_save', request.body)

    async def save_virtual_bill_type_async(
        self,
        request: kingdeejdy_fi_models.SaveVirtualBillTypeRequest,
    ) -> dict:
        """
        保存外部单据分类
        """
        return await self._kernel.post_async('/jdy/iac/virtual_basetype_save', request.body)

    def get_virtual_bill_list(
        self,
        request: kingdeejdy_fi_models.VirtualBillListRequest,
    ) -> dict:
        """
        外部单据列表
        """
        return self._kernel.post('/jdy/iac/virtual_bill_list', request.body)

    async def get_virtual_bill_list_async(
        self,
        request: kingdeejdy_fi_models.VirtualBillListRequest,
    ) -> dict:
        """
        外部单据列表
        """
        return await self._kernel.post_async('/jdy/iac/virtual_bill_list', request.body)

    def get_virtual_bill_detail(
        self,
        request: kingdeejdy_fi_models.VirtualBillDetailRequest,
    ) -> dict:
        """
        外部单据详情
        """
        return self._kernel.post('/jdy/iac/virtual_bill_detail', request.body)

    async def get_virtual_bill_detail_async(
        self,
        request: kingdeejdy_fi_models.VirtualBillDetailRequest,
    ) -> dict:
        """
        外部单据详情
        """
        return await self._kernel.post_async('/jdy/iac/virtual_bill_detail', request.body)

    def save_virtual_bill(
        self,
        request: kingdeejdy_fi_models.SaveVirtualBillRequest,
    ) -> dict:
        """
        保存外部单据(支持批量)
        """
        return self._kernel.post('/jdy/iac/virtual_bill_save', request.body)

    async def save_virtual_bill_async(
        self,
        request: kingdeejdy_fi_models.SaveVirtualBillRequest,
    ) -> dict:
        """
        保存外部单据(支持批量)
        """
        return await self._kernel.post_async('/jdy/iac/virtual_bill_save', request.body)
