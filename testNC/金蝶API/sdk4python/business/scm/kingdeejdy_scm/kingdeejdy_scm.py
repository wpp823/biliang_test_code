# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from kingdeejdy_kernel.kingdeejdy_kernel import KingdeejdyKernel
from Tea.core import TeaCore

from business.scm.kingdeejdy_scm import models as kingdeejdy_scm_models


class KingdeejdyScm:
    _kernel: KingdeejdyKernel = None

    def __init__(
        self, 
        kernel: KingdeejdyKernel,
    ):
        self._kernel = kernel

    def get_payment_list(
        self,
        request: kingdeejdy_scm_models.PaymentListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        付款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_credit_list', request.body)
        )

    async def get_payment_list_async(
        self,
        request: kingdeejdy_scm_models.PaymentListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        付款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_credit_list', request.body)
        )

    def save_payment(
        self,
        request: kingdeejdy_scm_models.SavePaymentRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        付款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_credit_save', request.body)
        )

    async def save_payment_async(
        self,
        request: kingdeejdy_scm_models.SavePaymentRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        付款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_credit_save', request.body)
        )

    def get_payment_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.PaymenyDetailResponse:
        """
        付款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PaymenyDetailResponse(),
            self._kernel.post(f'/jdy/arap/ap_credit_detail', request.body)
        )

    async def get_payment_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.PaymenyDetailResponse:
        """
        付款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PaymenyDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_credit_detail', request.body)
        )

    def get_apother_credit_list(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应付单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_other_credit_list', request.body)
        )

    async def get_apother_credit_list_async(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应付单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_other_credit_list', request.body)
        )

    def save_apother_credit(
        self,
        request: kingdeejdy_scm_models.OtherCreditSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应付单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_other_credit_save', request.body)
        )

    async def save_apother_credit_async(
        self,
        request: kingdeejdy_scm_models.OtherCreditSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应付单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_other_credit_save', request.body)
        )

    def get_apother_credit_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.APOtherCreditDetailResponse:
        """
        其他应付单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.APOtherCreditDetailResponse(),
            self._kernel.post(f'/jdy/arap/ap_other_credit_detail', request.body)
        )

    async def get_apother_credit_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.APOtherCreditDetailResponse:
        """
        其他应付单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.APOtherCreditDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_other_credit_detail', request.body)
        )

    def get_ar_other_credit_list(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应收单列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_other_credit_list', request.body)
        )

    async def get_ar_other_credit_list_async(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应收单列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_other_credit_list', request.body)
        )

    def save_ar_other_credit(
        self,
        request: kingdeejdy_scm_models.OtherCreditSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应收单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_other_credit_save', request.body)
        )

    async def save_ar_other_credit_async(
        self,
        request: kingdeejdy_scm_models.OtherCreditSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他应收单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_other_credit_save', request.body)
        )

    def get_arother_credit_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.APOtherCreditDetailResponse:
        """
        其他应收单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.APOtherCreditDetailResponse(),
            self._kernel.post(f'/jdy/arap/ar_other_credit_detail', request.body)
        )

    async def get_arother_credit_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.APOtherCreditDetailResponse:
        """
        其他应收单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.APOtherCreditDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_other_credit_detail', request.body)
        )

    def get_ap_other_credit_ret_list(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他支出退款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_other_credit_ret_list', request.body)
        )

    async def get_ap_other_credit_ret_list_async(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他支出退款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_other_credit_ret_list', request.body)
        )

    def save_apother_credit_ret(
        self,
        request: kingdeejdy_scm_models.OtherCreditRetSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他支出退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_other_credit_ret_save', request.body)
        )

    async def save_apother_credit_ret_async(
        self,
        request: kingdeejdy_scm_models.OtherCreditRetSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他支出退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_other_credit_ret_save', request.body)
        )

    def get_ap_other_credit_ret_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.OtherCreditRetDetailResponse:
        """
        其他支出退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.OtherCreditRetDetailResponse(),
            self._kernel.post(f'/jdy/arap/ap_other_credit_ret_detail', request.body)
        )

    async def get_ap_other_credit_ret_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.OtherCreditRetDetailResponse:
        """
        其他支出退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.OtherCreditRetDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_other_credit_ret_detail', request.body)
        )

    def get_ar_other_credit_ret_list(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他收入退款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_other_credit_ret_list', request.body)
        )

    async def get_ar_other_credit_ret_list_async(
        self,
        request: kingdeejdy_scm_models.CreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他收入退款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_other_credit_ret_list', request.body)
        )

    def save_ar_other_credit_ret(
        self,
        request: kingdeejdy_scm_models.OtherCreditRetSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他收入退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_other_credit_ret_save', request.body)
        )

    async def save_ar_other_credit_ret_async(
        self,
        request: kingdeejdy_scm_models.OtherCreditRetSaveRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        其他收入退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_other_credit_ret_save', request.body)
        )

    def get_ar_other_credit_ret_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.OtherCreditRetDetailResponse:
        """
        其他收入退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.OtherCreditRetDetailResponse(),
            self._kernel.post(f'/jdy/arap/ar_other_credit_ret_detail', request.body)
        )

    async def get_ar_other_credit_ret_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.OtherCreditRetDetailResponse:
        """
        其他收入退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.OtherCreditRetDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_other_credit_ret_detail', request.body)
        )

    def get_arap_initbase_list(
        self,
        request: kingdeejdy_scm_models.InitbaseRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        初始数据列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_initbase_list', request.body)
        )

    async def get_arap_initbase_list_async(
        self,
        request: kingdeejdy_scm_models.InitbaseRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        初始数据列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_initbase_list', request.body)
        )

    def get_ar_customer_credit(
        self,
        request: kingdeejdy_scm_models.CustomerIdRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        客户信用额度查询
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_customer_credit', request.body)
        )

    async def get_ar_customer_credit_async(
        self,
        request: kingdeejdy_scm_models.CustomerIdRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        客户信用额度查询
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_customer_credit', request.body)
        )

    def get_ar_order_statement_rpt(
        self,
        request: kingdeejdy_scm_models.ArOrderStatementRptRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询客户应收账款明细表（订货专用）
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_orderstatementrpt', request.body)
        )

    async def get_ar_order_statement_rpt_async(
        self,
        request: kingdeejdy_scm_models.ArOrderStatementRptRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询客户应收账款明细表（订货专用）
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_orderstatementrpt', request.body)
        )

    def get_arap_balance(
        self,
        request: kingdeejdy_scm_models.ArapBalanceRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询指定期间的应收/付余额
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_balance', request.body)
        )

    async def get_arap_balance_async(
        self,
        request: kingdeejdy_scm_models.ArapBalanceRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询指定期间的应收/付余额
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_balance', request.body)
        )

    def get_ar_summary_report(
        self,
        request: kingdeejdy_scm_models.ArApSummaryReportRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询应收汇总表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_summaryreport', request.body)
        )

    async def get_ar_summary_report_async(
        self,
        request: kingdeejdy_scm_models.ArApSummaryReportRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询应收汇总表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_summaryreport', request.body)
        )

    def get_ap_summary_report(
        self,
        request: kingdeejdy_scm_models.ArApSummaryReportRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询应付汇总表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_summaryreport', request.body)
        )

    async def get_ap_summary_report_async(
        self,
        request: kingdeejdy_scm_models.ArApSummaryReportRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询应付汇总表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_summaryreport', request.body)
        )

    def sava_ar_ap_operate(
        self,
        request: kingdeejdy_scm_models.ArApOperateRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        应收应付的单据操作
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_operate', request.body)
        )

    async def sava_ar_ap_operate_async(
        self,
        request: kingdeejdy_scm_models.ArApOperateRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        应收应付的单据操作
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_operate', request.body)
        )

    def get_ar_report(
        self,
        request: kingdeejdy_scm_models.ArReportRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询客户应收统计表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_report', request.body)
        )

    async def get_ar_report_async(
        self,
        request: kingdeejdy_scm_models.ArReportRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        查询客户应收统计表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_report', request.body)
        )

    def get_ar_credit_list(
        self,
        request: kingdeejdy_scm_models.ArCreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        收款单列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_credit_list', request.body)
        )

    async def get_ar_credit_list_async(
        self,
        request: kingdeejdy_scm_models.ArCreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        收款单列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_credit_list', request.body)
        )

    def save_ar_credit(
        self,
        request: kingdeejdy_scm_models.SaveArCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        收款单新增或修改一张收款单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_credit_save', request.body)
        )

    async def save_ar_credit_async(
        self,
        request: kingdeejdy_scm_models.SaveArCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        收款单新增或修改一张收款单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_credit_save', request.body)
        )

    def get_ar_credit_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ArCreditDetailResponse:
        """
        收款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ArCreditDetailResponse(),
            self._kernel.post(f'/jdy/arap/ar_credit_detail', request.body)
        )

    async def get_ar_credit_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ArCreditDetailResponse:
        """
        收款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ArCreditDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_credit_detail', request.body)
        )

    def get_ap_init_other_base_list(
        self,
        request: kingdeejdy_scm_models.InitBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初其他应付列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_initotherbase_list', request.body)
        )

    async def get_ap_init_other_base_list_async(
        self,
        request: kingdeejdy_scm_models.InitBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初其他应付列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_initotherbase_list', request.body)
        )

    def get_ar_init_other_base_list(
        self,
        request: kingdeejdy_scm_models.ArInitOtherBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初其他应收列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_initotherbase_list', request.body)
        )

    async def get_ar_init_other_base_list_async(
        self,
        request: kingdeejdy_scm_models.ArInitOtherBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初其他应收列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_initotherbase_list', request.body)
        )

    def get_ap_init_base_list(
        self,
        request: kingdeejdy_scm_models.InitBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初应付列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_initbase_list', request.body)
        )

    async def get_ap_init_base_list_async(
        self,
        request: kingdeejdy_scm_models.InitBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初应付列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_initbase_list', request.body)
        )

    def get_ar_init_base_list(
        self,
        request: kingdeejdy_scm_models.InitBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初应收列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_initbase_list', request.body)
        )

    async def get_ar_init_base_list_async(
        self,
        request: kingdeejdy_scm_models.InitBaseListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        期初应收列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_initbase_list', request.body)
        )

    def get_ar_ap_balance_or_debt_list(
        self,
        request: kingdeejdy_scm_models.ArApBalanceOrDebtListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        欠款&余额列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_balance_or_debt_list', request.body)
        )

    async def get_ar_ap_balance_or_debt_list_async(
        self,
        request: kingdeejdy_scm_models.ArApBalanceOrDebtListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        欠款&余额列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_balance_or_debt_list', request.body)
        )

    def get_ar_ap_account_bill_type_request(
        self,
        request: kingdeejdy_scm_models.NoBodyRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        获取账户收支明细单据类型
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_account_billtype', request.body)
        )

    async def get_ar_ap_account_bill_type_request_async(
        self,
        request: kingdeejdy_scm_models.NoBodyRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        获取账户收支明细单据类型
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_account_billtype', request.body)
        )

    def get_ar_ap_account_detail_summary(
        self,
        request: kingdeejdy_scm_models.ArApAccountDetailSummaryRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        账户收支明细表分类统计
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_account_detail_summary', request.body)
        )

    async def get_ar_ap_account_detail_summary_async(
        self,
        request: kingdeejdy_scm_models.ArApAccountDetailSummaryRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        账户收支明细表分类统计
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_account_detail_summary', request.body)
        )

    def get_ar_ap_account_detail_bybillno(
        self,
        request: kingdeejdy_scm_models.ArApAccountDetailBybillnoRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        账户收支明细表按单统计
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_account_detail_bybillno', request.body)
        )

    async def get_ar_ap_account_detail_bybillno_async(
        self,
        request: kingdeejdy_scm_models.ArApAccountDetailBybillnoRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        账户收支明细表按单统计
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_account_detail_bybillno', request.body)
        )

    def get_ar_ap_account_balance(
        self,
        request: kingdeejdy_scm_models.ArApAccountBalanceRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金分析主页面
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_account_balance', request.body)
        )

    async def get_ar_ap_account_balance_async(
        self,
        request: kingdeejdy_scm_models.ArApAccountBalanceRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金分析主页面
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_account_balance', request.body)
        )

    def get_ar_ap_account_detail_list(
        self,
        request: kingdeejdy_scm_models.ArApAccountDetailListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金帐户明细列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_account_detail_list', request.body)
        )

    async def get_ar_ap_account_detail_list_async(
        self,
        request: kingdeejdy_scm_models.ArApAccountDetailListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金帐户明细列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_account_detail_list', request.body)
        )

    def get_boss_get_buy_module(
        self,
        request: kingdeejdy_scm_models.NoBodyRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-获取购买模块
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/boss_get_buy_module', request.body)
        )

    async def get_boss_get_buy_module_async(
        self,
        request: kingdeejdy_scm_models.NoBodyRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-获取购买模块
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/boss_get_buy_module', request.body)
        )

    def get_boss_balance_trend(
        self,
        request: kingdeejdy_scm_models.NoBodyRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金余额趋势
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/boss_balance_trend', request.body)
        )

    async def get_boss_balance_trend_async(
        self,
        request: kingdeejdy_scm_models.NoBodyRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金余额趋势
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/boss_balance_trend', request.body)
        )

    def get_boss_balance_home_page(
        self,
        request: kingdeejdy_scm_models.BossBalanceHomePageRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金余额首页
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/boss_balance_home_page', request.body)
        )

    async def get_boss_balance_home_page_async(
        self,
        request: kingdeejdy_scm_models.BossBalanceHomePageRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金余额首页
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/boss_balance_home_page', request.body)
        )

    def get_boss_debit_credit_trend(
        self,
        request: kingdeejdy_scm_models.BossDebitCreditTrendRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金收支趋势
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/boss_debit_credit_trend', request.body)
        )

    async def get_boss_debit_credit_trend_async(
        self,
        request: kingdeejdy_scm_models.BossDebitCreditTrendRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金收支趋势
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/boss_debit_credit_trend', request.body)
        )

    def get_boss_account_details(
        self,
        request: kingdeejdy_scm_models.BossAccountDetailsRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金流水明细
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/boss_account_details', request.body)
        )

    async def get_boss_account_details_async(
        self,
        request: kingdeejdy_scm_models.BossAccountDetailsRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金流水明细
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/boss_account_details', request.body)
        )

    def get_boss_account_balance(
        self,
        request: kingdeejdy_scm_models.BossAccountBalanceRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金账户余额
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/boss_account_balance', request.body)
        )

    async def get_boss_account_balance_async(
        self,
        request: kingdeejdy_scm_models.BossAccountBalanceRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金看板-资金账户余额
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/boss_account_balance', request.body)
        )

    def get_ar_ap_account_balance_list(
        self,
        request: kingdeejdy_scm_models.ArApAccountBalanceListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金分析主页面查询接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_account_balance_list', request.body)
        )

    async def get_ar_ap_account_balance_list_async(
        self,
        request: kingdeejdy_scm_models.ArApAccountBalanceListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金分析主页面查询接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_account_balance_list', request.body)
        )

    def get_ar_ap_capital_trend(
        self,
        request: kingdeejdy_scm_models.ArApCapitalTrendRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金趋势图（按日）
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/arap_capital_trend', request.body)
        )

    async def get_ar_ap_capital_trend_async(
        self,
        request: kingdeejdy_scm_models.ArApCapitalTrendRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        资金趋势图（按日）
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/arap_capital_trend', request.body)
        )

    def get_ap_pre_credit_list(
        self,
        request: kingdeejdy_scm_models.PreCreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_precredit_list', request.body)
        )

    async def get_ap_pre_credit_list_async(
        self,
        request: kingdeejdy_scm_models.PreCreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_precredit_list', request.body)
        )

    def save_ap_pre_credit(
        self,
        request: kingdeejdy_scm_models.SaveApPreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付款单新增&修改接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_precredit_save', request.body)
        )

    async def save_ap_pre_credit_async(
        self,
        request: kingdeejdy_scm_models.SaveApPreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付款单新增&修改接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_precredit_save', request.body)
        )

    def get_ap_pre_credit_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ApPreCreditDetailResponse:
        """
        预付款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApPreCreditDetailResponse(),
            self._kernel.post(f'/jdy/arap/ap_precredit_detail', request.body)
        )

    async def get_ap_pre_credit_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ApPreCreditDetailResponse:
        """
        预付款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApPreCreditDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_precredit_detail', request.body)
        )

    def get_ap_pre_credit_ret_list(
        self,
        request: kingdeejdy_scm_models.PaymentListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付退款单列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_precredit_ret_list', request.body)
        )

    async def get_ap_pre_credit_ret_list_async(
        self,
        request: kingdeejdy_scm_models.PaymentListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付退款单列表
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_precredit_ret_list', request.body)
        )

    def save_ap_pre_credit_ret(
        self,
        request: kingdeejdy_scm_models.SavePreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ap_precredit_ret_save', request.body)
        )

    async def save_ap_pre_credit_ret_async(
        self,
        request: kingdeejdy_scm_models.SavePreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预付退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_precredit_ret_save', request.body)
        )

    def get_ap_pre_credit_ret_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ApPreCreditRetDetailResponse:
        """
        预付退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApPreCreditRetDetailResponse(),
            self._kernel.post(f'/jdy/arap/ap_precredit_ret_detail', request.body)
        )

    async def get_ap_pre_credit_ret_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ApPreCreditRetDetailResponse:
        """
        预付退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApPreCreditRetDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ap_precredit_ret_detail', request.body)
        )

    def get_ar_pre_credit_list(
        self,
        request: kingdeejdy_scm_models.PreCreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_precredit_list', request.body)
        )

    async def get_ar_pre_credit_list_async(
        self,
        request: kingdeejdy_scm_models.PreCreditListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_precredit_list', request.body)
        )

    def save_ar_pre_credit(
        self,
        request: kingdeejdy_scm_models.SavePreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_precredit_save', request.body)
        )

    async def save_ar_pre_credit_async(
        self,
        request: kingdeejdy_scm_models.SavePreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_precredit_save', request.body)
        )

    def get_ar_pre_credit_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ArPreCreditDetailResponse:
        """
        预收款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ArPreCreditDetailResponse(),
            self._kernel.post(f'/jdy/arap/ar_precredit_detail', request.body)
        )

    async def get_ar_pre_credit_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ArPreCreditDetailResponse:
        """
        预收款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ArPreCreditDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_precredit_detail', request.body)
        )

    def get_ar_pre_credit_ret_list(
        self,
        request: kingdeejdy_scm_models.PaymentListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收退款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_precredit_ret_list', request.body)
        )

    async def get_ar_pre_credit_ret_list_async(
        self,
        request: kingdeejdy_scm_models.PaymentListRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收退款单列表接口
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_precredit_ret_list', request.body)
        )

    def save_ar_pre_credit_ret(
        self,
        request: kingdeejdy_scm_models.SavePreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            self._kernel.post(f'/jdy/arap/ar_precredit_ret_save', request.body)
        )

    async def save_ar_pre_credit_ret_async(
        self,
        request: kingdeejdy_scm_models.SavePreCreditRequest,
    ) -> kingdeejdy_scm_models.ApiResponse:
        """
        预收退款单新增&修改
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ApiResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_precredit_ret_save', request.body)
        )

    def get_ar_pre_credit_ret_detail(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ArPreCreditRetDetailResponse:
        """
        预收退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ArPreCreditRetDetailResponse(),
            self._kernel.post(f'/jdy/arap/ar_precredit_ret_detail', request.body)
        )

    async def get_ar_pre_credit_ret_detail_async(
        self,
        request: kingdeejdy_scm_models.CreditDetailRequest,
    ) -> kingdeejdy_scm_models.ArPreCreditRetDetailResponse:
        """
        预收退款单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ArPreCreditRetDetailResponse(),
            await self._kernel.post_async(f'/jdy/arap/ar_precredit_ret_detail', request.body)
        )

    def company_send(
        self,
        request: kingdeejdy_scm_models.CompanySendRequest,
    ) -> dict:
        """
        企业互联发送数据接口
        """
        return self._kernel.post(f'/jdy/pur/company_send', request.body)

    async def company_send_async(
        self,
        request: kingdeejdy_scm_models.CompanySendRequest,
    ) -> dict:
        """
        企业互联发送数据接口
        """
        return await self._kernel.post_async(f'/jdy/pur/company_send', request.body)

    def bill_push(
        self,
        request: kingdeejdy_scm_models.BillPushRequest,
    ) -> dict:
        """
        单据下推操作
        """
        return self._kernel.post(f'/jdy/sal/bill_push', request.body)

    async def bill_push_async(
        self,
        request: kingdeejdy_scm_models.BillPushRequest,
    ) -> dict:
        """
        单据下推操作
        """
        return await self._kernel.post_async(f'/jdy/sal/bill_push', request.body)

    def multi_unit_cal(
        self,
        request: kingdeejdy_scm_models.MultiUnitCalRequest,
    ) -> dict:
        """
        商品多单位录入计算逻辑
        """
        return self._kernel.post(f'/jdy/sal/sal_multiunit_cal', request.body)

    async def multi_unit_cal_async(
        self,
        request: kingdeejdy_scm_models.MultiUnitCalRequest,
    ) -> dict:
        """
        商品多单位录入计算逻辑
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_multiunit_cal', request.body)

    def get_customer_debit(
        self,
        request: kingdeejdy_scm_models.CustomerDebitRequest,
    ) -> dict:
        """
        查询客户上次的欠款和应收款余额
        """
        return self._kernel.post(f'/jdy/sal/sal_customer_debt', request.body)

    async def get_customer_debit_async(
        self,
        request: kingdeejdy_scm_models.CustomerDebitRequest,
    ) -> dict:
        """
        查询客户上次的欠款和应收款余额
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_customer_debt', request.body)

    def get_sale_batch_list(
        self,
        request: kingdeejdy_scm_models.SaleBatchListRequest,
    ) -> dict:
        """
        查询商品批次列表
        """
        return self._kernel.post(f'/jdy/sal/sal_batch_list', request.body)

    async def get_sale_batch_list_async(
        self,
        request: kingdeejdy_scm_models.SaleBatchListRequest,
    ) -> dict:
        """
        查询商品批次列表
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_batch_list', request.body)

    def get_sale_price_for_material(
        self,
        request: kingdeejdy_scm_models.SalePriceForMaterialRequest,
    ) -> dict:
        """
        查询商品价格
        """
        return self._kernel.post(f'/jdy/sal/sal_material_price_query', request.body)

    async def get_sale_price_for_material_async(
        self,
        request: kingdeejdy_scm_models.SalePriceForMaterialRequest,
    ) -> dict:
        """
        查询商品价格
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_material_price_query', request.body)

    def get_sale_price_list_for_material(
        self,
        request: kingdeejdy_scm_models.SalePriceListRequest,
    ) -> dict:
        """
        查询商品价格策略
        """
        return self._kernel.post(f'/jdy/sal/sal_material_price_list', request.body)

    async def get_sale_price_list_for_material_async(
        self,
        request: kingdeejdy_scm_models.SalePriceListRequest,
    ) -> dict:
        """
        查询商品价格策略
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_material_price_list', request.body)

    def get_sale_all_price_list_for_material(
        self,
        request: kingdeejdy_scm_models.SaleAllPriceListRequest,
    ) -> dict:
        """
        获取商品的多种价格
        """
        return self._kernel.post(f'/jdy/sal/sal_all_price_list', request.body)

    async def get_sale_all_price_list_for_material_async(
        self,
        request: kingdeejdy_scm_models.SaleAllPriceListRequest,
    ) -> dict:
        """
        获取商品的多种价格
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_all_price_list', request.body)

    def get_material_stock(
        self,
        request: kingdeejdy_scm_models.MaterialStockRequest,
    ) -> dict:
        """
        查询商品库存分布
        """
        return self._kernel.post(f'/jdy/sal/sal_material_stock_query', request.body)

    async def get_material_stock_async(
        self,
        request: kingdeejdy_scm_models.MaterialStockRequest,
    ) -> dict:
        """
        查询商品库存分布
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_material_stock_query', request.body)

    def get_batch_info_for_material(
        self,
        request: kingdeejdy_scm_models.BatchInfoForMaterialRequest,
    ) -> dict:
        """
        根据系统参数查询商品批次信息
        """
        return self._kernel.post(f'/jdy/inv/batch_rule_query', request.body)

    async def get_batch_info_for_material_async(
        self,
        request: kingdeejdy_scm_models.BatchInfoForMaterialRequest,
    ) -> dict:
        """
        根据系统参数查询商品批次信息
        """
        return await self._kernel.post_async(f'/jdy/inv/batch_rule_query', request.body)

    def get_home_page_to_do(
        self,
        request: kingdeejdy_scm_models.HomePageToDoRequest,
    ) -> dict:
        """
        首页代办-全模块数据查询
        """
        return self._kernel.post(f'/jdy/sal/homepage_todo_list', request.body)

    async def get_home_page_to_do_async(
        self,
        request: kingdeejdy_scm_models.HomePageToDoRequest,
    ) -> dict:
        """
        首页代办-全模块数据查询
        """
        return await self._kernel.post_async(f'/jdy/sal/homepage_todo_list', request.body)

    def get_spid_inv_list(
        self,
        request: kingdeejdy_scm_models.SpidInvListRequest,
    ) -> dict:
        """
        查询仓库下的仓位的即时库存列表
        """
        return self._kernel.post(f'/jdy/inv/spid_inv_list', request.body)

    async def get_spid_inv_list_async(
        self,
        request: kingdeejdy_scm_models.SpidInvListRequest,
    ) -> dict:
        """
        查询仓库下的仓位的即时库存列表
        """
        return await self._kernel.post_async(f'/jdy/inv/spid_inv_list', request.body)

    def get_inv_operate(
        self,
        request: kingdeejdy_scm_models.InvOperateRequest,
    ) -> dict:
        """
        仓存类单据（删除、审核、反审核）操作
        接口将停止维护，推荐使用：批量操作接口
        """
        return self._kernel.post(f'/jdy/inv/inv_operate', request.body)

    async def get_inv_operate_async(
        self,
        request: kingdeejdy_scm_models.InvOperateRequest,
    ) -> dict:
        """
        仓存类单据（删除、审核、反审核）操作
        接口将停止维护，推荐使用：批量操作接口
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_operate', request.body)

    def get_stock_inv_list(
        self,
        request: kingdeejdy_scm_models.StockInvListRequest,
    ) -> dict:
        """
        查询仓库的即时库存列表
        """
        return self._kernel.post(f'/jdy/inv/stock_inv_list', request.body)

    async def get_stock_inv_list_async(
        self,
        request: kingdeejdy_scm_models.StockInvListRequest,
    ) -> dict:
        """
        查询仓库的即时库存列表
        """
        return await self._kernel.post_async(f'/jdy/inv/stock_inv_list', request.body)

    def save_inv_other_in(
        self,
        request: kingdeejdy_scm_models.InvOtherInSaveRequest,
    ) -> dict:
        """
        其他入库单保存新增
        """
        return self._kernel.post(f'/jdy/inv/inv_otherin_save', request.body)

    async def save_inv_other_in_async(
        self,
        request: kingdeejdy_scm_models.InvOtherInSaveRequest,
    ) -> dict:
        """
        其他入库单保存新增
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_otherin_save', request.body)

    def get_inv_other_in_list(
        self,
        request: kingdeejdy_scm_models.InvOtherOutInListRequest,
    ) -> dict:
        """
        其他入库单列表查询
        """
        return self._kernel.post(f'/jdy/inv/inv_otherin_list', request.body)

    async def get_inv_other_in_list_async(
        self,
        request: kingdeejdy_scm_models.InvOtherOutInListRequest,
    ) -> dict:
        """
        其他入库单列表查询
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_otherin_list', request.body)

    def get_inv_other_in_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvOtherInDetailResponse:
        """
        获取其他入库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvOtherInDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_otherin_detail', request.body)
        )

    async def get_inv_other_in_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvOtherInDetailResponse:
        """
        获取其他入库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvOtherInDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_otherin_detail', request.body)
        )

    def get_inv_other_in_draw(
        self,
        request: kingdeejdy_scm_models.InvOtherInDrawRequest,
    ) -> dict:
        """
        其他入库单选择源单
        """
        return self._kernel.post(f'/jdy/inv/inv_otherin_draw', request.body)

    async def get_inv_other_in_draw_async(
        self,
        request: kingdeejdy_scm_models.InvOtherInDrawRequest,
    ) -> dict:
        """
        其他入库单选择源单
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_otherin_draw', request.body)

    def get_inv_material_cost(
        self,
        request: kingdeejdy_scm_models.InvOtherInDrawRequest,
    ) -> dict:
        """
        其他出入库成本查询
        根据价格策略的其他出入库单取价获取商品的入库成本
        """
        return self._kernel.post(f'/jdy/inv/inv_material_cost_query', request.body)

    async def get_inv_material_cost_async(
        self,
        request: kingdeejdy_scm_models.InvOtherInDrawRequest,
    ) -> dict:
        """
        其他出入库成本查询
        根据价格策略的其他出入库单取价获取商品的入库成本
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_material_cost_query', request.body)

    def save_inv_other_out(
        self,
        request: kingdeejdy_scm_models.InvOtherOutSaveRequest,
    ) -> dict:
        """
        其他出库单保存新增
        """
        return self._kernel.post(f'/jdy/inv/inv_otherout_save', request.body)

    async def save_inv_other_out_async(
        self,
        request: kingdeejdy_scm_models.InvOtherOutSaveRequest,
    ) -> dict:
        """
        其他出库单保存新增
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_otherout_save', request.body)

    def get_inv_other_out_list(
        self,
        request: kingdeejdy_scm_models.InvOtherOutInListRequest,
    ) -> dict:
        """
        其他出库单列表查询
        """
        return self._kernel.post(f'/jdy/inv/inv_otherout_list', request.body)

    async def get_inv_other_out_list_async(
        self,
        request: kingdeejdy_scm_models.InvOtherOutInListRequest,
    ) -> dict:
        """
        其他出库单列表查询
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_otherout_list', request.body)

    def get_inv_other_out_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvOtherOutDetailResponse:
        """
        获取其他出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvOtherOutDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_otherout_detail', request.body)
        )

    async def get_inv_other_out_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvOtherOutDetailResponse:
        """
        获取其他出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvOtherOutDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_otherout_detail', request.body)
        )

    def get_inv_other_out_draw(
        self,
        request: kingdeejdy_scm_models.InvOtherOutDrawRequest,
    ) -> dict:
        """
        其他出库单选择源单
        其他出库单选择其他入库单生成其他出库单
        """
        return self._kernel.post(f'/jdy/inv/inv_otherout_draw', request.body)

    async def get_inv_other_out_draw_async(
        self,
        request: kingdeejdy_scm_models.InvOtherOutDrawRequest,
    ) -> dict:
        """
        其他出库单选择源单
        其他出库单选择其他入库单生成其他出库单
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_otherout_draw', request.body)

    def save_inv_check_task(
        self,
        request: kingdeejdy_scm_models.InvCheckTaskRequest,
    ) -> dict:
        """
        盘点任务保存
        """
        return self._kernel.post(f'/jdy/inv/check_task_save', request.body)

    async def save_inv_check_task_async(
        self,
        request: kingdeejdy_scm_models.InvCheckTaskRequest,
    ) -> dict:
        """
        盘点任务保存
        """
        return await self._kernel.post_async(f'/jdy/inv/check_task_save', request.body)

    def get_inv_check_task_list(
        self,
        request: kingdeejdy_scm_models.InvCheckTaskListRequest,
    ) -> dict:
        """
        盘点任务列表
        """
        return self._kernel.post(f'/jdy/inv/check_task_list', request.body)

    async def get_inv_check_task_list_async(
        self,
        request: kingdeejdy_scm_models.InvCheckTaskListRequest,
    ) -> dict:
        """
        盘点任务列表
        """
        return await self._kernel.post_async(f'/jdy/inv/check_task_list', request.body)

    def get_inv_check_task_detail(
        self,
        request: kingdeejdy_scm_models.InvCheckTaskDetailRequest,
    ) -> kingdeejdy_scm_models.InvCheckTaskDetailResponse:
        """
        盘点任务详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvCheckTaskDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_check_loss_bill_detail', request.body)
        )

    async def get_inv_check_task_detail_async(
        self,
        request: kingdeejdy_scm_models.InvCheckTaskDetailRequest,
    ) -> kingdeejdy_scm_models.InvCheckTaskDetailResponse:
        """
        盘点任务详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvCheckTaskDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_check_loss_bill_detail', request.body)
        )

    def save_inv_multi_check_bill(
        self,
        request: kingdeejdy_scm_models.InvCheckBillSaveRequest,
    ) -> dict:
        """
        分量盘点单保存
        """
        return self._kernel.post(f'/jdy/inv/inv_multi_check_bill_save', request.body)

    async def save_inv_multi_check_bill_async(
        self,
        request: kingdeejdy_scm_models.InvCheckBillSaveRequest,
    ) -> dict:
        """
        分量盘点单保存
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_multi_check_bill_save', request.body)

    def get_inv_multi_check_bill_list(
        self,
        request: kingdeejdy_scm_models.InvMultiCheckBillListRequest,
    ) -> dict:
        """
        分量盘点单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_multi_check_bill_list', request.body)

    async def get_inv_multi_check_bill_list_async(
        self,
        request: kingdeejdy_scm_models.InvMultiCheckBillListRequest,
    ) -> dict:
        """
        分量盘点单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_multi_check_bill_list', request.body)

    def get_inv_multi_check_bill_items(
        self,
        request: kingdeejdy_scm_models.InvMultiCheckBillListRequest,
    ) -> dict:
        """
        分量盘点单生成分录清单
        """
        return self._kernel.post(f'/jdy/inv/inv_multi_check_bill_items', request.body)

    async def get_inv_multi_check_bill_items_async(
        self,
        request: kingdeejdy_scm_models.InvMultiCheckBillListRequest,
    ) -> dict:
        """
        分量盘点单生成分录清单
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_multi_check_bill_items', request.body)

    def get_inv_multi_check_bill_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvMultiBillDetailResponse:
        """
        分量盘点单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvMultiBillDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_multi_check_bill_detail', request.body)
        )

    async def get_inv_multi_check_bill_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvMultiBillDetailResponse:
        """
        分量盘点单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvMultiBillDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_multi_check_bill_detail', request.body)
        )

    def save_inv_check_bill(
        self,
        request: kingdeejdy_scm_models.InvCheckBillSaveRequest,
    ) -> dict:
        """
        盘点单保存
        """
        return self._kernel.post(f'/jdy/inv/inv_check_bill_save', request.body)

    async def save_inv_check_bill_async(
        self,
        request: kingdeejdy_scm_models.InvCheckBillSaveRequest,
    ) -> dict:
        """
        盘点单保存
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_bill_save', request.body)

    def get_inv_check_bill_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvBillDetailResponse:
        """
        盘点单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvBillDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_check_bill_detail', request.body)
        )

    async def get_inv_check_bill_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvBillDetailResponse:
        """
        盘点单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvBillDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_check_bill_detail', request.body)
        )

    def get_inv_check_bill_list(
        self,
        request: kingdeejdy_scm_models.InvCheckBillListRequest,
    ) -> dict:
        """
        盘点单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_check_bill_list', request.body)

    async def get_inv_check_bill_list_async(
        self,
        request: kingdeejdy_scm_models.InvCheckBillListRequest,
    ) -> dict:
        """
        盘点单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_bill_list', request.body)

    def get_inv_check_bill_summary(
        self,
        request: kingdeejdy_scm_models.InvCheckBillSummaryRequest,
    ) -> dict:
        """
        盘点单汇总
        """
        return self._kernel.post(f'/jdy/inv/inv_check_bill_summary', request.body)

    async def get_inv_check_bill_summary_async(
        self,
        request: kingdeejdy_scm_models.InvCheckBillSummaryRequest,
    ) -> dict:
        """
        盘点单汇总
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_bill_summary', request.body)

    def get_inv_check_bill_gain_loss_deal(
        self,
        request: kingdeejdy_scm_models.InvCheckBillGainLossDealRequest,
    ) -> dict:
        """
        盘点单盈亏处理
        """
        return self._kernel.post(f'/jdy/inv/inv_check_bill_gainloss_deal', request.body)

    async def get_inv_check_bill_gain_loss_deal_async(
        self,
        request: kingdeejdy_scm_models.InvCheckBillGainLossDealRequest,
    ) -> dict:
        """
        盘点单盈亏处理
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_bill_gainloss_deal', request.body)

    def get_inv_serial_base_list(
        self,
        request: kingdeejdy_scm_models.InvSerialBaselistRequest,
    ) -> dict:
        """
        序列号基本信息列表查询
        """
        return self._kernel.post(f'/jdy/inv/inv_serial_baselist', request.body)

    async def get_inv_serial_base_list_async(
        self,
        request: kingdeejdy_scm_models.InvSerialBaselistRequest,
    ) -> dict:
        """
        序列号基本信息列表查询
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_serial_baselist', request.body)

    def get_inv_fuzzy_query_sn_list_by_sn_prefix(
        self,
        request: kingdeejdy_scm_models.InvFuzzyQuerySnListBySnPrefixRequest,
    ) -> dict:
        """
        序列号模糊查询（只匹配更新了库存的序列号）
        """
        return self._kernel.post(f'/jdy/inv/inv_fuzzyquery_snlist_bysnprefix', request.body)

    async def get_inv_fuzzy_query_sn_list_by_sn_prefix_async(
        self,
        request: kingdeejdy_scm_models.InvFuzzyQuerySnListBySnPrefixRequest,
    ) -> dict:
        """
        序列号模糊查询（只匹配更新了库存的序列号）
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_fuzzyquery_snlist_bysnprefix', request.body)

    def get_inv_list_v2(
        self,
        request: kingdeejdy_scm_models.InvListV2Request,
    ) -> dict:
        """
        查询即时库存中库存列表
        """
        return self._kernel.post(f'/jdy/inv/inv_list_v2', request.body)

    async def get_inv_list_v2_async(
        self,
        request: kingdeejdy_scm_models.InvListV2Request,
    ) -> dict:
        """
        查询即时库存中库存列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_list_v2', request.body)

    def inv_occupy(
        self,
        request: kingdeejdy_scm_models.InvOccupyRequest,
    ) -> dict:
        """
        库存占用
        """
        return self._kernel.post(f'/jdy/inv/inv_occupy', request.body)

    async def inv_occupy_async(
        self,
        request: kingdeejdy_scm_models.InvOccupyRequest,
    ) -> dict:
        """
        库存占用
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_occupy', request.body)

    def inv_release_occupy(
        self,
        request: kingdeejdy_scm_models.InvReleaseOccupyRequest,
    ) -> dict:
        """
        库存占用释放
        """
        return self._kernel.post(f'/jdy/inv/inv_release_occupy', request.body)

    async def inv_release_occupy_async(
        self,
        request: kingdeejdy_scm_models.InvReleaseOccupyRequest,
    ) -> dict:
        """
        库存占用释放
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_release_occupy', request.body)

    def get_inv_synchronous_list(
        self,
        request: kingdeejdy_scm_models.InvSynchronousListRequest,
    ) -> dict:
        """
        库存同步列表
        """
        return self._kernel.post(f'/jdy/inv/inv_synchronous_list', request.body)

    async def get_inv_synchronous_list_async(
        self,
        request: kingdeejdy_scm_models.InvSynchronousListRequest,
    ) -> dict:
        """
        库存同步列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_synchronous_list', request.body)

    def get_batch_kfperiod_inv_list(
        self,
        request: kingdeejdy_scm_models.BatchKfperiodInvListRequest,
    ) -> dict:
        """
        批次保质期及库存列表查询
        """
        return self._kernel.post(f'/jdy/inv/batch_kfperiod_inv_list', request.body)

    async def get_batch_kfperiod_inv_list_async(
        self,
        request: kingdeejdy_scm_models.BatchKfperiodInvListRequest,
    ) -> dict:
        """
        批次保质期及库存列表查询
        """
        return await self._kernel.post_async(f'/jdy/inv/batch_kfperiod_inv_list', request.body)

    def save_inv_init(
        self,
        request: kingdeejdy_scm_models.InvInitSaveRequest,
    ) -> dict:
        """
        期初保存新增
        """
        return self._kernel.post(f'/jdy/inv/inv_init_save', request.body)

    async def save_inv_init_async(
        self,
        request: kingdeejdy_scm_models.InvInitSaveRequest,
    ) -> dict:
        """
        期初保存新增
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_init_save', request.body)

    def get_inv_init_list(
        self,
        request: kingdeejdy_scm_models.InvInitListRequest,
    ) -> dict:
        """
        期初列表
        """
        return self._kernel.post(f'/jdy/inv/inv_init_list', request.body)

    async def get_inv_init_list_async(
        self,
        request: kingdeejdy_scm_models.InvInitListRequest,
    ) -> dict:
        """
        期初列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_init_list', request.body)

    def get_inv_init_sn_list_by_ids(
        self,
        request: kingdeejdy_scm_models.InvQuerySnListByIdsRequest,
    ) -> dict:
        """
        期初列表
        """
        return self._kernel.post(f'/jdy/inv/inv_query_snlist_byids', request.body)

    async def get_inv_init_sn_list_by_ids_async(
        self,
        request: kingdeejdy_scm_models.InvQuerySnListByIdsRequest,
    ) -> dict:
        """
        期初列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_query_snlist_byids', request.body)

    def save_inv_check_loss_bill(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillSaveRequest,
    ) -> dict:
        """
        盘亏单保存
        """
        return self._kernel.post(f'/jdy/inv/inv_check_loss_bill_save', request.body)

    async def save_inv_check_loss_bill_async(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillSaveRequest,
    ) -> dict:
        """
        盘亏单保存
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_loss_bill_save', request.body)

    def get_inv_check_loss_bill_list(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillListRequest,
    ) -> dict:
        """
        盘亏单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_check_loss_bill_list', request.body)

    async def get_inv_check_loss_bill_list_async(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillListRequest,
    ) -> dict:
        """
        盘亏单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_loss_bill_list', request.body)

    def get_inv_check_loss_bill_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvCheckLossBillDetailResponse:
        """
        盘亏单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvCheckLossBillDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_check_loss_bill_detail', request.body)
        )

    async def get_inv_check_loss_bill_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvCheckLossBillDetailResponse:
        """
        盘亏单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvCheckLossBillDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_check_loss_bill_detail', request.body)
        )

    def save_inv_check_gain_bill(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillSaveRequest,
    ) -> dict:
        """
        盘盈单保存
        """
        return self._kernel.post(f'/jdy/inv/inv_check_gain_bill_save', request.body)

    async def save_inv_check_gain_bill_async(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillSaveRequest,
    ) -> dict:
        """
        盘盈单保存
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_gain_bill_save', request.body)

    def get_inv_check_gain_bill_list(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillListRequest,
    ) -> dict:
        """
        盘盈单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_check_gain_bill_list', request.body)

    async def get_inv_check_gain_bill_list_async(
        self,
        request: kingdeejdy_scm_models.InvCheckGainLossBillListRequest,
    ) -> dict:
        """
        盘盈单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_check_gain_bill_list', request.body)

    def get_inv_check_gain_bill_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvCheckGainBillDetailResponse:
        """
        盘盈单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvCheckGainBillDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_check_gain_bill_detail', request.body)
        )

    async def get_inv_check_gain_bill_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvCheckGainBillDetailResponse:
        """
        盘盈单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvCheckGainBillDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_check_gain_bill_detail', request.body)
        )

    def save_inv_tf_move(
        self,
        request: kingdeejdy_scm_models.InvTfMoveSaveRequest,
    ) -> dict:
        """
        移仓单保存
        """
        return self._kernel.post(f'/jdy/inv/inv_tfmove_save', request.body)

    async def save_inv_tf_move_async(
        self,
        request: kingdeejdy_scm_models.InvTfMoveSaveRequest,
    ) -> dict:
        """
        移仓单保存
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfmove_save', request.body)

    def get_inv_tf_move_list(
        self,
        request: kingdeejdy_scm_models.InvTfMoveListRequest,
    ) -> dict:
        """
        移仓单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_tfmove_list', request.body)

    async def get_inv_tf_move_list_async(
        self,
        request: kingdeejdy_scm_models.InvTfMoveListRequest,
    ) -> dict:
        """
        移仓单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfmove_list', request.body)

    def get_inv_tf_move_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvTfMoveDetailResponse:
        """
        移仓单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvTfMoveDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_tfmove_detail', request.body)
        )

    async def get_inv_tf_move_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvTfMoveDetailResponse:
        """
        移仓单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvTfMoveDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_tfmove_detail', request.body)
        )

    def save_inv_tf_in(
        self,
        request: kingdeejdy_scm_models.InvTfInSaveRequest,
    ) -> dict:
        """
        调拨入库单保存
        """
        return self._kernel.post(f'/jdy/inv/inv_tfin_save', request.body)

    async def save_inv_tf_in_async(
        self,
        request: kingdeejdy_scm_models.InvTfInSaveRequest,
    ) -> dict:
        """
        调拨入库单保存
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfin_save', request.body)

    def get_inv_tf_in_list(
        self,
        request: kingdeejdy_scm_models.InvTfInListRequest,
    ) -> dict:
        """
        调拨入库单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_tfin_list', request.body)

    async def get_inv_tf_in_list_async(
        self,
        request: kingdeejdy_scm_models.InvTfInListRequest,
    ) -> dict:
        """
        调拨入库单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfin_list', request.body)

    def get_inv_tf_in_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvTfInDetailResponse:
        """
        调拨入库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvTfInDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_tfin_detail', request.body)
        )

    async def get_inv_tf_in_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvTfInDetailResponse:
        """
        调拨入库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvTfInDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_tfin_detail', request.body)
        )

    def save_inv_tf_out(
        self,
        request: kingdeejdy_scm_models.InvTfOutSaveRequest,
    ) -> dict:
        """
        调拨出库单保存
        """
        return self._kernel.post(f'/jdy/inv/inv_tfout_save', request.body)

    async def save_inv_tf_out_async(
        self,
        request: kingdeejdy_scm_models.InvTfOutSaveRequest,
    ) -> dict:
        """
        调拨出库单保存
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfout_save', request.body)

    def inv_tf_in_draw(
        self,
        request: kingdeejdy_scm_models.InvTfInDrawRequest,
    ) -> dict:
        """
        调拨出库单入库
        """
        return self._kernel.post(f'/jdy/inv/inv_tfin_draw', request.body)

    async def inv_tf_in_draw_async(
        self,
        request: kingdeejdy_scm_models.InvTfInDrawRequest,
    ) -> dict:
        """
        调拨出库单入库
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfin_draw', request.body)

    def get_inv_tf_out_list(
        self,
        request: kingdeejdy_scm_models.InvTfOutListRequest,
    ) -> dict:
        """
        调拨出库单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_tfout_list', request.body)

    async def get_inv_tf_out_list_async(
        self,
        request: kingdeejdy_scm_models.InvTfOutListRequest,
    ) -> dict:
        """
        调拨出库单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfout_list', request.body)

    def get_inv_tf_out_detail(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvTfOutDetailResponse:
        """
        调拨出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvTfOutDetailResponse(),
            self._kernel.post(f'/jdy/inv/inv_tfout_detail', request.body)
        )

    async def get_inv_tf_out_detail_async(
        self,
        request: kingdeejdy_scm_models.InvBillDetailRequest,
    ) -> kingdeejdy_scm_models.InvTfOutDetailResponse:
        """
        调拨出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.InvTfOutDetailResponse(),
            await self._kernel.post_async(f'/jdy/inv/inv_tfout_detail', request.body)
        )

    def get_inv_tf_diff_list(
        self,
        request: kingdeejdy_scm_models.InvTfDiffListRequest,
    ) -> dict:
        """
        调拨差异单列表
        """
        return self._kernel.post(f'/jdy/inv/inv_tfdiff_list', request.body)

    async def get_inv_tf_diff_list_async(
        self,
        request: kingdeejdy_scm_models.InvTfDiffListRequest,
    ) -> dict:
        """
        调拨差异单列表
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfdiff_list', request.body)

    def get_inv_tf_diff_push(
        self,
        request: kingdeejdy_scm_models.InvTfDiffPushRequest,
    ) -> dict:
        """
        调拨差异处理
        """
        return self._kernel.post(f'/jdy/inv/inv_tfdiff_push', request.body)

    async def get_inv_tf_diff_push_async(
        self,
        request: kingdeejdy_scm_models.InvTfDiffPushRequest,
    ) -> dict:
        """
        调拨差异处理
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_tfdiff_push', request.body)

    def get_ls_tf_out_deal_diff(
        self,
        request: kingdeejdy_scm_models.LsTfOutDealDiffRequest,
    ) -> dict:
        """
        零售调拨出库差异处理
        """
        return self._kernel.post(f'/jdy/inv/ls_tfout_deal_diff', request.body)

    async def get_ls_tf_out_deal_diff_async(
        self,
        request: kingdeejdy_scm_models.LsTfOutDealDiffRequest,
    ) -> dict:
        """
        零售调拨出库差异处理
        """
        return await self._kernel.post_async(f'/jdy/inv/ls_tfout_deal_diff', request.body)

    def get_inv_home_page_to_do_list(
        self,
        request: kingdeejdy_scm_models.InvHomePageToDoListRequest,
    ) -> dict:
        """
        查询销售助手首页采购单据待办数量
        """
        return self._kernel.post(f'/jdy/inv/inv_homepage_todolist', request.body)

    async def get_inv_home_page_to_do_list_async(
        self,
        request: kingdeejdy_scm_models.InvHomePageToDoListRequest,
    ) -> dict:
        """
        查询销售助手首页采购单据待办数量
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_homepage_todolist', request.body)

    def get_inv_detail_list(
        self,
        request: kingdeejdy_scm_models.InvDetailListRequest,
    ) -> dict:
        """
        商品收发明细表查询
        """
        return self._kernel.post(f'/jdy/inv/inv_detail_list', request.body)

    async def get_inv_detail_list_async(
        self,
        request: kingdeejdy_scm_models.InvDetailListRequest,
    ) -> dict:
        """
        商品收发明细表查询
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_detail_list', request.body)

    def get_inv_serial_status_list(
        self,
        request: kingdeejdy_scm_models.InvSerialStatusListRequest,
    ) -> dict:
        """
        序列号商品状态查询
        """
        return self._kernel.post(f'/jdy/inv/inv_serial_status_list', request.body)

    async def get_inv_serial_status_list_async(
        self,
        request: kingdeejdy_scm_models.InvSerialStatusListRequest,
    ) -> dict:
        """
        序列号商品状态查询
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_serial_status_list', request.body)

    def get_inv_batch_status_list(
        self,
        request: kingdeejdy_scm_models.InvBatchStatusListRequest,
    ) -> dict:
        """
        批次商品状态查询
        """
        return self._kernel.post(f'/jdy/inv/inv_batch_status_list', request.body)

    async def get_inv_batch_status_list_async(
        self,
        request: kingdeejdy_scm_models.InvBatchStatusListRequest,
    ) -> dict:
        """
        批次商品状态查询
        """
        return await self._kernel.post_async(f'/jdy/inv/inv_batch_status_list', request.body)

    def get_supplier_debit(
        self,
        request: kingdeejdy_scm_models.SupplierDebitRequest,
    ) -> dict:
        """
        查询客户上次的欠款和应收款余额
        """
        return self._kernel.post(f'/jdy/pur/pur_supplier_debt', request.body)

    async def get_supplier_debit_async(
        self,
        request: kingdeejdy_scm_models.SupplierDebitRequest,
    ) -> dict:
        """
        查询客户上次的欠款和应收款余额
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_supplier_debt', request.body)

    def get_material_purchase_price(
        self,
        request: kingdeejdy_scm_models.MaterialPurchasePriceRequest,
    ) -> dict:
        """
        查询商品的多种价格
        """
        return self._kernel.post(f'/jdy/pur/pur_all_price_list', request.body)

    async def get_material_purchase_price_async(
        self,
        request: kingdeejdy_scm_models.MaterialPurchasePriceRequest,
    ) -> dict:
        """
        查询商品的多种价格
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_all_price_list', request.body)

    def get_material_purchase_record(
        self,
        request: kingdeejdy_scm_models.MaterialPurchaseRecordRequest,
    ) -> dict:
        """
        查询商品采购记录
        """
        return self._kernel.post(f'/jdy/pur/pur_material_records', request.body)

    async def get_material_purchase_record_async(
        self,
        request: kingdeejdy_scm_models.MaterialPurchaseRecordRequest,
    ) -> dict:
        """
        查询商品采购记录
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_material_records', request.body)

    def get_pur_inbound_list(
        self,
        request: kingdeejdy_scm_models.PurInboundListRequest,
    ) -> dict:
        """
        采购入库单列表
        """
        return self._kernel.post(f'/jdy/pur/pur_inbound_list', request.body)

    async def get_pur_inbound_list_async(
        self,
        request: kingdeejdy_scm_models.PurInboundListRequest,
    ) -> dict:
        """
        采购入库单列表
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_inbound_list', request.body)

    def get_pur_inbound_detail(
        self,
        request: kingdeejdy_scm_models.PurInboundDetailRequest,
    ) -> kingdeejdy_scm_models.PurInboundDetailResponse:
        """
        采购入库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PurInboundDetailResponse(),
            self._kernel.post(f'/jdy/pur/pur_inbound_detail', request.body)
        )

    async def get_pur_inbound_detail_async(
        self,
        request: kingdeejdy_scm_models.PurInboundDetailRequest,
    ) -> kingdeejdy_scm_models.PurInboundDetailResponse:
        """
        采购入库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PurInboundDetailResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_inbound_detail', request.body)
        )

    def save_pur_inbound(
        self,
        request: kingdeejdy_scm_models.PurInboundSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购入库单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/pur/pur_inbound_save', request.body)
        )

    async def save_pur_inbound_async(
        self,
        request: kingdeejdy_scm_models.PurInboundSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购入库单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_inbound_save', request.body)
        )

    def get_supplier_debit_balance(
        self,
        request: kingdeejdy_scm_models.SupplierDebitBalanceRequest,
    ) -> dict:
        """
        查询采购可抵扣预付款余额
        """
        return self._kernel.post(f'/jdy/pur/sal_supplier_debt_balance', request.body)

    async def get_supplier_debit_balance_async(
        self,
        request: kingdeejdy_scm_models.SupplierDebitBalanceRequest,
    ) -> dict:
        """
        查询采购可抵扣预付款余额
        """
        return await self._kernel.post_async(f'/jdy/pur/sal_supplier_debt_balance', request.body)

    def get_request_order_list(
        self,
        request: kingdeejdy_scm_models.RequestOrderListRequest,
    ) -> dict:
        """
        采购申请单列表
        """
        return self._kernel.post(f'/jdy/pur/pur_request_list', request.body)

    async def get_request_order_list_async(
        self,
        request: kingdeejdy_scm_models.RequestOrderListRequest,
    ) -> dict:
        """
        采购申请单列表
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_request_list', request.body)

    def get_request_order_detail(
        self,
        request: kingdeejdy_scm_models.RequestOrderDetailRequest,
    ) -> kingdeejdy_scm_models.RequestOrderDetailResponse:
        """
        采购申请单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.RequestOrderDetailResponse(),
            self._kernel.post(f'/jdy/pur/pur_request_detail', request.body)
        )

    async def get_request_order_detail_async(
        self,
        request: kingdeejdy_scm_models.RequestOrderDetailRequest,
    ) -> kingdeejdy_scm_models.RequestOrderDetailResponse:
        """
        采购申请单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.RequestOrderDetailResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_request_detail', request.body)
        )

    def save_request_order(
        self,
        request: kingdeejdy_scm_models.RequestOrderRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购申请单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/pur/pur_request_save', request.body)
        )

    async def save_request_order_async(
        self,
        request: kingdeejdy_scm_models.RequestOrderRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购申请单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_request_save', request.body)
        )

    def purchase_operate(
        self,
        request: kingdeejdy_scm_models.PurchaseOperateRequest,
    ) -> dict:
        """
        采购类单据操作
        """
        return self._kernel.post(f'/jdy/pur/pur_operate', request.body)

    async def purchase_operate_async(
        self,
        request: kingdeejdy_scm_models.PurchaseOperateRequest,
    ) -> dict:
        """
        采购类单据操作
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_operate', request.body)

    def get_purchase_order_list(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderListRequest,
    ) -> dict:
        """
        采购订单列表
        """
        return self._kernel.post(f'/jdy/pur/pur_request_list', request.body)

    async def get_purchase_order_list_async(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderListRequest,
    ) -> dict:
        """
        采购订单列表
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_request_list', request.body)

    def get_purchase_order_detail(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderDetailRequest,
    ) -> kingdeejdy_scm_models.PurchaseOrderDetailResponse:
        """
        采购订单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PurchaseOrderDetailResponse(),
            self._kernel.post(f'/jdy/pur/pur_order_detail', request.body)
        )

    async def get_purchase_order_detail_async(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderDetailRequest,
    ) -> kingdeejdy_scm_models.PurchaseOrderDetailResponse:
        """
        采购订单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PurchaseOrderDetailResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_order_detail', request.body)
        )

    def save_purchase_order(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购订单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/pur/pur_order_save', request.body)
        )

    async def save_purchase_order_async(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购订单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_order_save', request.body)
        )

    def draw_purchase_order(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderDrawRequest,
    ) -> dict:
        """
        采购订单选择源单
        """
        return self._kernel.post(f'/jdy/pur/pur_order_draw', request.body)

    async def draw_purchase_order_async(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderDrawRequest,
    ) -> dict:
        """
        采购订单选择源单
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_order_draw', request.body)

    def get_purchase_return_list(
        self,
        request: kingdeejdy_scm_models.PurchaseReturnListRequest,
    ) -> dict:
        """
        采购退货单列表
        """
        return self._kernel.post(f'/jdy/pur/pur_rtn_list', request.body)

    async def get_purchase_return_list_async(
        self,
        request: kingdeejdy_scm_models.PurchaseReturnListRequest,
    ) -> dict:
        """
        采购退货单列表
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_rtn_list', request.body)

    def get_purchase_return_detail(
        self,
        request: kingdeejdy_scm_models.PurchaseReturnDetailRequest,
    ) -> kingdeejdy_scm_models.PurchaseReturnDetailResponse:
        """
        采购退货单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PurchaseReturnDetailResponse(),
            self._kernel.post(f'/jdy/pur/pur_rtn_detail', request.body)
        )

    async def get_purchase_return_detail_async(
        self,
        request: kingdeejdy_scm_models.PurchaseReturnDetailRequest,
    ) -> kingdeejdy_scm_models.PurchaseReturnDetailResponse:
        """
        采购退货单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.PurchaseReturnDetailResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_rtn_detail', request.body)
        )

    def save_purchase_return(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购退货单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/pur/pur_rtn_save', request.body)
        )

    async def save_purchase_return_async(
        self,
        request: kingdeejdy_scm_models.PurchaseOrderSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        采购退货单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/pur/pur_rtn_save', request.body)
        )

    def get_purchase_home_page_todo_list(
        self,
        request: kingdeejdy_scm_models.PurchaseHomePageTodoListRequest,
    ) -> dict:
        """
        查询销售助手首页采购单据待办数量
        """
        return self._kernel.post(f'/jdy/pur/pur_homepage_todolist', request.body)

    async def get_purchase_home_page_todo_list_async(
        self,
        request: kingdeejdy_scm_models.PurchaseHomePageTodoListRequest,
    ) -> dict:
        """
        查询销售助手首页采购单据待办数量
        """
        return await self._kernel.post_async(f'/jdy/pur/pur_homepage_todolist', request.body)

    def get_order_list(
        self,
        request: kingdeejdy_scm_models.OrderListRequest,
    ) -> dict:
        return self._kernel.post(f'/jdy/sal/sal_order_list', request.body)

    async def get_order_list_async(
        self,
        request: kingdeejdy_scm_models.OrderListRequest,
    ) -> dict:
        return await self._kernel.post_async(f'/jdy/sal/sal_order_list', request.body)

    def get_order_detail(
        self,
        request: kingdeejdy_scm_models.OrderDetailRequest,
    ) -> kingdeejdy_scm_models.OrderDetailResponse:
        return TeaCore.from_map(
            kingdeejdy_scm_models.OrderDetailResponse(),
            self._kernel.post(f'/jdy/sal/sal_order_detail', request.body)
        )

    async def get_order_detail_async(
        self,
        request: kingdeejdy_scm_models.OrderDetailRequest,
    ) -> kingdeejdy_scm_models.OrderDetailResponse:
        return TeaCore.from_map(
            kingdeejdy_scm_models.OrderDetailResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_order_detail', request.body)
        )

    def save_order(
        self,
        request: kingdeejdy_scm_models.OrderSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改一张销售订单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/sal/sal_order_save', request.body)
        )

    async def save_order_async(
        self,
        request: kingdeejdy_scm_models.OrderSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改一张销售订单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_order_save', request.body)
        )

    def lock_order(
        self,
        request: kingdeejdy_scm_models.OrderLockRequest,
    ) -> dict:
        """
        销售订单锁库
        """
        return self._kernel.post(f'/jdy/sal/sal_order_lock', request.body)

    async def lock_order_async(
        self,
        request: kingdeejdy_scm_models.OrderLockRequest,
    ) -> dict:
        """
        销售订单锁库
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_order_lock', request.body)

    def get_order_status(
        self,
        request: kingdeejdy_scm_models.GetOrderStatusRequest,
    ) -> dict:
        """
        查询销售订单状态
        """
        return self._kernel.post(f'/jdy/sal/sal_order_iostatus_list', request.body)

    async def get_order_status_async(
        self,
        request: kingdeejdy_scm_models.GetOrderStatusRequest,
    ) -> dict:
        """
        查询销售订单状态
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_order_iostatus_list', request.body)

    def get_outbound_list(
        self,
        request: kingdeejdy_scm_models.OutboundListRequest,
    ) -> dict:
        """
        获取销售出库单列表接口
        """
        return self._kernel.post(f'/jdy/sal/sal_outbound_list', request.body)

    async def get_outbound_list_async(
        self,
        request: kingdeejdy_scm_models.OutboundListRequest,
    ) -> dict:
        """
        获取销售出库单列表接口
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_outbound_list', request.body)

    def get_outbound_detail(
        self,
        request: kingdeejdy_scm_models.OutboundDetailRequest,
    ) -> kingdeejdy_scm_models.OutboundDetailResponse:
        """
        获取销售出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.OutboundDetailResponse(),
            self._kernel.post(f'/jdy/sal/sal_outbound_detail', request.body)
        )

    async def get_outbound_detail_async(
        self,
        request: kingdeejdy_scm_models.OutboundDetailRequest,
    ) -> kingdeejdy_scm_models.OutboundDetailResponse:
        """
        获取销售出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.OutboundDetailResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_outbound_detail', request.body)
        )

    def save_outbound(
        self,
        request: kingdeejdy_scm_models.OutboundSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或修改一张销售出库单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/sal/sal_outbound_save', request.body)
        )

    async def save_outbound_async(
        self,
        request: kingdeejdy_scm_models.OutboundSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或修改一张销售出库单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_outbound_save', request.body)
        )

    def get_sal_inbound_list(
        self,
        request: kingdeejdy_scm_models.SalInboundListRequest,
    ) -> dict:
        """
        获取销售退货单列表接口
        """
        return self._kernel.post(f'/jdy/sal/sal_inbound_list', request.body)

    async def get_sal_inbound_list_async(
        self,
        request: kingdeejdy_scm_models.SalInboundListRequest,
    ) -> dict:
        """
        获取销售退货单列表接口
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_inbound_list', request.body)

    def get_sal_inbound_detail(
        self,
        request: kingdeejdy_scm_models.SalInboundDetailRequest,
    ) -> kingdeejdy_scm_models.SalInboundDetailResponse:
        """
        获取销售出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SalInboundDetailResponse(),
            self._kernel.post(f'/jdy/sal/sal_outbound_detail', request.body)
        )

    async def get_sal_inbound_detail_async(
        self,
        request: kingdeejdy_scm_models.SalInboundDetailRequest,
    ) -> kingdeejdy_scm_models.SalInboundDetailResponse:
        """
        获取销售出库单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SalInboundDetailResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_outbound_detail', request.body)
        )

    def save_sal_inbound(
        self,
        request: kingdeejdy_scm_models.SalInboundSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改一张销售订单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/sal/sal_order_save', request.body)
        )

    async def save_sal_inbound_async(
        self,
        request: kingdeejdy_scm_models.SalInboundSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改一张销售订单
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_order_save', request.body)
        )

    def get_product_report_list(
        self,
        request: kingdeejdy_scm_models.ProductReportListRequest,
    ) -> dict:
        """
        获取本品上报单列表接口
        """
        return self._kernel.post(f'/jdy/sal/sal_product_report_list', request.body)

    async def get_product_report_list_async(
        self,
        request: kingdeejdy_scm_models.ProductReportListRequest,
    ) -> dict:
        """
        获取本品上报单列表接口
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_product_report_list', request.body)

    def get_product_report_detail(
        self,
        request: kingdeejdy_scm_models.ProductReportDetailRequest,
    ) -> kingdeejdy_scm_models.ProductReportDetailResponse:
        """
        获取本品上报详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ProductReportDetailResponse(),
            self._kernel.post(f'/jdy/sal/sal_product_report_detail', request.body)
        )

    async def get_product_report_detail_async(
        self,
        request: kingdeejdy_scm_models.ProductReportDetailRequest,
    ) -> kingdeejdy_scm_models.ProductReportDetailResponse:
        """
        获取本品上报详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ProductReportDetailResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_product_report_detail', request.body)
        )

    def save_product_report(
        self,
        request: kingdeejdy_scm_models.ProductReportSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改本品上报
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/sal/sal_product_report_save', request.body)
        )

    async def save_product_report_async(
        self,
        request: kingdeejdy_scm_models.ProductReportSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改本品上报
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_product_report_save', request.body)
        )

    def get_exchange_list(
        self,
        request: kingdeejdy_scm_models.ExchangeListRequest,
    ) -> dict:
        """
        获取销售换货单列表接口
        """
        return self._kernel.post(f'/jdy/sal/sal_exchange_request_list', request.body)

    async def get_exchange_list_async(
        self,
        request: kingdeejdy_scm_models.ExchangeListRequest,
    ) -> dict:
        """
        获取销售换货单列表接口
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_exchange_request_list', request.body)

    def get_exchange_detail(
        self,
        request: kingdeejdy_scm_models.ExchangeDetailRequest,
    ) -> kingdeejdy_scm_models.ExchangeDetailResponse:
        """
        获取销售换货申请单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ExchangeDetailResponse(),
            self._kernel.post(f'/jdy/sal/sal_exchange_request_detail', request.body)
        )

    async def get_exchange_detail_async(
        self,
        request: kingdeejdy_scm_models.ExchangeDetailRequest,
    ) -> kingdeejdy_scm_models.ExchangeDetailResponse:
        """
        获取销售换货申请单详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ExchangeDetailResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_exchange_request_detail', request.body)
        )

    def save_exchange(
        self,
        request: kingdeejdy_scm_models.ExchangeSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        销售换货申请单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/sal/sal_exchange_request_save', request.body)
        )

    async def save_exchange_async(
        self,
        request: kingdeejdy_scm_models.ExchangeSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        销售换货申请单保存
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_exchange_request_save', request.body)
        )

    def get_computing_report_list(
        self,
        request: kingdeejdy_scm_models.ComputingReportListRequest,
    ) -> dict:
        """
        获取本品上报单列表接口
        """
        return self._kernel.post(f'/jdy/sal/sal_competing_report_list', request.body)

    async def get_computing_report_list_async(
        self,
        request: kingdeejdy_scm_models.ComputingReportListRequest,
    ) -> dict:
        """
        获取本品上报单列表接口
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_competing_report_list', request.body)

    def get_computing_report_detail(
        self,
        request: kingdeejdy_scm_models.ComputingReportDetailRequest,
    ) -> kingdeejdy_scm_models.ComputingReportDetailResponse:
        """
        获取竞品上报详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ComputingReportDetailResponse(),
            self._kernel.post(f'/jdy/sal/sal_competing_report_detail', request.body)
        )

    async def get_computing_report_detail_async(
        self,
        request: kingdeejdy_scm_models.ComputingReportDetailRequest,
    ) -> kingdeejdy_scm_models.ComputingReportDetailResponse:
        """
        获取竞品上报详情
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.ComputingReportDetailResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_competing_report_detail', request.body)
        )

    def save_computing_report(
        self,
        request: kingdeejdy_scm_models.ComputingReportSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改本品上报
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            self._kernel.post(f'/jdy/sal/sal_competing_report_save', request.body)
        )

    async def save_computing_report_async(
        self,
        request: kingdeejdy_scm_models.ComputingReportSaveRequest,
    ) -> kingdeejdy_scm_models.SaveResponse:
        """
        新增或者修改本品上报
        """
        return TeaCore.from_map(
            kingdeejdy_scm_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/sal/sal_competing_report_save', request.body)
        )

    def get_rank(
        self,
        request: kingdeejdy_scm_models.RankRequest,
    ) -> dict:
        """
        排行榜
        """
        return self._kernel.post(f'/jdy/sal/sal_amount_rank', request.body)

    async def get_rank_async(
        self,
        request: kingdeejdy_scm_models.RankRequest,
    ) -> dict:
        """
        排行榜
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_amount_rank', request.body)

    def get_goal_order_list(
        self,
        request: kingdeejdy_scm_models.GoalOrderListRequest,
    ) -> dict:
        """
        最新销售订单列表
        """
        return self._kernel.post(f'/jdy/sal/sal_goal_order_list', request.body)

    async def get_goal_order_list_async(
        self,
        request: kingdeejdy_scm_models.GoalOrderListRequest,
    ) -> dict:
        """
        最新销售订单列表
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_goal_order_list', request.body)

    def get_goal_completion_rate_for_emp(
        self,
        request: kingdeejdy_scm_models.GoalCompletionRateRequest,
    ) -> dict:
        """
        查询部门销售金额和销售目标达成率
        """
        return self._kernel.post(f'/jdy/sal/sal_emp_amount_goal', request.body)

    async def get_goal_completion_rate_for_emp_async(
        self,
        request: kingdeejdy_scm_models.GoalCompletionRateRequest,
    ) -> dict:
        """
        查询部门销售金额和销售目标达成率
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_emp_amount_goal', request.body)

    def get_goal_completion_rate_for_all(
        self,
        request: kingdeejdy_scm_models.GoalCompletionRateRequest,
    ) -> dict:
        """
        查询整体销售金额和销售目标达成率
        """
        return self._kernel.post(f'/jdy/sal/sal_total_amount_goal', request.body)

    async def get_goal_completion_rate_for_all_async(
        self,
        request: kingdeejdy_scm_models.GoalCompletionRateRequest,
    ) -> dict:
        """
        查询整体销售金额和销售目标达成率
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_total_amount_goal', request.body)

    def get_goal_completion_rate_for_dept(
        self,
        request: kingdeejdy_scm_models.GoalCompletionRateRequest,
    ) -> dict:
        """
        查询部门销售金额和销售目标达成率
        """
        return self._kernel.post(f'/jdy/sal/sal_dept_amount_goal', request.body)

    async def get_goal_completion_rate_for_dept_async(
        self,
        request: kingdeejdy_scm_models.GoalCompletionRateRequest,
    ) -> dict:
        """
        查询部门销售金额和销售目标达成率
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_dept_amount_goal', request.body)

    def get_material_sale_record(
        self,
        request: kingdeejdy_scm_models.MaterialSaleRecordRequest,
    ) -> dict:
        """
        查询商品销售记录
        """
        return self._kernel.post(f'/jdy/sal/sal_material_records', request.body)

    async def get_material_sale_record_async(
        self,
        request: kingdeejdy_scm_models.MaterialSaleRecordRequest,
    ) -> dict:
        """
        查询商品销售记录
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_material_records', request.body)

    def delivery_operate(
        self,
        request: kingdeejdy_scm_models.DeliveryOperateRequest,
    ) -> dict:
        """
        配送/取消配送操作
        """
        return self._kernel.post(f'/jdy/sal/delivery_operate', request.body)

    async def delivery_operate_async(
        self,
        request: kingdeejdy_scm_models.DeliveryOperateRequest,
    ) -> dict:
        """
        配送/取消配送操作
        """
        return await self._kernel.post_async(f'/jdy/sal/delivery_operate', request.body)

    def get_customer_debit_balance(
        self,
        request: kingdeejdy_scm_models.CustomerDebitBalanceRequest,
    ) -> dict:
        """
        查询客户可抵扣预收款余额
        """
        return self._kernel.post(f'/jdy/sal/sal_customer_debt_balance', request.body)

    async def get_customer_debit_balance_async(
        self,
        request: kingdeejdy_scm_models.CustomerDebitBalanceRequest,
    ) -> dict:
        """
        查询客户可抵扣预收款余额
        """
        return await self._kernel.post_async(f'/jdy/sal/sal_customer_debt_balance', request.body)
