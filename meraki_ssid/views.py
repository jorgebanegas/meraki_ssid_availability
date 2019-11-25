from flask import Blueprint, render_template, request
import json
import requests

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('collage.html')

@main.route('/list')
def list():
    return render_template('list.html')

@main.route('/bar')
def bar():
    return render_template('sidebar.html')

@main.route('/meraki')
def meraki():
    url = "https://dashboard.meraki.com/api/v0/"
    url2 = "https://dashboard.meraki.com/api/v0/networks/L_646829496481103974/ssids"
    headers = {
            'X-Cisco-Meraki-API-Key': "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
        }

    response = requests.request("GET", url + "organizations", headers=headers)
    json_data = json.loads(response.text)
    org_id = json_data[0]['id']
    org = json_data[0]
    print(json_data, "\n\n")

    response = requests.request("GET", url + "organizations/" + org_id + "/networks", headers=headers)

    json_data = json.loads(response.text)
    network_id = json_data[0]['id']
    print(json_data, "\n\n")

    response = requests.request("GET", url + "/networks/" + network_id + "ssids", headers=headers)

    response = requests.request("GET", url2, headers=headers)
    json_data = json.loads(response.text)
    print(json_data, "\n\n")
    print(org)
    return render_template('meraki.html',ssids = json_data, org = org)

@main.route('/meraki', methods=['POST','GET']) 
def meraki_post():
    ssid = request.form.get("input-type-select")
    return f'{ssid}'
