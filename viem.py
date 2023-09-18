import model
import contorller


class Viem:
    def __init__(self):
        self.contorller = contorller.Contorller()

    def __input_button(self):
        """
            选项显示界面
        :return:
        """
        print(
            """
            1.添加学生数据
            2.输出学生数据
            3.删除学生数据
            4.修改学生数据
            """)

    def __button(self):
        """
            按钮函数，选择对应选项
        :return:
        """
        self.__input_button()
        try:
            button = int(input("请输入选项:"))
            if button == 1:
                self.__increase_data()
            elif button == 2:
                self.__print_data()
            elif button == 3:
                self.__del_data()
            elif button == 4:
                self.__revise_data()
            else:
                return 1
        except Exception as arr:
            return 1

    def __increase_data(self):
        """
            增加数据界面
        :return:
        """
        uid = int(input("请输入需要增加的学生uid:"))
        name = input("请输入学生姓名:")
        gender = input("请输入学生的性别:")
        mode = model.Model(uid, name, gender).data_dict()
        come = self.contorller.append_student_data(mode)
        if come:
            print("数据添加成功！")
        else:
            print("数据添加失败！")

    def __print_data(self):
        """
            查询学生数据
        :return:
        """
        uid = int(input('请输入需要查询的uid:'))
        data = self.contorller.print_student_data(uid)
        if data:
            print(data)
        else:
            print('数据未找到')

    def __del_data(self):
        uid = int(input('请输入需要删除的uid:'))
        data = self.contorller.print_student_data(uid)
        if data:
            yn = input(f'是否删除以下数据\n%s\n请输入(Y/N):' % data)
            if str(yn).lower() == 'y':
                outcome = self.contorller.del_student_data(uid)
                if outcome:
                    print('数据已删除！')
            else:
                print('已停止删除操作！')
        else:
            print('数据不存在！')

    def __revise_data(self):
        uid = int(input('请输入需要修改的学生的id:'))
        outcome = self.contorller.print_student_data(uid)
        if outcome:
            name = input('修改后的学生姓名:')
            gender = input('修改后的学生性别:')
            mode = model.Model(outcome['uid'], name, gender).data_dict()
            tf = self.contorller.revise_student_data(mode)
            if tf:
                print('修改成功')
            else:
                print('修改失败')
        else:
            print('需要修改的学生不存在！')

    def main(self):
        while True:
            self.__button()
