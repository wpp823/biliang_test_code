from base.base import mysql_conn_session


class SxoConstsDao():
    """获取shopxo中的常量表信息,适用于无需创建表模型操作"""

    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def get_express_info(self, express_name):
        """
        获取快递信息

        :param express_name:
        :return:
        """

        ret_data = None
        sql_str = f'select * from sxo_express where name = "{express_name}" LIMIT 0,1;'
        results = self.conn.execute(sql_str)

        if results:
            for item in results:
                ret_data = item._asdict()

        return ret_data
