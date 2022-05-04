import subprocess

def lambda_handler(event, context):
    input_path = '/function/' + event['input']
    output_path = '/function/' + event['output']
    try:
        subprocess.run(['usd_from_gltf', input_path, output_path], check=True, stdout=subprocess.PIPE)
        return {
            'status': 'success'
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
