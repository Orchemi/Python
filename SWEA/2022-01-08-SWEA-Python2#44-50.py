# 연습문제 1
class Student:

    total = 0
    scores = []
    scores_dict = {}

    def __init__(self):
        scores = [int(i) for i in input().split(", ")]

        self.kor = scores[0]
        self.eng = scores[1]
        self.mat = scores[2]

    def sum_score(self):
        total = self.kor + self.eng + self.mat
        print("국어, 영어, 수학의 총점: {0}".format(total))


a = Student()
a.sum_score()


# 연습문제 2
class Korean:
    def __init__(self):
        self.nationality = "대한민국"

    def printNationality(self):
        print("{0}".format(self.nationality))
        print("{0}".format(self.nationality))


a = Korean()
a.printNationality()


# 연습문제 3
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise TypeError
        self.__name = name


class GraduateStudent(Student):
    def __init__(self, name, major):
        Student.__init__(self, name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, major):
        if type(major) != str:
            raise TypeError

        self.__major = major


p1 = Student("홍길동")
print("이름: {0}".format(p1.name))

p2 = GraduateStudent("이순신", "컴퓨터")
print("이름: {0}, 전공: {1}".format(p2.name, p2.major))


# 연습문제 4
class Circle:
    def __init__(self, r):
        self.r = r

    def calcArea(self):
        print("원의 면적: {0}".format(self.r ** 2 * pi))


pi = 3.14
c1 = Circle(2)
c1.calcArea()


# 연습문제 5
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcArea(self):
        print("사각형의 면적: {0}".format(self.a * self.b))


r1 = Rectangle(4, 5)
r1.calcArea()


# 연습문제 6
class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__(self)

        self.length = length

    def area(self):
        return self.length ** 2


s1 = Square(3)
print("정사각형의 면적: {0}".format(s1.area()))


# 연습문제 7
class Person:
    def __init__(self):
        pass

    def getGender(self):
        return "Unknown"


class Male(Person):
    def __init__(self):
        Person.__init__(self)

    def getGender(self):
        return "Male"


class Female(Person):
    def __init__(self):
        Person.__init__(self)

    def getGender(self):
        return "Female"


p1 = Male()
print(p1.getGender())

p2 = Female()
print(p2.getGender())
