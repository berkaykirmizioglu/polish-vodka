from flask import Flask, render_template, flash
from forms import AgeForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e60707cfcb4754c3e3ae5f362650ffcd'


@app.route("/", methods=['GET', 'POST'])
def home():
    form = AgeForm()
    if form.validate_on_submit():
        flash(f'Now you can navigate to our homepage!', 'success')
    return render_template('home.html', title='Age Form', form=form)


if __name__ == '__main__':
    app.run(debug=True)
