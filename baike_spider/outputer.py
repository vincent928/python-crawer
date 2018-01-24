# -*- coding: utf-8 -*-
# html输出器


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output/output.html', 'w')

        fout.write("<html>")
        fout.write("<head><meta chaset='utf-8'></head>")
        fout.write("<body>")
        fout.write("<table>")

        # python默认编码格式ascii ，需要转成utf-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"% data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('UTF-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()