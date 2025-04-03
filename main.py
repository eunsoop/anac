def translate(origin, to, text):
    if origin == "한국어" and to == "독일어":
        translate_ko_de(text)
    elif origin == "독일어" and to == "한국어":
        translate_de_ko(text)

def translate_ko_de(text):
    # 구현 (한국어 -> 독일어)
    # 대충 겁나 쩌는 코드가 있음
    # GPT가 대충 만들어줌
    print("번역 결과: ", text)

def translate_de_ko(text):
    # 구현 (독일어 -> 한국어)
    pass