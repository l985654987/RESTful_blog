请求url:http://127.0.0.1:8000/api/app_1/reg

说明:创建新用户

请求方式:POST

|  请求参数   | 类型   | 说明       | 是否必填 | 返回参数 | 备注 |
| :---------: | ------ | ---------- | -------- | -------- | ---- |
|  username   | string | 设置用户名 | Y        | code     |      |
|  password   | string | 设置密码   | Y        | mesage   |      |
| re_password | string | 确认密码   | Y        |          |      |  
  
    
      





请求url:http://127.0.0.1:8000/api/app_1/login

说明:登录

请求方式:POST

| 请求参数 | 类型   | 说明   | 是否必填 | 返回参数 | 备注 |
| -------- | ------ | ------ | -------- | -------- | ---- |
| username | string | 用户名 | Y        | code     |      |
| password | string | 密码   | Y        | mesage   |      |





请求url:http://127.0.0.1:8000/api/app_1/home

说明:获取所有数据

请求方式:GET

| 返回参数 | 参数类型 | 备注 |
| -------- | -------- | ---- |
| data     | object   |      |





请求url:http://127.0.0.1:8000/api/app_1/my

说明:获取当前用户所创建的全部数据

请求方式:GET

| 返回参数 | 参数类型 | 备注 |
| -------- | -------- | ---- |
| data     | object   |      |







请求url:http://127.0.0.1:8000/api/app_1/content/1/

说明:获取单个数据

请求方式:GET

| 返回参数 | 参数类型 | 备注 |
| -------- | -------- | ---- |
| data     | object   |      |
