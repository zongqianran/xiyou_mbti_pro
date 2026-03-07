
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

mbti_map = {
    "ISFJ": {
        "name": "唐僧",
        "img": "images/tangseng/tangseng.png",
        "desc": "唐僧性情温厚，心志坚定。他不以武力见长，却以信念支撑漫长取经之路。面对妖魔险阻，他始终守持戒律与慈悲之心，体现出一种柔而不弱、静而不退的精神力量。" ,
        "role":"在西游取经团队中，唐僧是精神核心。他象征佛法与修行的终极目标，也是团队前行的意义所在。孙悟空的勇武、八戒的世俗、沙僧的稳重，皆围绕唐僧这一精神中心展开。。",
        "analysis":"ENTP型人格充满创造力与挑战精神，喜欢打破规则并寻找新的解决方案。孙悟空面对妖怪常常随机应变，正是典型的ENTP特征。"
    },
    "ESFP": {
        "name": "猪八戒",
        "img": "images/zhubajie/zhubajie.png",
        "desc": "性情率直，喜怒形于色。猪八戒贪食好乐，时有懈怠，却又心地不坏、情感真诚。其人虽多俗气，却也显露出一种率性而为的人间气息。",
        "role":"西游团队中的气氛调和者。八戒虽常抱怨辛劳，却在关键时刻仍愿出力，与悟空并肩对敌，使团队在紧张旅途中保留几分人情温度。",
        "analysis":"ESFP人格重视现实体验与情感表达，往往活跃于群体之中。猪八戒的行为既体现人性的欲望，也表现出真诚与善良。从传统思想看，他象征“凡心未净”的人性面向——既有欲望与懒散，也具改过向善的可能。"
    },
    "ENTP": {
        "name": "孙悟空",
        "img": "images/sunwukong/sunwukong.png",
        "desc": "石破天惊而生，性灵通达，桀骜不驯。自花果山称王至护送唐僧西行，孙悟空始终以机敏与胆识破局开路。其心不受拘束，敢于挑战天庭秩序，又能在取经之路上逐渐收敛锋芒，显现出由“任性之灵”向“护道之心”的转化。",
        "role":"西游取经团队的护法与开路者。凡遇妖魔险阻，多由悟空先行探路、降妖伏魔，使取经之路得以继续。其行动力与决断力，构成团队中最为锋锐的力量。",
        "analysis":"ENTP型人格富于创造力与探索精神，善于在困境中寻找突破。孙悟空不拘旧法，常以机变取胜，其思维活跃、行动果断，正是“变通之智”的体现。从哲学意义上看，他既具道家“逍遥不羁”的气质，又在取经之路中逐渐接受佛家戒律的约束，体现出由自由之性到自觉之德的转化。"
    },
    "ENFJ": {
        "name": "女儿国国王",
        "img": "images/nverguoguowang/nverguoguowang.png",
        "desc": "女儿国国王气度温婉而不失威仪。她以一国之主的身份统御臣民，又以女子的真情面对取经僧人。其情不失礼，其爱不逾矩，在柔情与责任之间展现出极高的情感智慧与人格修养。",
        "role":"在《西游记》的叙事中，女儿国象征人间情欲与世俗牵绊。国王的出现，使唐僧的取经之路第一次真正面对“人间情感”的考验。她既是情感的象征，也是对修行之心的一次温柔试炼。",
        "analysis":"ENFJ 型人格往往兼具领导力与情感感召力，能够理解他人的情绪并以理想引导群体。女儿国国王正体现了这种特质：她既能治理一国，又能以真情表达内心。从中国传统思想来看，这种人格气质接近儒家所说的“仁者爱人”，以情感为纽带，以德行凝聚人心。"
    },
    "ESTJ": {
        "name": "哪吒",
        "img": "images/nezha/nezha.png",
        "desc": "少年英武，刚毅果决。哪吒自幼性烈，敢于担当，在天庭体系中以勇猛与纪律著称。",
        "role":"天庭秩序的重要守护者。在神魔冲突之中，哪吒往往代表天界力量，执行命令、维持秩序。",
        "analysis":"ESTJ人格重视秩序、规则与效率。哪吒的行事方式果断直接，体现出强烈的责任意识。从哲学角度看，这种人格气质与儒家“立身以义、行事以法”的精神相契。"
    },
    "INFJ": {
        "name": "观音",
        "img": "images/guanyin/guanyin.png",
        "desc": "慈悲广大，智慧深远。观音菩萨在西游世界中既是指引者，也是守护者，以悲愿化解众生苦难。",
        "role":"取经事业的总策划者与精神导师。正是观音选定唐僧、安排徒弟，使西行之路得以展开。",
        "analysis":"INFJ人格以理想主义与洞察力著称。观音既能洞察众生之苦，又能设计长远布局。从思想层面看，她体现佛家“慈悲与智慧并行”的境界。"
    },
    "ISTJ": {
        "name": "二郎神",
        "img": "images/erlangshen/erlangshen.png",
        "desc": "威严沉稳，纪律严明。二郎神杨戬以武艺高强与冷静理性著称，是天界中极具威望的战神。",
        "role":"天庭的重要守卫力量。在大闹天宫等关键情节中，他代表秩序力量与孙悟空对峙。",
        "analysis":"ISTJ人格强调责任、原则与执行力。二郎神的行为体现出严格的秩序意识。从传统思想看，这种人格气质接近儒家“守法度、尽其职”的精神。"
    },
    "INTJ": {
        "name": "太上老君",
        "img": "images/taishanglaojun/taishanglaojun.png",
        "desc": "深居兜率宫，炼丹悟道，观世如棋。太上老君不常出手，却往往在关键处布置局势。",
        "role":"天界中的智慧象征。其法宝与丹药多次影响西游世界的重要事件。",
        "analysis":"INTJ人格善于战略思考与长远规划。太上老君以冷静与远见观察世局，其思维方式与道家“以无为观万物”的哲学气质相近。"
    }
}

@app.route('/result', methods=['POST'])
def result():
    scores = {"E":0,"I":0,"S":0,"N":0,"T":0,"F":0,"J":0,"P":0}

    for value in request.form.values():
        scores[value] += 1

# 隐藏彩蛋：一道题都没做
    if len(request.form) == 0:
        character = mbti_map["ENTP"] # 孙悟空
        mbti = "ENTP"
        radar_data = [90, 40, 75, 30]

        easter_egg = "你什么都没选。这很像齐天大圣——不按套路出牌。"

        return render_template(
            "result.html",
            mbti=mbti,
            character=character,
            radar_data=radar_data,
            easter_egg=easter_egg
        )

    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    character = mbti_map.get(mbti)

    radar_data = [
        scores["E"]*25,
        scores["S"]*25,
        scores["T"]*25,
        scores["J"]*25
    ]

    return render_template("result.html",
                           mbti=mbti,
                           character=character,
                           radar_data=radar_data)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)