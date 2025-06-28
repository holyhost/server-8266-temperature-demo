from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# 缓存所有数据
all_data = [
    {
    "cur_time": "20250628121738",
    "humidity": "82.6",
    "temperature": "29"
    },
    {
    "cur_time": "20250628121741",
    "humidity": "84.6",
    "temperature": "30"
    },
    {
    "cur_time": "20250628121745",
    "humidity": "83.8",
    "temperature": "31"
    },
    {
    "cur_time": "20250628121748",
    "humidity": "80.6",
    "temperature": "32"
    },
    {
    "cur_time": "20250628121752",
    "humidity": "83.1",
    "temperature": "33"
    },
    {
    "cur_time": "20250628121756",
    "humidity": "81.1",
    "temperature": "30"
    }
]

@app.route("/")
@app.route("/home")
@app.route("/th")
def hello_world():
    # 获取最新100条数据
    temperature_and_humidity_data = all_data[-100:]
    # 准备 一个月的数据，一周的数据，一天的数据，这里只设置最新100条数据
    result = {
        'monthdata': [],
        'weekdata': [],
        'daydata':[], 
        'recentdata': temperature_and_humidity_data
    }
    return render_template('th.html', data_list=result)


@app.route("/getdata")
def getdata():
    return all_data


@app.route("/temperature", methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':
        print('this is POST request')
        return 'post 请求 成功！'
    elif request.method == 'GET':
        print('this is GET request')
        temperature = request.args.get('temperature', '')
        humidity = request.args.get('humidity', '')
        print(f'温度={temperature}, 湿度={humidity}')
        cur_time = datetime.now().strftime('%Y%m%d%H%M%S')
        # 存到缓存里面,
        all_data.append(
            {
                'cur_time': cur_time,
                'temperature': temperature,
                'humidity': humidity
            }
        )
        print(cur_time)
        # 获取当前时间
        
        return 'get 请求 成功！'
    
    return "接口请求 成功！"