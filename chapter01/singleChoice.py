# Creates quizzes with questions and answers in random order, along with the answer key.
'''
姓名：

工号：

部门：


                      2017信息安全知识测试卷 X

1.电脑在人离开岗位（  ）分钟后自动锁屏。
A. 10
B. 5
C. 20
D. 30

2.密码定期更换，建议至少每（  ）更改一次。
A. 一天
B. 半个月
C. 一个月
D. 三个
......

'''
import random

# The quiz data. Keys are radio title and values are list of options,the first of these options is the correct answer.
questionBanks = {
    '电脑在人离开岗位（  ）分钟后自动锁屏。': ['5', '10', '20', '30'],
    '密码定期更换，建议至少每（  ）更改一次。': ['三个月', '一天', '半个月', '一个月'],
    '信息本身是（  ）': ['无形的', '有形的', '计算机', '以上都正确'],
    '信息安全的基本属性是（  ）': ['以上都正确', '保密性', '完整性', '可用性'],
    '口令破解的最好方法是（  ）': ['组合破解', '暴力破解', '字典攻击', '生日攻击'],
    'HTTP默认端口号为（  ）': ['80', '8080', '23', '21'],
    '社会工程学常被黑客用于（  ）': ['口令获取', 'ARP', 'TCP', 'DDOS'],
    '网络安全的最后一道防线是': ['数据加密', '访问控制', '接入控制', '身份识别'],
    '打电话请求密码属于（  ）攻击方式': ['社会工程学', '木马', '电话系统漏洞', '拒绝服务'],
    '以下哪一项不属于计算机病毒的防治策略（  ）': ['禁毒能力', '防毒能力', '查毒能力', '解毒能力']
}
# Get student number ---> stuNum
infoNum = int(input("\n您要出几份考卷？   "))
# Generate infoNum quiz files
for quizNum in range(infoNum):
    # create the quiz and answer key files
    quizfile = open('infosecurity{}.txt'.format(quizNum + 1), 'w', encoding='utf-8')
    answerkeyFile = open('infosecurity_answer{}.txt'.format(quizNum + 1), 'w', encoding='utf-8')
    # write out the header for the quiz
    quizfile.write('\n姓名：      工号：      部门：        \n\n')
    quizfile.write(' '*20 + '2017信息安全知识考试{}\n\n'.format(quizNum + 1))
    # shuffle the order of the radios
    radios = list(questionBanks.keys())
    random.shuffle(radios)
    # loop through all questionBanks,making a question for each
    for questionNum in range(len(radios)):
        # get the right answer --> correctAnswer
        correctAnswer = questionBanks[radios[questionNum]][0]
        # print('{}-->{}'.format(radios[questionNum],correctAnswer))
        # Generate random answer options pool
        answerOptions = questionBanks[radios[questionNum]]
        random.shuffle(answerOptions)
        # write the question and the answer options to quiz file.
        quizfile.write('{}. {} \n'.format(questionNum + 1,radios[questionNum]))
        for i in range(4):
            quizfile.write('{}. {}\n'.format('ABCD'[i],answerOptions[i]))

        # add line
        quizfile.write('\n')
        # write the answer key to a file
        answerkeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
