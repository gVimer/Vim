from xml.etree import ElementTree
def PareTreeNode(Tree,Num):
  Data=[]
  for nIndex,Item in enumerate(Tree.find("target")):
    if Item.get("line-number")==str(Num):
      TimeDesc= Item.find("commit").find("date"   ).text
      Date    = __import__("re").compile("T.*").sub("",TimeDesc)
      Version = Item.find("commit").get("revision")
      Name    = Item.find("commit").find("author" ).text
      return Date+" "+Version+" "+Name.upper()
if __name__ == "__main__":
  ArgOfFilePath=__import__("sys").argv
  if len(ArgOfFilePath)==3:
    pHandler= __import__("os").popen('SVN BLAME --xml '.lower()+ArgOfFilePath[1])
    XmlData = pHandler.buffer.read().decode(encoding='UTF-8')
    Info=PareTreeNode(ElementTree.fromstring(XmlData),ArgOfFilePath[2])
    __import__("sys").stdout.write(Info)
        
