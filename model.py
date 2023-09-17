class Model:
    def __init__(self, uid, name, gender):
        self.uid = uid
        self.name = name
        self.gender = gender

    def data_dict(self):
        """
            将数据打包成字典
        :return: dict，返回打包好的数据
        """
        dict_data = {
            'uid': self.uid,
            'name': self.name,
            'gender': self.gender
        }
        return dict_data
