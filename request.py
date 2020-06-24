import requests
import json
import click as ck

@ck.command()
@ck.option('--url', '-u', default='http://localhost:8000', help='url to query demo at')
@ck.option('--api_endpoint', '-a', default='/predict', help='api endpoint for bidaf model')
@ck.option('--data', '-d', default='data.json', help='json body for the request')
@ck.option('--output_file', '-o', default='out.json', help='saves response body to it') 
def main(url, api_endpoint, data, output_file):
  actual_url = url + api_endpoint
  req_body = open(data,)
  r = requests.post(url = actual_url, data = json.dumps(json.load(req_body)))
  with open(output_file, "w") as resp_body:
    json.dump(r.json(), resp_body, indent=4)
  

if __name__ == '__main__':
    main()

