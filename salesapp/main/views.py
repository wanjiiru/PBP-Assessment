import matplotlib
from flask import render_template, redirect, url_for

from . import main
from ..forms import UploadFileForm


@main.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('upload.html', form=form)


@main.route('/main')
def home():
    return render_template('index.html')


@main.route('/barGraph')
def bar_graph():
    # libraries
    import numpy as np
    import matplotlib.pyplot as plt
    x_axis = []
    y_axis = []

    from salesapp.models.invoice import Invoice
    top_five = Invoice.query.order_by(Invoice.quantity.desc()).limit(5).all()
    for i in top_five:
        x_axis.append(i.contact_name)
        y_axis.append(i.quantity)

        # Make  dataset
    height = x_axis
    bars = y_axis
    y_pos = np.arange(len(bars))

    # Create horizontal bars
    plt.barh(y_pos, height)

    # Create names on the y-axis
    plt.yticks(y_pos, bars)

    # Show graph
    # plt.show()
    plt.savefig('salesapp/static/images/bar.png')

    return render_template('index.html', name='Bar Graph', url='/static/images/bar.png')


@main.route('/table')
def table():
    import matplotlib.pyplot as plt
    x = [2, 4, 6]
    y = [1, 3, 5]
    plt.plot(x, y)
    # plt.show()
    xx = plt.savefig('salesapp/static/images')
    print(xx)
    return render_template('index.html', name='Table', url='/static/images/table.png')
