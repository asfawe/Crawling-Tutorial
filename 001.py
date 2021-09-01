import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont # QIcon(아이콘)은 말 그대로 아이콘이다. QPixmap(픽스맵)는 이미지를 띄울수 있다. QFont(큐폰트) 폰트를 지정할수 있다. 사이즈,컬러 등등
from PyQt5.QtCore import QCoreApplication #QCoreApplication(코어어플리캐잇션은) 종료를 할때 쓴다.
import random

class 대표선출프로그램(QWidget):
    def __init__(self): # 클래스가 인스턴스화가 될때 제일 먼저 실행을 한다.
        super().__init__() #super(수퍼)는 QWidget(위젯)을 나타낸다.
        self.UI초기화()

    def UI초기화(self):
        self.이미지()
        self.버튼()
        self.툴팁()
        self.대리인번호()

        self.setWindowTitle('대표를 선출하라!')
        self.setWindowIcon(QIcon('img/weniv-licat.png'))
        self.setGeometry(500, 500, 400, 400)
        self.show()




    def 이미지(self):
        self.대표이미지 = QLabel(self) # QLabel(라벨)은 글자도 넣을수 있고 그림도 넣을수 있다.
        self.대표이미지.setPixmap(QPixmap('img/weniv-licat.png').scaled(35, 44)) # scaled(스켈)은(그림) 크기를 정하는 것이다.
        self.대표이미지.move(10, 10) # move(무부)는 어디에 나타낼지 정할수 있다.

    def 버튼(self):
        self.대표선출버튼 = QPushButton('대표 선출', self)
        self.대표선출버튼.setFixedSize(340, 40) # setFixedSize(셋픽스드사이즈) 괄호안에 있는 숫자는 with(위스) height(하이트) 다. 버튼의 with,height다.
        self.대표선출버튼.move(30, 290)
        self.대표선출버튼.clicked.connect(self.choice)

        self.종료버튼 = QPushButton('종료 버튼', self)
        self.종료버튼.setFixedSize(340, 40)
        self.종료버튼.move(30, 340)
        self.종료버튼.clicked.connect(self.close)

    def 툴팁(self):
        self.대표선출버튼.setToolTip('이 버튼을 누르면 대표를 선출합니다.\n주의하세요. 되돌릴수 없습니다.')
        self.종료버튼.setToolTip('이 버튼을 누르면 프로그램을 종료합니다.')
        self.대표이미지.setToolTip('생선가게 대표 라이켓')
        self.setToolTip('이곳은 QWidget')

    def 대리인번호(self):
        self.대리인번호라벨 = QLabel('000', self)
        self.대리인번호라벨.setFont(QFont("Helvetica", pointSize=75, weight=2))
        self.대리인번호라벨.move(100, 100)

    def choice(self):
        s = str(random.randint(1, 1000))
        print(s)
        self.대리인번호라벨.setText(s)

    def close(self):
        return QCoreApplication.instance().quit()

프로그램무한반복 = QApplication(sys.argv) # 무한반복을 하기위한 선언
실행인스턴스 = 대표선출프로그램()
프로그램무한반복.exec_()