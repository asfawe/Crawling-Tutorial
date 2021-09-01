import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont # QIcon(아이콘)은 말 그대로 아이콘이다. QPixmap(픽스맵)는 이미지를 띄울수 있다. QFont(큐폰트) 폰트를 지정할수 있다. 사이즈,컬러 등등
from PyQt5.QtCore import QCoreApplication, QDateTime #QCoreApplication(코어어플리캐잇션은) 종료를 할때 쓴다.
import requests
from bs4 import BeautifulSoup
import xlsxwriter

class 대표선출프로그램(QWidget):
    def __init__(self): # 클래스가 인스턴스화가 될때 제일 먼저 실행을 한다.
        super().__init__() #super(수퍼)는 QWidget(위젯)을 나타낸다.
        self.UI초기화()

    def UI초기화(self):
        self.제목라벨 = QLabel('(주)캣네생선', self)
        self.제목라벨.move(50, 50)
        self.제목라벨.setFont(QFont("Helvetica", pointSize=20, weight=2))

        self.시총라벨 = QLabel('시가총액 : - 원', self)
        self.시총라벨.move(50, 110)

        self.시총순위라벨 = QLabel('시가총액 순위 : 위니브 월드 - 위', self)
        self.시총순위라벨.move(50, 140)

        self.현재가 = QLabel('현재가 : - 원', self)
        self.현재가.move(50, 170)

        self.최고최저가 = QLabel('52주 최고 | 52주 최저 : - 원 | - 원', self)
        self.최고최저가.move(50, 200)

        self.배당율 = QLabel('배당율 : - %', self)
        self.배당율.move(50, 230)

        self.오픈날짜 = QLabel('오픈날짜 : 2020년 1월 1일', self)
        self.오픈날짜.move(50, 260)

        self.오픈된날짜 = QLabel('오픈된날짜 : - 일', self)
        self.오픈된날짜.move(50, 290)

        self.매출비용순익 = QLabel('매출/비용/순익 : -원/-원/-원', self)
        self.매출비용순익.move(50, 320)

        작성버튼 = QPushButton('재무 보고서 작성', self)
        작성버튼.move(30, 430)
        작성버튼.resize(340, 50)
        작성버튼.clicked.connect(self.write)

        엑셀버튼 = QPushButton('엑셀 보고서 작성', self)
        엑셀버튼.move(30, 490)
        엑셀버튼.resize(340, 50)
        엑셀버튼.clicked.connect(self.excel)

        종료버튼 = QPushButton('프로그램 종료', self)
        종료버튼.move(30, 550)
        종료버튼.resize(340, 50)
        종료버튼.clicked.connect(self.close)

        self.대표이미지 = QLabel(self)
        self.대표이미지.setPixmap(QPixmap('img/weniv-licat.png').scaled(35, 44))
        self.대표이미지.move(10, 10)

        self.setWindowTitle('재무 보고서를 만들어라!')
        self.setWindowIcon(QIcon('img/weniv-licat.png'))
        self.setGeometry(800, 300, 400, 630)
        self.show()

    def write(self):
        url = 'http://paullab.co.kr/stock.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        values = soup.select('.tables td')
        # print(values)
        self.시총라벨값 = values[0].text
        self.시총라벨.setText(f'시가총액 : {values[0].text}')
        self.시총라벨.resize(400, 20)

        self.시총순위라벨값 = values[1].text
        self.시총순위라벨.setText(f'시가총액 순위 : {values[1].text}')
        self.시총순위라벨.resize(400, 20)

        self.현재가값 = values[3].text
        self.현재가.setText(f'현재가 : {values[3].text}')
        self.현재가.resize(400, 20)

        s = values[4].text.strip().replace('\n', '').split('l')
        # print(s)
        self.최고최저가값 = f'{s[0]} | {s[1]}'
        self.최고최저가.setText(f'52주 최고 | 52주 최저 : {s[0]} | {s[1]}')
        self.최고최저가.resize(400, 20)

        i = values[5].text.strip()
        # print(i)
        self.배당율값 = i
        self.배당율.setText(f'배당율 : {i}')
        self.배당율.resize(400, 20)

        self.매출값 = values[6].text
        self.비용값 = values[7].text
        self.순익값 = values[8].text
        self.매출비용순익.setText(f'매출/비용/순익 :\n{values[6].text}\n /{values[7].text}\n /{values[8].text}')
        self.매출비용순익.resize(400, 80)

        day = QDateTime(2020, 1, 1, 00, 00, 00)
        # print(type(day))
        # print(dir(day))
        day = str(day.daysTo(QDateTime.currentDateTime()))
        self.오픈된날짜계산값 = day
        self.오픈된날짜.setText(f'오픈된 날짜 : {day} 일')
        self.오픈된날짜.resize(400, 20)

    def excel(self):
        workbook = xlsxwriter.Workbook('재무보고서.xlsx')
        worksheet = workbook.add_worksheet('보고서')
        
        #셀 안에 문자값 입력하기
        worksheet.write('A1', '시가총액')
        worksheet.write('A2', '시가총액순위')
        worksheet.write('A3', '현재가')
        worksheet.write('A4', '52주최고|최저')
        worksheet.write('A5', '오픈날짜')
        worksheet.write('A6', '오픈된날짜')
        worksheet.write('A7', '배당율')
        worksheet.write('A8', '매출')
        worksheet.write('A9', '비용')
        worksheet.write('A10', '순익')

        worksheet.write('B1', self.시총라벨값)
        worksheet.write('B2', self.시총순위라벨값)
        worksheet.write('B3', self.현재가값)
        worksheet.write('B4', self.최고최저가값)
        worksheet.write('B5', '2020. 1. 1.')
        worksheet.write('B6', self.오픈된날짜계산값)
        worksheet.write('B7', self.배당율값)
        worksheet.write('B8', self.매출값)
        worksheet.write('B9', self.비용값)
        worksheet.write('B10', self.순익값)


        workbook.close()

    def close(self):
        return QCoreApplication.instance().quit()

프로그램무한반복 = QApplication(sys.argv) # 무한반복을 하기위한 선언
실행인스턴스 = 대표선출프로그램()
프로그램무한반복.exec_()