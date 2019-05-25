
### 创建新用户
请求url:http://127.0.0.1:8000/api/app_1/reg
请求方式:POST

|  请求参数   | 类型   | 说明       | 是否必填 | 返回参数 | 备注 |
| :---------: | ------ | ---------- | -------- | -------- | ---- |
|  username   | string | 设置用户名 | Y        | code     |      |
|  password   | string | 设置密码   | Y        | mesage   |      |
| re_password | string | 确认密码   | Y        |          |      |  
  
<br>
<br>

### 登录
请求url:http://127.0.0.1:8000/api/app_1/login

请求方式:POST

| 请求参数 | 类型   | 说明   | 是否必填 | 返回参数 | 备注 |
| -------- | ------ | ------ | -------- | -------- | ---- |
| username | string | 用户名 | Y        | code     |      |
| password | string | 密码   | Y        | mesage   |      |


<br>
<br>

### 获取所有数据简介
请求url:http://127.0.0.1:8000/api/app_1/home



请求方式:GET

| 返回参数 | 参数类型 | 备注 |
| -------- | -------- | ---- |
| data     | object   |      |


<br>
<br>

### 获取当前用户所创建的全部数据
请求url:http://127.0.0.1:8000/api/app_1/my


请求方式:GET

| 返回参数 | 参数类型 | 备注 |
| -------- | -------- | ---- |
| data     | object   |      |



<br>
<br>


### 获取单个详细数据
请求url:http://127.0.0.1:8000/api/app_1/content/1/
请求方式:GET

| 返回参数 | 参数类型 | 备注 |
| -------- | -------- | ---- |
| data     | object   |      |
