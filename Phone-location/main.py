from flask import Flask,request,render_template
import requests

app=Flask(__name__)

key="" # use your own api key 

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        country_code=request.form.get('code')
        phone_no=request.form.get('phone')
        final_no= '+' + country_code + phone_no
        url= f"https://phonevalidation.abstractapi.com/v1/?api_key={key}&phone={final_no}"
        response = requests.get(url)
        data=response.json()

        ph_no=(data['phone'])
        c_nm=(data['country']['name'])
        c_code=(data['country']['prefix'])
        device=(data['type'])
        retailer=(data['carrier'])

        return render_template('home.html',ph_no=ph_no,
                               c_nm=c_nm,c_code=c_code,device=device,retailer=retailer)
        
    return render_template('home.html')

 
if __name__=='__main__':
    app.run(debug=True)




