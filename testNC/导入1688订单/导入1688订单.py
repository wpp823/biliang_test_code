import os

import xlrd3


class ExcelUtils():
    def __init__(self, excel_file_path, sheet_name):  # 设置动态读取的地址和表单名
        self.excel_file_path = excel_file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        ''' 根据文件路径及表格名称获取表格对象 '''
        wook_book = xlrd3.open_workbook(self.excel_file_path,formatting_info=True)
        sheet = wook_book.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        ''' 获取表格的行数 '''
        row_count = self.sheet.nrows
        return row_count

    def get_coulumn_count(self):
        '''获取表格列数'''
        column_count = self.sheet.ncols
        return column_count

    def ger_merge_cell_value(self, row_index, col_index):
        '''获取Excel单元格的数据（包含合并单元格）'''
        cell_value = None
        for (min_row, max_row, min_col, max_col) in self.sheet.merged_cells:
            if min_row <= row_index < max_row:
                if min_col <= col_index < max_col:
                    cell_value = self.sheet.cell_value(min_row, min_col)  # 合并单元格的值等于合并第一个单元格的值
                    break
                else:
                    cell_value = self.sheet.cell_value(row_index, col_index)
            else:
                cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_all_data(self):
        ''' 把excel数据转换成如下格式
                [{"字段名1":"字段值1","字段名2":"字段值2"...},{}]'''
        excel_data_list = []
        row_head = self.sheet.row_values(0, 0)
        for row_num in range(1, self.get_row_count()):
            row_dict = {}
            for col_num in range(self.get_coulumn_count()):
                row_dict[row_head[col_num]] = self.ger_merge_cell_value(row_num, col_num)
            excel_data_list.append(row_dict)
        return excel_data_list


if __name__ == '__main__':
    # file_path = os.path.join( '1642995899297_108906773.xlsx')
    excelutils = ExcelUtils('1642995899297_108906773.xls', '1642995899297_108906773')
    for excel_row in excelutils.get_all_data():
        print(excel_row)
