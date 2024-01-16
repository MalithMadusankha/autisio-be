from models.analysis import Analysis
from controller.game import getLast
from controller.audio import getLastRespond
import pandas as pd
import joblib

# Load model
load_mode = joblib.load('AnalysisModel.joblib')

print(load_mode)

def sourece_detect():
    print("<===== Analysis =====>")
    focused = getLast("focused")
    selectiv = getLast("selectiv")
    divided = getLast("divided")
    sustained = getLast("sustained")
    audioGame = getLastRespond()
    # s2 = [[5],[8], [15],[10],[20], [10],[1],[1]]
    
    print("focused", focused)
    print("selectiv", selectiv)
    print("divided", divided)
    print("sustained", sustained)
    print("audioGame", audioGame)
    
    father_value = audioGame[0]['father']
    mother_value = audioGame[0]['mother']

    dataObj = {
        "focused": focused['duration'],
        "selectiv": selectiv['duration'],
        "divided": divided['duration'],
        "sustained": sustained['duration'],
        "father":father_value,
        "mother":mother_value,
        "status":""
    }

    s2 = [[focused['duration']], [selectiv['duration']], [divided['duration']], [sustained['duration']], [father_value], [mother_value]]

    
    print(len(s2))
    df = pd.DataFrame({'Game 1': s2[0], 'Game 2': s2[1], 'Game 3': s2[2], 'Game 4': s2[3], 
                       'Father': s2[4], 'Mothe': s2[5]})


    sample = df.iloc[:, :].values

    predict_res = load_mode.predict(sample)
    print('predic', predict_res)

    if predict_res[0] == 1:
        dataObj["status"] = "Health"
    else:
        dataObj["status"] = "Unealth"

    return {"status_code": 200, "result": dataObj}
