from app.anbudong import KMeans1, deal_data
from utils.file_base import FileBaseUtil
from utils.logger_base import logger
from utils.pandas_base import PandasBaseUtil


def main():
    """
    主程序入口
    """
    excel_path = 'weiyizhuanzhi.xlsx'
    if not FileBaseUtil(excel_path).check_file_exist():
        logger.error("指定文件不存在")
        return

    pandasUtil = PandasBaseUtil()
    pandasUtil.read_excel(excel_path)
    exec_data = pandasUtil.excel_data.iloc[:,1:]

    centroids, clusterAssment = KMeans1(exec_data.values, 6)
    # logger.info(clusterAssment)

    ret = deal_data(clusterAssment)
    logger.info(ret)


if __name__ == "__main__":
    main()
