import xml.etree.cElementTree as ET
import random

title = "Test"
alldata = {}
myAttrib = {"as":"geometry"}
objectOffsetX = 250
dbOffsetX = 300
arrowOffsetY = 80

mxfile = ET.Element("mxfile",host="app.diagrams.net" ,agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" ,version="25.0.1")
diagram = ET.SubElement(mxfile,"diagram", name=title, id="zV9YV6nwBBEvuBxtZrv_")
mxGraphModel = ET.SubElement(diagram,"mxGraphModel",dx="1434", dy="746", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="850", pageHeight="1100", math="0", pageName=title, shadow="0")
root = ET.SubElement(mxGraphModel,"root")
ET.SubElement(root,"mxCell" ,id="0")
ET.SubElement(root,"mxCell", id="1" ,parent="0" )

def createDispatchArrow(sourceX,targetX,value,id):
    mxCellTemp = ET.SubElement(root,"mxCell",id=id, value=value ,style="endArrow=classic;html=1;rounded=0;", edge="1",   parent="1")
    mxGeometry = ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib, x="-0.1086", y="10", width="50", height="50", relative="1" ) 
    ET.SubElement(mxGeometry,"Array", attrib={"as":"points"})
    ET.SubElement(mxGeometry,"mxPoint",x=sourceX, y=str(10 + (int(id)-8)*arrowOffsetY), attrib={"as":"sourcePoint"})
    ET.SubElement(mxGeometry,"mxPoint",x=targetX, y=str(10 + (int(id)-8)*arrowOffsetY), attrib={"as":"targetPoint"})
    ET.SubElement(mxGeometry,"mxPoint",relative="1" , attrib={"as":"offset"})

def createReturnArrow(sourceX,targetX,value,id):
      mxCellTemp = ET.SubElement(root,"mxCell",id=id,value=value, style="html=1;endArrow=open;dashed=1;curved=0;rounded=0;", edge="1", parent="1")
      mxGeometry = ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib,relative="1",x="-0.1086", y="10" ,width="50", height="50")
      ET.SubElement(mxGeometry,"Array",attrib={"as":"points"})
      ET.SubElement(mxGeometry,"mxPoint",x=sourceX, y=str(10 + (int(id)-8)*arrowOffsetY), attrib={"as":"sourcePoint"})
      ET.SubElement(mxGeometry,"mxPoint",x=targetX, y=str(10 + (int(id)-8)*arrowOffsetY), attrib={"as":"targetPoint"})
      ET.SubElement(mxGeometry,"mxPoint",relative="1" , attrib={"as":"offset"})

def createObjects(type,offsetX,value,id):
    if(type == "user"):
      mxCellTemp = ET.SubElement(root,"mxCell",id=id, value="" ,style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={'curved':0,'rounded':0};participant=umlActor;", vertex="1", parent="1")
      ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib, x="30", y="80", width="20", height="1000" )
    else:
      mxCellTemp = ET.SubElement(root,"mxCell",id=id, value=value, style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={'curved':0,'rounded':0};", vertex="1", parent="1")
      ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib,x=offsetX, y="80", width="100", height="1000" )

def createTextBox(endpoint,method,posX,posY,id):
    mxCellTemp = ET.SubElement(root,"mxCell",id=id,value="endpoint:/"+endpoint+"<div>method:"+method+"</div>", style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;", vertex="1" ,parent="1")  
    ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib,x=posX, y=posY, width="140", height="40")

def createBlockElements(type,offsetX,value,id):
    if(type == "title"):
      mxCellTemp = ET.SubElement(root,"mxCell",id=id ,value="<span style='font-family: Delivery-Bold, sans-serif; text-align: left; background-color: rgb(255, 255, 255);'><font style='font-size: 14px;'>"+value+"</font></span>", style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontStyle=1", vertex="1" ,parent="1")
      ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib,x="30",y="20",width="110",height="30")     
    elif(type == "db"):
      mxCellTemp = ET.SubElement(root,"mxCell",id=id, value=value, style="verticalAlign=middle;align=center;spacingTop=8;spacingLeft=2;spacingRight=12;shape=cube;size=10;direction=south;fontStyle=4;html=1;whiteSpace=wrap;", vertex="1", parent="1")
      ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib,x=offsetX, y="200", width="260", height="350" )    
    elif(type == "activeLineB"):
      mxCellTemp = ET.SubElement(root,"mxCell",id="6", value=value, style="html=1;points=[[0,0,0,0,5],[0,1,0,0,-5],[1,0,0,0,5],[1,1,0,0,-5]];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={'curved':0,'rounded':0};", vertex="1", parent="3")
      ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib, x="45", y="90", width="10", height="220" )
    elif(type == "activeLineF"):
      mxCellTemp = ET.SubElement(root,"mxCell",id="7", value=value, style="html=1;points=[[0,0,0,0,5],[0,1,0,0,-5],[1,0,0,0,5],[1,1,0,0,-5]];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={';curved';:0,';rounded';:0};", vertex="1", parent="4")
      ET.SubElement(mxCellTemp,"mxGeometry", attrib=myAttrib, x="45", y="90", width="10", height="220")


basicSetup = "title/"+title+";user/x;front/Frontend;back/Backend;db/Database"
setUpArray = basicSetup.split(";")
for i in range(len(setUpArray)):
  id = i+3
  obj = setUpArray[i].split("/")
  if(obj[0]=="user"):
    createObjects(obj[0],"",obj[1],str(id)) 
    alldata["user"]= {"id":"8","x":"30", "y":"80", "width":"20", "height":"400"} 
  elif(obj[0]=="db"):
    offsetX =  str(20 + dbOffsetX*(int(id)-4))
    createBlockElements(obj[0],offsetX,obj[1],str(id))
    alldata[obj[0]] = {"x":offsetX, "y":"200", "width":"260", "height":"350", "id":str(id)} 
  elif(obj[0]=="title"):
     createBlockElements(obj[0],"",obj[1],str(id))
  else:
    offsetX =  str(20 + objectOffsetX*(int(id)-4))
    createObjects(obj[0],offsetX,obj[1],str(id))
    alldata[obj[0]] = {"x":offsetX,"y":"80","width":"100","height":"400", "id":str(id)} 

def createArrows(objData,id):
  objArr = objData.split(":")
  s = objArr[1]
  t = objArr[2]
  sourceX = str(int(alldata[s]["x"] ) + ((int(alldata[s]["width"])/2)-0.5))
  if(t != "db"):
    targetX = str(int(alldata[t]["x"] ) + ((int(alldata[t]["width"])/2)-0.5))
  else:
    targetX =  alldata[t]["x"]
  if(objArr[0] == "->"):
    createDispatchArrow(sourceX ,targetX,objArr[3],id)
    if(len(objArr)>4):
      if(int(alldata[s]["id"])>int(alldata[t]["id"])):
         posX = str((float(sourceX) + ((float(targetX) - float(sourceX))/2) -70))
      else:
         posX = str((float(targetX) + ((float(sourceX) - float(targetX))/2)-70))
      posY = str(20 + (int(id)-8)*arrowOffsetY)
      print(posX)
      print(posY)
      createTextBox(objArr[4],objArr[5],posX,posY,str(random.randint(100, 999)))
  elif(objArr[0] == "<-"):
    createReturnArrow(sourceX,targetX,objArr[3],id)
    if(len(objArr)>4):
      posX = str((float(sourceX) + ((float(targetX) - float(sourceX))/2) - 70))
      posY = str(20 + (int(id)-8)*arrowOffsetY)
      createTextBox(objArr[4],objArr[5],posX,posY,str(random.randint(100, 999)))

def checker(input):
   a=input.split(":")
   if(len(a)!=6):
      print("ERROR")
      print(a)
      return False
   return True
     
    
txt = ""
historyFile = open("commandHistory.txt","a")
historyFile.write("\n"+title+":'"+txt+"'\n")
input = txt.split(",")
for x in range(len(input)):
   if(checker(input[x])):
    createArrows(input[x],str(x+11))

tree = ET.ElementTree(mxfile)
tree.write("filename.xml")