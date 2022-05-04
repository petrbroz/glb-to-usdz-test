import requests
import subprocess

def lambda_handler(event, context):
    url = event['url']
    input_path = '/tmp/input.glb'
    output_path = '/tmp/output.usdz'
    try:
        print('Downloading file')
        r = requests.get(url, allow_redirects=True)
        open(input_path, 'wb').write(r.content)
        print('Converting file')
        subprocess.run(['usd_from_gltf', input_path, output_path], check=True, stdout=subprocess.PIPE)
        return {
            'status': 'success'
        }
    except requests.exceptions.RequestException as err:
        print(err)
        return {
            'status': 'failed',
            'message': 'Download failed'
        }
    except subprocess.CalledProcessError as err:
        print(err)
        return {
            'status': 'failed',
            'message': 'Conversion failed'
        }
    except Exception as err:
        print(err)
        return {
            'status': 'failed',
            'message': 'Unknown error'
        }
