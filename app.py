from flask import Flask, render_template
import datetime
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamo:8000")


def put_time():

    table = dynamodb.Table('Logs')
    response = table.put_item(
        Item={
            'time': str(datetime.datetime.now())
        }
    )
    return response


def scan_times():
    table = dynamodb.Table('Logs')
    response = table.scan()

    return response['Items']


@app.route('/')
def hello():
    put_time()
    times = scan_times()
    return render_template('index.html', times=times)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
