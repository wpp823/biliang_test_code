# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from business.basedata.kingdeejdy_basedata import models as kingdeejdy_basedata_models
from kingdeejdy_kernel.kingdeejdy_kernel import KingdeejdyKernel


class KingdeejdyBasedata:
    _kernel: KingdeejdyKernel = None

    def __init__(
            self,
            kernel: KingdeejdyKernel,
    ):
        self._kernel = kernel

    def get_supplier_group_list(self,request: kingdeejdy_basedata_models.SupplierGroupListRequest,) -> kingdeejdy_basedata_models.SupplierGroupListResponse:
        """
        供应商分类列表
        """
        return TeaCore.from_map( kingdeejdy_basedata_models.SupplierGroupListResponse(),self._kernel.post(f'/jdy/basedata/supplier_group_list', request.body))

    async def get_supplier_group_list_async(
            self,
            request: kingdeejdy_basedata_models.SupplierGroupListRequest,
    ) -> kingdeejdy_basedata_models.SupplierGroupListResponse:
        """
        供应商分类列表
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SupplierGroupListResponse(),
            await self._kernel.post_async(f'/jdy/basedata/supplier_group_list', request.body)
        )

    def save_supplier_group(
            self,
            request: kingdeejdy_basedata_models.SupplierGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存供应商分类
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/supplier_group_save', request.body)
        )

    async def save_supplier_group_async(
            self,
            request: kingdeejdy_basedata_models.SupplierGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存供应商分类
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/supplier_group_save', request.body)
        )

    def ge_supplier_list(
            self,
            request: kingdeejdy_basedata_models.SupplierListRequest,
    ) -> dict:
        """
        供应商列表
        """
        return self._kernel.post(f'/jdy/basedata/supplier_list', request.body)

    async def ge_supplier_list_async(
            self,
            request: kingdeejdy_basedata_models.SupplierListRequest,
    ) -> dict:
        """
        供应商列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/supplier_list', request.body)

    def get_supplier_detail(
            self,
            request: kingdeejdy_basedata_models.SupplierDetailRequest,
    ) -> kingdeejdy_basedata_models.SupplierDetailResponse:
        """
        供应商详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SupplierDetailResponse(),
            self._kernel.post(f'/jdy/basedata/supplier_detail', request.body)
        )

    async def get_supplier_detail_async(
            self,
            request: kingdeejdy_basedata_models.SupplierDetailRequest,
    ) -> kingdeejdy_basedata_models.SupplierDetailResponse:
        """
        供应商详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SupplierDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/supplier_detail', request.body)
        )

    def get_supplier_detail_batch(
            self,
            request: kingdeejdy_basedata_models.SupplierDetailBatchRequest,
    ) -> dict:
        """
        批量查询供应商详情
        """
        return self._kernel.post(f'/jdy/basedata/supplier_detail_batch', request.body)

    async def get_supplier_detail_batch_async(
            self,
            request: kingdeejdy_basedata_models.SupplierDetailBatchRequest,
    ) -> dict:
        """
        批量查询供应商详情
        """
        return await self._kernel.post_async(f'/jdy/basedata/supplier_detail_batch', request.body)

    def save_supplier(
            self,
            request: kingdeejdy_basedata_models.SupplierSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存供应商
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/supplier_save', request.body)
        )

    async def save_supplier_async(
            self,
            request: kingdeejdy_basedata_models.SupplierSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存供应商
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/supplier_save', request.body)
        )

    def save_supplier_batch(
            self,
            request: kingdeejdy_basedata_models.SaveSupplierBatchRequest,
    ) -> dict:
        """
        供应商批量保存
        """
        return self._kernel.post(f'/jdy/basedata/supplier_batch_save', request.body)

    async def save_supplier_batch_async(
            self,
            request: kingdeejdy_basedata_models.SaveSupplierBatchRequest,
    ) -> dict:
        """
        供应商批量保存
        """
        return await self._kernel.post_async(f'/jdy/basedata/supplier_batch_save', request.body)

    def get_customer_group_list(
            self,
            request: kingdeejdy_basedata_models.CustomerGroupListRequest,
    ) -> kingdeejdy_basedata_models.CustomerGroupListResponse:
        """
        查询客户类别列表
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.CustomerGroupListResponse(),
            self._kernel.post(f'/jdy/basedata/customer_group_list', request.body)
        )

    async def get_customer_group_list_async(
            self,
            request: kingdeejdy_basedata_models.CustomerGroupListRequest,
    ) -> kingdeejdy_basedata_models.CustomerGroupListResponse:
        """
        查询客户类别列表
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.CustomerGroupListResponse(),
            await self._kernel.post_async(f'/jdy/basedata/customer_group_list', request.body)
        )

    def save_customer_group(
            self,
            request: kingdeejdy_basedata_models.CustomerGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存客户类别
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/customer_group_save', request.body)
        )

    async def save_customer_group_async(
            self,
            request: kingdeejdy_basedata_models.CustomerGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存客户类别
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/customer_group_save', request.body)
        )

    def get_customer_list(
            self,
            request: kingdeejdy_basedata_models.CustomerListRequest,
    ) -> dict:
        """
        查询客户列表
        """
        return self._kernel.post(f'/jdy/basedata/customer_list', request.body)

    async def get_customer_list_async(
            self,
            request: kingdeejdy_basedata_models.CustomerListRequest,
    ) -> dict:
        """
        查询客户列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/customer_list', request.body)

    def get_customer_detail(
            self,
            request: kingdeejdy_basedata_models.CustomerDetailRequest,
    ) -> kingdeejdy_basedata_models.CustomerDetailResponse:
        """
        查询客户详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.CustomerDetailResponse(),
            self._kernel.post(f'/jdy/basedata/customer_detail', request.body)
        )

    async def get_customer_detail_async(
            self,
            request: kingdeejdy_basedata_models.CustomerDetailRequest,
    ) -> kingdeejdy_basedata_models.CustomerDetailResponse:
        """
        查询客户详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.CustomerDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/customer_detail', request.body)
        )

    def get_customer_detail_batch(
            self,
            request: kingdeejdy_basedata_models.CustomerDetailBatchRequest,
    ) -> dict:
        """
        批量查询客户详情
        """
        return self._kernel.post(f'/jdy/basedata/customer_detail_batch', request.body)

    async def get_customer_detail_batch_async(
            self,
            request: kingdeejdy_basedata_models.CustomerDetailBatchRequest,
    ) -> dict:
        """
        批量查询客户详情
        """
        return await self._kernel.post_async(f'/jdy/basedata/customer_detail_batch', request.body)

    def save_customer(
            self,
            request: kingdeejdy_basedata_models.CustomerSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        客户保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/customer_save', request.body)
        )

    async def save_customer_async(
            self,
            request: kingdeejdy_basedata_models.CustomerSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        客户保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/customer_save', request.body)
        )

    def save_customer_batch(
            self,
            request: kingdeejdy_basedata_models.CustomerBatchSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        客户批量保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/customer_batch_save', request.body)
        )

    async def save_customer_batch_async(
            self,
            request: kingdeejdy_basedata_models.CustomerBatchSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        客户批量保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/customer_batch_save', request.body)
        )

    def get_department_list(
            self,
            request: kingdeejdy_basedata_models.DepartmentListRequest,
    ) -> dict:
        """
        查询部门列表
        """
        return self._kernel.post(f'/jdy/basedata/dept_list', request.body)

    async def get_department_list_async(
            self,
            request: kingdeejdy_basedata_models.DepartmentListRequest,
    ) -> dict:
        """
        查询部门列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/dept_list', request.body)

    def get_department_detail(
            self,
            request: kingdeejdy_basedata_models.DepartmentDetailRequest,
    ) -> kingdeejdy_basedata_models.DepartmentDetailResponse:
        """
        查询部门详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.DepartmentDetailResponse(),
            self._kernel.post(f'/jdy/basedata/dept_detail', request.body)
        )

    async def get_department_detail_async(
            self,
            request: kingdeejdy_basedata_models.DepartmentDetailRequest,
    ) -> kingdeejdy_basedata_models.DepartmentDetailResponse:
        """
        查询部门详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.DepartmentDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/dept_detail', request.body)
        )

    def save_department(
            self,
            request: kingdeejdy_basedata_models.DepartmentSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存部门
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/dept_save', request.body)
        )

    async def save_department_async(
            self,
            request: kingdeejdy_basedata_models.DepartmentSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存部门
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/dept_save', request.body)
        )

    def get_employee_list(
            self,
            request: kingdeejdy_basedata_models.EmployeeListRequest,
    ) -> dict:
        """
        查询职员列表
        """
        return self._kernel.post(f'/jdy/basedata/emp_list', request.body)

    async def get_employee_list_async(
            self,
            request: kingdeejdy_basedata_models.EmployeeListRequest,
    ) -> dict:
        """
        查询职员列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/emp_list', request.body)

    def get_employee_detail(
            self,
            request: kingdeejdy_basedata_models.EmployeeDetailRequest,
    ) -> kingdeejdy_basedata_models.EmployeeDetailResponse:
        """
        查询职员详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.EmployeeDetailResponse(),
            self._kernel.post(f'/jdy/basedata/emp_detail', request.body)
        )

    async def get_employee_detail_async(
            self,
            request: kingdeejdy_basedata_models.EmployeeDetailRequest,
    ) -> kingdeejdy_basedata_models.EmployeeDetailResponse:
        """
        查询职员详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.EmployeeDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/emp_detail', request.body)
        )

    def save_employee(
            self,
            request: kingdeejdy_basedata_models.EmployeeSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存职员
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/emp_save', request.body)
        )

    async def save_employee_async(
            self,
            request: kingdeejdy_basedata_models.EmployeeSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存职员
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/emp_save', request.body)
        )

    def ge_settling_termt_list(
            self,
            request: kingdeejdy_basedata_models.SettlingTermListRequest,
    ) -> dict:
        """
        结算期限列表
        """
        return self._kernel.post(f'/jdy/basedata/settlingterm_list', request.body)

    async def ge_settling_termt_list_async(
            self,
            request: kingdeejdy_basedata_models.SettlingTermListRequest,
    ) -> dict:
        """
        结算期限列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/settlingterm_list', request.body)

    def get_settling_term_detail(
            self,
            request: kingdeejdy_basedata_models.SettlingTermDetailRequest,
    ) -> kingdeejdy_basedata_models.SettlingTermDetailResponse:
        """
        结算期限详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SettlingTermDetailResponse(),
            self._kernel.post(f'/jdy/basedata/settlingterm_detail', request.body)
        )

    async def get_settling_term_detail_async(
            self,
            request: kingdeejdy_basedata_models.SettlingTermDetailRequest,
    ) -> kingdeejdy_basedata_models.SettlingTermDetailResponse:
        """
        结算期限详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SettlingTermDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/settlingterm_detail', request.body)
        )

    def save_settling_term(
            self,
            request: kingdeejdy_basedata_models.SettlingTermSaveRequest,
    ) -> dict:
        return self._kernel.post(f'/jdy/basedata/settlingterm_save', request.body)

    async def save_settling_term_async(
            self,
            request: kingdeejdy_basedata_models.SettlingTermSaveRequest,
    ) -> dict:
        return await self._kernel.post_async(f'/jdy/basedata/settlingterm_save', request.body)

    def ge_settlement_list(
            self,
            request: kingdeejdy_basedata_models.SettlementListRequest,
    ) -> dict:
        """
        结算方式列表
        """
        return self._kernel.post(f'/jdy/basedata/settlement_type_list', request.body)

    async def ge_settlement_list_async(
            self,
            request: kingdeejdy_basedata_models.SettlementListRequest,
    ) -> dict:
        """
        结算方式列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/settlement_type_list', request.body)

    def save_settlement(
            self,
            request: kingdeejdy_basedata_models.SettlementSaveRequest,
    ) -> dict:
        """
        保存结算方式
        """
        return self._kernel.post(f'/jdy/basedata/settlement_type_save', request.body)

    async def save_settlement_async(
            self,
            request: kingdeejdy_basedata_models.SettlementSaveRequest,
    ) -> dict:
        """
        保存结算方式
        """
        return await self._kernel.post_async(f'/jdy/basedata/settlement_type_save', request.body)

    def get_stock_group_list(
            self,
            request: kingdeejdy_basedata_models.StockGroupListRequest,
    ) -> dict:
        """
        仓库分类列表
        """
        return self._kernel.post(f'/jdy/basedata/store_group_list', request.body)

    async def get_stock_group_list_async(
            self,
            request: kingdeejdy_basedata_models.StockGroupListRequest,
    ) -> dict:
        """
        仓库分类列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/store_group_list', request.body)

    def get_stock_group_detail(
            self,
            request: kingdeejdy_basedata_models.StockGroupDetailRequest,
    ) -> dict:
        """
        查询仓库分类详情
        """
        return self._kernel.post(f'/jdy/basedata/store_group_detail', request.body)

    async def get_stock_group_detail_async(
            self,
            request: kingdeejdy_basedata_models.StockGroupDetailRequest,
    ) -> dict:
        """
        查询仓库分类详情
        """
        return await self._kernel.post_async(f'/jdy/basedata/store_group_detail', request.body)

    def get_stock_list(
            self,
            request: kingdeejdy_basedata_models.StockListRequest,
    ) -> dict:
        """
        仓库列表
        """
        return self._kernel.post(f'/jdy/basedata/store_list', request.body)

    async def get_stock_list_async(
            self,
            request: kingdeejdy_basedata_models.StockListRequest,
    ) -> dict:
        """
        仓库列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/store_list', request.body)

    def get_stock_detail(
            self,
            request: kingdeejdy_basedata_models.StockDetailRequest,
    ) -> kingdeejdy_basedata_models.StockDetailResponse:
        """
        查询仓库详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.StockDetailResponse(),
            self._kernel.post(f'/jdy/basedata/store_detail', request.body)
        )

    async def get_stock_detail_async(
            self,
            request: kingdeejdy_basedata_models.StockDetailRequest,
    ) -> kingdeejdy_basedata_models.StockDetailResponse:
        """
        查询仓库详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.StockDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/store_detail', request.body)
        )

    def save_stock(
            self,
            request: kingdeejdy_basedata_models.StockSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存仓库
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/store_save', request.body)
        )

    async def save_stock_async(
            self,
            request: kingdeejdy_basedata_models.StockSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存仓库
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/store_save', request.body)
        )

    def get_stock_space_list(
            self,
            request: kingdeejdy_basedata_models.StockSpaceListRequest,
    ) -> dict:
        """
        仓位列表
        """
        return self._kernel.post(f'/jdy/basedata/space_list', request.body)

    async def get_stock_space_list_async(
            self,
            request: kingdeejdy_basedata_models.StockSpaceListRequest,
    ) -> dict:
        """
        仓位列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/space_list', request.body)

    def save_stock_group(
            self,
            request: kingdeejdy_basedata_models.StockGroupSaveRequest,
    ) -> dict:
        """
        保存仓库分类
        """
        return self._kernel.post(f'/jdy/basedata/store_group_save', request.body)

    async def save_stock_group_async(
            self,
            request: kingdeejdy_basedata_models.StockGroupSaveRequest,
    ) -> dict:
        """
        保存仓库分类
        """
        return await self._kernel.post_async(f'/jdy/basedata/store_group_save', request.body)

    def get_measure_unit_list(
            self,
            request: kingdeejdy_basedata_models.MeasureUnitListRequest,
    ) -> dict:
        """
        计量单位列表
        """
        return self._kernel.post(f'/jdy/basedata/measure_unit_list', request.body)

    async def get_measure_unit_list_async(
            self,
            request: kingdeejdy_basedata_models.MeasureUnitListRequest,
    ) -> dict:
        """
        计量单位列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/measure_unit_list', request.body)

    def get_measure_unit_detail(
            self,
            request: kingdeejdy_basedata_models.MeasureUnitDetailRequest,
    ) -> kingdeejdy_basedata_models.MeasureUnitDetailResponse:
        """
        计量单位详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.MeasureUnitDetailResponse(),
            self._kernel.post(f'/jdy/basedata/measure_unit_detail', request.body)
        )

    async def get_measure_unit_detail_async(
            self,
            request: kingdeejdy_basedata_models.MeasureUnitDetailRequest,
    ) -> kingdeejdy_basedata_models.MeasureUnitDetailResponse:
        """
        计量单位详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.MeasureUnitDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/measure_unit_detail', request.body)
        )

    def save_measure_unit(
            self,
            request: kingdeejdy_basedata_models.MeasureUnitSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存计量单位
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/measure_unit_save', request.body)
        )

    async def save_measure_unit_async(
            self,
            request: kingdeejdy_basedata_models.MeasureUnitSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存计量单位
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/measure_unit_save', request.body)
        )

    def get_material_measure_unit_list(
            self,
            request: kingdeejdy_basedata_models.MaterialMeasureUnitListRequest,
    ) -> dict:
        """
        商品单位列表
        """
        return self._kernel.post(f'/jdy/basedata/material_unit_list', request.body)

    async def get_material_measure_unit_list_async(
            self,
            request: kingdeejdy_basedata_models.MaterialMeasureUnitListRequest,
    ) -> dict:
        """
        商品单位列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_unit_list', request.body)

    def get_material_measure_unit_detail(
            self,
            request: kingdeejdy_basedata_models.MaterialMeasureUnitDetailRequest,
    ) -> dict:
        """
        商品单位详情
        """
        return self._kernel.post(f'/jdy/basedata/material_unit_detail', request.body)

    async def get_material_measure_unit_detail_async(
            self,
            request: kingdeejdy_basedata_models.MaterialMeasureUnitDetailRequest,
    ) -> dict:
        """
        商品单位详情
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_unit_detail', request.body)

    def get_currency_list(
            self,
            request: kingdeejdy_basedata_models.CurrencyListRequest,
    ) -> dict:
        """
        币别列表
        """
        return self._kernel.post(f'/jdy/basedata/currency_list', request.body)

    async def get_currency_list_async(
            self,
            request: kingdeejdy_basedata_models.CurrencyListRequest,
    ) -> dict:
        """
        币别列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/currency_list', request.body)

    def get_currency_detail(
            self,
            request: kingdeejdy_basedata_models.CurrencyDetailRequest,
    ) -> kingdeejdy_basedata_models.CurrencyDetailResponse:
        """
        币别详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.CurrencyDetailResponse(),
            self._kernel.post(f'/jdy/basedata/currency_detail', request.body)
        )

    async def get_currency_detail_async(
            self,
            request: kingdeejdy_basedata_models.CurrencyDetailRequest,
    ) -> kingdeejdy_basedata_models.CurrencyDetailResponse:
        """
        币别详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.CurrencyDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/currency_detail', request.body)
        )

    def save_currency(
            self,
            request: kingdeejdy_basedata_models.CurrencySaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        币别详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/currency_save', request.body)
        )

    async def save_currency_async(
            self,
            request: kingdeejdy_basedata_models.CurrencySaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        币别详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/currency_save', request.body)
        )

    def get_attribute_group_list(
            self,
            request: kingdeejdy_basedata_models.AttributeGroupListRequest,
    ) -> dict:
        """
        查询辅助属性分类列表
        """
        return self._kernel.post(f'/jdy/basedata/auxtype_list', request.body)

    async def get_attribute_group_list_async(
            self,
            request: kingdeejdy_basedata_models.AttributeGroupListRequest,
    ) -> dict:
        """
        查询辅助属性分类列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/auxtype_list', request.body)

    def save_attribute_group(
            self,
            request: kingdeejdy_basedata_models.AttributeGroupSaveRequest,
    ) -> dict:
        """
        保存辅助属性分类
        """
        return self._kernel.post(f'/jdy/basedata/auxtype_save', request.body)

    async def save_attribute_group_async(
            self,
            request: kingdeejdy_basedata_models.AttributeGroupSaveRequest,
    ) -> dict:
        """
        保存辅助属性分类
        """
        return await self._kernel.post_async(f'/jdy/basedata/auxtype_save', request.body)

    def get_attribute_list(
            self,
            request: kingdeejdy_basedata_models.AttributeListRequest,
    ) -> dict:
        """
        查询辅助属性列表
        """
        return self._kernel.post(f'/jdy/basedata/auxdetail_list', request.body)

    async def get_attribute_list_async(
            self,
            request: kingdeejdy_basedata_models.AttributeListRequest,
    ) -> dict:
        """
        查询辅助属性列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/auxdetail_list', request.body)

    def get_attribute_detail(
            self,
            request: kingdeejdy_basedata_models.AttributeDetailRequest,
    ) -> kingdeejdy_basedata_models.AttributeDetailResponse:
        """
        辅助属性详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.AttributeDetailResponse(),
            self._kernel.post(f'/jdy/basedata/auxdetail_detail', request.body)
        )

    async def get_attribute_detail_async(
            self,
            request: kingdeejdy_basedata_models.AttributeDetailRequest,
    ) -> kingdeejdy_basedata_models.AttributeDetailResponse:
        """
        辅助属性详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.AttributeDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/auxdetail_detail', request.body)
        )

    def save_attribute(
            self,
            request: kingdeejdy_basedata_models.AttributeSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存辅助属性
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/auxdetail_save', request.body)
        )

    async def save_attribute_async(
            self,
            request: kingdeejdy_basedata_models.AttributeSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存辅助属性
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/auxdetail_save', request.body)
        )

    def get_aux_group_list(
            self,
            request: kingdeejdy_basedata_models.AuxGroupListRequest,
    ) -> dict:
        """
        查询辅助资料分类列表
        """
        return self._kernel.post(f'/jdy/basedata/auxinfotype_list', request.body)

    async def get_aux_group_list_async(
            self,
            request: kingdeejdy_basedata_models.AuxGroupListRequest,
    ) -> dict:
        """
        查询辅助资料分类列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/auxinfotype_list', request.body)

    def get_aux_group_detail(
            self,
            request: kingdeejdy_basedata_models.AuxGroupDetailRequest,
    ) -> dict:
        """
        查询辅助资料分类
        """
        return self._kernel.post(f'/jdy/basedata/auxtype_detail', request.body)

    async def get_aux_group_detail_async(
            self,
            request: kingdeejdy_basedata_models.AuxGroupDetailRequest,
    ) -> dict:
        """
        查询辅助资料分类
        """
        return await self._kernel.post_async(f'/jdy/basedata/auxtype_detail', request.body)

    def save_aux_group(
            self,
            request: kingdeejdy_basedata_models.AuxGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存辅助资料分类
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/auxinfotype_save', request.body)
        )

    async def save_aux_group_async(
            self,
            request: kingdeejdy_basedata_models.AuxGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存辅助资料分类
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/auxinfotype_save', request.body)
        )

    def get_aux_list(
            self,
            request: kingdeejdy_basedata_models.AuxListRequest,
    ) -> dict:
        """
        查询辅助资料列表
        """
        return self._kernel.post(f'/jdy/basedata/auxinfo_list', request.body)

    async def get_aux_list_async(
            self,
            request: kingdeejdy_basedata_models.AuxListRequest,
    ) -> dict:
        """
        查询辅助资料列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/auxinfo_list', request.body)

    def get_aux_detail(
            self,
            request: kingdeejdy_basedata_models.AuxDetailRequest,
    ) -> kingdeejdy_basedata_models.AuxDetailResponse:
        """
        辅助资料详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.AuxDetailResponse(),
            self._kernel.post(f'/jdy/basedata/auxinfo_detail', request.body)
        )

    async def get_aux_detail_async(
            self,
            request: kingdeejdy_basedata_models.AuxDetailRequest,
    ) -> kingdeejdy_basedata_models.AuxDetailResponse:
        """
        辅助资料详情
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.AuxDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/auxinfo_detail', request.body)
        )

    def save_aux(
            self,
            request: kingdeejdy_basedata_models.AuxSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存辅助资料
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/auxinfo_save', request.body)
        )

    async def save_aux_async(
            self,
            request: kingdeejdy_basedata_models.AuxSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存辅助资料
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/auxinfo_save', request.body)
        )

    def get_brand_list(
            self,
            request: kingdeejdy_basedata_models.BrandListRequest,
    ) -> dict:
        """
        商品品牌列表
        """
        return self._kernel.post(f'/jdy/basedata/material_brand_list', request)

    async def get_brand_list_async(
            self,
            request: kingdeejdy_basedata_models.BrandListRequest,
    ) -> dict:
        """
        商品品牌列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_brand_list', request)

    def save_brand(
            self,
            request: kingdeejdy_basedata_models.BrandSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存商品品牌
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/material_brand_save', request)
        )

    async def save_brand_async(
            self,
            request: kingdeejdy_basedata_models.BrandSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存商品品牌
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/material_brand_save', request)
        )

    def get_material_group_list(
            self,
            request: kingdeejdy_basedata_models.MaterialGroupListRequest,
    ) -> dict:
        """
        商品类别列表
        """
        return self._kernel.post(f'/jdy/basedata/material_group_list', request)

    async def get_material_group_list_async(
            self,
            request: kingdeejdy_basedata_models.MaterialGroupListRequest,
    ) -> dict:
        """
        商品类别列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_group_list', request)

    def save_material_group(
            self,
            request: kingdeejdy_basedata_models.MaterialGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        商品类别保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/material_group_save', request)
        )

    async def save_material_group_async(
            self,
            request: kingdeejdy_basedata_models.MaterialGroupSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        商品类别保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/material_group_save', request)
        )

    def get_label_list(
            self,
            request: kingdeejdy_basedata_models.LabelListRequest,
    ) -> dict:
        """
        商品标签列表
        """
        return self._kernel.post(f'/jdy/basedata/material_label_list', request)

    async def get_label_list_async(
            self,
            request: kingdeejdy_basedata_models.LabelListRequest,
    ) -> dict:
        """
        商品标签列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_label_list', request)

    def save_label(
            self,
            request: kingdeejdy_basedata_models.LabelSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存商品标签
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/material_label_save', request)
        )

    async def save_label_async(
            self,
            request: kingdeejdy_basedata_models.LabelSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        保存商品标签
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/material_label_save', request)
        )

    def get_material_list(
            self,
            request: kingdeejdy_basedata_models.MaterialListRequest,
    ) -> dict:
        """
        开单的商品列表
        """
        return self._kernel.post(f'/jdy/basedata/material_list', request)

    async def get_material_list_async(
            self,
            request: kingdeejdy_basedata_models.MaterialListRequest,
    ) -> dict:
        """
        开单的商品列表
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_list', request)

    def get_material_detail(
            self,
            request: kingdeejdy_basedata_models.MaterialDetailRequest,
    ) -> kingdeejdy_basedata_models.MaterialDetailResponse:
        """
        获取商品基础资料详情接口
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.MaterialDetailResponse(),
            self._kernel.post(f'/jdy/basedata/material_detail', request)
        )

    async def get_material_detail_async(
            self,
            request: kingdeejdy_basedata_models.MaterialDetailRequest,
    ) -> kingdeejdy_basedata_models.MaterialDetailResponse:
        """
        获取商品基础资料详情接口
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.MaterialDetailResponse(),
            await self._kernel.post_async(f'/jdy/basedata/material_detail', request)
        )

    def save_material(
            self,
            request: kingdeejdy_basedata_models.MaterialSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        商品保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            self._kernel.post(f'/jdy/basedata/material_save', request)
        )

    async def save_material_async(
            self,
            request: kingdeejdy_basedata_models.MaterialSaveRequest,
    ) -> kingdeejdy_basedata_models.SaveResponse:
        """
        商品保存
        """
        return TeaCore.from_map(
            kingdeejdy_basedata_models.SaveResponse(),
            await self._kernel.post_async(f'/jdy/basedata/material_save', request)
        )

    def update_image(
            self,
            request: kingdeejdy_basedata_models.ImageUploadRequest,
    ) -> dict:
        """
        商品图片上传
        """
        return self._kernel.post(f'/jdy/basedata/image_upload', request)

    async def update_image_async(
            self,
            request: kingdeejdy_basedata_models.ImageUploadRequest,
    ) -> dict:
        """
        商品图片上传
        """
        return await self._kernel.post_async(f'/jdy/basedata/image_upload', request)

    def delete_image(
            self,
            request: kingdeejdy_basedata_models.ImageDeleteRequest,
    ) -> dict:
        """
        商品图片删除
        """
        return self._kernel.post(f'/jdy/basedata/image_delete', request)

    async def delete_image_async(
            self,
            request: kingdeejdy_basedata_models.ImageDeleteRequest,
    ) -> dict:
        """
        商品图片删除
        """
        return await self._kernel.post_async(f'/jdy/basedata/image_delete', request)

    def get_customer_material_price(
            self,
            request: kingdeejdy_basedata_models.CustomerMaterialPriceRequest,
    ) -> dict:
        """
        商品价格资料
        """
        return self._kernel.post(f'/jdy/basedata/customer_material_price_list', request)

    async def get_customer_material_price_async(
            self,
            request: kingdeejdy_basedata_models.CustomerMaterialPriceRequest,
    ) -> dict:
        """
        商品价格资料
        """
        return await self._kernel.post_async(f'/jdy/basedata/customer_material_price_list', request)

    def get_material_detail_batch(
            self,
            request: kingdeejdy_basedata_models.MaterialDetailBatchRequest,
    ) -> dict:
        """
        批量获取商品详情
        """
        return self._kernel.post(f'/jdy/basedata/material_detail_batch', request)

    async def get_material_detail_batch_async(
            self,
            request: kingdeejdy_basedata_models.MaterialDetailBatchRequest,
    ) -> dict:
        """
        批量获取商品详情
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_detail_batch', request)

    def material_batch_save(
            self,
            request: kingdeejdy_basedata_models.MaterialBatchSaveRequest,
    ) -> dict:
        """
        商品批量保存
        """
        return self._kernel.post(f'/jdy/basedata/material_batch_save', request)

    async def material_batch_save_async(
            self,
            request: kingdeejdy_basedata_models.MaterialBatchSaveRequest,
    ) -> dict:
        """
        商品批量保存
        """
        return await self._kernel.post_async(f'/jdy/basedata/material_batch_save', request)
