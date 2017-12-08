#coding:utf-8
from xml.dom import minidom
import codecs

#写入xml文档的方法
def create_xml_test(filename):
    #新建xml文档对象
    xml = minidom.Document()

    #创建第一个节点，第一个节点就是根节点了
    root = xml.createElement('root')

    #写入属性（xmlns:xsi是命名空间，同样还可以写入xsi:schemaLocation指定xsd文件）
    root.setAttribute("xmlns:xsi","http://www.xxx.com")

    #创建节点后，还需要添加到文档中才有效
    xml.appendChild(root)

    #创建节点，添加到根节点
    text_node = xml.createElement('element')
    text_node.setAttribute('id',"hai")
    root.appendChild(text_node)

    #给text_node节点加入文本，文本也是一种节点
    text = xml.createTextNode('hello world')
    text_node.appendChild(text)

    #一个节点加了文本之后，还可以继续追加其他东西
    tag = xml.createElement('tag')
    tag.setAttribute('data','tag data')
    text_node.appendChild(tag)

    #写好之后，就需要保持文档了
    fp = open(filename,"w")
    xml.writexml(fp,indent="\t", newl="\n", encoding="utf-8")
    fp.close()

if __name__ == "__main__":
    #在当前目录下，创建new.xml
    create_xml_test('new.xml')