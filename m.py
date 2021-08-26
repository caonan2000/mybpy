#----mybpy (ver:1.08)--2021.8.25 publish-----QQ group: mybpy (519692851)---

#if you want use mybpy,please paste the following tow lines to blender py console or script head
'''

import sys;sys.path.append(r'd:\mybpy')
import importlib as imp;import m;imp.reload(m);from m import *


'''

#----------------------------------------------------------------------------

import bpy
import bmesh
import math
import mathutils
import operator
import bpy_extras.object_utils
import os,sys,inspect,ctypes,winreg


#================My self definate string quick language===============
def sq(S):
    s=S.replace('`','\n')
    s=s.replace('~','\t')
    return s

def exe(S=''):
    try: exec(sq(S))
    except:pass
    
def run(S=''):
    if S=='':  # Console: rec();run(); #after rec run script immediatly
        try:exec('bpy.ops.text.run_script(override("TEXT_EDITOR"))')
        except:pass
    else: exe(S)
    
#================PATH=======================================
    
#------------path of mybpy\m.py-------------------------------

def pathM(arg=''):
    dirname,filename=os.path.split(os.path.abspath(__file__))
    if arg.upper()=='FILE':d=filename
    else:d=dirname;d=repr(d);
    return d
        
def pathBlender(arg=''):
    dirname,filename = os.path.split(os.path.abspath(sys.argv[0])) 
    if arg.upper()=='FILE':d=filename
    else:d=dirname;d=repr(d);
    return d

def pathBl(a=''):pathBlender(a)
   

def fileMe():
    f=inspect.stack()[1][1];fp=bpy.data.texts[f[1:]].filepath;
    return fp
    
def pathMe(arg=''):
    f=inspect.stack()[1][1];fp=bpy.data.texts[f[1:]].filepath;
    dirname,filename = os.path.split(fp) 
    if arg.upper()=='FILE':d=filename
    else:d=dirname;d=repr(d);d=d[1:len(d)-1]
    return d


disk="D:"
pathCC=disk+"\\mybpy\\tx"
pathHDR=pathCC;fileHDR="default.hdr"
pathTmp=disk+"/mybpyTmp"


def getDesktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return winreg.QueryValueEx(key, "Desktop")[0]

#===============File======================================

def fileRead(FilePath=''):
    f=open(FilePath,encoding="utf-8");s=f.read();f.close()
    return s

def read(f):return fileRead(f)


#===========Varible===============================
#------------------------------------------------
def Vector(ls):
    return mathutils.Vector(ls)

#------------------------------------------------
def radians(angle):
    return math.radians(angle)

def rd(angle):return radians(angle)

#------------------------------------------------
def degrees(rd):
    return math.degrees(rd)

def dgrs(rd):return degrees(rd)


#----------version-------------------------------
def version():
    v=bpy.app.version
    return v[0]+v[1]/100

def vs():return version()

#------------language-----------------------------
def language():
    return bpy.app.translations.locale

def lang():return language()
def lan():return language()

#------------LastVertIndex (meshVertSortNew use it)------------------------
#LastVertIndex

#============Function=============================
#-----------tp (type)----------------------------
def tp(v):
    if str(type(v))=="<class 'tuple'>": return "("
    if str(type(v))=="<class 'list'>":return "["
    if str(type(v))=="<class 'dict'>":return "{"
    if str(type(v))=="<class 'str'>":return "s"
    if str(type(v))=="<class 'int'>":return "1"
    if str(type(v))=="<class 'float'>":return "."
    if str(type(v))=="<class 'function'>":return "f"
    if str(type(v))=="<class 'bool'>":return "b"


#-----------isType(variable, OrType, OrType1)--------------------
def isType(v,Type,OrType='',OrType1=''):
    if tp(v)==Type or tp(v)==OrType or tp(v)==OrType1: return True
    else:return False

def isTp(v,Type,OrType='',OrType1=''):return isType(v,Type,OrType,OrType1)

#-----------isNumber(v)--------------------------------------
def isNumber(v):
    if tp(v)=='1' or tp(v)=='.':return True
    else: return False

def IsNumber(v):return isNumber(v)
def isNum(v):return isNumber(v)
def IsNum(v):return isNumber(v)

#-----------If(Term,True return,False return)---------------
def If(Term,T=True,F=False):
    if Term: return T
    else:return F
    
def IF(Term,T=True,F=False):return If(Term,T,F)
def iif(Term,T=True,F=False):return If(Term,T,F)

#---------------And()------------------------------------------------------------------------
def And(t0,t1=True,t2=True,t3=True,t4=True,t5=True,t6=True,t7=True,t8=True,t9=True):
    if t0 and t1 and t2 and t3 and t4 and t5 and t6 and t7 and t8 and t9:return True
    else:return False

def AND(t0,t1=True,t2=True,t3=True,t4=True,t5=True,t6=True,t7=True,t8=True,t9=True):And(t0,t1,t2,t3,t4,t5,t6,t7,t8,t9)
#---------------Or()-------------------------------------------------------------------------
def Or(t0,t1=False,t2=False,t3=False,t4=False,t5=False,t6=False,t7=False,t8=False,t9=False):
    return True in (t0,t1,t2,t3,t4,t5,t6,t7,t8,t9)

def OR(t0,t1=False,t2=False,t3=False,t4=False,t5=False,t6=False,t7=False,t8=False,t9=False):Or(t0,t1,t2,t3,t4,t5,t6,t7,t8,t9) 

#----------listIndex (find the value,return index)-----------------
def listIndex_(ls,v):   #---v must single----
    for i,V in enumerate(ls):
        if V==v:return i

def listIndex(ls,v):    #----v allow list
    if str(type(v))=="<class 'list'>":
        lsV=[]
        for V in v:
            lsV.append(listIndex_(ls,V))
        return lsV
    else: return listIndex_(ls,v)

    
def lsI(ls,v): return listIndex(ls,v)

#-----------combine list then sort--------------------------
def combineList(List1,List2):
     List1.extend(List2); List1.sort()

def cmb(List1,List2):combineList(List1,List2)

#------------listCut--[1,2,3,4,5,6]--Cuts=2---->[[1,2,3],[4,5,6]]----------
def listCut(ls,Cuts=1):
    n=int(len(ls)/Cuts);Ls=[];
    for i in range(Cuts):
        Ls.append(ls[n*i:n*(i+1)])
    return Ls

#------------listCut1--[1,2,3,4,5,6]--Cuts=2--->[[1,3,5],[2,4,6]]---order by squence
def listCut1(ls,Cuts=1):
    n=int(len(ls)/Cuts);Ls=[];
    for i in range(Cuts):
        L=[]
        for ii in range(n):L.append(ls[i+ii*Cuts])    
        Ls.append(L)
    return Ls



#----------------roundVert---(x,y,z) r=2 digit round----------------
def rnd1(v,r):
    s=str(round(float((v).strip()),r))
    if s=='0.0' or s=='-0.0':s='0'
    return s

def roundV(ls='',r=2):
    if ls=='':return ls;
    if isType(ls,'s'):
        i=ls.find('(');i1=ls.find(')');s=ls[i+1:i1];S=s.split(',');
        ss=ls[0:i+1]+rnd1(S[0],r)+','+rnd1(S[1],r)+','+rnd1(S[2],r)+ls[i1:]
        return ss
        

#---------last (return last object)---------------------------
def last(Type='OBJECT'):
  
    if Type.upper()=='OBJECT': i=len(bpy.data.objects)-1;return bpy.data.objects[i]
    if Type.upper()=='MESH':obj=bpy.context.object;i=len(obj.data)-1;return bpy.data.objects.data[i]
    if Type.upper()=='DRIVER':obj=bpy.context.object;d=obj.animation_data.drivers;i=len(d)-1;return d[i].driver
    if Type.upper() in ('MATERIAL','MT'):m=bpy.data.materials; i=len(m)-1;return m[i]
    if Type.upper()=='VI':obj=bpy.context.object;mx=len(obj.data.vertices);LastVertIndex=mx;return mx;



#=================Collection=====================================
#--------get collectionIndex() use for m() move to coll, Note:index is +1 than collections list index --- 
def collectionIndex(Name=''):
    i=0; #--0 is default master scene
    for ii,c in enumerate(bpy.data.collections) :
        if c.name.upper()==Name.upper():
            i=ii+1
    return i


#---------collection Active-------(0 Scene Master)--1 Collection  +1 than children.index--
def collectionActive(Name=0):
    if vs()>2.8:
        if isType(Name,'1'):
            if Name==0: layerColl=bpy.context.view_layer.layer_collection
            else: layerColl=bpy.context.view_layer.layer_collection.children[Name-1]
        else:
            layerColl=bpy.context.view_layer.layer_collection.children[Name]
        bpy.context.view_layer.active_layer_collection= layerColl

def collActive(Name=0):collectionActive(Name)
def cActive(Name=0):collectionActive(Name)
def cAct(n=0):collectionActive(n)

#---------collection New and Activate-----(if Not New return exsited collection and activate)---------------
def collectionNew(Name=''):
    if vs()>=2.8:
        if Name in bpy.data.collections: collectionActive(Name); return bpy.data.collections[Name]
        else:
            new_collection = bpy.data.collections.new(Name)
            bpy.context.scene.collection.children.link(new_collection) # Add the new collection to the scene
            collectionActive(Name)
            return new_collection
        

def collectionNew_OLD(Name='',Nested=False):   #--Not USE, error is not Rename, rewrite as above already  #if nested=True is under the current selected collection
    if Name=='':
        bpy.ops.outliner.collection_new(override('OUTLINER'),nested=Nested);
    else:
        I=collectionIndex(Name)
        if I==0:
            bpy.ops.outliner.collection_new(override('OUTLINER'),nested=Nested);  
            #n=len(bpy.data.collections)-1;bpy.data.collections[n].name=Name #----collection index not stable, maybe wrong name

def cNew(Name=''):return collectionNew(Name)           
def collection(Name=''):return collectionNew(Name)   
def coll(Name=''):return collectionNew(Name)
def c(Name=''):return collection(Name)

#---------collection Rename ----------------
def collectionRename(Name0='',Name1=''):  #Name0=Original Name, Name1=New Name
    try:bpy.data.collections[Name0].name=Name1
    except:pass
    
def cRename(Name0='',Name1=''):collectionRename(Name0,Name1)

def cName(Name='',Name1=''):  # 2 use way:  cName('New Collection') ;  cName('old Collection name','rename collection name')  
    if Name1=='':cNew(Name)  #---new Collection
    else:cRename(Name,Name1) #rename Collection


#----------collectionInitial---------------
def collectionInitial():  #only keep collections[0]
    if len(bpy.data.collections)>1:
        for c in bpy.data.collections:
            if c.name!='Collection': bpy.data.collections.remove(c)
            
def cIni():collectionInitial()


#============Mode=================================

#------------Info show more detail mode-----------
def infoMore(t=True):
    bpy.app.debug_wm = t

#------------UI-----------------------------------
def areaUI(SetUI='VIEW_3D'):

    #------------Version Different----------------
    if vs()<2.8:
        ui_type=bpy.context.area.type
        def ui_set(Set):bpy.context.area.type=Set
    else:
        ui_type=bpy.context.area.ui_type
        def ui_set(Set):bpy.context.area.ui_type=Set
    #---------------------------------------------

    UI=ui_type; SetUI=SetUI.upper();
    if SetUI=='SHADERNODETREE':SetUI='ShaderNodeTree'
    
    if SetUI=='NAME': return UI
    if UI!=SetUI: ui_set(SetUI)
    return UI

def ui(Set='VIEW_3D'):return areaUI(Set)

#-------------AreaFind------------------------------
def areaFind(Type='IMAGE_EDITOR'):
    A=bpy.context.screen.areas
    for a in A:
        if a.type==Type: return a
    return None


#------------Mode Index (myself definition)---------------------------------
#0:Object, #1:Edit-Vert, #2:Edge, #3:Face #other is return mode name #nothing return None
def modeIndexName(i):
    ls=['OBJECT','VERT','EDGE','FACE']
    return ls[i]

def modeIndex():
    try:
        md=bpy.context.object.mode
        if md=='OBJECT':return 0
        if md=='EDIT':
            for i in range(3):
                if bpy.context.tool_settings.mesh_select_mode[i]: return i+1
        return md
    except:return ''
        

def modeI():return modeIndex()

#-----------mode---------------------------------------------
def mode(m='OBJECT'):
    ModeName0=bpy.context.object.mode
    if m.upper()=='NAME':return bpy.context.object.mode
    bpy.ops.object.mode_set(mode=m.upper())
    return ModeName0
    
def tab():
    if bpy.context.object.mode=='OBJECT':mode('EDIT')
    else:mode('OBJECT')
    
def m0():
    try:
        if bpy.context.object.mode!='OBJECT':mode('OBJECT')
    except:pass
    
#--------mA():mode in select All faces then keep object mode-  
def modeObjectButSelectAllFace():
    m3();a();m0()
def mA():modeObjectButSelectAllFace()
#-----------select mode--------------------------------------
def selectMode(m='VERT'):
    try:
        if bpy.context.object.mode!='EDIT':mode('EDIT')
        bpy.ops.mesh.select_mode(type=m.upper())
    except: pass
    
def sMode(m='VERT'):selectMode(m)
def m1():sMode('VERT')
def m2():sMode('EDGE')
def m3():sMode('FACE')
def m4():exec('sculptMode()')


def m(i=''):    #<--when i=int is mode select ; i=str is collection move shotkey,default m(''),move to master scene
    if str(type(i))=="<class 'int'>":
        if i==0: m0() #OBJECT MODE
        if i==1: m1() #EDIT-VERT
        if i==2: m2() #EDIT-EDGE
        if i==3: m3() #EDIT-FACE
        if i==4: m4() #SCULPT MODE
        
    if str(type(i))=="<class 'str'>" and vs()>=2.8:  #--Move to Collection (or Add New Coll)--[2.79 No collection]
        if modeI()!=0:m0()
        Is_new=False;cName=''
        I=collectionIndex(i)
        if I==0:
            if i.isnumeric():I=int(i)
            else:Is_new=True;cName=i
  
        bpy.ops.object.move_to_collection(collection_index=I, is_new=Is_new, new_collection_name=cName)
        if Is_new:bpy.ops.object.move_to_collection(collection_index=len(bpy.data.collections))
       
#-----------proportional Edit Mode----------------------------
def proportionalEditMode(Size=1,Falloff=1):

    f=Falloff;bpy.context.scene.tool_settings.proportional_size=Size
    if isTp(f,'s'):
        f=f.upper()
        bpy.context.scene.tool_settings.proportional_edit_falloff = f
        
    
    #--------------------Version Different----------------------------
    if vs()<2.8:
        if f=='CLOSE' or f==0  or f==False or Size==0: bpy.context.scene.tool_settings.proportional_edit ='DISABLED';return;
        else:
            if bpy.context.object.mode!='EDIT': m1()
            bpy.context.scene.tool_settings.proportional_edit ='ENABLED';
    else:        
        if f=='CLOSE' or f==0  or f==False or Size==0: bpy.context.scene.tool_settings.use_proportional_edit = False;return;
        else:
            if bpy.context.object.mode!='EDIT': m1()
            bpy.context.scene.tool_settings.use_proportional_edit =True;
    #-----------------------------------------------------------------
     
def pMode(size=1,f=1): proportionalEditMode(size,f)
def oMode(size=1,f=1): proportionalEditMode(size,f)
def o(s=1,f=1):pMode(s,f)



def isOmode():return bpy.context.scene.tool_settings.use_proportional_edit_objects  #return True or False


#================Vert Convert==================================
#----------Vector 2 tuple-------------------------------------------------
def vector2tuple(v):
    return (v.x,v.y,v.z)
    
    
def v2t(v):return vector2tuple(v)


#----------rotation 2 tuple-----------------------------------------------
def rotation2tuple(v):
    return (v.x,v.y,v.z)
    
def r2t(v):return rotation2tuple(v)

#----------v2e (vert index to edge index)---------------------------------
 #--only one edge, return is int index---
def v2E_(ls):
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    for e in bm.edges:
        v0=e.verts[0].index
        v1=e.verts[1].index        
        if v0==ls[0]:
            if v1==ls[1]:
                return e.index
        if v0==ls[1]:
            if v1==ls[0]:
                return e.index
    return None

 #-----many edges, return list ---
def v2e(ls):
    cnt=len(ls);LS=[]
    for i in range(cnt-1):
        L=[ls[i],ls[i+1]];e=v2E_(L)
        if not(e==None):LS.append(e)
    return LS

def v2E(ls):v2e(ls)

#------------v2f (vert to face)------------------------------
  #--only one face, return is int index---
def v2F_(ls):
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    for f in bm.faces:
        hasV=0
        for i in ls:
            for v in f.verts:
                if v.index==i:
                    hasV+=1
                    break
            if hasV==3:
                return f.index
    return None   

  #------many faces,return list (rewrite, no need Verts order)---- 
def v2f(ls):
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    ff=[]
    for f in bm.faces:
        hasV=0
        for i in ls:
            for v in f.verts:
                if v.index==i:
                    hasV+=1
                    break
            if hasV==3:
                ff.append(f.index)
                break
    return ff 

def v2F(ls):v2f(ls)   
 
  #------many faces (by order of Verts), return list (v2f old version,be rewrited)---------
def v2f_byOrder(ls):
    cnt=len(ls);LS=[];f0=None
    for i in range(cnt-2):
        L=[ls[i],ls[i+1],ls[i+2]];f=v2F_(L)
        if not(f==None):
            if f!=f0:LS.append(f);f0=f
    return LS
   
#--------------edge index to vert index----------------------------
def e2v(eIndex):
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    lsV=[]
    for e in bm.edges[eIndex:eIndex+1]:
        for v in e.verts:
            if v.index!=None:lsV.append(v.index)
    return lsV

#---------------face index to vert index---------------------------
def f2v(fIndex):
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    lsV=[]
    for f in bm.faces[fIndex:fIndex+1]:
        for v in f.verts:
            if v.index!=None:lsV.append(v.index)
    return lsV



#--------------context---------------------
def context():
    return bpy.context

def ctxt(): return bpy.context
def ctx():return bpy.context
def ct():return bpy.context

#-------------contextObject----------------
def contextObject():
    return bpy.context.object

def cObj():return contextObject()



def contextObjectName():
    return bpy.context.object.name
def cObjName():return contextObjectName()



#===========Selection=========================================
#----------------name-------------------------------
def name(Name='OBJ'):
    obj=bpy.context.object
    obj.name=Name
    return Name

def nm(Name='OBJ'):return name(Name)
def f2(Name='OBJ'):return name(Name)

def n(Name=''):
    if Name=='':exec('newLine()')   #=_n() : add new line in Text Editor  
    else:return name(Name)       #=name()

#----------------return list of select Object----------------------------------------------------
def listSelectObject():
    n=len(bpy.context.selected_objects)
    if n<=0:return []
    else:
        ls=[]
        for o in bpy.context.selected_objects:
            ls.append(o.name)
        return ls    

#----------------return list of object select vert or edge or face (in edit mode) ---------------
def listSelect(v='V'):
    if v.upper()=='O':return listSelectObject()
    else:return listSelectVEF(v)


def listSelectVEF(v='V'):
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    vv=v.upper()
    if vv=='V':bmV=bm.verts
    if vv=='E':bmV=bm.edges
    if vv=='F':bmV=bm.faces
    ls=[]
    for v in bmV:
        if v.select: ls.append(v.index) 
    return ls

def lsSel(v='V'):return listSelect(v)

def listMulSelect(VEFtype,ls):    #ls can be list of exec to  mul select, example: lsV(['sV([1,2];alt()','sV[3,4];alt()'])')
    if ls=='':return listSelect(VEFtype)
    else:
        if isType(ls,'s'):ls=[ls]
        LS=[];
        for L in ls:
            exec(L)
            LS.extend(listSelect(VEFtype))
        return LS

def lsV(ls=''): return listMulSelect('V',ls)
def lsE(ls=''): return listMulSelect('E',ls)
def lsF(ls=''): return listMulSelect('F',ls)
def lsO(ls=''): return listMulSelect('O',ls)


#-------------VertX/Y/Z (return)--------------------------------

def vertCo(Index):
    obj=bpy.context.object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    for v in bm.verts[Index:Index+1]:pass
    return v2t(v.co)

def vCo(i):return vertCo(i)


def vertX(Index):
    obj=bpy.context.object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    for v in bm.verts[Index:Index+1]:pass
    return v.co.x
def vX(i):return vertX(i)


def vertY(Index):
    obj=bpy.context.object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    for v in bm.verts[Index:Index+1]:pass
    return v.co.y
def vY(i):return vertY(i)


def vertZ(Index):
    obj=bpy.context.object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    for v in bm.verts[Index:Index+1]:pass
    return v.co.z

def vZ(i):return vertZ(i)




#-------------vertInRange---------------------------------------
def vertInRang(x=[],y=[],z=[]):
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    
def vRng(x=[],y=[],z=[]):vertInRange(x,y,z)

#-----------selectCollectionObject----------------------------
def selectCollectionObject(cName):  #cName can be string or list,  if cName=0 is Scene Master Collection
    try:
        exec('aa()'); #--deselect all first
        if isType(cName,'1'):cName=[cName] # Scene MasterCollection or Index of collection need -1
        if isType(cName,'s'):cName=[cName] # cName string to list
        for n in cName:
            if n==0:
                allObj=bpy.context.scene.collection.objects
            else:
                if isType(n,'1'):allObj=bpy.data.collections[n-1].all_objects
                else:allObj=bpy.data.collections[n].all_objects
            for o in allObj:o.select_set(True);
    except:pass
    
#-----------select all----------------------------------------
def selectAll(cName=''):   #cName=collection Name
    try:
        if mode('name')=='EDIT':bpy.ops.mesh.select_all(action='SELECT')
        else:
            if cName=='':bpy.ops.object.select_all(action='SELECT');
            else:selectCollectionObject(cName)
    except:pass

    
def a(cName=''):selectAll(cName)   


#-----------selectCollectionObject----------------------------
def deselectCollectionObject(cName):  #cName can be string or list
    try:
        if isType(cName,'1'):cName=[cName] # Scene MasterCollection or Index of collection need -1
        if isType(cName,'s'):cName=[cName] # cName string to list
        for n in cName:
            if n==0:
                allObj=bpy.context.scene.collection.objects
            else:
                if isType(n,'1'):allObj=bpy.data.collections[n-1].all_objects
                else:allObj=bpy.data.collections[n].all_objects
            for o in allObj:o.select_set(False);
    except:pass
    
#----------deselect all---------------------------------------
def deselectAll(cName=''):  #cName=collection Name
    if mode('name')=='EDIT':exec('sN()')
    else:
        if cName=='':bpy.ops.object.select_all(action='DESELECT');
        else:deselectCollectionObject(cName)
    
def alt_a(cName=''):deselectAll(cName)
def altA(cName=''):alt_a(cName)
def aa(cName=''): alt_a(cName)

        
#-----------deselectEditMesh---------------------
def deselectEditMesh(Mode='V',ls=[]):
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    
    md=Mode.upper()
    if md=='V': bmV=bm.verts
    if md=='E': bmV=bm.edges
    if md=='F': bmV=bm.faces
    
    for v in bmV:v.select=False
    
    bmesh.update_edit_mesh(obj.data, True)
#-------------deselectEditMeshAll() VERT EDGE FACE All DESELECT-----
def deselectEditMeshAll():
    deselectEditMesh('V')
    deselectEditMesh('E')
    deselectEditMesh('F')
    
def selNone():
    if mode('name')=='EDIT':deselectEditMeshAll()
    else:altA()
    
def selN():selNone()
def sN():selN()
#----------selectFaceAfterSelVert----------------------
def selectFaceAfterSelVert(bm=''):
    if bm=='': obj=bpy.context.object;bm=bmesh.from_edit_mesh(obj.data)

    for f in bm.faces:
        hasNoSelV=False
        for v in f.verts:
            if v.select==False:hasNoSelV=True;break   
        if hasNoSelV:continue
        f.select=True

#-----------selectEdgeAfterSelVert---------------------
def selectEdgeAfterSelVert(bm=''):
    if bm=='': obj=bpy.context.object;bm=bmesh.from_edit_mesh(obj.data)
    
    for e in bm.edges:
        hasNoSelV=False
        for v in e.verts:
            if v.select==False:hasNoSelV=True;break   
        if hasNoSelV:continue
        e.select=True
        
#----------selectVertInSimpleTerm----------------------    
def selectVertInSimpleTerm(s=''):   # 'x>0 & x<10 & y>=0 & y<10 & z>0 & z<1'  &=and |=or  ,=and
    obj=bpy.context.object
    bm=bmesh.from_edit_mesh(obj.data)
    for e in bm.edges:e.select=False;
    for f in bm.faces:f.select=False;
    for v in bm.verts:
        v.select=False;
        ss=s.replace('x','v.co.x')
        ss=ss.replace('y','v.co.y')
        ss=ss.replace('z','v.co.z')
        ss=ss.replace('&',' and ')
        ss=ss.replace('|',' or ')
        ss=ss.replace(',',' and ')
        ss='if '+ss+':v.select=True'
        exec(sq(ss))
    selectFaceAfterSelVert(bm)
    bmesh.update_edit_mesh(obj.data, True)

#------------selectVertLinkTerm------------'link=[vert index1,..],no=[vert index]'---
def selectVertLinkTerm(s=''):  # Faces select
    nli=s.find('no=')
    if nli<0:endL=len(s)-1
    else:endL=nli-1
    lk=eval(s[5:endL])
    
    if nli>0:nl=eval(s[nli+3:])
    else:nl=[]


    obj=bpy.context.object
    bm=bmesh.from_edit_mesh(obj.data)
    for f in bm.faces:
        f.select=False
        Linked=False
        for v in f.verts:
            if v.index in nl:Linked=False;break
            if v.index in lk:Linked=True
        if Linked:
            f.select=True
            for v in f.verts: lk.append(v.index)
            
    bmesh.update_edit_mesh(obj.data, True)

    
#-----------selectEditMesh---------------------

def selectEditMesh(Mode='V',ls=[],VertOnly=False): 
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    #bm.faces.active = None
    
    sN();
    md=Mode.upper()
    
    if isType(ls,'1'):ls=[ls]
    if isType(ls,'s'):
        if ls[:4]=='link':selectVertLinkTerm(ls);return
        else: selectVertInSimpleTerm(ls);return
    
    if ls!=[]:
        
        if md=='V': bmV=bm.verts
        if md=='E': bmV=bm.edges
        if md=='F': bmV=bm.faces
        
        cnt=len(bmV)
        for v in bmV:v.select=False
        
        for i in ls:
            if i<cnt:
                for v in bmV[i:i+1]:v.select=True
                
        bmesh.update_edit_mesh(obj.data,True)
        
    else:   #-------------select Face or Edge which Verts select----------
        if Mode=='F':
            for f in bm.faces:
                f.select=False;hasNoSelV=False
                for v in f.verts:
                    if v.select==False:hasNoSelV=True;break
                if hasNoSelV:f.select=False;continue
                f.select=True

        if Mode=='E':
            for e in bm.edges:
                e.select=False;hasNoSelV=False
                for v in e.verts:
                    if v.select==False:hasNoSelV=True;break
                if hasNoSelV:e.select=False;continue
                e.select=True

                
    if Mode=='V' and VertOnly==False: #--edge and face both select when select 2 or 4 Verts in then same time         
        selectEdgeAfterSelVert(bm)            
        selectFaceAfterSelVert(bm)
    

#-----------select vert------------------------
def selectVert(ls=[]):selectEditMesh('V',ls)
def selV(ls=[]):selectVert(ls)
def sV(ls=[]):selV(ls)
def sv(ls=[]):sV(ls)
def v(ls=[]):selectVert(ls)
#-----------select edge------------------------
def selectEdge(ls=[]):
     m2();selectEditMesh('E',ls)

def selE(ls=[]):selectEdge(ls)
def sE(ls=[]):selectEdge(ls)
def sE_(ls=[]):selE(v2e(ls))  #<--note: use verts list  as Argument

#-----------select face------------------------
def selectFace(ls=[]):
    m3();selectEditMesh('F',ls)


def selF(ls=[]):selectFace(ls)
def sF(ls=[]):selectFace(ls)
def sF_(ls=[]):selF(v2f(ls))  #<--note: use verts list as Argument

#-----------select object----------------------------------
def selectObject(ObjName=''):
    if modeIndex()!=0:m0()
    if ObjName=='':return;
    #---------Version Different----------------------------
    if vs()<2.8:
        bpy.data.objects[ObjName].select=True
        bpy.context.scene.objects.active = bpy.data.objects[ObjName]
    else:
        bpy.data.objects[ObjName].select_set(True)
        bpy.context.scene.objects[ObjName].select_set(True)
        #bpy.context.collection.objects[ObjName].select_set(True)
        bpy.context.view_layer.objects.active=bpy.data.objects[ObjName]
    #-------------------------------------------------------

def selectObj(ls=''):   #allow multi select
    if isTp(ls,'s'):selectObject(ls)
    if isTp(ls,'[','('):
        for n in ls: selectObject(n)

def sO(a=''):
    sN();
    if isTp(a,'1'):   #------if  a is number, select first number of objects lastest add
        for obj in bpy.context.scene.objects[0:a]:
            selectObject(obj.name)
    else:selectObj(a)  #select only one


def so(n):sO(n)


def sO_(ListOrstrName=''):selectObj(listOrstrName)  #allow multi select
def so_(n):sO_(n)
    
#----------select_linked_pick----------------------------------
def selectLink(v=''):
    if v=='':v=lsV();v=v[0]
    #---------------Version Different------------------------
    if vs()<2.9:
        bpy.ops.mesh.select_linked_pick(deselect=False, delimit={'SEAM'}, index=v)
    else:
        bpy.ops.mesh.select_linked_pick(deselect=False, delimit={'SEAM'}, object_index=0, index=v)
#------------l() mul functions:  only x value is selecetLink(x), has y,z, is goto location
def l(x='',y='',z=''):
    if y=='' and z=='': selectLink(x)
    else:exec('GoLocation(x,y,z)') 

#----------loop_mul_select (only surpot edge)-------------------------------------
def selectLoop(Ring=False):
    bpy.ops.mesh.loop_multi_select(Ring)  #return edge, ring=False is horizontal
    selectFaceAfterSelVert()
        
def alt_clk(r=False):selectLoop(r)
def alt(r=False):alt_clk(r)


def shft_alt_clk(r=False):selectLoop(r);
def shftAlt(r=False):shft_alt_clk(r);
def shfAlt(r=False):shft_alt_clk(r);

#-----------loop_mul_select_face -------------------------------------------------
def selectLoopFace(lsVertEge1,lsVertEge2):  #use listVertEge1, listVertEge2 as arguments
    v(lsV(['v('+str(lsVertEge1)+');alt()','v('+str(lsVertEge2)+');alt()']))

def altClickFace(ls1,ls2):selectLoopFace(ls1,ls2)
def altF(ls1,ls2):altClickFace(ls1,ls2)    

#----------hide---------------------------------------------------------------------
def hide():
    if mode()=='EDIT':u=ui();m3();bpy.ops.mesh.hide(unselected=False)
    else:u=ui();bpy.ops.object.hide_view_set(unselected=False)
    ui(u)
def h():hide()

def unHide():
    if mode()=='EDIT':u=ui();m3();bpy.ops.mesh.reveal()
    else: u=ui();bpy.ops.object.hide_view_clear()
    ui(u)
    
def altH():unHide()

def revHide():
    if mode()=='EDIT':u=ui();m3();bpy.ops.mesh.hide(unselected=True)
    else:u=ui();bpy.ops.object.hide_view_set(unselected=True)
    ui(u)
    
def shft_h():revHide()
def H():revHide()
#==================View3D================================================
def override(AreaType='VIEW_3D'):  #----ctrR use: must overrideContext before use--------
    #----standard codes answer in  https://blender.stackexchange.com-------need override context --------

    win      = bpy.context.window
    scr      = win.screen
    areas  = [area for area in scr.areas if area.type ==AreaType.upper()]
    region   = [region for region in areas[0].regions if region.type == 'WINDOW']
    Override = {'window':win,
                'screen':scr,
                'area'  :areas[0],
                'region':region[0],
                'scene' :bpy.context.scene,
                }
    
    return Override


def ovrd(a='VIEW_3D'):return override(a)
def ov(a='VIEW_3D'):return override(a)


#-----------Another override function writing way---(let ripMove()[v] OK) if override() wrong can try this function--(codes from plug:Bumarin_For_Sculptor: misc.py)--
def override1(AreaType='VIEW_3D'):
    #=== Iterates through the blender GUI's windows, screens, areas, regions to find the View3D space and its associated window.  Populate an 'oContextOverride context' that can be used with bpy.ops that require to be used from within a View3D (like most addon code that runs of View3D panels)
    # Tip: If your operator fails the log will show an "PyContext: 'xyz' not found".  To fix stuff 'xyz' into the override context and try again!
        for oWindow in bpy.context.window_manager.windows:          ###IMPROVE: Find way to avoid doing four levels of traversals at every request!!
            oScreen = oWindow.screen
            for oArea in oScreen.areas:
                if oArea.type == AreaType.upper():                         ###LEARN: Frequently, bpy.ops operators are called from View3d's toolbox or property panel.  By finding that window/screen/area we can fool operators in thinking they were called from the View3D!
                    for oRegion in oArea.regions:
                        if oRegion.type == 'WINDOW':                ###LEARN: View3D has several 'windows' like 'HEADER' and 'WINDOW'.  Most bpy.ops require 'WINDOW'
                            #=== Now that we've (finally!) found the damn View3D stuff all that into a dictionary bpy.ops operators can accept to specify their context.  I stuffed extra info in there like selected objects, active objects, etc as most operators require them.  (If anything is missing operator will fail and log a 'PyContext: error on the log with what is missing in context override) ===
                            oContextOverride = {'window': oWindow, 'screen': oScreen, 'area': oArea, 'region': oRegion, 'scene': bpy.context.scene, 'edit_object': bpy.context.edit_object, 'active_object': bpy.context.active_object, 'selected_objects': bpy.context.selected_objects}   # Stuff the override context with very common requests by operators.  MORE COULD BE NEEDED!
                            print("-AssembleOverrideContextForView3dOps() created override context: ", oContextOverride)
                            return oContextOverride
        raise Exception("ERROR: AssembleOverrideContextForView3dOps() could not find a VIEW_3D with WINDOW region to create override context to enable View3D operators.  Operator cannot function.")

def ov1(a='VIEW_3D'): override1(a)
#----------------------------------------------------------------------------------------------------------------
def contextArea(Type='VIEW_3D'): #if context has 3D_View use context , not use find first 3D View.   ca0() use
    sc=bpy.context.screen

    for a in sc.areas:
        if a.type==Type:return a
        
    sc=bpy.data.screens['Layout']
    for a in sc.areas:
        if a.type==Type:return a

    
#---------------snap----------------------------------
def snapCursor2Vert(vIndex):
    
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    
    if str(type(vIndex))=="<class 'int'>":vI=vIndex
    else:vI=vIndex[0]
        
    v=bm.verts[vI]
    snapCursor2Vector(v.co)

def snapCs2v(v):snapCursor2Vert(v)
def cV(v): snapCs2v(v)


#-------------------snapCursor2Vector location (Vct is tuple)--------
def snapCursor2Location(Vct):
    #----------------Version Different-----------------
    if vs()<2.8:bpy.context.scene.cursor_location=Vector(Vct)
    else:bpy.context.scene.cursor.location=Vector(Vct)

def cL(v):snapCursor2Location(v)

#--------------------------------------------------
def snapCursor2Center():
    cL((0,0,0))
    

def c0():snapCursor2Center()
#def cO():c0()

#--------orign Set Cursor------------------------
def orignSetCursor():
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

def oC():orignSetCursor()

#=================Get Index of Vert/Edge/Face====================================================

#----------------show object data select vert or edge or face (in object mode)---------------
def getSelectObjData(v='V'):
    obj=bpy.context.object;me=obj.data
    vv=v.upper()
    if vv=='V':V=obj.data.vertices
    if vv=='E':V=obj.data.edges
    if vv=='F':V=obj.data.palygons
    
    s=""
    for v in V:
        if v.select: s=s+str(v.index)+',' 
    ss='['+s[:len(s)-1]+']'
    #print(ss)
    return ss
    

#----------------show object select vert or edge or face (in edit mode) ---------------
def getSelect(v='V'):
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    vv=v.upper()
    if vv=='V':bmV=bm.verts
    if vv=='E':bmV=bm.edges
    if vv=='F':bmV=bm.faces
    
    s=""
    for v in bmV:
        if v.select: s=s+str(v.index)+',' 
    ss='['+s[:len(s)-1]+']'
    #print(ss)
    return ss


#-----------------nv() not with Vector <>---------------------------------
def nv(s):
    s=s.replace('<','')
    s=s.replace('>','')
    s=s.replace(' ','')
    s=s.replace('Vector','')
    return s

#----------------show select Grab Vert [[id,()],..] -----------------------
def getGrabVect(Show=True):  
    md=bpy.context.object.mode
    if md!='EDIT':bpy.ops.object.mode_set(mode='EDIT')
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me);
    V=bm.verts
    s=""
    for v in V:
        if v.select:s=s+'['+str(v.index)+','+nv(str(v.co))+'],'

    ss='['+s[:len(s)-1]+']'
    if Show:
        #print(ss)
        return ss
        #clip.copy(ss)
    if md!='EDIT':bpy.ops.object.mode_set(mode=md)
   
    

#----------------show select Grab Edge [[id,()],...]-----------------------
def getGrabEdge(Show=True):  
    md=bpy.context.object.mode
    if md!='EDIT':bpy.ops.object.mode_set(mode='EDIT')
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me);
    E=bm.edges
    s=""
    for e in E:
        if e.select:s=s+'['+str(e.index)+','+'('+str(e.verts[0].index)+','+str(e.verts[1].index)+')],'

    ss='['+s[:len(s)-1]+']'
    if Show:
        #print(ss)
        return ss
    if md!='EDIT':bpy.ops.object.mode_set(mode=md)


#----------------show select Grab Face [[id,()],...]-----------------------
def getGrabFace(Show=True):  
    md=bpy.context.object.mode
    if md!='EDIT':bpy.ops.object.mode_set(mode='EDIT')
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me);
    F=bm.faces
    s=""
    for f in F:
        if f.select:s=s+'['+str(f.index)+','+'('+str(f.verts[0].index)+','+str(f.verts[1].index)+','+str(f.verts[2].index)+','+str(f.verts[3].index)+')],'

    ss='['+s[:len(s)-1]+']'
    if Show:
        #print(ss)
        return ss
    if md!='EDIT':bpy.ops.object.mode_set(mode=md)



#------------------show select Grab  [Vert,Edge,Face]-------------------
def getGrab():
    v=getGrabVect(False)
    e=getGrabEdge(False)
    f=getGrabFace(False)
    ss='['+str(v)+','+str(e)+','+str(f)+']'
    #print(ss)
    return ss

#---------------getVertLocation-----(in Edit mode get Vert Location for rec() use)-------------
def getVertLocation(vIndex=[]):
    if vIndex==[]:return '';
    else:return 'l'+str(vertCo(vIndex[0]))+';'

def getVertL(v): return getVertLocation(v)

#-----------------show cursor vector---------------------------------------
def getCursor():
    L=bpy.context.scene.cursor.location
    ss=nv(str(L))
    #print(ss)
    return ss

#------------------material diffuse color (return rgb tuple)--------------------------------------------
def materialDiffuseColor():
    c=bpy.context.object.active_material.diffuse_color
    n=3  #<--round n
    ss='('+ str(round(c[0],n)) +','+str(round(c[1],n))+','+str(round(c[2],n))+')'
    #print(ss)
    return ss
#------------------get selected Object name list-----------------------------------------------
def getSelectedOjbect():
    obj=bpy.context.selected_objects
    if obj==[]: return ''
    else:
        for o in obj:s=s+",'"+o.name+"'"
        ss='['+s[1:]+']';
        return ss;
def getO():return getSelectedObject()    
#-------------------Object(Camera) Location & Rotation (return )----------------------
def getObjectLocationRotation(n=4):  #n is  round  for rotation
    obj=bpy.context.object
    r=obj.rotation_euler
    ss=nv(str(obj.location))+',('+str(round(r.x,n))+','+str(round(r.y,n))+','+str(round(r.z,n)) +')'
    #print(ss)
    return ss
#--------------------getObjLocation for object rec use-------------------------
def getObjLocation(): 
    obj=bpy.context.object
    ss=nv(str(obj.location))
    return ss

def getObjL():return getObjLocation()
#--------------------getClipboard-------------------------------------
def getClipboard():
    try:return bpy.data.window_managers[0].clipboard
    except:return ''
#---------------------Quick Short command for get---------------------
    

def getV(): return getSelect('V')  #---get Select Verts Index in list
def getE(): return getSelect('E')  #---get Select Edgs Index in list
def getF(): return getSelect('F')  #---get Select Faces Index in list


def getLR():return objectLocationRotation() #--for camera use, Get Location & Rotation of Camera, as Parameters for function: ca(LR)


def getDFC():return materialDiffuseColor()  #---2.79 use get DFC color
def getRGB():return getDFC()

def getG():return getGrab()  #----get whole Vert/Edge/Face Index and location in the list of object for makeObject() use 
def getGV():return getGrabVect()  #--grab Vert Index List of object
def getGE():return getGrabEdge()  #--grab Edge Index list of object
def getGF():return getGrabFace()  #--grab Face Index list of object 


#------------------getInfo---------------------------------------------
def getInfo():
    try:
        bpy.ops.info.select_all(override('INFO'),action='SELECT')
        bpy.ops.info.report_copy(override('INFO'))
        return bpy.data.window_managers[0].clipboard
    except: return ""
    
def getInfoLast():
    try:
        ls=getInfo().split('\n')
        return ls[-2]
    except:return ""

def getInfoValue(a='transform.translate',a1='g'):  #from info get a Value(default:transform.translate value), to rec as a1 (defautl g)
    g='';I=getInfoLast();n=I.find(a);
    if n>0: i1=I.find('=(');i2=I.find(')');g=a1+I[i1+1:i2+1]+';'
    return g

def getInfoR(a='transform.rotate',r=2):    #from info get Roatate Value
    v='';I=getInfoLast();n=I.find(a);
    if n>0:
        i1=I.find('=');i2=I.find(',');V=I[i1+1:i2];V=str(round(degrees(float(V)),r))
        a1=I.find('axis')+6;a2=I.find("',");A=I[a1:a2].lower()
        v='r'+A+'('+V+');'
    return v


def getSelectObj():  #----return 'sO()' 
    ls=lsO();Obj=''
    if len(ls)==0:Obj=''
    if len(ls)==1:Obj="sO('"+ls[0]+"');"
    else:Obj='sO('+str(ls)+');'
    return Obj

def getInfoObjAction(r,recObjName=''):# when object mode,from Info get Action for rec  
    I=getInfoLast();s='';Obj=''

    #------------rec Object Name--------------------------
    if recObjName!='':Obj=getSelectObj()

    #-------last Info is move then rec location ----------  
    a='transform.translate';n=I.find(a);
    if n>0:
        N=len(bpy.context.selected_objects)
        if N==0:return ''
        if N==1 and isOmode()==False: l=getObjL();s=Obj+'l'+roundV(l,r)+';'; return s
        else:g=getInfoValue();s=Obj+roundV(g,r);return s
            
    #-------last Info is resize---------------------------
    a='transform.resize';n=I.find(a);
    if n>0:s=getInfoValue(a,'s');s=Obj+roundV(s,r);return s

    #-------last Info is rotate---------------------------
    a='transform.rotate';n=I.find(a);
    if n>0:s=Obj+getInfoR(a,r);return s


    #--------if not any action then s=selectObj-----------
    if s=='':s=getSelectObj()
    
    return s    



def getInfoEditAction(r): # when edit mode,from Info get Action for rec
    ls=lsV();s='';g='';l=''
    I=getInfoLast();s='';
    #-------last Info is move then rec location ----------

    a='transform.translate';n=I.find(a);
    if n>0:
        
        if len(ls)<=0:return s
        if len(ls)==1 and isOmode()==False :l=getVertL(ls);l=roundV(l,r);s='v('+str(ls[0])+');'+l;
        else:g=getInfoValue();g=roundV(g,r);s='v('+getV()+');'+g;
        return s

    #-------last Info is resize---------------------------
    a='transform.resize';n=I.find(a);
    if n>0:s=getInfoValue(a,'s');s='v('+getV()+');'+roundV(s,r);return s

    #-------last Info is rotate---------------------------
    a='transform.rotate';n=I.find(a);
    if n>0:rr=getInfoR(a,r);s='v('+getV()+');'+rr;return s


    #--------if not any action then return selected Verts-----------
    if s=='':s='v('+getV()+');'
    
    
    return s



def getInfoAnyMode(r):  #any mode rec : for example proptional mode toggle
    I=getInfoLast();s='';
    #-----oMode change------------
    n=-1
    if I.find('bpy.context.scene.tool_settings')>=0:a='proportional_edit';n=I.find(a);
    if n>0:
        if I[n:].find('False')>=0:s='o(0);'
        else:
            Fall=bpy.context.scene.tool_settings.proportional_edit_falloff
            Fall=IF(Fall=='SMOOTH','',",'"+Fall+"'")
            Size=str(round(bpy.context.scene.tool_settings.proportional_size,r))
            s='o('+Size+Fall+');'


    #----Mode change---------------
    a='editmode_toggle';n=I.find(a);
    if n>0:
        i=modeI();
        if i!='':s='m' + str(i) +'();';return s
        

    
    return s


#==================record==============================================
def record(r=2,n=''):  #---record into the Text Editor  #(r=2 is Vert location or translation keep digitRound), n='obj' or n='o':obj mode rec obj name  
    try:
        a=contextArea('TEXT_EDITOR');t=a.spaces[0].text
        
        mI=modeI();s='';

        s=getInfoAnyMode(r)  #-----any mode rec

        if s=='':
            if mI==0: 
                s=getInfoObjAction(r,n)   #--object mode rec
            else:      
                s=getInfoEditAction(r)  #--edit mode rec
            
        t.write(s);
        
    except:pass

    
def rec(r=2,n=''):record(r,n)

def reco(r=2,n='o'):record(r,n) # when object mode add selectObject

#---------------add New Line--------------------------------------------
def newLine(): # add new line
    a=contextArea('TEXT_EDITOR');t=a.spaces[0].text;t.write('\n');
    
def _n():newLine()   #n()=_n();  if argmument blank, n()=_n();  if n('OBJ') = name('OBJ') 

#===========Object Oprations============================================


#-----------delete--------------------------------------------
def clear(Type=''):
    if Type=='':
        if modeI()==0: bpy.ops.object.delete(use_global=False, confirm=False);return
        if modeI()==1: bpy.ops.mesh.delete(type='VERT');return
        if modeI()==2: bpy.ops.mesh.delete(type='EDGE');return
        if modeI()==3: bpy.ops.mesh.delete(type='FACE');return
    else:
        bpy.ops.mesh.delete(type=Type.upper())
        
def x(t=''):clear(t)

#---------clearOtherOjbect (keep select object Only)-----------
def clearOtherObject():
    override = bpy.context.copy()
    override['selected_objects'] = list(bpy.context.scene.objects)
    bpy.ops.object.delete(override)


def clearOther():clearOtherObject()

#------------dissovleFaces-----------------------------------------
def dissovleFaces():
    bpy.ops.mesh.dissolve_faces()

def faceDsvl():dissovleFaces()
def fDsv():faceDsvl()
def faceMelt():faceDsvl()
def fMelt():faceMelt()


#---------mesh rebuild after vertices re-ordered by x,z,y (in order to keep same in different bl versions)-------------------
def meshVertSortAll(Round=4):  
    md0=mode("EDIT");obj=bpy.context.object;bm=bmesh.from_edit_mesh(obj.data);v0=[];vi=[];i=0;n=Round

    #---------Vert------------------------------
    for V in bm.verts: v0.append([V.index,round(V.co.x,n),round(V.co.y,n),round(V.co.z,n)])
    v0.sort(key = operator.itemgetter(1,3,2))
    i=0;
    for VV in v0:vi.append([VV[0],i]);i+=1
    vi.sort()
    i=0;
    for V in bm.verts:V.index=vi[i][1];i+=1
    bm.verts.sort();

    #---------Edge-------------------------------
    ei=[]
    for E in bm.edges:
        eVi=[];
        for i in range(2):eVi.append(E.verts[i].index)
        eVi.sort();eVi.append(E.index);ei.append(eVi)
    ei.sort(key=operator.itemgetter(0,1))
    i=0
    for EI in ei: EI.append(i);i+=1;
    ei.sort(key=operator.itemgetter(2))
    i=0;
    for E in bm.edges:E.index=ei[i][3];i+=1
    bm.edges.sort();

    #---------Face-------------------------------
    fi=[]
    for F in bm.faces:
        fVi=[];
        for FV in F.verts:fVi.append(FV.index);
        fVi.sort();fVi.append(F.index);fi.append(fVi)
    fi.sort(key=operator.itemgetter(0,1,2,3))
    i=0
    for FI in fi: FI.append(i);i+=1;
    fi.sort(key=operator.itemgetter(4))
    i=0;
    for F in bm.faces:F.index=fi[i][5];i+=1
    bm.faces.sort();
    
    #----------------------------------------------
    if md0!='EDIT':mode(md0)

#--------------------------------------------------
def reIndexAll(Round=4):meshVertSortAll(Round)



#-----------reIndex meshSort ----------------------
def reIndexBgnI(bgnV=0,bgnE=0,bgnF=0,Round=4):  #----has problem, not use for the time 
    md0=mode("EDIT");obj=bpy.context.object;bm=bmesh.from_edit_mesh(obj.data);v0=[];vi=[];i=0;n=Round

    #---------Vert------------------------------
    for V in bm.verts[bgnV:]: v0.append([V.index,round(V.co.x,n),round(V.co.y,n),round(V.co.z,n)])
    v0.sort(key = operator.itemgetter(1,3,2))
    i=0;
    for VV in v0:vi.append([VV[0],i]);i+=1
    vi.sort()
    i=0;
    for V in bm.verts[bgnV:]:V.index=vi[i][1];i+=1
    bm.verts.sort();

    #---------Edge-------------------------------
    ei=[]
    for E in bm.edges[bgnE:]:
        eVi=[];
        for i in range(2):eVi.append(E.verts[i].index)
        eVi.sort();eVi.append(E.index);ei.append(eVi)
    ei.sort(key=operator.itemgetter(0,1))
    i=0
    for EI in ei: EI.append(i);i+=1;
    ei.sort(key=operator.itemgetter(2))
    i=0;
    for E in bm.edges[bgnE:]:E.index=ei[i][3];i+=1
    bm.edges.sort();

    #---------Face-------------------------------
    fi=[]
    for F in bm.faces[bgnF:]:
        fVi=[];
        for FV in F.verts:fVi.append(FV.index);
        fVi.sort();fVi.append(F.index);fi.append(fVi)
    fi.sort(key=operator.itemgetter(0,1,2,3))
    i=0
    for FI in fi: FI.append(i);i+=1;
    fi.sort(key=operator.itemgetter(4))
    i=0;
    for F in bm.faces[bgnF:]:F.index=fi[i][5];i+=1
    bm.faces.sort();
    
    #----------------------------------------------
    if md0!='EDIT':mode(md0)
    
    
#----------------------------------------------------    
def reIndex(Round=4):reIndexAll(Round)
def reindex(Round=4):reIndexAll(Round)
def ri(Round=4):reIndex(Round)


#-----------------only new verts reindex------------
def meshVertSortNew(Round=4):
    pass
    #msg(LastVertIndex)
    



#---------object move----------------------------------------------
def objMove(ls,obj=[]):
    me=obj.data
    bm = bmesh.new()   
    bm.from_mesh(me)   
    v=[];e=[];f=[];
    for v in bm.verts:
        v.co.x +=ls[0]
        v.co.y +=ls[1]
        v.co.z +=ls[2]

    bm.to_mesh(me)
    bm.free()  

#----------makeObj()----from [v,e,f] data----------Part='All': no need to reindex of verts----
def makeObject(ls,Name='Object',Part='ALL',Smooth=True):
    v=[];e=[];f=[];
    if Part.upper()=='ALL':
        for L in ls[0]: v.append(L[1])
        for L in ls[1]: e.append(L[1])
        for L in ls[2]: f.append(L[1])

    mesh = bpy.data.meshes.new(Name)
    mesh.from_pydata(v,e,f);
    bpy_extras.object_utils.object_data_add(bpy.context, mesh, operator=None)

    if Smooth: bpy.ops.object.shade_smooth()

    #mesh.update()
    #objNew = bpy.data.objects.new(Name, mesh)
    #-----------Version Different------------------
    #if vs()<2.8:bpy.context.scene.objects.link(objNew)
    #else:bpy.context.collection.objects.link(objNew)
    #----------------------------------------------

    
def makeObj(ls,Name='Obj',Part='ALL'):makeObject(ls,Name,Part)


#------------------grab--------------------------------------------
#---grab-(goto)--if ls=tuple: translate(move); if ls=list struct [[V index,Vector()],...] then set V to the Vector directly---------------------------------------
def grab(x=[],y=[],z=[]):
    ls=x
    if IsNum(x) and IsNum(y) and IsNum(z):ls=(x,y,z)
    else:ls=x
   
    
    if str(type(ls))=="<class 'tuple'>":
        
        P_edit_falloff=bpy.context.scene.tool_settings.proportional_edit_falloff
        P_edit_size=bpy.context.scene.tool_settings.proportional_size
        #-----------Version Different--------------------
        if vs()<2.8:
            P_edit=bpy.context.scene.tool_settings.proportional_edit
            bpy.ops.transform.translate(value=ls, constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional=P_edit, proportional_edit_falloff=P_edit_falloff, proportional_size=P_edit_size)
        else:
            P_edit=bpy.context.scene.tool_settings.use_proportional_edit        
            bpy.ops.transform.translate(value=ls, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=P_edit, proportional_edit_falloff=P_edit_falloff, proportional_size=P_edit_size, use_proportional_connected=False, use_proportional_projected=P_edit)
        #------------------------------------------------


    if str(type(ls))=="<class 'list'>":
        md=bpy.context.object.mode
        if md!='EDIT':m1()
        obj=bpy.context.edit_object;me=obj.data
        bm=bmesh.from_edit_mesh(me)
        for L in ls:
            for v in bm.verts[L[0]:L[0]+1]:
                v.co.x=L[1][0]; v.co.y=L[1][1];v.co.z=L[1][2]
        bmesh.update_edit_mesh(me, True)
        if md!='EDIT':mode(md)        

                     
    
def goto(x=[],y=[],z=[]):grab(x,y,z)

def g(x=[],y=[],z=[]):grab(x,y,z)

def gx(n):g((n,0,0))
def gy(n):g((0,n,0))
def gz(n):g((0,0,n))

#---------gotoMid---------------------------------------------------------
def gotoMid(Axis='x'):
    if mode('name')!='EDIT':m1()
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    S='''for v in bm.verts:
        if v.select:
            ls=[]
            for e in v.link_edges:
                for vv in e.verts:
                    if vv==v:continue
                    if vv.select:break
                    ls.append(vv)
            if len(ls)>1:
                diff=abs(round(ls[0].co.Axis-ls[1].co.Axis,6))
                if diff>0:
                    if ls[0].co.Axis<ls[1].co.Axis:A=ls[0].co.Axis+diff/2
                    else:A=ls[1].co.Axis+diff/2
                    v.co.Axis=A
     '''
    S=S.replace('Axis',Axis);
    exec(S);
    
    
def gMid(a='x'):gotoMid(a)                

#----------vert slide (shft_v)----------------------------------------
def vertSlide(v=0.5):
    bpy.ops.transform.vert_slide(override1(),value=v, mirror=True, correct_uv=True)
    
def shft_v(v=0.5):vertSlide(v)
def shfV(v=0.5):vertSlide(v)
#def V(v=0.5):vertSlide(v)


#-----------------GoLocation(x,y,z)-------------------------------
def GoLocation(x,y,z):
    md=bpy.context.object.mode
    if md=='OBJECT':
        obj=bpy.context.object
        obj.location=Vector((x,y,z))
    else:
        obj=bpy.context.edit_object;me=obj.data
        bm=bmesh.from_edit_mesh(me)
        ls=lsV()
        for L in ls:
            for v in bm.verts[L:L+1]:
                v.co.x=x; v.co.y=y;v.co.z=z
        bmesh.update_edit_mesh(me, True)     

#-----------rotate----------------------------------------------------
def rotate(Angle=90,Axis='X'):
    v=math.radians(Angle)

    P_edit_falloff=bpy.context.scene.tool_settings.proportional_edit_falloff
    P_edit_size=bpy.context.scene.tool_settings.proportional_size

    if Axis.upper()=='X':A=(1,0,0);Con_Axis=(True,False,False)
    if Axis.upper()=='Y':A=(0,1,0);Con_Axis=(False,True,False)
    if Axis.upper()=='Z':A=(0,0,1);Con_Axis=(False,False,True)

    #----------Version Different------------------------
    if vs()<2.8:
        P_edit=bpy.context.scene.tool_settings.proportional_edit
        bpy.ops.transform.rotate(value=v, axis=A, constraint_axis=Con_Axis, constraint_orientation='GLOBAL', mirror=False, proportional=P_edit, proportional_edit_falloff= P_edit_falloff, proportional_size=P_edit_size)
    else:
        P_edit=bpy.context.scene.tool_settings.use_proportional_edit
        bpy.ops.transform.rotate(value=v, orient_axis=Axis.upper(), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=Con_Axis,mirror=False, use_proportional_edit=P_edit, proportional_edit_falloff=P_edit_falloff, proportional_size=P_edit_size, use_proportional_connected=False, use_proportional_projected=False)


    #---------------------------------------------------

def ry(j=90):rotate(j,'Y')
def rz(j=90):rotate(j,'Z')
def rx(j=90):rotate(j,'X')

def r(x=0,y=0,z=0): rx(x);ry(y);rz(z)


#-----------resize----------------------------------------------------
def resize(x,y,z):
    
    
    P_edit_falloff=bpy.context.scene.tool_settings.proportional_edit_falloff
    P_edit_size=bpy.context.scene.tool_settings.proportional_size

    #----------------------Version Different---------------------------
    if vs()<2.8:
        P_edit=bpy.context.scene.tool_settings.proportional_edit
        bpy.ops.transform.resize(value=(x, y, z),  proportional=P_edit, proportional_edit_falloff=P_edit_falloff, proportional_size=P_edit_size)
    else:
        P_edit=bpy.context.scene.tool_settings.use_proportional_edit
        bpy.ops.transform.resize(value=(x, y, z),  use_proportional_edit=P_edit, proportional_edit_falloff=P_edit_falloff, proportional_size=P_edit_size)
    #------------------------------------------------------------------
        

def s(x,y='',z=''):
    if y=='' and z=='':resize(x,x,x)
    else:resize(x,y,z)

def sx(v):resize(v,1,1)
def sy(v):resize(1,v,1)
def sz(v):resize(1,1,v)

#-----------rename---------------------------------------------------
def rename(name=''):
    bpy.context.object.name = name
    
def F2(name=''):rename(name)


#------------extrude-------------------------------------------------
def extrude(x=0,y=0,z=0):
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(x, y, z)})

def e(x=0,y=0,z=0):extrude(x,y,z)
def ex(x):extrude(x,0,0)
def ey(y):extrude(0,y,0)
def ez(z):extrude(0,0,z)

#------------extrude_indiv-------------------------------------------
def extrudeIndiv(v=0):
   bpy.ops.mesh.extrude_faces_move(TRANSFORM_OT_shrink_fatten={"value":v})

def eI(v=0):extrudeIndiv(v)
def ei(v=0):eI(v)
#-----------face add (fill)-------------------------------------------------
def faceAdd():
    m0();m1();
    bpy.ops.mesh.edge_face_add()
    
def fill():faceAdd()
def f():faceAdd()


#-----------subdive face to be half--------------------
def subHalfFace(v=0):  #v=0 is horizontal subdive, v=1 is vertical subdive
    subd(1);#fMelt();
    
#-----------duplicate------------------------------------------------
def duplicate(Link=False):
    if mode('name')=='EDIT':bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0)})
    else:bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":Link, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0,0,0)})
def shft_d():duplicate()
def D():shft_d()

def alt_d():duplicate(Link=True)
def altD():alt_d()

#-----------object join-----------------------------------------------
def objectJoin():
    bpy.ops.object.join()

def ctrl_j():objectJoin()
def ctrJ():ctrl_j()

#------------bridge edge----------------------------------------------
def bridge():
    bpy.ops.mesh.bridge_edge_loops()

#-------------bevel--------------------------------------------------
def bevel(Offset,Segments):
    bpy.ops.mesh.bevel(offset=Offset, segments=Segments)

def ctrl_b(Offset,Segments):bevel(Offset,Segments)
def ctrB(Offset,Segments):ctrl_b(Offset,Segments)
def b(Offset,Segments):ctrl_b(Offset,Segments)  

#-----------shade smooth---------------------------------------------
def shadeSmooth():
    if modeI!=0:m0()
    bpy.ops.object.shade_smooth()

def smooth():shadeSmooth()
def smth():shadeSmooth()
def sm():shadeSmooth()

#---------------bisect-----------------------------------------------
def bisect(Axis='X',Co=(0,0,0)):
    ax=Axis;
    if mode('name')!='EDIT':m3()
    if str(type(ax))=="<class 'str'>": ax=Axis.upper();
    if ax=='X' or ax==0:a=(1,0,0)
    if ax=='Y' or ax==1:a=(0,1,0)
    if ax=='Z' or ax==2:a=(0,0,1)

    if ax=='XY' or ax==3:a=(1,1,0)
    if ax=='XZ' or ax==4:a=(1,0,1)
    if ax=='YZ' or ax==5:a=(0,1,1)

    bpy.ops.mesh.bisect(plane_co=Co, plane_no=a, xstart=0, xend=0, ystart=0, yend=0)


#-------------loopCut(ctrR)---------------------------------------------------------------
def loopCutReturnList(Cuts):  #return [[LoopEdge1_vert1,LoopEdge1_vert2],[LoopEdge2_vert1,LoopEdge2_vert2]...]  each loopEdge Vert list only 2 First Verts for each Loop ,need add alt() when select use;
    obj=bpy.context.edit_object;bm=bmesh.from_edit_mesh(obj.data);ls=lsV()[:Cuts];Ls=[]

    for I in ls:
        L=[I];Found=False
        for v in bm.verts[I:I+1]:
            for E in v.link_edges:
                for V in E.verts:
                   if V.index!=I and V.index!=I+1 and V.index!=I-1:L.append(V.index);Found=True;break
                if Found:break   
        Ls.append(L)
    return Ls

    
def loopCut(Cuts=1,Slide=0):   # need select Edge first (use that edge to decide direction of loopCuting)
    if mode('name')!='EDIT':m2()
    ls=lsE();EdgeIndex=If(ls==[],0,ls[0]); #get first selected edge to decide how to loopCut,if not select use 0 as first index of edge
    
    #-----version different----------(>2.8 need add '"object_index":0,' befor 'edge_index' )---------
    if vs()<2.8:bpy.ops.mesh.loopcut_slide(override(),MESH_OT_loopcut={"number_cuts":Cuts, "smoothness":0, "falloff":'INVERSE_SQUARE', "edge_index":EdgeIndex}, TRANSFORM_OT_edge_slide={"value":Slide})
    else:bpy.ops.mesh.loopcut_slide(override(),MESH_OT_loopcut={"number_cuts":Cuts, "smoothness":0, "falloff":'INVERSE_SQUARE',"object_index":0,  "edge_index":EdgeIndex}, TRANSFORM_OT_edge_slide={"value":Slide})
    #------------------------------------------------------------------------------------------------
    return loopCutReturnList(Cuts)  #return first 2 verts of each loop [[v1,v2],[],[]...];   when use need add alt(); example:  ls=ctrR(2);v(ls[0]);alt();

def ctrl_r(Cuts=1,Slide=0):return loopCut(Cuts,Slide)
def ctrR(Cuts=1,Slide=0):return loopCut(Cuts,Slide)
def cR(Cuts=1,Slide=0):return ctrR(Cuts,Slide)
def cr(Cuts=1,Slide=0):return ctrR(Cuts,Slide)


#--------------loopCut Old (use bisect instead of loopCut function)-----NO MORE USE----
def loopCut_OLD(Axis='X',Co=0,LinkIndex='all'):  #use bisect as loop Cut
    obj=bpy.context.object;
    if mode('name')!='EDIT':m3()

    if LinkIndex=='all':a()
    else:l(LinkIndex);

    if isTp(Co,'1','.'):
        ax=Axis
        if str(type(ax))=="<class 'str'>":ax=Axis.upper()
        if ax=='X' or ax==0:Co=(Co,0,0)
        if ax=='Y' or ax==1:Co=(0,Co,0)
        if ax=='Z' or ax==2:Co=(0,0,Co)

    bisect(Axis,Co)
        
#def ctrl_r(a='X',c=0,l='all'):loopCut(a,c,l)
#def ctrR(a='X',c=0,l='all'):ctrl_r(a,c,l)



#-----------faceLoopSelect----------
def faceLoopSelect1(FaceIndex,r=0):  
    obj=bpy.context.object
    bm=bmesh.from_edit_mesh(obj.data)
    m2();
    ls=[]
    for f in bm.faces[FaceIndex:FaceIndex+1]:
        f.select=True
        for e in f.edges[r:r+1]:
            sE(e.index);alt();
            ls.extend(lsE());
        for e in f.edges[r+2:r+3]:
            sE(e.index);alt();
            ls.extend(lsE());
    sE(ls);sF_(lsV());
    bmesh.update_edit_mesh(obj.data)

def faceLoopSelect2(FaceIndex):
    loopFaceSelect1(FaceIndex,0)

    
def faceLoopSelect(r=0):
    ls=lsF();sN();
    if len(ls)>0:
        if len(ls)==1:
            faceLoopSelect1(ls[0],r)
        else:
            faceLoopSelect2(ls)
    

def faceLoopMerge(): #----not usefull, has some wrong---
    ls=lsF();n=int(len(ls)/4);
    for i in range(0,n):
        ii=n*4-i*3
        sF([ls[i],ls[ii-1]]);faceMelt();
        sF([ls[ii-2],ls[ii-3]]);faceMelt();
        
#----------loopFaceSubdive---------------------
def faceLoopSubdive(r=0):
    exec('faceLoopSelect('+str(r)+');subd(1)')


#-------------------FaceCut-----------------------------------------
def faceCut():
    exec('subdive()')
#-------------------EdgeClear---------------------------------------
def edgeClear():
    bpy.ops.mesh.dissolve_edges(use_verts=False)

#--------------knife cut--------------------------------------------
def knifeCut():
    bpy.ops.mesh.knife_tool(override(),use_occlude_geometry=True, only_selected=False)

def k():knifeCut()

#---------------rip move-(not function yet, if run flash exit app)-------------------------------------------
def ripMove(x=0,y=0,z=0):
    
    if mode('name')!='EDIT':m1()

    win      = bpy.context.window
    scr      = win.screen
    areas3d  = [area for area in scr.areas if area.type == 'VIEW_3D']
    region   = [region for region in areas3d[0].regions if region.type == 'WINDOW']
    Override = {'window':win,
                'screen':scr,
                'area'  :areas3d[0],
                'region':region[0],
                'scene' :bpy.context.scene,
                'selected_objects':bpy.context.object
                }

    #----------------Version Different------------------------------
    if vs()<2.8:bpy.ops.mesh.rip_move(Override,MESH_OT_rip={"mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "release_confirm":False, "use_accurate":False, "use_fill":False}, TRANSFORM_OT_translate={"value":(x,y,z), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
    else:bpy.ops.mesh.rip_move(Override,MESH_OT_rip={"mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "release_confirm":False, "use_accurate":False, "use_fill":False}, TRANSFORM_OT_translate={"value":(x, y, z), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

#def v(x=0,y=0,z=0):ripMove(x,y,z)

#--------------inset------------------------------------------------
def inset(Thick=0,Depth=0):
    bpy.ops.mesh.inset(thickness=Thick, depth=Depth)

def i(t=0,d=0):inset(t,d)

#--------------split------------------------------------------------
def split():
    if mode('name')!='EDIT':mode('EDIT');
    bpy.ops.mesh.split()
    
def y():split()

#---------------part(split to an independent obj)-----------------------------------------------
def p():
    bpy.ops.mesh.separate(type='SELECTED')

def p_OLD():#-----Before use myself write, not good than standard ops codes above-----------
    if mode('name')!='EDIT':m3();
    md='FACE';md=modeIndexName(modeI())
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    vi=[];verts=[]
    for v in bm.verts:
        if v.select:
            vi.append(v.index)
            verts.append(v2t(v.co))
    
    edges=[]
    for e in bm.edges:
        if e.select:
            edges.append(lsI(vi,e2v(e.index)))

    faces=[]
    for f in bm.faces:
        if f.select:  
             faces.append(lsI(vi,f2v(f.index)))
    
    
    mesh = bpy.data.meshes.new(obj.name)
    mesh.from_pydata(verts,edges,faces)
    mesh.update()
    
    
    objNew = bpy.data.objects.new(obj.name, mesh)
    
    #-----------Version Different------------------
    if vs()<2.8:bpy.context.scene.objects.link(objNew)
    else:bpy.context.collection.objects.link(objNew)
    #----------------------------------------------
    
    bpy.ops.mesh.delete(type=md)
    objNew.matrix_world=obj.matrix_world


#------------normals-------------------------------------------------
def flipNormals():
    bpy.ops.mesh.flip_normals()


#--------clearX/clearY/clearZ (clear all things over X/Y/Z axis)------------
    
def clearAxisOver(a='x',d='+',v=0):#a:axis, d:direction, v:value
    md=mode('name');
    if md!='EDIT':m1();
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data);sN()

    if d=='+':
        if a.upper()=='X':
             for V in bm.verts:
                    if V.co.x>v:V.select=True

        if a.upper()=='Y':
             for V in bm.verts:
                    if V.co.y>v:V.select=True
            
        if a.upper()=='Z':
            for V in bm.verts:
                    if V.co.z>v:V.select=True
    else:
        if a.upper()=='X':
             for V in bm.verts:
                    if V.co.x<v:V.select=True

        if a.upper()=='Y':
             for V in bm.verts:
                    if V.co.y<v:V.select=True
            
        if a.upper()=='Z':
            for V in bm.verts:
                    if V.co.z<v:V.select=True    

    
    bpy.ops.mesh.delete(type='VERT')
    bmesh.update_edit_mesh(obj.data)
    if md!='EDIT':mode(md);
    

def clearX(d='+',v=0):clearAxisOver('x',d,v)
def clearY(d='+',v=0):clearAxisOver('y',d,v)
def clearZ(d='+',v=0):clearAxisOver('z',d,v)

#---x0/z0/y0 (keep veters not over x/y/z axis,if over change to 0 (for mirror use)--
def keepNotOver(Sign='<',Vlaue=0,Axis='X'):
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    V=Vlaue
    if Sign=='<':
        if Axis.upper()=='X':
            for v in bm.verts:
                if v.co.x<V:v.co.x=V
        
        if Axis.upper()=='Y':
             for v in bm.verts:
                if v.co.y<V:v.co.y=V

        if Axis.upper()=='Z':
             for v in bm.verts:
                if v.co.z<V:v.co.z=V
                
    if Sign=='>':
        if Axis.upper()=='X':
            for v in bm.verts:
                if v.co.x>V:v.co.x=V
        
        if Axis.upper()=='Y':
             for v in bm.verts:
                if v.co.y>V:v.co.y=V

        if Axis.upper()=='Z':
             for v in bm.verts:
                if v.co.z>V:v.co.z=V


def x0(s='<',v=0):keepNotOver(s,v,'X')
def y0(s='<',v=0):keepNotOver(s,v,'Y')
def z0(s='<',v=0):keepNotOver(s,v,'Z')



#------------transform apply---------------------------------------
def transformApply():
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

def ctrl_a():transformApply()
def ctrA():ctrl_a()

#--------------subdive--------------------------------------------
def subdive(n=1):
    #-----------Version Different---------------------------------
    if vs()<2.8:bpy.ops.mesh.subdivide(number_cuts=n)
    else:bpy.ops.mesh.subdivide(number_cuts=n, quadcorner='INNERVERT')

def subd(n=1):subdive(n)

#=================Modifier===============================================

def subSurf(Viewport=3,Type='',Apply=False):

    #----------Version Different---------------------
    if vs()<2.8:
        bpy.ops.object.subdivision_set(level=Viewport)
    else:
        bpy.ops.object.modifier_add(type='SUBSURF')
        md=bpy.context.object.modifiers;i=len(md)-1;md[i].levels = Viewport
        if Type!='':
            if Type[:1].upper()=='S':typ='SIMPLE'
            else:typ='CATMULL_CLARK'
            bpy.context.object.modifiers[mdfname].subdivision_type = typ

        if Apply:
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mdfname)

    #-------------------------------------------------

def subsurf(v=3,t='',a=False):subSurf(v,t,a)    
def subs(v=3,t='',a=False):subSurf(v,t,a)
def subSurfApply(v=3,t=''):subSurf(v,t,a=True)
def subSurfA(v=3,t=''):subSurfApply(v,t)

def ctrl_1(v=1):bpy.ops.object.subdivision_set(level=v, relative=False)
def ctrl_2(v=2):bpy.ops.object.subdivision_set(level=v, relative=False)
def ctrl_3(v=3):bpy.ops.object.subdivision_set(level=v, relative=False)
def ctrl_4(v=4):bpy.ops.object.subdivision_set(level=v, relative=False)
def ctrl_5(v=5):bpy.ops.object.subdivision_set(level=v, relative=False)
def ctrl_6(v=6):bpy.ops.object.subdivision_set(level=v, relative=False)

def ctr1(v=1):ctrl_1(v)
def ctr2(v=2):ctrl_2(v)
def ctr3(v=3):ctrl_3(v)
def ctr4(v=4):ctrl_4(v)
def ctr5(v=5):ctrl_5(v)
def ctr6(v=6):ctrl_6(v)

#----------------boolean modifier-----------------
def booleanModifier(ObjName='',Operation='DIFFERENCE'):
    bpy.ops.object.modifier_add(type='BOOLEAN')
    i=len(bpy.context.object.modifiers)-1
    m=bpy.context.object.modifiers[i]
    m.object = bpy.data.objects[ObjName]
    m.operation = Operation.upper()
    return m

def bl(ObjName='',Operation='DIFFERENCE'):return booleanModifier(ObjName,Operation)

#----------------mirror modifier-------------------
def mirrorModifier(Axis='x',UseClip=True,MirObj=''):
    bpy.ops.object.modifier_add(type='MIRROR')
    md=bpy.context.object.modifiers;j=len(md)-1;md=md[j]
    zh=Axis.upper()
    if zh[0]!='X':
        i=ord(zh[0])-ord('X')
        md.use_axis[0]=False
        md.use_axis[i] = True
    md.use_clip = UseClip
    if MirObj!='':md.mirror_object=bpy.data.objects[MirObj]

 
def mirror(a='x',c=True,mObj=''):mirrorModifier(a,c,mObj)
def mir(a='x',c=True,mObj=''):mirrorModifier(a,c,mObj)


def mirrorUseClip(UseClip=True,md=''):
    if md=='':
        md=bpy.context.object.modifiers
        for Md in md:
            if Md.type=='MIRROR': Md.use_clip=UseClip
def mirClip(UseClip=True,md=''):mirrorUseClip(UseClip,md)
def mClip(UseClip=True,md=''):mirrorUseClip(UseClip,md)

#-----------------simple Deform-----------------
def simpleDeform(Method='TWIST'):
    bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
    i=len(bpy.context.object.modifiers)-1
    sd=bpy.context.object.modifiers[i]
    sd.deform_method=Method.upper()
    return sd

def sDeform(Method='TWIST'):return simpleDeform(Method)

#-----------------apply modifier------------------
def applyModifier(a=''):
    try:
        if mode('name')!='OBJECT':m0();
        M=bpy.context.object.modifiers
        if a.lower()[:3]=='obj':
            for m in M:bpy.ops.object.modifier_apply(modifier=m.name) 
        else:
            i=len(M)-1;m=M[i];bpy.ops.object.modifier_apply(modifier=m.name)
            
    except:pass
    
def ap(a=''):applyModifier(a='')


#=================Sculpt==========================================

#-------sculpt mode------------------------------
def sculptMode():
    try:bpy.ops.object.mode_set(mode='SCULPT')
    except:pass

#-------brush size----(Radius)---------------------------
def brushSize(Size=''):
    if isTp(Size,'1','.'): bpy.context.tool_settings.unified_paint_settings.size=Size #--NotUSE: bpy.context.tool_settings.sculpt.brush.size=Size
    return bpy.context.tool_settings.unified_paint_settings.size

def bSize(s=''):return brushSize(s)
def bRadius(r=''):return brushSize(r)

#--------brush strength--------------------------
def brushStrength(v=''):
    if isTp(v,'1','.'): bpy.context.tool_settings.sculpt.brush.strength=v
    return bpy.context.tool_settings.unified_paint_settings.strength

def bStrength(v):return brushStrength(v)
def bSt(v):return brushStrength(v)


#--------brush AutoSmooth--------------------------
def brushAutoSmooth(v=''):
    if isTp(v,'1','.'): bpy.context.tool_settings.sculpt.brush.auto_smooth_factor=v
    return bpy.context.tool_settings.sculpt.brush.auto_smooth_factor

def bAutoSmooth(v):return brushAutoSmooth(v)
def bAS(v): return brushAutoSmooth(v)
def bSmooth(v): return brushAutoSmooth(v)
def bSm(v):return bSmooth(v)

#-------brush Use Setting------------------------
def brushUse(Name='Grab',Radius='',Strength='',AutoSmooth=''):
    Name=Name.capitalize();
    bpy.context.tool_settings.sculpt.brush=bpy.data.brushes[Name]

    if isTp(Radius,'1','.'):brushSize(Radius)
    if isTp(Strength,'1,','.'):brushStrength(Strength)
    if isTp(AutoSmooth,'1','.'):brushAutoSmooth(AutoSmooth)
    
    return bpy.context.tool_settings.sculpt.brush

def bUse(n='Grab',r='',s='',a=''):return brushUse(n,r,s,a)
def brush(n='Grab',r='',s='',a=''):return brushUse(n,r,s,a)
def br(n='Grab',r='',s='',a=''):return brush(n,r,s,a)
def b(n='Grab',r='',s='',a=''):return brush(n,r,s,a)

#=================Outliner===============================================


#-----------------shft_s-------(copy)--------------------------------------------
def shft_s(i=1):
    if i==1:cs0()
    if i==2:bpy.ops.view3d.snap_cursor_to_selected()
    if i==3:bpy.ops.view3d.snap_cursor_to_active()
    if i==4:bpy.ops.view3d.snap_cursor_to_grid()
    
    if i==6:bpy.ops.view3d.snap_selected_to_grid()
    if i==7:bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
    if i==8:bSpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    if i==9:bpy.ops.view3d.snap_selected_to_active()

def shfS(i):shft_s(i)
def S(i):shft_s(i)  

    

#===============Model=========================================

#-------------Create basic Model-----------------------------
def plane(Size=2):
    #------------Version Different-----------------------------------------------------
    if vs()<2.8:bpy.ops.mesh.primitive_plane_add(radius=Size, location=(0, 0, 0))
    else:bpy.ops.mesh.primitive_plane_add(size=Size, location=(0, 0, 0))
    #----------------------------------------------------------------------------------
def pl(Size=2):plane(Size)

def cubeCreate():
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    reIndex()
    
def cube(v=0):
    cubeCreate();
    if v>0:subSurf(v);smooth()

def Cube(v=0):cube(v=0)
def cu(v=0):cube(v=0)


def circle(Radius=1):
    bpy.ops.mesh.primitive_circle_add(radius=Radius, enter_editmode=False, location=(0, 0, 0))


def sphere(Radius=1):
    #--------------Version Different-------------------------------
    if vs()<2.8:bpy.ops.mesh.primitive_uv_sphere_add(size=Radius, view_align=False, enter_editmode=False, location=(0, 0, 0))
    else:bpy.ops.mesh.primitive_uv_sphere_add(radius=Radius, enter_editmode=False, location=(0, 0, 0))
    #--------------------------------------------------------------

def sph(Radius=1):sphere(Radius)
def sp(Radius=1):sphere(Radius)

def icoSphere(Radius=1):
    bpy.ops.mesh.primitive_ico_sphere_add(radius=Radius, enter_editmode=False, location=(0, 0, 0))

def cylinder(Radius=1,Depth=2):
    bpy.ops.mesh.primitive_cylinder_add(radius=Radius, depth=Depth, enter_editmode=False, location=(0, 0, 0))

def cone(Radius1=1,Radius2=0,Depth=2):
    bpy.ops.mesh.primitive_cone_add(radius1=Radius1, radius2=Radius2, depth=2, enter_editmode=False, location=(0, 0, 0))

def torus():
    bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)

def grid(Size=2):
    bpy.ops.mesh.primitive_grid_add(size=Size, enter_editmode=False, location=(0, 0, 0))

def monkey(Size=2):
    #----------Version Different-------------------
    if vs()<2.8:bpy.ops.mesh.primitive_monkey_add(radius=Size,location=(0, 0, 0))
    else:bpy.ops.mesh.primitive_monkey_add(size=Size,location=(0, 0, 0))
    #reIndex()

def text(Text='Text'):
    txt_data = bpy.data.curves.new(name=Text, type='FONT')
    txt_ob = bpy.data.objects.new(name="Text", object_data=txt_data)
    bpy.context.collection.objects.link(txt_ob)
    txt_data.body = Text        
    txt_data.align_x = 'CENTER' 

def empty(Type='ARROWS'):
    bpy.ops.object.empty_add(type=Type.upper(), location=(0, 0, 0))
    return bpy.context.object

#-----------Self Special Models-------------------------------
#------------halfSphere---------------------------------------
def halfSphere(Axis='X'):
    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=True, location=(0, 0, 0))
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    vv=bm.verts
    zh=Axis.upper()
    if zh=='X' or zh=='X+':
        for v in vv[0:251]:v.select=False
        for v in vv[296:297]:v.select=False
        for v in vv[477:482]:v.select=False
        
    if zh=='X-':
        ls=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235]
        selectVert(ls)
    
    if zh=='Y' or zh=='Y+':
        ls=[133,134,135,136,137,138,139,140,141,146,147,148,149,150,151,152,153,154,155,156,157,158,161,162,163,164,165,166,167,168,169,170,171,172,173,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,313,314,315,316,317,318,319,320,321,322,323,324,325,328,329,330,331,332,333,334,335,336,337,338,339,340,345,346,347,348,349,350,351,352,353]
        selectVert(ls)
        
    if zh=='Y-':
        ls=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,373,374,375,376,377,378,379,380,381,382,383,384,385,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481]
        selectVert(ls)
    
    if zh=='Z' or zh=='Z+':
        ls=[8,9,18,19,20,21,22,23,24,33,34,35,36,37,38,39,48,49,50,51,52,53,54,63,64,65,66,67,68,69,78,79,80,81,82,83,84,93,94,95,96,97,98,99,108,109,110,111,112,113,114,123,124,125,126,127,128,129,138,139,140,141,142,143,144,153,154,155,156,157,158,159,168,169,170,171,172,173,174,183,184,185,186,187,188,189,198,199,200,201,202,203,204,205,214,215,216,217,218,219,220,229,230,231,232,233,234,235,244,245,246,247,248,249,250,259,260,261,262,263,264,265,274,275,276,277,278,279,280,289,290,291,292,293,294,295,305,306,307,308,309,310,311,320,321,322,323,324,325,326,335,336,337,338,339,340,341,350,351,352,353,354,355,356,365,366,367,368,369,370,371,380,381,382,383,384,385,386,395,396,397,398,399,400,401,410,411,412,413,414,415,416,425,426,427,428,429,430,431,440,441,442,443,444,445,446,455,456,457,458,459,460,461,470,471,472,473,474,475,476,477,478,479,480,481]
        selectVert(ls)

    if zh=='Z-':
        ls=[0,1,2,3,4,5,6,10,11,12,13,14,15,16,25,26,27,28,29,30,31,40,41,42,43,44,45,46,55,56,57,58,59,60,61,70,71,72,73,74,75,76,85,86,87,88,89,90,91,100,101,102,103,104,105,106,115,116,117,118,119,120,121,130,131,132,133,134,135,136,145,146,147,148,149,150,151,160,161,162,163,164,165,166,175,176,177,178,179,180,181,190,191,192,193,194,195,196,206,207,208,209,210,211,212,221,222,223,224,225,226,227,236,237,238,239,240,241,242,251,252,253,254,255,256,257,266,267,268,269,270,271,272,281,282,283,284,285,286,287,296,297,298,299,300,301,302,303,312,313,314,315,316,317,318,327,328,329,330,331,332,333,342,343,344,345,346,347,348,357,358,359,360,361,362,363,372,373,374,375,376,377,378,387,388,389,390,391,392,393,402,403,404,405,406,407,408,417,418,419,420,421,422,423,432,433,434,435,436,437,438,447,448,449,450,451,452,453,462,463,464,465,466,467,468]
        selectVert(ls)
        
        
    bpy.ops.mesh.delete(type='VERT')
    mode("OBJECT")

def hSphere(a='X'):halfSphere(a)

#-----------mirrorSphere-------------------------------------
def mirrorSphere(Axis='X'):
    zh=Axis.upper()
    halfSphere(zh)
    bpy.ops.object.modifier_add(type='MIRROR')
    if zh[0]!='X':
        i=ord(zh[0])-ord('X')
        bpy.context.object.modifiers["Mirror"].use_axis[0]=False
        bpy.context.object.modifiers["Mirror"].use_axis[i] = True

def mirSphere(a='X'):mirrorSphere(a)
def mSphere(a='X'):mirrorSphere(a)

#-------------halfCube---------------------------------------
def halfCube(Axis='X'):
    bpy.ops.mesh.primitive_cube_add(enter_editmode=True, location=(0, 0, 0))
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    zh=Axis.upper()
    if zh=='X' or zh=='X+':
        selF([0]);x();x0()
        
    if zh=='X-':
        selF([2]);x();x0('>')
    
    if zh=='Y' or zh=='Y+':
        selF([3]);x();y0()
        
    if zh=='Y-':
        selF([1]);x();y0('>')
    
    if zh=='Z' or zh=='Z+':
        selF([4]);x();z0()
    
    if zh=='Z-':
        selF([5]);x();z0('>')

    mode("OBJECT")

def hCube(a='X'):halfCube(a)

#-------------mirrorCube---------------------------------------
def mirrorCube(Axis='X'):
    if isTp(Axis,'s'):
        zh=Axis.upper()
        halfCube(zh);reIndex()
        mirror(Axis,True)

    if isTp(Axis,'1'):
        cube(Axis);ap();clearX('-',-0.01);
        reIndex()
        mirror('X',True)

        
def mirCube(a='X'): mirrorCube(a)
def mCube(a='X'):mirrorCube(a)
def mcube(a='X'):mCube(a)
def mCu(a='X'):mirrorCube(a)
def mcu(a='X'):mCu(a)
#---------------backWall---------------------------------------

def wall(Type='wallOnly',Name='wall'):
    plane();rx(90);gy(10);s(30);sx(5);n(Name)
    if Type in ('withGround','g'):gz(30);m2();sN();selE([1]);ey(-50);selE([1]);ctrB(0.2,10);sm();



#===================Bone Armature==============================
def parentSet(Type='ARMATURE_AUTO'):
    bpy.ops.object.parent_set(type=Type)

def ctrl_p(Type='ARMATURE_AUTO'):parentSet(Type)
def ctrP(Type='ARMATURE_AUTO'):parentSet(Type)


#==========mybpy self plugs samples===(Maybe Future,mybpy will as plug privide drop file function as mybpy maya surport, No use for the timebeing)==================

#-------msgboxOperator----to show msg----------------
class msgOperator(bpy.types.Operator):
    bl_idname = "mybpy.msg"
    bl_label = "mybpy msg"
 
    text = bpy.props.StringProperty(name="msg")
 
    def execute(self, context):
        message = self.text
        self.report({'INFO'}, message)
        wm = context.window_manager
        return wm.invoke_popup(self)
    
def regMsg():
    try:bpy.utils.register_class(msgOperator)
    except:pass

def unregMsg():
    try:bpy.utils.unregister_class(msgOperator)
    except:pass
    
def runMsg(Text=''):
    try:bpy.ops.mybpy.msg(text=Text)
    except:regMsg();bpy.ops.mybpy.msg(text=Text)
    
def msg(Text=''):
    if isType(Text,'s'):Text='"'+Text+'"'
    if Text==[]:Text='[]'
    if Text==None:Text='<None>'
    if isType(Text,'s')==False:Text=str(Text)    
    runMsg(Text)


# Sample Plugs:(from: https://www.baidu.com/link?url=iZIndYwnuRjibjC-GTQbpcRxatN8hcq-OjRAJ463A3l8YgsckKrFXz7mzzpiKaXv&wd=&eqid=cfa3d05700031ecf00000006611f5c36

#-----InfoPrint Sample-------------------------------------------
class InfoPrintOperator(bpy.types.Operator):
    bl_idname = "mybpy.info_print"
    bl_label = "mybpy info print Operator"
    text=bpy.props.StringProperty(name="String Value")
    def execute(self, context):
        self.report({'INFO'},self.text)
        return {'FINISHED'}
 
def regInfoPrint():
    try:bpy.utils.register_class(InfoPrintOperator)
    except:pass

def infoPrint(Text=''):
    regInfoPrint();bpy.ops.mybpy.info_print(text=Text)
    
def Print(text=''):infoPrint(text)
def prnt(text=''):infoPrint(text)

#-------SimpleMouseOperator------------------------
class SimpleMouseOperator(bpy.types.Operator):
    """ This operator shows the mouse location,
        this string is used for the tooltip and API docs
    """
    bl_idname = "mybpy.mouse_position"
    bl_label = "mybpy Simple Mouse Position"
 
    x = bpy.props.IntProperty()
    y = bpy.props.IntProperty()
 
    def execute(self, context):
        # rather than printing, use the report function,
        # this way the message appears in the header,
        self.report({'INFO'}, "Mouse coords are %d %d" % (self.x, self.y))
        return {'FINISHED'}
 
    def invoke(self, context, event):
        self.x = event.mouse_x
        self.y = event.mouse_y
        return self.execute(context)
 
def regSimpleMouse():bpy.utils.register_class(SimpleMouseOperator)
 
# Test call to the newly defined operator.
# Here we call the operator and invoke it, meaning that the settings are taken
# from the mouse.
#bpy.ops.wm.mouse_position('INVOKE_DEFAULT')
 
# Another test call, this time call execute() directly with pre-defined settings.
#bpy.ops.wm.mouse_position('EXEC_DEFAULT', x=20, y=66)

#---------------------------
class ExportSomeData(bpy.types.Operator):  #---only 2.79 not error---
    """Test exporter which just writes hello world"""
    bl_idname = "mybpy.expor_some_data"
    bl_label = "mybpy Export Some Data"
 
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")
 
    @classmethod
    def poll(cls, context):
        return context.object is not None
 
    def execute(self, context):
        file = open(self.filepath, 'r')
        print(file.read())
        file.close()
        #file.write("Hello World " + context.object.name)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
 
# Only needed if you want to add into a dynamic menu
def menu_func(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(ExportSomeData.bl_idname, text="Text Export Operator")
 
# Register and add to the file selector
def regExportSomeData():
    bpy.utils.register_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.append(menu_func)
 
# test call
#bpy.ops.mybpy.export_some_data('INVOKE_DEFAULT')

#-----Dinog Sample------------------------------
class DinogOperator(bpy.types.Operator):
    bl_idname = "mybpy.dialog_operator"
    bl_label = "mybpy Dialog Operator"
 
    my_float = bpy.props.FloatProperty(name="Some Floating Point")
    my_bool = bpy.props.BoolProperty(name="Toggle Option")
    my_string = bpy.props.StringProperty(name="String Value")
 
    def execute(self, context):
        message = "Popup Values: %f, %d, '%s'" % \
            (self.my_float, self.my_bool, self.my_string)
        self.report({'INFO'}, message)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def regDialog():bpy.utils.register_class(DialogOperator)
 
# test call
#bpy.ops.mybpy.dialog_operator('INVOKE_DEFAULT')


#-------CustomDrawSample----------------------
 
class CustomDrawOperator(bpy.types.Operator):
    bl_idname = "mybpy.custom_draw"
    bl_label = "mybpye Custom Draw"
 
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")
 
    my_float = bpy.props.FloatProperty(name="Float")
    my_bool = bpy.props.BoolProperty(name="Toggle Option")
    my_string = bpy.props.StringProperty(name="String Value")
 
    def execute(self, context):
        print("Test", self)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
 
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Custom Interface!")
 
        row = col.row()
        row.prop(self, "my_float")
        row.prop(self, "my_bool")
 
        col.prop(self, "my_string")
 
def regCustomDraw():bpy.utils.register_class(CustomDrawOperator)
 
# test call
#bpy.ops.mybpy.custom_draw('INVOKE_DEFAULT')
#
#--------------Modal---This operator defines a Operator.modal function that will keep being run to handle events until it returns {'FINISHED'} or {'CANCELLED'}
 
class ModalOperator(bpy.types.Operator):
    bl_idname = "mybpy.modal_operator"
    bl_label = "mybpy Simple Modal Operator"
 
    def __init__(self):
        print("Start")
 
    def __del__(self):
        print("End")
 
    def execute(self, context):
        context.object.location.x = self.value / 100.0
        return {'FINISHED'}
 
    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':  # Apply
            self.value = event.mouse_x
            self.execute(context)
        elif event.type == 'LEFTMOUSE':  # Confirm
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:  # Cancel
            context.object.location.x = self.init_loc_x
            return {'CANCELLED'}
 
        return {'RUNNING_MODAL'}
 
    def invoke(self, context, event):
        self.init_loc_x = context.object.location.x
        self.value = event.mouse_x
        self.execute(context)
 
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
 
def regModal():bpy.utils.register_class(ModalOperator)
 
# test call
#bpy.ops.mybpy.modal_operator('INVOKE_DEFAULT')


#-----------------MySel definate plug-------------------------------


#-----------------File Drop Operator-----(Not complete, for the future, no use now)-----------------------------------
class fileDrop(bpy.types.Operator):
    """ This operator shows the mouse location,
        this string is used for the tooltip and API docs
    """
    bl_idname = "mybpy.file_drop"
    bl_label = "mybpy File Drop=On"

    filepath=''

    def invoke(self, context, _event):
        context.window_manager.popup_menu(self.draw_menu, title=bpy.path.basename(self.filepath), icon='QUESTION')
        return {'FINISHED'}

    def draw_menu(self, menu, _context):
        layout = menu.layout
        col = layout.column()
        col.operator_context = 'INVOKE_DEFAULT'
        props = col.operator("wm.open_mainfile", text="Open", icon='FILE_FOLDER')
        props.filepath = self.filepath
        props.display_file_selector = False

        layout.separator()
        col = layout.column()
        col.operator_context = 'INVOKE_DEFAULT'
        col.operator("wm.link", text="Link...", icon='LINK_BLEND').filepath = self.filepath
        col.operator("wm.append", text="Append...", icon='APPEND_BLEND').filepath = self.filepath



def fileDropOn():
    bpy.utils.register_class(fileDrop)

def fdOn():fileDropOn()
def fOn():fileDropOn()


def fileDropOff():
    byp.utils.unregister_class(fileDrop)
    
def fdOff():fileDropOff()
def fOff():fileDropOff()

#==================Other Plug On=====================================

#---------------Human Rig (need tick plug_on 'Rigging:Rigify')-------------------------------------
def humanRig():
    try:bpy.ops.object.armature_human_metarig_add()
    except:print('no tick plug_on "Rigging:Rigify"')

def human():humanRig()
def man():humanRig()

#----------------looptool----------------------------------------
def loopToolCircle():
    try:bpy.ops.mesh.looptools_circle(custom_radius=False, fit='best', flatten=True, influence=100, lock_x=False, lock_y=False, lock_z=False, radius=1, regular=True)
    except:pass#print('no looptool plug_on')

def lpCircle():loopToolCircle()
def lpC():loopToolCircle()

#----------------looptool  Relax----------------------------------
def loopToolRelax():
    try:bpy.ops.mesh.looptools_relax(input='selected', interpolation='cubic', iterations='1', regular=True)
    except:pass#print('no looptool plug_on')


def lpRelax():loopToolRelax()
#-----------Create Model by Name------------------------------
def shft_a(Name):pass  #not do yet
def A():shft_a(Name)

#===================UV=================================================
#--------uv add----------------------------------------------------
def uvAdd(Name=''):
    bpy.ops.mesh.uv_texture_add()

    if Name!='':
        m=bpy.context.object.data;
       #-----------Version Different-------------
        if vs()<2.8:n=len(m.uv_textures)-1;m.uv_textures[n].name=Name
        else:n=len(m.uv_layers)-1;m.uv_layers[n].name=Name
       #------------------------------------------
            

#--------ensure uv has (if not has add one)-------------------------------
def uvHas(Name=''):
    mesh=bpy.context.object.data
   #-----------Version Different-------------
    if vs()<2.8:u=mesh.uv_textures
    else:u=mesh.uv_layers
   #------------------------------------------
            
    if Name=='':
        if len(u)==0: uvAdd()
    else:
        try:uv=u[Name]
        except:uvAdd(Name)

        
#--------uv clear(remove)------------------------------------------
def uvClear():
    bpy.ops.mesh.uv_texture_remove()

#--------uv select linked------------------------------------------
def uvSelectLinked():
    bpy.ops.uv.select_linked()

def uvL():uvSelectLinked()

#--------uv select all---------------------------------------------
def uvSelectAll():
    bpy.ops.uv.select_all(action='SELECT')
    
def uvA():uvSelectAll()
def uva():uvA()

#---------uv select nothing----------------------------------------
def uvSelectNothing():
    bpy.ops.uv.select_all(action='DESELECT')
    
def uvN():uvSelectNothing()


#---------uv grab (go) --------------------------------------------------
def uvGrab(x='',y='',div=100):  #m=mode type  ;div=100 percent
    mO=False
    if mode('name')!='EDIT':mO=True;m3();a();
    if tp(x)=="(" or tp(x)=="[":y=x[1];x=x[0];
    #uvN();uvA();               

    obj = bpy.context.active_object;me = obj.data
    bm = bmesh.from_edit_mesh(me)

    uv_layer = bm.loops.layers.uv.verify()
  #--------Version Different-------------------
    if vs()<2.8:bm.faces.layers.tex.verify()  # currently 2.79 blender needs both layers.
  #--------------------------------------------
    # adjust UVs
    for f in bm.faces:
        if f.select:
            for l in f.loops:
                luv = l[uv_layer]
                luv.uv=(x/div,y/div) # apply the location as x,y
            
                #if luv.select:
                    #luv.uv = l.vert.co.xy # apply the location of the vertex as a UV
        
                
          
    bmesh.update_edit_mesh(me)
    if mO:m0()
    

def uvG(x='',y='',d=100):uvGrab(x,y,d)    
def uvg(x='',y='',d=100):uvG(x,y,d)
def u(x='',y='',d=100):uvG(x,y,d)


#================Material & Texture & Images===========================

#---------------Color Convert---------------------------------
def rgb2hex(rgbcolor, tohex=True):
    '''RGB转HEX      :param rgbcolor: RGB颜色元组，Tuple[int, int, int]     :param tohex: 是否转十六进制字符串，默认转     :return: int or str      >>> rgb2hex((255, 255, 255))     16777215     >>> rgb2hex((255, 255, 255), tohex=True)     '0xffffff'     '''
    r, g, b = rgbcolor
    result = (r << 16) + (g << 8) + b
    return hex(result) if tohex else result

def hex2rgb(hexcolor):
    '''HEX转RGB      :param hexcolor: int or str     :return: Tuple[int, int, int]      >>> hex2rgb(16777215)     (255, 255, 255)     >>> hex2rgb('0xffffff')     (255, 255, 255)     '''
    hexcolor = int(hexcolor, base=16) if isinstance(hexcolor, str) else hexcolor
    rgb = ((hexcolor >> 16) & 0xff, (hexcolor >> 8) & 0xff, hexcolor & 0xff)
    return rgb

#--------------load reference image-----------------------------------
def imageRef(FilePath=''):
    #----------------Version Different---------------------------
    if vs()<2.8:
        bpy.ops.object.empty_add(type='IMAGE', location=(0,0,0));rx(90)
        Path,File=os.path.split(FilePath)
        imgOpen(Path,File);bpy.context.object.data=bpy.data.images[File]

    else:
        bpy.ops.object.load_reference_image(filepath=FilePath);
        rx(90)

def imgRef(FilePath=''):imageRef(FilePath)

#---------------Image Exist-------------------------------------------
def imageExist(Name='cc.png'):
    try:mt=bpy.data.images[Name];return True
    except:return False
    
def imgExist(Name='cc'):return imageExist(Name)

#---------------Image Clear--------------------------------------------
def imageClear(Name=''):
    if Name=='':
        n=len(bpy.data.images)
        if n>0:
            for m in bpy.data.images:bpy.data.images.remove(m)
    else:
        bpy.data.images.remove(bpy.data.images[Name])
        
def imgClear(Name=''):imageClear(Name)

#--------------Image Open  (suport PathFile one Argument)----------------------------------------------
def imageOpen(Path='',File=''):
    if File=='' and Path!='': Path,File = os.path.split(Path)
    else:
        if Path=='' and File=='': bpy.ops.image.open(filepath=pathCC+"\\cc.png", directory=pathCC, files=[{"name":"cc.png", "name":"cc.png"}], relative_path=True, show_multiview=False)
        else:bpy.ops.image.open(filepath=Path + File,directory=Path,files=[{"name":File, "name":File}], relative_path=True, show_multiview=False)

def imgOpen(Path='',File=''):imageOpen(Path,File)

#--------------Image pack---------------------------------------------------
def imagePackAll():
    img=bpy.data.images
    if len(img)>0:
        for IMG in img:IMG.pack()
        
def imagePack(ImgName=''):
    if ImgName=='':imagePackAll()
    else:bpy.data.images[ImgName].pack()
    
def imageUnpack(ImgName=''):
    if ImgName=='':imagePackAll()
    else:bpy.data.images[ImgName].unpack()


def imgPack(ImgName=''):imagePack(ImgName)
def imgUnpack(ImgName=''):imageUnpack(ImgName)

def pack():imagePackAll()

#---------------Texture Exist-------------------------------------------
def textureExist(Name='cc'):
    try:mt=bpy.data.textures[Name];return True
    except:return False
    
def txExist(Name='cc'):return textureExist(Name)

#---------------Texture Clear--------------------------------------------
def textureClear(Name=''):
    if Name=='':
        n=len(bpy.data.textures)
        if n>0:
            for m in bpy.data.textures:bpy.data.textures.remove(m)
    else:
        bpy.data.textures.remove(bpy.data.textures[Name])
        
def txClear(Name=''):textureClear(Name)



#---------------Material Exist-------------------------------------------
def materialExist(Name='cc'):
    try:mt=bpy.data.materials[Name];return True
    except:return False
    
def mtExist(Name='cc'):return materialExist(Name)
        
#---------------Material Clear--------------------------------------------
def materialClear(Name=''):
    if Name=='':
        n=len(bpy.data.materials)
        if n>0:
            for m in bpy.data.materials:bpy.data.materials.remove(m)
    else:
        bpy.data.materials.remove(bpy.data.materials[Name])
        
def mtClear(Name=''):materialClear(Name)

def mtSlotClear():
    bpy.ops.object.material_slot_remove()



#----------------Material Assign Object-----------------------------------
def materialAssignObject(mtName=''):
    obj=bpy.context.object
    if mtName=='':
        bpy.ops.object.material_slot_add()
        n=len(obj.material_slots)-1;nn=len(bpy.data.materials)-1
        obj.material_slots[n].material=bpy.data.materials[nn]
    else:
        try:ms=obj.material_slots[mtName]
        except:
            bpy.ops.object.material_slot_add()
            n=len(obj.material_slots)-1 
            obj.material_slots[n].material=bpy.data.materials[mtName]

def mtAsgnObj(mtName=''):materialAssignObject(mtName)
def mtAO(mtName=''):mtAsgnObj(mtName)
def mtAo(mtName=''):mtAsgnObj(mtName)

#----------------Material New---------------------------------------------

def materialNew():
    bpy.ops.material.new();m=last('mt')
    return m

def mtNew():return materialNew()

def material(Name='',*args,**kwargs):
    if Name=='':m=materialNew();mtAsgnObj();return m 
    if Name=='cc':cc(*args,**kwargs);return bpy.data.materials['cc']
    if Name=='img':exec(sq("mtSlotClear();m=mtNew();mtAsgnObj();nodes('img',last('mt'),*args,**kwargs)"));m=last('mt');return m
    
def mt(Name='',*args,**kwargs):return material(Name,*args,**kwargs)

def img(FilePath):mt('img',FilePath)

#-----------------material diffuse color----------------------
def materialDiffuseColor(rgb=(0,0,0)):   #--2.8: rgb + alpha
    #--------Version Different-----------------
    if vs()<2.8: rgb=rgb[:3]
    else:
        if len(rgb)<4: rgb=list(rgb);rgb.append(1)
    #----------------------------------------------    
    bpy.context.object.active_material.diffuse_color = rgb

def mtDfColor(rgb):materialDiffuseColor(rgb)
def dfColor(rgb):materialDiffuseColor(rgb)
def dfc(rgb):materialDiffuseColor(rgb)
def mtColor(rgb):materialDiffuseColor(rgb)


#------------------------------------------
def isExistNode(Name,mt):
    for n in mt.node_tree.nodes:
        if n.name==Name:return True
    return False

def iNodeBSDF(mt):
    #------------version different-----------------------
    if vs()<2.8:N='ShaderNodeMaterial'
    else:N='ShaderNodeBsdfPrincipled'
    #----------------------------------------------------
    i=-1;
    for n in mt.node_tree.nodes:
        i=i+1       
        if n.rna_type.identifier==N:return i
    return i 

def iNodeOut(mt):
    #------------version different-----------------------
    if vs()<2.8:N='ShaderNodeOutput'
    else:N='ShaderNodeOutPutMaterial'
    #----------------------------------------------------
    i=-1;
    for n in mt.node_tree.nodes:
        i=i+1
        if n.rna_type.identifier==N:return i
    return i 

def iNodeType(NodeType,mt):
    i=-1;
    for n in mt.node_tree.nodes:
        i=+i
        if n.rna_type.identifier==NodeType:return i
    return i 

#-----------------Color Card (cc) Material & Texture  ---------------
def colorCardTexture():
    if txExist('cc')==False:
        bpy.ops.texture.new();n=len(bpy.data.textures)-1;bpy.data.textures[n].name='cc'
        if imgExist('cc.png')==False:imgOpen()
        bpy.data.textures['cc'].image= bpy.data.images["cc.png"]
        #imgPack('cc.png')
        

def ccTx():colorCardTexture()

def ccMake():
    if mtExist('cc')==False:
        bpy.ops.material.new();n=len(bpy.data.materials)-1; mt=bpy.data.materials[n];mt.name="cc";ccTx()    
        #-----------Version Different-----------------------------------------------------------------------
        if vs()<2.8:mt.texture_slots.add();mt.texture_slots[0].texture=bpy.data.textures['cc'];mt.use_textures[0] = True
        else:
            mt.node_tree.nodes.new(type="ShaderNodeTexImage");n=mt.node_tree.nodes;i=len(n)-1;n[i].image=bpy.data.images['cc.png']
            I=n[iNodeBSDF(mt)].inputs[0];O=n[i].outputs[0]; mt.node_tree.links.new(I,O);n[i].location.x=-300
        #---------------------------------------------------------------------------------------------------

   
def materialColorCard(x='',y=''): 
    if mtExist('cc')==False:ccMake()
    mtAsgnObj('cc')
    if isNum(x) and isNum(y):u(x,y)
    
def cc(x='',y=50):materialColorCard(x,y)



#================World=================================================
def hasWorld(Name=''):
    if Name=='':
        if len(bpy.data.worlds)<1: bpy.ops.world.new();return bpy.context.scene.world;
    else: return bpy.data.worlds[Name]


#=================Nodes================================================
    
#--------------Node Dictionary-----------------------------------------
nodeDict0={'out':'ShaderNodeOutputMaterial','img':'ShaderNodeTexImage','bs':'ShaderNodeBsdfPrincipled','mix':'ShaderNodeMixShader','geo':'ShaderNodeNewGeometry','mt':'ShaderNodeMaterial'
          }


#--------------For 'Node' Function using pre-functions----------------------
def nodeType(myDefTypeName,nodeDict=nodeDict0):  #node name convert  ( use nodes[i].rna_type() from it's error can know what's type name )
    try:
        n=nodeDict[myDefTypeName.lower()]
    except:
        n=myDefTypeName
    #------------version different-----------------------
    if vs()<2.8:
        if n=='ShaderNodeOutPutMaterial':n='ShaderNodeOutput'
    #----------------------------------------------------
    return n
    
def nType(Type,nodeDict=nodeDict0):return nodeType(Type,nodeDict)

def nodeArgTrim(a):
    a=a.replace('[','');a=a.replace(']','');a=a.replace('][',';');a=a.replace('] [',';');a=a.replace('->','~;');
    return a
    
def nodeClear(mt=''):
    if mt=='':mt=last('mt')
    if len(mt.node_tree.nodes)>0:
        for n in mt.node_tree.nodes:mt.node_tree.nodes.remove(n)

def nodeAdd(Type,mt=''):
    if mt=='':mt=last('mt')
    nt=mt.node_tree;n=nt.nodes.new(type=nType(Type));
    return n

def node(Type,mt=''):return nodeAdd(Type,mt='')
def nd(Type,mt=''):return node(Type,mt='')

def nodeLink(OutputsNode,Oi,InputsNode,Ii,mt=''):  # Note: reverse original bpy links.new(), but same with self link in node editor (Left (output) at first,right(input) at second)
    if mt=='':mt=last('mt')
    mt.node_tree.links.new(InputsNode.inputs[Ii],OutputsNode.outputs[Oi]);

def nodelink(OutputsNode,Oi,InputsNode,Ii,mt=''):nodeLink(OutputsNode,Oi,InputsNode,Ii,mt)


#---------------nodes save as script--------------------------------------------
def nodesSaveAsScript():
    pass


#----------------nodes save as plug----------------------------------------------
def nodesSaveAsPlug():
    pass

#---------------- Get Node Type-------------------------------------------------
def getNodeType():
    mt=last('mt'); N=mt.node_tree.nodes
    for n in N:
        if n.select:
            print('"'+n.rna_type.identifier+'"')

def getnodetype():getNodeType()

#---------------nodes----(NodeTypeName= myself defined useful nodes)----------------------------
def nodes(NodeTypeName='',mt='',*args,**kwargs):
    if NodeTypeName.lower()=='img':nodesImagePaste(mt,*args,**kwargs)


#---------------nodeImagePaste(if  two image at both sides use list)--------------------------------
def nodesImagePaste(mt,*args,**kwargs): 
    #-------------img file path---------------------------
    File=args[0]; img1='';img2=''
    if tp(File)=='[':
        img1=File[0]
        if len(File)>=2:img2=File[1]
    else:img1=File
    #------------Base nodes--------------------------
    mt.use_nodes=True;n0=mt.node_tree.nodes[0];n1=mt.node_tree.nodes[1]
    if n0.type[:3]!='OUT':n0=mt.node_tree.nodes[1];n1=mt.node_tree.nodes[0]
    #------------first img nodes---------------------
    Path,File=os.path.split(img1);imgOpen(Path,File)
    n2=nodeAdd('img',mt);n2.image=bpy.data.images[File]
    l=n2.location;l.x=-n2.width*1.2;l.y=n2.height*2.1
    nodeLink(n2,0,n1,0,mt)
    #------------second img as backside--------------
    if img2!='':
        Path,File=os.path.split(img2);imgOpen(Path,File)
        n3=nodeAdd('bs',mt);l3=n3.location;l1=n1.location;l3.x=l1.x;l3.y=l1.y-600
        n4=nodeAdd('img',mt);n4.image=bpy.data.images[File];l4=n4.location;l2=n2.location;l4.x=l2.x;l4.y=l3.y-100
        nodeLink(n4,0,n3,0,mt);
        n5=nodeAdd('mix',mt);l5=n5.location;l5.x=l3.x+700;l5.y=l3.y+300
        n6=nodeAdd('geo',mt);l6=n6.location;l6.x=l5.x-200;l6.y=l5.y+200
        nodeLink(n1,0,n5,1,mt); nodeLink(n3,0,n5,2,mt); nodeLink(n6,6,n5,0,mt);nodeLink(n5,0,n0,0,mt)
        l0=n0.location;l0.x=l5.x+200;l0.y=l5.y

        
#--------------------HDR new  hdr(0): default hdr without img only light, hdr(3): 3 sphere to 4 sphere Enviroment light    
def hdrNew(Path='',File=''):
    pass


#---------------------HDR---(can be PathFile one Argument)--------------------------------------
def hdr(Path='',File=''):
    if isTp(Path,'1') or isTp(File,'1'): hdrNew(Path,File)
    else:
        if File=='' and Path!='': Path,File = os.path.split(Path)
        else:
            if Path=='':Path=pathHDR
            if File=='':File=fileHDR

        imgOpen(Path,File)
        #----------Version Different---------------------------------------
        if vs()>=2.8:
            if len(bpy.data.worlds)<=0:bpy.ops.world.new();
            w=bpy.data.worlds[0];bpy.context.scene.world=w;w.use_nodes=True;
            cnt=len(w.node_tree.nodes)
            if cnt>0:
                for i in range(cnt):
                    if w.node_tree.nodes[i].type=='TEX_ENVIRONMENT':w.node_tree.nodes.remove(w.node_tree.nodes[i])
            w.node_tree.nodes.new(type="ShaderNodeTexEnvironment");
            n=w.node_tree.nodes;i=len(n)-1;[i];n[i].image=bpy.data.images[File]
            I=n[0].inputs[0];O=n[2].outputs[0]; w.node_tree.links.new(I,O);
        #------------------------------------------------------------------    

#==================Render========================================
def render():
    bpy.ops.render.render(use_viewport=True)
    #-------------Version Different-----------
    if vs()<2.8:
        try:a=areaFind('IMAGE_EDITOR');a.spaces[0].image=bpy.data.images['Render Result']
        except:pass
    #-----------------------------------------

#------------renderSameView--(keep Render same View visible perporties)--------------------
def renderSameView():   #plant to do , need to complete, 'kkk
    sc=bpy.context.scene;
    
    
        
    
#==================Camera=====================================
def lockCameraToView():  #---not function yet
    u=ui('VIEW_3D')
    bpy.context.space_data.lock_camera = True
    ui(u)

def camera(l=(-7,-3,3),r=(1.3,0,-1.18)):  # n=name,l=location, r=rotation  (-5.8490,-11.9373,1.2016),(1.426,-0.0,-0.473) front         
    if modeIndex()!=0:m0()
    #----------Version Different------------------------
    if vs()<2.8:
        bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=l, rotation=r)  #roatation  need /57.3
        #bpy.context.scene.camera = bpy.context.object
    else:bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=l, rotation=r)
    #--------------------------------------------------
    bpy.context.scene.camera = bpy.context.object
    

    #lockCameraToView()

def ca(l=(-5.8490,-11.9373,1.2016),r=(1.426,-0.0,-0.473)):
    try:
        if mode('name')!='OBJECT':m0()
        sun();light();camera(l,r);
        if vs()<2.8:render()
    except:pass


#-------------------ca0---(ctr + alt +0)-------------------------------------
      
def cameraSameView(): # add the camera same View default camera  (not use, location and rotation not same)
    a=contextArea()
    l=v2t(a.spaces[0].region_3d.view_location)
    r=r2t(a.spaces[0].region_3d.view_rotation)
    #msg(a.spaces[0].region_3d.view_zoom)
    camera(l,r);


def ca0(): #ctr+alt+0  and add sun light
    try:
        if mode('name')!='OBJECT':m0()
        sun();light();cameraSameView();
        if vs()<2.8:render()
    except:pass
    

#=================Light=======================================
def light(l=(-5.16631, -4.22163, 3.151),e=1,t='HEMI',r=1): #e=Energy, t=Type,r=radius
    #------------Version Different------------------------------------
    if vs()<2.8:bpy.ops.object.lamp_add(type=t.upper(), radius=r, view_align=False, location=l)
    else:
        if t.upper()=='HEMI': t='SUN'
        bpy.ops.object.light_add(type=t.upper(), radius=r, location=l)
    #------------------------------------------------------------------
    if e!=1:bpy.context.object.data.energy = e

         
def sun(l=(-5.16631, -4.22163, 3.151),e=1,r=1,Sky=True):
    light(l,e,'SUN',r)
    if vs()<2.8 and Sky:bpy.context.object.data.sky.use_sky = True


#===================Animation (keyframe/ Driver)=====================================
def frameEnd(Set=100):
    bpy.context.scene.frame_end=Set

def fEnd(Set=100):frameEnd(Set)
def fE(Set=100):frameEnd(Set)
#---------------------------------------------------
def frameStart(Set=1):
    bpy.context.scene.frame_start=Set

def fStart(Set=1):frameStart(Set)
def fS(Set=1):frameStart(Set)
#---------------------------------------------------
def frameCurrent(Set=1):
    bpy.context.scene.frame_current=Set

def fCur(Set=1):frameCurrent(Set)
def fC(Set=1):frameCurrent(Set)
#---------------------------------------------------
def kfTypeDict(Type=''):
    d=['Location', 'Rotation', 'Scaling', 'BUILTIN_KSI_LocRot', 'LocRotScale', 'BUILTIN_KSI_LocScale', 'BUILTIN_KSI_RotScale', 'BUILTIN_KSI_DeltaLocation', 'BUILTIN_KSI_DeltaRotation', 'BUILTIN_KSI_DeltaScal']

def kfType(Type):
    t=Type
    if Type.lower()=='l':t='Location'
    if Type.lower()=='r':t='Rotation'
    if Type.lower()=='s':t='Scaling'
    return t

def keyframeInsert(Type=''):
    bpy.ops.anim.keyframe_insert_menu(type=kfType(Type))

def ki(i='',Type=''):
    exec(sq("if tp(i)=='1':fC(i);`else:`~if Type=='':Type=i;`keyframeInsert(Type)"));
   

#-------------Driver---------------------------------
def driverAdd(Path):  #not use now  (show driver data in bpy.context.object.animation.drivers.driver)
    obj=bpy.context.object;a=obj.animation_data;a.driver_add(Path);i=len(a.drivers)-1;
    return a.drivers[i]


def driver(Obj,Path,Exp): #Obj=modifer
    Obj.driver_add(Path);d=last('driver');d.expression=Exp
    return d

def drv(Obj,Path,Exp):return driver(Obj,Path,Exp)

#==================ClearAll======================================

#---------------world Clear------------------------------------------
def worldClear(Name=''):
    if Name=='':
        n=len(bpy.data.worlds)
        if n>0:
            for w in bpy.data.worlds:bpy.data.worlds.remove(w)
    else:
        bpy.data.worlds.remove(bpy.data.worlds[Name])
        
def wldClear(Name=''):worldClear(Name)

#---------------obj Clear--------------------------------------------
def objectClear(Name=''):
    if Name=='':
        n=len(bpy.data.objects)
        if n>0:
            for obj in bpy.data.objects:bpy.data.objects.remove(obj)
    else:
        bpy.data.objects.remove(bpy.data.objects[Name])
        
def objClear(Name=''):objectClear(Name)

#-----------initial--clear all objects-----------------------
def clearAll():
   
    try:
        if vs()<2.8:c0()
        #if bpy.context.object.mode!='OBJECT':mode('OBJECT')
        #bpy.ops.object.select_all(action='SELECT');
        #bpy.ops.object.delete(use_global=False)
        objClear();mtClear();txClear();imgClear();wldClear();cIni();
    except:pass

def clearALL():clearAll()
def clearall():clearAll()

def clean():clearAll()
def cl():clearAll()



#===========================My Self Export=========================
#--------------my self export verts/edges/faces index and co to excel ()-------
def lsVEF():  #return list
    obj=bpy.context.object
    md=mode('name');
    if md!='EDIT': m1()
    
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me);
    V=bm.verts;E=bm.edges;F=bm.faces
    ls=[];lsV=[];lsVV=[];lsE=[];lsEE=[];lsF=[];lsFF=[];
    #-------Vert-------------
    lsV=[['v','x','y','z']]
    for v in V:lsVV=[v.index,round(v.co.x,4),round(v.co.y,4),round(v.co.z,4)];lsV.append(lsVV)
    #-------Edge-------------
    lsE=[['e','v0','v0x','v0y','v0z','v1','v1x','v1y','v1z']]
    for e in E:lsEE=[e.index,e.verts[0].index,round(e.verts[0].co.x,4),round(e.verts[0].co.y,4),round(e.verts[0].co.z,4),e.verts[1].index,round(e.verts[1].co.x,4),round(e.verts[1].co.y,4),round(e.verts[1].co.z,4)];lsE.append(lsEE)
    #-------Face-------------
    lsF=[['f','v0','v0x','v0y','v0z','v1','v1x','v1y','v1z','v2','v2x','v2y','v2z','v3','v3x','v3y','v3z']]
    for f in F:
        lsFF=[f.index];FV=f.verts;lsF3=[]
        for i in range(4):
            lsF3.extend([FV[i].index,round(FV[i].co.x,4),round(FV[i].co.y,4),round(FV[i].co.z,4)])   
        lsFF.extend(lsF3);lsF.append(lsFF)
 
    ls=[lsV,lsE,lsF]
    if md!='EDIT':mode(md)
    return ls
#-------------#VEF list save to txt file--------------------------
def txtVEF(FilePath='c:/VEF.txt'):
    ls=lsVEF();f=open(FilePath,'w');f.write(str(ls)); f.close()
    
def VEF(FilePath='c:/VEF.txt'):txtVEF(FilePath)
def vef(FilePath='c:/VEF.txt'):txtVEF(FilePath)


#===============my run script SQL============================
def eachV(SQL=''):
    #md=mode();
    #if md!='EDIT':m1()
    obj=bpy.context.object
    bm=bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:
        exec(sq(SQL))

    bmesh.update_edit_mesh(obj.data, True)
    #if md!='EDIT':mode(md)

def eachv(SQL=''):eachV(SQL)



def eachSelectV(SQL=''):
    #md=mode();
    #if md!='EDIT':m1()
    obj=bpy.context.object
    bm=bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:
        if v.select: exec(sq(SQL))

    bmesh.update_edit_mesh(obj.data, True)
    #if md!='EDIT':mode(md)

def eachSV(SQL=''):eachSelectV(SQL)
def eachsv(SQL=''):eachSelectV(SQL)

#-------sameX/ sameY/ sameZ---selected Verts same with the last Vert (can easy append to lsV)---------
def sameLocation(Axis='XYZ',ls=[]):
    if ls==[]:ls=lsV();
    if len(ls)<2:return
    obj=bpy.context.object;bm=bmesh.from_edit_mesh(obj.data)
    A=Axis.upper();X=If(A.find('X')>=0,True,False);Y=If(A.find('Y')>=0,True,False);Z=If(A.find('Z')>=0,True,False);

    for V in bm.verts[ls[-1]:ls[-1]+1]:pass

    for i in ls[:-1]:
        for v in bm.verts[i:i+1]:
            if X: v.co.x=V.co.x  
            if Y: v.co.y=V.co.y
            if Z: v.co.z=V.co.z
    bmesh.update_edit_mesh(obj.data, True)
    
def same(Axis='X',ls=[]):sameLocation(Axis,ls)

def sameX(ls=[]):same('X',ls)
def sameY(ls=[]):same('Y',ls)
def sameZ(ls=[]):same('Z',ls)
def sameXY(ls=[]):same('XY',ls)
def sameXZ(ls=[]):same('XZ',ls)
def sameYZ(ls=[]):same('YZ',ls)
def sameXYZ(ls=[]):same('XYZ',ls)

#------------maxX/Y/Z---minX/Y/Z----(in selected verts,if no select is all)----return Value or Index of axis local location -----------------

def maxLocation(Axis='X',Compare='>',Return='value'):   # use exec return value skill:  exec(stringCodes,globalDictionary,localDictionary)
    A=Axis.lower();ls=lsV()
    if ls==[]: a();ls=lsV()
    obj=bpy.context.object;bm=bmesh.from_edit_mesh(obj.data);
    L=locals();exec(sq('`V=0;I=ls[0];`for i in ls:`~for v in bm.verts[i:i+1]:`~~W=v.co.'+A+'`~~if W'+Compare+'V:V=W;I=v.index'),{},L)
    V=L['V'];I=L['I']
    if Return=='value':return V  #value of local location
    else:return I  #index of vert

def maxX():return maxLocation('X')
def maxY():return maxLocation('Y')
def maxZ():return maxLocation('Z')

def minX():return maxLocation('X','<')
def minY():return maxLocation('Y','<')
def minZ():return maxLocation('Z','<')

def maxXi():return maxLocation('X','>','index')
def maxYi():return maxLocation('Y','>','index')
def maxZi():return maxLocation('Z','>','index')

def minXi():return maxLocation('X','<','index')
def minYi():return maxLocation('Y','<','index')
def minZi():return maxLocation('Z','<','index')



#==============Maya Surport==========================================S=========
def mayaDropBlendScript_filePath():
    return 'c:/mybpy_mayaDropBlend'

def mayaDropBlendScript_pyScript(b="obj"):
    s="import bpy;bpy.ops.wm.read_factory_settings(use_empty=True);\
scene = bpy.context.scene;\
bpy.ops.wm.open_mainfile(filepath=[']<'>+$theFile+<'>[']);\
bpy.ops.export_scene."+b+"(filepath=[']"+mayaDropBlendScript_filePath()+"."+b+"[']);";

    s=s.replace("[']",'\\"');s=s.replace("<'>",'"')
    return s;

def mayaDropBlendScript_finishScript(b='obj'):
    s="try:"
    s=s+"os.remove([']"+mayaDropBlendScript_filePath()+".py[']);";
    s=s+"os.remove([']"+mayaDropBlendScript_filePath()+"."+b+"[']);";
    s=s+"os.remove([']"+mayaDropBlendScript_filePath()+".mtl[']);";
    s=s+"\\"+"nexcept:pass"
    
    s=s.replace("[']",'\\"')
    return s;


def mayaDropBlendScript_py(b='obj'):
    s="""
//-----------------------------------------------
global proc int
performFileDropAction_Blender_Py(string $theFile)
{
    int $i=0;
    string $ss=[pyScript];
    string $s="s='"+$ss+"';f=open([FilePath],'w');f.write(s); f.close()";
    python($s);    
    $i=1;return($i);

}

//------------------------------------------------
global proc int
performFileDropAction_Blender_Finish(string $theFile)
{
    int $i=0;
    string $s=[FinishScript];
    python($s);    
    $i=1;return($i);

}

"""
    s=s.replace('[FilePath]','[\]"'+mayaDropBlendScript_filePath()+'.py[\]"');s=s.replace('[\]','\\')
    s=s.replace('[pyScript]','"'+mayaDropBlendScript_pyScript(b)+'"')
    s=s.replace('[FinishScript]','"'+mayaDropBlendScript_finishScript(b)+'"')
    return s;



def mayaDropBlendScript_object():  # part script of Bl object to maya
    pathPy=mayaDropBlendScript_filePath()
    s="""
  //---------Blender export object file--------------
    string $s="import os;os.system(r'[\]""+$pathBlender+"/blender[\]" --background --factory-startup --python [pathPy] --');";
    python($s);
"""
    s=s.replace("[\]","\\");s=s.replace('[pathPy]',pathPy+'.py')
    return s



#----------------------------------------------------------------------------
def mayaDropBlendScript(b='obj'):  #---proc main script  -- b:  filetype when export : default is obj, also can be 'fbx'
    s1="""

//---Proc: Blender File Drop----------------------
global proc int
performFileDropAction_Blender(string $theFile)
{
  int $r=0;
  string $pathBlender=[pathBlender];
  string $F=toupper(substring($theFile,size($theFile)-5,size($theFile)));
  string $bufs[];tokenize $theFile "/" $bufs;string $fileName = $bufs[size($bufs)-1];
  if ($F==".BLEND"||$F=="BLEND1")
  {$r=2;
   performFileDropAction_Blender_Py($theFile);
"""
    
    s2="""
  //----------Import the file blender exported-----------
    performFileImportAction([fileBlenderExported]);
    performFileDropAction_Blender_Finish($theFile);
  }
  return($r);
}
"""
    
    p=pathBlender();p=p.replace("\\","/");p=p.replace("//","/");p=p.replace("'",'"');
    s1=s1.replace('[pathBlender]',p);
    
    si=''; #string insert between s1 and s2
    si+=mayaDropBlendScript_object()

    s2=s2.replace('[fileBlenderExported]','"'+mayaDropBlendScript_filePath()+'.'+b+'"')
    s3=mayaDropBlendScript_py(b)
    s=s1+si+s2+s3
    return s

#---------------------------------------------------------------------------
def mayaDropBlend_plugIn(a,b):  # Write performFileDropAction_plugIn part
        if a=='blender':return 'if($r==0){$r=performFileDropAction_Blender($theFile);};//if run $r=2'
        else:return ''
            
def mayaDropBlend_proc(a,b):   # Write performFileDropAction_Blend part
    if a=='blender':return mayaDropBlendScript(b)
    else: return ''
        
#---------------------------------------------------------------------------
def mayaDropImgClear():  #----clear the function of self def maya Drop img--- 
      FilePath=r'C:\Users\Administrator\Documents\maya\scripts\performFileDropAction.mel'
      os.remove(FilePath)
      
def mayaDropImg(a=1,b=''):  #---1 is add function ----0 is clear function
    if a==0:mayaDropImgClear()
    else:
        myDocPath=r'C:\Users\Administrator\Documents'
        if 'maya' in os.listdir(myDocPath):
            if 'scripts' in os.listdir(myDocPath+'\\maya'):
                FilePath=myDocPath+'\\maya\\scripts\\performFileDropAction.mel'
                s1="""
global proc int
performFileDropAction (string $theFile)
{
int $r=performFileDropAction_plugIn($theFile);// <--Self Definate Plug In 
if($r==0){$r=performFileImportAction( $theFile );}; //<--Original
return($r);
}

//---plugIn--------------------
global proc int //When return=0 continue,r<>0 not continue
performFileDropAction_plugIn(string $theFile)
{
int $r=0;
"""
                s2="""
if($r==0){$r=performFileDropAction_addImgShader($theFile);};//if run $r=1
return($r);
}


//---Proc: Drop Image file paste Texture immediately ----------------------
global proc int
performFileDropAction_addImgShader(string $theFile)
{
int $r=0;
string $F=toupper(substring($theFile,size($theFile)-3,size($theFile)));
string $bufs[];tokenize $theFile "/" $bufs;string $fileName = $bufs[size($bufs)-1];

if ($F==".PNG"||$F==".JPG"||$F==".HDR")
{
if($F==".HDR") //drop HDR File if no any obj is selected Add Enirement Sphere
{ string $s[]=`ls -sl`;if ($s[0]==""){polySphere;scale -r 100 100 100;polyNormal -normalMode 0 -userNormalMode 0 -ch 1;}}

python("import maya.cmds as mc");
python("sel=mc.ls(sl=1)");
python("file_tex='"+$theFile+"'");
python("mc.sets(name='imgGrp', renderable=True, empty=True)");
python("shaderNode = mc.shadingNode('phong', name='"+$fileName+"', asShader=True)");
python("fileNode = mc.shadingNode('file', name='file', asTexture=True)");
python("mc.setAttr(fileNode+'.fileTextureName', file_tex , type='string')");
python("shadingGroup=mc.sets(name='texGrp',renderable=True,empty=True)");
python("mc.connectAttr(shaderNode+'.outColor',shadingGroup+'.surfaceShader',force=True)");
python("mc.connectAttr(fileNode+'.outColor',shaderNode+'.color',force=True)");
python("mc.surfaceShaderList(shaderNode,add='imgGrp')");
python("mc.sets(sel,e=True,forceElement='imgGrp')");
python("mc.select(sel)");
python("mc.hyperShade(assign=shaderNode)");
select -cl;
$r=1;}

return($r);
}

"""
            s=s1+mayaDropBlend_plugIn(a,b)+s2+mayaDropBlend_proc(a,b)

            f=open(FilePath,'w');f.write(s); f.close()


#--------------------Drop Blender File Action---------------------------------------------------------
def mayaDropBlendClear():#-----Clear Drop Blender File Function in Maya only keep drop image Texture
    mayaDropImg()

def mayaDropBlend(b='obj'):
    if b==0:mayaDropBlendClear()
    else:mayaDropImg('blender',b)


def mayaDropBlender(b='obj'):mayaDropBlend(b)
def mayadropblender(b='obj'):mayaDropBlend(b)
def mayadropblend(b='obj'):mayaDropBlend(b)
def mayabl(b='obj'):mayaDropBlend(b)




#=============Chinese Defination==============================================
#=============常用特色中文命令定义(也可看出对应英文快捷命令,可直接控制台输入对应英文命令,中文则需要写外面文本编辑器粘进Blender)===========================


#----下面是粘在自己脚本前面加载mybpy的两行标准代码(其中第一行代码中的mybpy路径可修改为自己工程使用的单独保存的mybpy文件夹路径)------
#----也可粘入Blender的py控制台,使py控制台支持mybpy命令, 特别是执行录码命令 rec() ---------------------------------------------

'''
import sys;sys.path.append(r'd:\mybpy')
import importlib as imp;import m;imp.reload(m);from m import *


'''
#-----------录代码命令------------

def 录码(): rec()          #若带参数: rec(小数点保留位数).在控制台入输入rec()命令后, 支持录码的命令会在文本编辑器当前鼠标位置出现代码 (请特别注意鼠标选择位置,避免混乱及不小心的替换,出问题,马上按Ctr+Z撤销)
                           #连续录码:鼠标在Py控制台时,按键盘上箭头(调出上一步命令),再按Enter执行 (还可以自设更便捷的快捷键:将控制台shift+鼠标点左键按下Press设为console.history_cycle,shift+鼠标左击释放设为执行console.execute) 
                                                
def 录码执行(): rec();run();   #录码后马上执行脚本, run()相当于按 alt+P 马上执行脚本

def 录码折行执行(): rec();run();n()  #录码后会加折行符\n,n()命令相当于在文本编辑器里按回车折行, 然后马上执行

def 录码带物体名(): reco()    # =rec(2,'o') 传参的写法，选择模式下录的代码会带sO(物体名称）,其中sO是selectObject函数简写

#-----------贴图------------------

def 贴图(图片文件路径): img(图片文件路径)   #若正反两面贴图, 可用List格式引用路径,如: img([r'路径1',r'路径2']) , 注意若是电脑直接粘的单斜杠路径,一定引用时引号前面加r''

def 环境贴图(图片文件路径=''):hdr(图片文件路径) # 可忽略路径, 控制台直接敲hdr(), 默认是r'D:\mybpy\tx\default.hdr' (可自行替换)

def 色卡(x='',y=50):cc(x,y)  #即色卡cc.png贴图让uv集中成其中一点的颜色, x,y是uv集中成色卡图片的xy坐标位置(百分比数)


#--------------------------------

def 摄像及灯光():ca()   #需要场景中有物体,如无物体则报错

#----------建模相关特色命令----------------

def 方块(细分数=0):cube(细分数) #cu()
def 平面(尺寸=2):plane(尺寸)    #pl()
def 球体(尺寸=1):sphere(尺寸)   #sp()

def 镜像方块(细分数=1):mirrorCube(细分数)  #mCube()


def 移动(x=[],y=[],z=[]):g(x,y,z)
def 沿x移动(n):gx(n)
def 沿y移动(n):gy(n)
def 沿z移动(n):gz(n)

def 缩放(v):s(v)
def 沿x缩放(v):sx(v)
def 沿y缩放(y):sy(v)
def 沿z缩放(v):sz(v)

def 旋转(角度=90,轴='Y'):r(角度,轴)
def 沿x旋转(角度=90):rx(角度)
def 沿y旋转(角度=90):ry(角度)
def 沿z旋转(角度=90):rz(角度)


def 平滑():smooth()   #sm()
def 细分(细分数=1):subdive(细分数)   #编辑模式下的细分,必须先进入编辑模式,否则报错
def 细分器(细分数=3,类型='',是否应用=False):subSurf(细分数,类型,是否应用) #修改器中的细分器

def 环切(切线数=1,滑动量=0):return ctrR(切线数,滑动量)    # 要在编辑模式下运行,需先选一条要切的边作为要切的对象和以横切这条边为方向, 函数返回每条环切线第1条线段的两个点, 可后面跟alt() 环选命令选择每条环边

#----------模式----------------------------
def 物体模式():m0()
def 点编辑模式():m1()
def 线编辑模式():m2()
def 面编辑模式():m3()


#----------Maya功能优化-----------------
            
def 使maya支持拖拽贴图():mayaDropImg()

def 清除maya拖拽贴图功能():mayaDropImg(0)


def 使maya支持拖拽blender文件(传递文件格式='obj'):mayaDropBlend(传递文件格式)   #参数为通过什么中间格式文件来传递,不写默认为obj格式, 也可用fbx格式

def 清除maya拖拽blender文件功能():mayaDropBlend(0)





#*************如有问题欢迎进交流 QQ群: mybpy (519692851) *************************************

#*************百度Blender贴吧搜mybpy有详细说明, 主贴地址: https://tieba.baidu.com/p/7393914011

#*************最新版百度下载地址:https://pan.baidu.com/s/1FtOLcsuh-rwxpmSrrVmc_w  提取码:mbpy

#*************含历史版本下载地址:https://pan.baidu.com/s/1lWWFsxZ4_7tTxTuYmi2z2A  提取码:mbpy

#************* Github Download address: https://github.com/cn2000bd/mybpy  ******************* 



#========以下区域可自定义(可自己用def语句类似上面的设定或另外自设py文件引用mybpy)=============































