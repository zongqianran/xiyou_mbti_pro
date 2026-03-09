
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

mbti_map = {
    "ISFJ": {
        "name": "唐僧",
        "img": "images/tangseng/tangseng.png",
        "philosophy": "信念伦理与意义追寻",
        "desc": "唐僧性情温厚，心志坚定。他不以武力见长，却以信念支撑漫长取经之路。面对妖魔险阻，他始终守持戒律与慈悲之心，体现出一种柔而不弱、静而不退的精神力量。" ,
        "role":"在西游取经团队中，唐僧是精神核心。他象征佛法与修行的终极目标，也是团队前行的意义所在。孙悟空的勇武、八戒的世俗、沙僧的稳重，皆围绕唐僧这一精神中心展开。。",
        "analysis":"唐僧的力量并不来自能力，而来自信念。他始终坚持取经这一目标，即使在现实看来几乎不可能实现。从伦理哲学角度看，这种人格体现的是“信念伦理”：行动的意义并不完全由结果决定，而由主体是否忠于其内心法则决定。唐僧的存在为团队提供了一种方向性的力量。在一个充满诱惑与混乱的世界中，他代表一种精神轴心。正因为这种轴心的存在，取经之路才不仅是一段旅程，而成为一种意义的追寻。"
    },
    "ESFP": {
        "name": "猪八戒",
        "img": "images/zhubajie/zhubajie.png",
        "philosophy": "欲望结构与人性张力",
        "desc": "性情率直，喜怒形于色。猪八戒贪食好乐，时有懈怠，却又心地不坏、情感真诚。其人虽多俗气，却也显露出一种率性而为的人间气息。",
        "role":"西游团队中的气氛调和者。八戒虽常抱怨辛劳，却在关键时刻仍愿出力，与悟空并肩对敌，使团队在紧张旅途中保留几分人情温度。",
        "analysis":"猪八戒体现的是人性的矛盾结构。他既贪图享乐，又不完全放弃责任；既表现出懒散与欲望，又在关键时刻承担行动。这种不稳定正是人类真实状态的缩影。与理想化的英雄不同，八戒更接近普通人的处境：人在欲望与道德之间不断摇摆。正因为如此，他的形象具有独特的现实意义——人性并不纯粹，但正是在这种不纯粹之中，人仍然可能继续前行。"
    },
    "ENTP": {
        "name": "孙悟空",
        "img": "images/sunwukong/sunwukong.png",
        "philosophy": "主体性与权威结构",
        "desc": "石破天惊而生，性灵通达，桀骜不驯。自花果山称王至护送唐僧西行，孙悟空始终以机敏与胆识破局开路。其心不受拘束，敢于挑战天庭秩序，又能在取经之路上逐渐收敛锋芒，显现出由“任性之灵”向“护道之心”的转化。",
        "role":"西游取经团队的护法与开路者。凡遇妖魔险阻，多由悟空先行探路、降妖伏魔，使取经之路得以继续。其行动力与决断力，构成团队中最为锋锐的力量。",
        "analysis":"孙悟空象征一种原初的主体性。他并非从社会结构中诞生，而是自天地自然中出现，因此天然站在权威之外。他对天庭秩序的挑战并不仅是力量的对抗，而是一种存在论层面的提问：个体是否必须服从既定结构？真正的自由是否可能存在？然而他的成长也揭示了另一层意义——纯粹的反叛无法构成稳定的自由。被压五行山之后，悟空逐渐理解秩序的意义，并在行动中重新界定自身位置。于是，“齐天大圣”最终转化为“斗战胜佛”。这一变化表明，成熟的主体并不是永恒的反抗者，而是能够在理解世界结构之后仍然保持自我意识的人。"
    },
    "ENFJ": {
        "name": "女儿国国王",
        "img": "images/nverguoguowang/nverguoguowang.png",
        "philosophy": "情感伦理与他者关系",
        "desc": "女儿国国王气度温婉而不失威仪。她以一国之主的身份统御臣民，又以女子的真情面对取经僧人。其情不失礼，其爱不逾矩，在柔情与责任之间展现出极高的情感智慧与人格修养。",
        "role":"在《西游记》的叙事中，女儿国象征人间情欲与世俗牵绊。国王的出现，使唐僧的取经之路第一次真正面对“人间情感”的考验。她既是情感的象征，也是对修行之心的一次温柔试炼。",
        "analysis":"ENFJ 型人格往往兼具领导力与情感感召力，能够理解他人的情绪并以理想引导群体。女儿国国王正体现了这种特质：她既能治理一国，又能以真情表达内心。从中国传统思想来看，这种人格气质接近儒家所说的“仁者爱人”，以情感为纽带，以德行凝聚人心。"
    },
    "ESTJ": {
        "name": "哪吒",
        "img": "images/nezha/nezha.png",
        "philosophy": "个体反叛与责任伦理",
        "desc": "少年英武，刚毅果决。哪吒自幼性烈，敢于担当，在天庭体系中以勇猛与纪律著称。",
        "role":"天庭秩序的重要守护者。在神魔冲突之中，哪吒往往代表天界力量，执行命令、维持秩序。",
        "analysis":"ESTJ人格重视秩序、规则与效率。哪吒的行事方式果断直接，体现出强烈的责任意识。从哲学角度看，这种人格气质与儒家“立身以义、行事以法”的精神相契。"
    },
    "INFJ": {
        "name": "观音",
        "img": "images/guanyin/guanyin.png",
        "philosophy": "慈悲伦理与超越意识",
        "desc": "慈悲广大，智慧深远。观音菩萨在西游世界中既是指引者，也是守护者，以悲愿化解众生苦难。",
        "role":"取经事业的总策划者与精神导师。正是观音选定唐僧、安排徒弟，使西行之路得以展开。",
        "analysis":"观音象征一种超越性的伦理视角。她并不直接解决所有问题，而是通过引导，使个体在经历困难中成长。这种行为体现了佛教所谓“悲智双运”的原则：真正的慈悲并不是简单的救助，而是理解众生的处境，并给予他们走向觉悟的可能性。因此，观音的力量并非来自控制，而来自一种更高层次的理解。"
    },
    "ISTJ": {
        "name": "二郎神",
        "img": "images/erlangshen/erlangshen.png",
        "philosophy": "理性秩序与制度权威",
        "desc": "威严沉稳，纪律严明。二郎神杨戬以武艺高强与冷静理性著称，是天界中极具威望的战神。",
        "role":"天庭的重要守卫力量。在大闹天宫等关键情节中，他代表秩序力量与孙悟空对峙。",
        "analysis":"ISTJ人格强调责任、原则与执行力。二郎神的行为体现出严格的秩序意识。从传统思想看，这种人格气质接近儒家“守法度、尽其职”的精神。"
    },
    "INTJ": {
        "name": "太上老君",
        "img": "images/taishanglaojun/taishanglaojun.png",
        "philosophy": "超然意识与宇宙秩序",
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