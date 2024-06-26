from flask import Flask, jsonify,request

from student import Student

app=Flask(__name__)

## API
# route or an endpoint.
## Using our Orm to handle requests.

# API 
# MODEL VIEW CONTROLLER

# CREATE<POST> READ(GET) UPDATE<PUT> DELETE<DELETE>

@app.route("/")
def hello_world():
    return "Welcome to my students API !"

@app.route("/student",methods=["GET"])
def students_list():
    st=Student()
    ls=st.list()
    return jsonify(ls)

@app.route("/student",methods=["POST"])
def add_student():
 
    data=request.get_json()
    print(data)

    if not data:
        return jsonify({"message":"No json received"}),400
    
    name=data.get('name') # data.name =undefined,data['name']
    email=data.get('email')

    if  name is None or email is None:
        return jsonify({'message':"Required fields missing. ie name or email"}), 400

    st=Student()
    db_res=st.add(data['name'],data['email'])
    if db_res is None:
        return jsonify({'message':"Failed to add student"}), 400
    return jsonify(db_res),201

if __name__ == "__main__":
    app.run(debug=True)