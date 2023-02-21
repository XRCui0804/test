import pandas


class PandasBaseUtil():
    """
    pandas基础工具类
    """

    def __init__(self, *args, **kwargs) -> None:
        pass

    def read_excel(self, file_path: str, sheet : str = None):
        """
        读取excel
        :param file_path 文件路径
        :param sheets 工作簿名称
        :return None
        :raise None
        """
        self.excel_data = None
        if isinstance(file_path, str) and file_path:
            if sheet:
                self.excel_data = pandas.read_excel(file_path, header=None, sheet_name=sheet)
            else:
                self.excel_data = pandas.read_excel(file_path, header=None)
