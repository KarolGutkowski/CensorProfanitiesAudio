import json

asrOutputJson=open('asrOutput10.json', 'r');
jsondata =asrOutputJson.read();
profanities = ["tablica brzydkich slow"];
obj = json.loads(jsondata);
f = open("output.txt", 'w')
list = obj['results']['items'];
for i in range(0, len(list)-1):
    if str(obj['results']['items'][i]['type']) != 'punctuation':
        if str(obj['results']['items'][i]['alternatives'][0]['content']).lower() in profanities:
            f.write(str(obj['results']['items'][i]['start_time'])+'\n')
            f.write(str(obj['results']['items'][i]['end_time'])+'\n')
