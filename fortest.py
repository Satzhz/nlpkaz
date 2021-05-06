import requests 
from streamparser import parse, reading_to_string, mainpos, parse_file



# url = f"http://192.168.99.100:32768/analyse?lang=kaz&q={text}"
# result = requests.get(url)
units = parse('^қашан/қаш<v><iv><opt><p1><sg>/қашан<adv><itg>/қашан<adv><itg>+е<cop><aor><p3><pl>/қашан<adv><itg>+е<cop><aor><p3><sg>$')        
for unit in units:
    a = unit.readings
    print(unit.readings)
    for item in a:
        if len(item) == 1:
            print(item)
    #     for i in item:
    #         # print(i[1])