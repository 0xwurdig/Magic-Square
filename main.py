import requests

host = "0.0.0.0"
program_name = "magic_square.aleo"
endpoint = f"http://{host}:3030/testnet3/program/{program_name}"

response = requests.get(endpoint)

content = response.content.decode('utf-8').strip('"').split("\\n")

print(endpoint)

for line in content:
    print(line)


#   Private Key  APrivateKey1zkp8CZNn3yeCseEtxuVPbDCwSyhGW6yZKUYKfgXmcpoGPWH
#      View Key  AViewKey1mSnpFFC8Mj4fXbK5YiWgZ3mjiV8CxA79bYNa8ymUpTrw
#       Address  aleo1rhgdu77hgyqd3xjj8ucu3jj9r2krwz6mnzyd80gncr5fxcwlh5rsvzp9px
