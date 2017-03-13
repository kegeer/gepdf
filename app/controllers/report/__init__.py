from os import path
import pdfkit

from flask import render_template, Blueprint, request, url_for, redirect, make_response

from app.models import db, Client, Result

report_blueprint = Blueprint(
    'report',
    __name__,
    template_folder=path.join(path.pardir, path.pardir, 'templates', 'report'),
    url_prefix='/report'
)


@report_blueprint.route('/')
def home():
    clients = Client.query.order_by(
        Client.name.desc()
    ).all()
    return render_template('home.html',
                           clients=clients)
@report_blueprint.route('/clients')
def clients():
    # 创建依机构建立的列表
    return render_template('clients.html')

@report_blueprint.route('/clients/<string:client_id>')
def client(client_id):
    client = Client.query.get_or_404(client_id)

    return render_template('client.html',
                           client=client)

@report_blueprint.route('/clients/new', methods=['GET', 'POST'])
def new_client():
    pass


@report_blueprint.route('/client/<string:client_id>/report')
def client_report(client_id):
    client = Client.query.get_or_404(client_id)
    result = Result.query.filter_by(client_id=client_id).first()

    return render_template('report.html',
                           client=client,
                           result=result, )
@report_blueprint.route('/client/<string:client_id>/report/print', methods=['POST'])
def client_report_print(client_id):
    if request.method == 'POST':
        page = client_report(client_id)
        css = path.join(path.dirname(__file__), '../../static/css/mendel.css').replace('\\', '/')
        pdf = pdfkit.from_string(page, False, css=css)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        return response
    else:
        return redirect(url_for('.client_report', client_id=client_id))