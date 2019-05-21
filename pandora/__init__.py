# -*- coding: utf-8 -*-
import flask


def create_app():
    app = flask.Flask(__name__)

    @app.route('/')
    def index():
        """
        只有 Hello World 的首页
        :return:
        """
        return "Hello, world!"

    # TODO: 捕获 404 错误，返回 404.html
    @app.errorhandler(404)
    def page_not_found(error):
        """
        以此项目中的404.html作为此Web Server工作时的404错误页
        """
        return flask.render_template("404.html"),404

    # TODO: 完成接受 HTTP_URL 的 picture_reshape
    # TODO: 完成接受相对路径的 picture_reshape
    @app.route('/pic', methods=['GET'])
    def picture_reshape():
        """
        **请使用 PIL 进行本函数的编写**
        获取请求的 query_string 中携带的 b64_url 值
        从 b64_url 下载一张图片的 base64 编码，reshape 转为 100*100，并开启抗锯齿（ANTIALIAS）
        对 reshape 后的图片分别使用 base64 与 md5 进行编码，以 JSON 格式返回，参数与返回格式如下
        
        :param: b64_url: 
            本题的 b64_url 以 arguments 的形式给出，可能会出现两种输入
            1. 一个 HTTP URL，指向一张 PNG 图片的 base64 编码结果
            2. 一个 TXT 文本文件的文件名，该 TXT 文本文件包含一张 PNG 图片的 base64 编码结果
                此 TXT 需要通过 SSH 从服务器中获取，并下载到`pandora`文件夹下，具体请参考挑战说明
        
        :return: JSON
        {
            "md5": <图片reshape后的md5编码: str>,
            "base64_picture": <图片reshape后的base64编码: str>
        }
        """
        from PIL import Image
        import requests
        import base64
        import hashlib
        import json
        url = str(flask.request.query_string,encoding='utf8')
        try:
            with open(url) as f:
                data = f.read()
        except :
            res = requests.get(url)
            data = res.text
        data = base64.b64decode(data)
        with open("temp.png","wb") as f:
            f.write(data)
        
        img = Image.open("temp.png")
        
        img = img.resize((100, 100),Image.ANTIALIAS)

        img.save("temp.png")
        
        with open("temp.png","rb") as f:
            data = f.read()

        md5_png = hashlib.md5(data).hexdigest()
        
        
        
        bs64_png = str(base64.b64encode(data),encoding='utf8')
        

        result_data = {"md5":md5_png,"base64_picture":bs64_png}
        
        return json.dumps(result_data)

    @app.route('/bs64png', methods=['GET'])
    def picture_get():
        return open("img.txt").read()


    # TODO: 爬取 996.icu Repo，获取企业名单
    @app.route('/996')
    def company_996():
        """
        从 github.com/996icu/996.ICU 项目中获取所有的已确认是996的公司名单，并

        :return: 以 JSON List 的格式返回，格式如下
        [{
            "city": <city_name 城市名称>,
            "company": <company_name 公司名称>,
            "exposure_time": <exposure_time 曝光时间>,
            "description": <description 描述>
        }, ...]
        """
        import json
        res_list = []
        with open("data.txt",encoding='utf16') as f:
            for x in f.readlines():
                if x[0]=='\t':
                    continue
                else:
                    line_data = x.strip().split('\t')
                    temp_dict = {}
                    temp_dict["city"] = line_data[0]
                    temp_dict["company"] = line_data[1]
                    temp_dict["exposure_time"] = line_data[2]
                    temp_dict["cidescriptionty"] = line_data[3]
                    res_list.append(temp_dict)
                    
                    
        return json.dumps(res_list)

    return app

