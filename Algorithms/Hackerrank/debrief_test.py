import requests

host = 'https://lightsoncrt.cerner.com/aura/rest/'
credentials = {'username': 'UCLON', 'password': 'T3u6Cf5gA8uVd8Jx'}
session = requests.session()
response_json = session.post('{}auth/token/'.format(host), data=credentials).json()

session.headers['Authorization'] = 'Bearer {}'.format(response_json['token'])

next_url_1 = '{}user-experience/'.format(host)
next_url_2 = '{}timer/'.format(host)
response_json_1 = session.get(next_url_1).json()
response_json_2 = session.get(next_url_2).json()
main_url_1 = response_json_1['services']['environment-daily']+str('?physician_indicator=2')
main_url_2 = response_json_2['services']['environment-daily']+str('?physician_indicator=2')
# url_domain = '&domain__name='
url_domain = '&domain__id__in='
url_date = '&transaction_date__range='
url_list = []

next_url_3 = '{0}clients/?domains__name={1}&mnemonic={2}&domains__is_production=True'.format(
    host, 'PROD', 'SMRC_QA')
clients_list = session.get(next_url_3).json()
print(next_url_3)
clients_list = clients_list['results']
domain_id_list = []
print(clients_list)
for client in clients_list:
    if client['mnemonic'] == 'SMRC_QA':
        for domain in client['domains']:
            if domain['id'] not in domain_id_list:
                domain_id_list.append(domain['id'])

print(domain_id_list)
