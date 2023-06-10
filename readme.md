## 数据库配置
pip3 install flask-sqlalchemy

pip3 install flask_migrate

flask db init

flask db migrate -m "Initial migrate"

flask db upgrade

## 生成jwt token 验证信息
pip3 install pyjwt

## 生成requirement.txt
pip3 freeze > requirement.txt
## 虚拟环境安装对应的依赖
创建虚拟环境: python3 -m venv env
进入已有虚拟环境: source env/bin/activate

pip3 install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


## 自用的简单部署
nohup python3 app.py &