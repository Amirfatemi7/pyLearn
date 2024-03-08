from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import math

my_app = QApplication([])

loader = QUiLoader()

my_window = loader.load("calculator.ui")

def sum():
    global a,calculate
    calculate = "sum"
    a = float(my_window.lineEdit_1.text())
    my_window.lineEdit_1.setText("")

def sub():
    global a,calculate
    calculate = "sub"
    a = float(my_window.lineEdit_1.text())
    my_window.lineEdit_1.setText("")

def multi():
    global a,calculate
    calculate = "multi"
    a = float(my_window.lineEdit_1.text())
    my_window.lineEdit_1.setText("")
def div():
    global a,calculate
    calculate = "div"
    a = float(my_window.lineEdit_1.text())
    my_window.lineEdit_1.setText("")
def sin():
    global a,calculate
    calculate = "sin"
    a = float(my_window.lineEdit_1.text())
    result()
def cos():
    global a,calculate
    calculate = "cos"
    a = float(my_window.lineEdit_1.text())
    result()
def tan():
    global a,calculate
    calculate = "tan"
    a = float(my_window.lineEdit_1.text())
    result()
def cot():
    global a,calculate
    calculate = "cot"
    a = float(my_window.lineEdit_1.text())
    result()
def log():
    global a,calculate
    calculate = "log"
    a = float(my_window.lineEdit_1.text())
    result()
def sqrt():
    global a,calculate
    calculate = "sqrt"
    a = float(my_window.lineEdit_1.text())
    result()
def clear():
    global a,calculate
    a = 0
    my_window.lineEdit_1.setText("") 
def percent():
    global a,calculate
    calculate = "percent"
    a = float(my_window.lineEdit_1.text())
    result()

def dot():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '.')
def zero():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '0')
def one():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '1')
def two():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '2')
def three():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '3')
def four():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '4')
def five():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '5')
def six():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '6')
def seven():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '7')
def eight():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '8')
def nine():
    my_window.lineEdit_1.setText(my_window.lineEdit_1.text() + '9')

def result():
    global calculate
    b = float(my_window.lineEdit_1.text())
    match calculate:
        case "sum":
            c = a + b 
        case "sub":
            c = a - b
        case "multi":
            c = a * b 
        case "div":
            c = a / b 
        case "sin":
            c = math.sin(math.radians(a)) 
        case "cos":
            c = math.cos(math.radians(a))  
        case "tan":
            c = math.tan(math.radians(a)) 
        case "cot":
            c = 1 / math.tan(math.radians(a)) 
        case "log":
            c = math.log(a) 
        case "sqrt":
            c = math.sqrt(a) 
        case "percent":
          c = a / 100 

    my_window.lineEdit_1.setText(str(c))



my_window.show()

my_window.btn_sum.clicked.connect(sum)
my_window.btn_sub.clicked.connect(sub)
my_window.btn_multi.clicked.connect(multi)
my_window.btn_div.clicked.connect(div)
my_window.btn_sin.clicked.connect(sin)
my_window.btn_cos.clicked.connect(cos)
my_window.btn_tan.clicked.connect(tan)
my_window.btn_cot.clicked.connect(cot)
my_window.btn_log.clicked.connect(log)
my_window.btn_sqrt.clicked.connect(sqrt)
my_window.btn_percent.clicked.connect(percent)
my_window.btn_dot.clicked.connect(dot)
my_window.btn_C.clicked.connect(clear)
my_window.btn_0.clicked.connect(zero)
my_window.btn_1.clicked.connect(one)
my_window.btn_2.clicked.connect(two)
my_window.btn_3.clicked.connect(three)
my_window.btn_4.clicked.connect(four)
my_window.btn_5.clicked.connect(five)
my_window.btn_6.clicked.connect(six)
my_window.btn_7.clicked.connect(seven)
my_window.btn_8.clicked.connect(eight)
my_window.btn_9.clicked.connect(nine)

my_window.btn_cal.clicked.connect(result)
# my_window.pushButton_1.clicked.connect(showtxt)

my_app.exec()


