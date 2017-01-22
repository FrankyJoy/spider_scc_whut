##网页输出器
import  os
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        for data in self.datas:
            with open(data['title']+'.html','w') as fout:
                fout.write("<html>")
                fout.write("<head>""<meta http-equiv='content-type' content='text/html;charset=utf-8'>""</head>")
                fout.write("<body>")
                fout.write("<table>")
                fout.write("<tr>")
                ##fout.write("<td>%s</td>" % data['url'])
                fout.write("<h1>%s</h1>" % data['title'])
                fout.write("<td>%s</td>" % data['summary'])
                fout.write("</tr>")
                fout.write("</table>")
                fout.write("</body>")
                fout.write("</html>")
                fout.close()


        # fout = open('output.html', 'w')
        # fout.write("<html>")
        # fout.write("<body>").encode('utf-8')
        # fout.write("<table>").encode('utf-8')
        #
        # for data in self.datas:
        #     fout.write("<tr>")
        #     fout.write("<td>%s</td>" % data['url'])
        #     fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
        #     ##fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
        #     fout.write("</tr>")
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        # fout.close()