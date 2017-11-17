# Creates quizzes with questions and answers in random order, along with the answer key.
'''
姓名：

学号：

班级：


                      省配对省会测试卷 X

1、 海南的省会是？
A. 海口
B. 成都
C. 福州
D. 呼和浩特

2. 黑龙江的省会是？
A. 哈尔滨
B. 武汉
C. 重庆
D. 香港
......

'''
import random

# The quiz data. Keys are provinces and values are their capitals.
capitals = {
    '北京': '北京',
    '天津': '天津',
    '上海': '上海',
    '重庆': '重庆',
    '河南': '郑州',
    '河北': '石家庄',
    '山西': '太原',
    '辽宁': '沈阳',
    '吉林': '长春',
    '黑龙江': '哈尔滨',
    '江苏': '南京',
    '浙江': '杭州',
    '安徽': '合肥',
    '福建': '福州',
    '江西': '南昌',
    '山东': '济南',
    '湖北': '武汉',
    '湖南': '长沙',
    '广东': '广州',
    '海南': '海口',
    '四川': '成都',
    '贵州': '贵阳',
    '云南': '昆明',
    '陕西': '西安',
    '甘肃': '兰州',
    '西藏': '拉萨',
    '内蒙': '呼和浩特',
    '宁夏': '银川',
    '新疆': '乌鲁木齐',
    '香港': '香港',
    '澳门': '澳门',
    '台湾': '台北'
}
# Get student number ---> stuNum
stuNum = int(input("\n您要出几份考卷？   "))
# Generate stuNum quiz files
for quizNum in range(stuNum):
    # create the quiz and answer key files
    quizFile = open('capitalsquiz{}.txt'.format(quizNum + 1), 'w', encoding='utf-8')
    answerKeyFile = open('capitalsquiz_answer{}.txt'.format(quizNum + 1), 'w', encoding='utf-8')
    # write out the header for the quiz
    quizFile.write('姓名：      学号：      班级：        \n\n')
    quizFile.write(' ' * 20 + '省 配 对 省 会 测 试 卷{}\n\n'.format(quizNum + 1))
    # shuffle the order of the provinces
    provinces = list(capitals.keys())
    random.shuffle(provinces)

    # loop through all provinces,making a question for each
    for questionNum in range(len(provinces)):

        # get the right answer ----> correctAnswer
        correctAnswer = capitals[provinces[questionNum]]

        # get wrong answer pool: all answers then exclude the correct answer
        wrongAnswers = list(capitals.values())
        wrongAnswers.remove(correctAnswer)

        # random take 3 from wrong answer pool and combine the right one to make 4 answer options
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # write the question and the answer options to the quiz file.
        quizFile.write('{}、{}的省会是？  \n'.format(questionNum + 1,provinces[questionNum]))
        for i in range(4):
            quizFile.write('{}. {}\n'.format('ABCD'[i], answerOptions[i]))
        # add line
        quizFile.write('\n')
        # write the answer key to a file
        answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
