from email_validator import validate_email, EmailNotValidError


def password_validation(password):
    l, u, p, d = 0, 0, 0, 0

    if len(password) >= 8:
        for i in password:

            if i.islower():
                l += 1

            if i.isupper():
                u += 1

            if i.isdigit():
                d += 1

            if i == '@' or i == '$' or i == '_':
                p += 1

    if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(password):
        return password
    else:
        return False


def email_validation(email):
    v = False
    try:
        v = validate_email(email)
    except EmailNotValidError as e:
        return str(e)
    return v["email"]


def classified_answers():
    dic = {
        "answers":
            {"E": ["Outgoing, talkative, and friendly", "It's exciting and interesting",
                   "Be primarily interested in and concerned with the external world",
                   "Going out with a group of friends. The more people, the more energy you feel",
                   "cruise, where there are lots of things to do and people to meet"],

             "I": ["Quiet, reserved, and calm", "It's tiring and a little nerve-wracking",
                   "Look at life from the inside out",
                   "Dinner with your best friend — just the two of you — and sharing what's on your mind",
                   "warm beach and a book, either alone or with just one other person"],

             "P": ["Relaxed and not too formal", "False", "Enjoy myself but give up control of the plans",
                   "I feel fine", "I spend most of my time understanding the problem"],

             "J": ["Formal exactly on time and by the book", "True",
                   "Make plans but do not have a lot of time to enjoy myself", "I feel devastated",
                   "I create a strategy as soon as possible"],

             "S": ["Practical", "I'm not the kind of person who often tries to come up with new ideas",
                   "Quite realistic, most of my ideas are possible",
                   "Write the report first, my writing is direct  and straightforward",
                   "Present situations", "Individual ornaments"],

             "N": ["Theoretical", "A bit unrealistic sometimes",
                   "They can be very unrealistic, but they are creative and smart",
                   "Write the outline first, I like to use a lot of metaphors.",
                   "Future possibilities.", "Tree as a whole"],

             "T": ["Making decisions in an impersonal way and using logical reasoning ",
                   "Solving logical problems, and making business decisions based on facts & figures",
                   "Based on their actions",
                   "Technical and scientific fields where logic is important",
                   "I will help the person find a solution"],

             "F": ["Base your decisions on personal values and how your actions affect others",
                   "Following your creative passions, practicing arts for self-expression",
                   "How I feel about them", "Anything that includes communications orientation",
                   "I will listen very carefully so I can understand and connect with the person"]
             }
    }
    return dic


def signup(name, email, password, answers):
    returned = append_letters(answers)
    with open("user_data.txt", "a") as f:
        f.write(f'{email}*{name}*{returned}*{password}\n')
    return returned

def lin(lines):
    if len(lines) == 3:
        return [lines[0], lines[1], lines[2]]
    elif len(lines) == 5:
        return [lines[0], lines[1], lines[2], lines[3], lines[4]]


def read(question_num):
    f = open("Extro_Intro.txt", mode='r')
    f1 = open("Sensing_Intuitive.txt", mode='r')
    f2 = open("Thinking_feeling.txt", mode='r')
    f3 = open("judging_perceiving.txt", mode='r')

    for line, line1, line2, line3 in zip(f, f1, f2, f3):
        lines = line.strip().split("*")
        lines1 = line1.strip().split("*")
        lines2 = line2.strip().split("*")
        lines3 = line3.strip().split("*")

        if int(lines[0][0:2]) == question_num:
            return lin(lines)
        elif int(lines1[0][0:2]) == question_num:
            lines = line1.strip().split("*")
            return lin(lines)
        elif int(lines2[0][0:2]) == question_num:
            lines = line2.strip().split("*")
            return lin(lines)
        elif int(lines3[0][0:2]) == question_num:
            lines = line3.strip().split("*")
            return lin(lines)


def analysis(end_answers):
    probabilities = {"E": 0, "I": 0, "P": 0, "J": 0, "S": 0, "N": 0, "T": 0, "F": 0}
    data = classified_answers()
    for i in end_answers:
        for k, j in zip(data["answers"], data["answers"].values()):
            if i in j:
                probabilities[k] += 1

    if probabilities["E"] > probabilities["I"]:
        l1 = 'E'
    else:
        l1 = 'I'
    if probabilities["S"] > probabilities["N"]:
        l2 = 'S'
    else:
        l2 = 'N'
    if probabilities["T"] > probabilities["F"]:
        l3 = 'T'
    else:
        l3 = 'F'
    if probabilities["J"] > probabilities["P"]:
        l4 = 'J'
    else:
        l4 = 'P'

    return [l1, l2, l3, l4]


def append_letters(end_answer):
    personality = ''.join(analysis(end_answer))
    return personality


def get_personality_traits(personality_type):
    with open("strength_and_weakness.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(personality_type):
                line = line.strip()
                line1 = line.split('*')
                break

    return [line1, predict_career(personality_type), tips(personality_type)]


def predict_career(personality_type):
    with open("career.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(personality_type):
                line1 = line.strip()
                line1 = line1.split("*")
                break
    return line1


def tips(personality_type):
    with open("Tips.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(personality_type):
                line1 = line.strip()
                break
    return line1


def email_result(email_receiver, type1, intro, strength1, weakness1, career1, tips1):
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import smtplib
    import ssl

    email_sender = 'ppredictiontest@gmail.com'
    email_password = "mwdexgvynobyvkkc"
    subject = 'Personality Analysis Result'

    body = f"""
    this is your personality type: {type1}\n
    {intro}\n
    strengths: {strength1}\n
    weaknesses: {weakness1}\n
    career: {career1}\n
    tips: {tips1}
    """

    email = MIMEMultipart("alternative")
    email['from'] = email_sender
    email['to'] = email_receiver
    email['Subject'] = subject
    part1 = MIMEText(body, "plain")
    email.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:  # THIS is to send the email server
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, email.as_string())  # THIS is to send the email server
