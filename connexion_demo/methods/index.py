

def index() -> str:
    methods = [
        {'url': '/', 'method': '[get]', 'name': '根目录', 'desc': '获取api的所有信息', 'required': None},
        {'url': '/auth/login', 'method': '[post]', 'name': '登陆', 'desc': '获取用户token',
         'required': 'username(str)，password(str)'},
        {'url': '/hello', 'method': '[get]', 'name': 'say hello', 'desc': 'say hello',
         'required': 'token'},
    ]
    string = ''
    for method in methods:
        string += f"{method['url']} {method['method']}, {method['name']}," \
                  f" {method['desc']}, required: {method['required']} \r\n"
    return string


def hello() -> str:
    return "hello"
