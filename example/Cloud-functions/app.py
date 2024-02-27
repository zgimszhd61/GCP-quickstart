# 导入functions_framework模块以便使用Google Cloud Functions
import functions_framework

# 使用functions_framework.http装饰器定义一个HTTP Cloud Function
@functions_framework.http
def hello_http(request):
    """
    HTTP Cloud Function。
    Args:
        request (flask.Request): Flask框架中的请求对象，用于获取HTTP请求的信息。
        参见 https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data
    Returns:
        返回响应文本，或者任何可以被转换成Response对象的值集合。
        使用 `make_response` 方法进行转换。
        参见 https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response。
    """
    # 尝试从请求体中以JSON格式获取数据，如果没有数据或不是JSON格式，则返回None
    request_json = request.get_json(silent=True)
    # 尝试从URL的查询参数中获取数据
    request_args = request.args

    # 如果请求中的JSON数据包含'name'键，使用该值作为名字
    if request_json and 'name' in request_json:
        name = request_json['name']
    # 如果URL查询参数中包含'name'，使用该值作为名字
    elif request_args and 'name' in request_args:
        name = request_args['name']
    # 如果都没有提供'name'，则默认使用'World'作为名字
    else:
        name = 'World'
    # 返回对应的问候语
    return 'Hello {}!'.format(name)
