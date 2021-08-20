from flask import Flask, render_template, request
import requests
import smtplib

my_email = "faheemzaini14@gmail.com"
password = "Er00r404"

app = Flask(__name__)

blog_url = "https://api.npoint.io/0b66dc372b0813481edf"
response = requests.get(blog_url)
blog_posts = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post<num>")
def blog(num):
    num = int(num)-1
    return render_template("post.html", id=num, heading=blog_posts[num]['title'], sub=blog_posts[num]['subtitle'],
                           main=blog_posts[num]['body'])


@app.route('/success', methods=['POST'])
def send_mail():
    u_name = request.form['username']
    email = request.form['email_id']
    phone = request.form['phone_no']
    message = request.form['message']
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='zainifaheem@gmail.com',
                            msg=f"NAME: {u_name}/nEMAIL: {email}/nPHONE: {phone}/nMESSAGE: {message}")
    return '<h3 style="color: blue">Success! You can go back and check out' \
           ' other things in this blog. We will contact you soon!</h3>'


if __name__ == '__main__':
    app.run(debug=True)
