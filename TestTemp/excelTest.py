#! /usr/bin/env python
#encoding=utf-8
#author=zgd
import xlwt

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()   # 初始化样式
    font = xlwt.Font()       # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def write_excel(path):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('50013')
    # row0 = [u'company', u'rspdesc',  'rsp_content']
    row1 = [u'250', 'json result is null...','response":{"rspCode":"20506","rspDesc":"json result is null..."},"transIDO":"de4ad6cb256942bd9010ea81d5c7bada"}']
    row2 = [u'210', 'success','response":{"rspCode":"20506","rspDesc":"json result is null..."},"transIDO":"de4ad6cb256942bd9010ea81d5c7bada"}']

    # 生成第一行和第二行
    for i in range(len(row2)):
        # data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))

    # 保存文件
    # workbook.save('demo.xls')
    path = "../TestReport/data.xls"
    workbook.save(path)


if __name__ == '__main__':
    # 设置路径

    print(u'创建demo.xls文件成功')










