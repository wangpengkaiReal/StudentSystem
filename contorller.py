import viem
import model


class Contorller:
    def __init__(self):
        self.__student_list = []

    def append_student_data(self, data):
        """
            添加学生数据
        :param data: model文件定义的数据类型，打包输入
        :return: 返回True or Flash
        """
        self.__student_list.append(data)
        return True

    def print_student_data(self, uid):
        """
            打印学生信息
        :param uid: str,需要查询的学生uid
        :return: dict，查询到的学生信息
        """
        for item in self.__student_list:
            if uid == item['uid']:
                return item

    def del_student_data(self, uid):
        """
            删除学生数据
        :param uid: str,需要删除的学生uid
        :return: Ture or False
        """
        for item in range(len(self.__student_list)):
            if uid == self.__student_list[item]['uid']:
                del self.__student_list[item]
                return True

    def revise_student_data(self, data):
        pass
