from models.analysis import Airpolution
import pandas as pd
import joblib
import sklearn
# 1.0.2 
print("Scikit-Learn version:", sklearn.__version__) # 1.3.0

# Load the model from the saved file
loaded_model = joblib.load('DecisionTreeClassifierModel.pickle')

def sourece_detect(gameResult):
    print("<===== Analysis =====>", )
    
    # Load model
    load_mode = joblib.load('DecisionTreeClassifierModel.pickle')
    
    s2 = [[5],[8], [15],[10],[20], [10],[5],[8],[5], [0]]
    print(len(s2))
    df = pd.DataFrame({'Game 1': s2[0], 'Game 2': s2[1], 'Game 3': s2[2],'Game 4': s2[3], 'Game 5': s2[4], 'Attention Reader': s2[5],'Response for Father': s2[6], 'Response for Mothe': s2[7], 'TTL': s2[8], 'Normal Child': s2[9]})
    print(df)


    sample = df.iloc[:,:].values 

    predict_res = load_mode.predict(sample)
    print('predic', predict_res)
    
    if predict_res[0] == 1:
        res = "Health"
    else :
        res = "Unealth"
        
    return {"status_code": 200, "result": res}
