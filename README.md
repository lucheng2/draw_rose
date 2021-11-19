# 送给吴欢的玫瑰花

- 使用turtle库画一朵玫瑰花

- 原理：

分析`原图`得到像素点数据，依靠这些数据画出一朵玫瑰花。
分析过程：用pillow读图片，转为灰度图，将阈值内的像素坐标记录成数组。
画图过程：用打印散点的方式，画图

![原图.jpg](原图.jpg) 

- 运行环境
  `python3 + 第三方包`
  ```bash
  pip install -r requirements.txt
  ```
- 运行
    ```bash
    python draw_rose.py
    ```
