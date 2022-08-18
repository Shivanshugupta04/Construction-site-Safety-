from flask import  Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)



Question={
    1:{
        "ques":"Is there  Proper height on Construction site?",
        "Options":["yes","No"],
        "Ans":None,
        "Path":{
            "yes": "https://1.bp.blogspot.com/--7FYqGVWCd4/XQIDDXghOuI/AAAAAAAABJk/SNDs0OGqA0sh3xoIa6A_KjzmUs1t-9jOACLcBGAs/s1600/leo%2Bthang%2Bvoi%2B3%2Bdiem%2Btiep%2Bxuc.jpg",
            "No" : "https://i.pinimg.com/736x/0b/9e/46/0b9e46dc04c7bf02ad00ced34b91e6af.jpg",
            },

        },
    2:{
        "ques":"Is there  Proper Surface on Construction site?",
        "options":["yes","No"],
        "Ans":None,
        "Path":{
            "Yes":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbzgN2WDMx-IIJVW4qWLCpRR9H2lGesIih3rKR9IOlarekOfSr_8wykqQ3tSnbZNWDGx4&usqp=CAU",
            "No":"https://cdn.vox-cdn.com/thumbor/COAWmP7BnM4al_Ybpa75AOAhh6U=/0x0:400x400/920x0/filters:focal(0x0:400x400):format(webp):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/19504276/04_ladder_basics.jpg"
        },
        },
    3:{
        "ques":"In ladder, missing steps are present??",
        "Options":["yes","No"],
        "Ans":None,
        "Path":{
            "yes":"https://media.gettyimages.com/photos/wooden-ladder-with-missing-step-picture-id485436771",
            "No":"https://cdn.vox-cdn.com/uploads/chorus_asset/file/19504276/04_ladder_basics.jpg",

        },

        },
    4:{
        "ques":"In ladder, Spreadbar are present?",
        "options":["yes","No"],
        "Ans":None,
        "Path":{
            "yes":"https://cdn11.bigcommerce.com/s-nu76q5988i/images/stencil/1280x1280/products/6990/3167/P6206-mk2_PI_jpeg1000__42923.1512058332.jpg",
            "No":"https://cdn11.bigcommerce.com/s-nu76q5988i/images/stencil/1280x1280/products/6990/3167/P6206-mk2_PI_jpeg1000__42923.1512058332.jpg",
        },

        },
    5: {
        "Ques":"Is the ladder is stand-in bent angle on the construction site?",
        "Options":["yes","No"],
        "Ans":None,
        "Path":{
            "yes":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3ZZGc7vyWgWEmmsu91beljb96b2-Fc86kRw&usqp=CAU",
            "No":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyl6Biu6a_LP1osZtemFrXox3P1w9xBYB2CFr250rMpUtWxJphbd4ALxHrLg1FaAp3Ujc&usqp=CAU"
        },
        },
    6:{
        "Ques":"Is the ladder have a secure extension present on the construction site?",
        "options":["yes","No"],
        "Ans":None,
        "Path":{
            "yes":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5tzfV1wKtEZS5LteBc5_avFbWhBF9OYlt8A&usqp=CAU",
            "No":"https://simplifiedsafety.com/media/wysiwyg/ladder-safety/extension_ladder.jpg",

        },
        },
    7:{
        "ques":"Is there  Proper method are used on Construction site?",
        "options":["yes","no"],
        "Ans":None,
        "Path":{
            "yes":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5tzfV1wKtEZS5LteBc5_avFbWhBF9OYlt8A&usqp=CAU",
            "No":"https://cdn11.bigcommerce.com/s-nu76q5988i/images/stencil/1280x1280/products/6990/3167/P6206-mk2_PI_jpeg1000__42923.1512058332.jpg",

        },
        },
    8:{
        "Ques":"Is the worker Carrying something while climbing the ladder?",
        "Options":["yes","No"],
        "Ans":None,
        "Path":{
            "Yes":"https://image1.masterfile.com/getImage/NjMyLTAyODg1MzE2ZW4uMDAwMDAwMDA=AMfpYJ/632-02885316en_Masterfile.jpg",
            "No":"https://cdn9.dissolve.com/p/D984_45_337/D984_45_337_1200.jpg",
        },
        },
    9:{
        "Ques":"Is worker wear proper footwear on construction site?",
        "Options":["Yes","No"],
        "Ans":None,
        "path":{
            "yes":"https://previews.123rf.com/images/federicofoto/federicofoto1408/federicofoto140800054/30502872-construction-worker-with-yellow-boots-and-a-spanner-in-roadworks.jpg",
            "No":"https://previews.123rf.com/images/kwangmoo/kwangmoo1801/kwangmoo180100321/93656945-il-muratore-con-le-scarpe-di-cuoio-fa-un-passo-sull-unghia-al-cantiere-concetto-di-incidente-di-lavo.jpg",

        },
        },
}

answers = [ 0, 0, 0, 0, 0, 0 ,0, 0, 0]

@app.route('/out', methods = ['POST'])
def out():
    input = np.array(answers).reshape(1, -1)
    safe = pickle.load(open('safe.sav', 'rb'))
    severe = pickle.load(open('severe.sav', 'rb'))
    inj = pickle.load(open('inj.sav', 'rb'))
    print(input)
    s = safe.predict(input).tolist()[0]
    se = severe.predict(input).tolist()[0]
    inj = inj.predict(input).tolist()[0]
    print(s, se, inj)
    return {"safe": s, "severe": se, "injured": inj}

@app.route('/Question', methods=['POST'])
def Ques():
    req=request.get_json()
    if req['Ans'] != None:
        Question[req['input']]['Ans'] = req['Ans']
        answers[req['input'] - 1] =  req['Ans']
        return Question[req["input"]]

    return Question[req["input"]]





if __name__ =='__main__':
    app.run(debug=True, port=9090)































