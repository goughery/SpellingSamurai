def getSpelled(intent):
    wordSpelled = ""
    if "value" in intent["slots"]["lettera"]:
        wordSpelled += intent["slots"]["lettera"]["value"].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterb"]:
        wordSpelled += intent["slots"]["letterb"]["value"].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterc"]:
        wordSpelled += intent['slots']['letterc']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterd"]:
        wordSpelled += intent['slots']['letterd']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["lettere"]:
        wordSpelled += intent['slots']['lettere']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterf"]:
        wordSpelled += intent['slots']['letterf']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterg"]:
        wordSpelled += intent['slots']['letterg']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterh"]:
        wordSpelled += intent['slots']['letterh']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letteri"]:
        wordSpelled += intent['slots']['letteri']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterj"]:
        wordSpelled += intent['slots']['letterj']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterk"]:
        wordSpelled += intent['slots']['letterk']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterl"]:
        wordSpelled += intent['slots']['letterl']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterm"]:
        wordSpelled += intent['slots']['letterm']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["lettern"]:
        wordSpelled += intent['slots']['lettern']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["lettero"]:
        wordSpelled += intent['slots']['lettero']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterp"]:
        wordSpelled += intent['slots']['letterp']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterq"]:
        wordSpelled += intent['slots']['letterq']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterr"]:
        wordSpelled += intent['slots']['letterr']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letters"]:
        wordSpelled += intent['slots']['letters']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["lettert"]:
        wordSpelled += intent['slots']['lettert']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letteru"]:
        wordSpelled += intent['slots']['letteru']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterv"]:
        wordSpelled += intent['slots']['letterv']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterw"]:
        wordSpelled += intent['slots']['letterw']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterx"]:
        wordSpelled += intent['slots']['letterx']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["lettery"]:
        wordSpelled += intent['slots']['lettery']['value'].lower().replace(" ", "").replace(".","")
    if "value" in intent["slots"]["letterz"]:
        wordSpelled += intent['slots']['letterz']['value'].lower().replace(" ", "").replace(".","")
    return wordSpelled