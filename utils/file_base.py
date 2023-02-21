import os


class FileBaseUtil():
    """
    文件处理基础类
    """
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def check_file_exist(self):
        """
        校验文件存在
        :param None
        :return <class bool>
        :raise None
        """
        if not (self.file_path and isinstance(self.file_path, str)):
            return False

        return os.path.exists(self.file_path)

    def read_file(self, mode: str = "rb"):
        """
        读取文件
        :param 
        :return 
        :raise 
        """
        if not self.check_file_exist():
            raise UserWarning("目标文件不存在")

        pass

    def write_data_to_file(self, data, mode: str = "w"):
        """
        写入数据至文件
        :param 
        :return 
        :raise 
        """
        pass
