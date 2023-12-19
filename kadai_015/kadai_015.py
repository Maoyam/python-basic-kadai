# クラスの定義
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 出力メソッド
    def printinfo(self):
        print(f"名前：{self.name}")
        print(f"年齢：{self.age}")

# インスタンス化
man = Human("チャーリー", 10)
# メソッドの実行
man.printinfo()
        