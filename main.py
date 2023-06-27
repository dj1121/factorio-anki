import configparser

def make_dict(path):
    Config = configparser.ConfigParser()
    Config.read(path, encoding="utf-8")
    Config.sections()

    d = {}
    for section in Config.sections():
        options = Config.options(section)
        for option in options:
            try:
                d[option] = Config.get(section, option)
            except:
                d[option] = None
    return d

def translate(source,target):
    translation = {}
    for key in source:
        if key in target:
            translation[source[key]] = target[key]
    
    return translation

def write_csv(translation):
    with open("deck.csv", "w", encoding="utf-8") as f:
        f.write("en;jp\n")
        for key in translation:
            f.write(f"{key};{translation[key]}\n")

d_en = make_dict(".\core.cfg")
d_jp = make_dict(".\core-jp.cfg")
translation = translate(d_en,d_jp)
write_csv(translation)
