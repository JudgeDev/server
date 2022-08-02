import epo_ops

print("Testing CII")

client = epo_ops.Client(
    key=" CPNmxLeOmOGqljxpALAGi3AQSQu078d2", secret="1IYeDbsalQAWx18E"
)  # Instantiate client

"""
response = client.published_data(  # Retrieve bibliography data
  reference_type = 'publication',  # publication, application, priority
  # original, docdb, epodoc
  input = epo_ops.models.Docdb('1000000', 'EP', 'A1')
  endpoint = 'claims',  # optional, defaults to biblio
  constituents = []  # optional, list of constituents
)
response = client.published_data_search(  # search data
  cql = 'pn=EP and 2020 and ipc=G06Q',  #
  range_begin = 1,  #
  range_end = 4,  #
  constituents = ['abstract']  # optional, list of constituents
)
"""

response = client.register_search(  # search data
    cql="grd=06.2022 and ic=G06Q",  #
    range_begin=1,  #
    range_end=4,  #
)

print(response.text)
