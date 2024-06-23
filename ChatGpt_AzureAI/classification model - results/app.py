import numpy as np


from flask import Flask,request,render_template,jsonify
import utils

model = utils.Model()


app = Flask(__name__)
@app.route('/')
def home():

    #return jsonify({"Health check":"Ok"})

    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def result():
    try:
    #data = request.form

    #print("Data:::",data)

    #Value = data['text']

    #print("text:",Value)

    #input_list = [data for data in Value.split(';')]

    # print("input_list::",input_list)

    # out = model.prediction(input_list)



    # ouput_list = list(zip(input_list,out))

    # #dict1 = {"data":,"Target Column":}
    # dict1 = {}

    # for ind,data in enumerate(input_list):

    #     dict1.update({f"data_{ind}":data , f"Target Column_{ind}":out[ind]})

    # print("Dictionary::",dict1)
    # #return jsonify({"Result {data : Target column}:": ouput_list})

    # #return render_template('index.html',prediction=ouput_list)

        if request.method == "GET":

            data = request.args.get

            print("Data:::",data)

            Value = data(('text'))

            print("text:",Value)

            input_list = [data for data in Value.split(';')]

            print("input_list::",input_list)

            out = model.prediction(input_list)


            ouput_list = list(zip(input_list,out))

            #dict1 = {"data":,"Target Column":}
            dict1 = {}

            for ind,data in enumerate(input_list):

                dict1.update({f"data_{ind}":data , f"Target Column_{ind}":out[ind]})

            print("Dictionary::",dict1)
            #return jsonify({"Result {data : Target column}:": ouput_list})

            return render_template('index.html',prediction=ouput_list)

        else:
            

            data = request.form.get

            print("Data:::",data)

            Value = data(('text'))

            print("text:",Value)

            input_list = [data for data in Value.split(';')]

            print("input_list::",input_list)

            out = model.prediction(input_list)


            ouput_list = list(zip(input_list,out))

            #dict1 = {"data":,"Target Column":}
            dict1 = {}

            for ind,data in enumerate(input_list):

                dict1.update({f"data_{ind}":data , f"Target Column_{ind}":out[ind]})

            print("Dictionary::",dict1)
            #return jsonify({"Result {data : Target column}:": ouput_list})

            return render_template('index.html',prediction=ouput_list)
        
    except Exception as e:
        print("Error: ",e)





if __name__ == "__main__":
    app.run(debug=True)  # For local testing
