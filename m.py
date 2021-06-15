#--------mybpy (ver:1.01)-----2021.6.13 edit----by:caonan (mail: caonan2000@163.com)

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
import os,sys,inspect,ctypes


#from s import msg

#================My self definate string quick language===============
def sq(SQL):
    s=SQL.replace('`','\n')
    s=s.replace('~','\t')
    return s

def exe(SQL):
    exec(sq(SQL))

def run(SQL):
    exec(sq(SQL))

#================PATH=======================================
    
#------------path of mybpy\m.py-------------------------------

def pathM(arg=''):
    dirname,filename=os.path.split(os.path.abspath(__file__))
    if arg.upper()=='FILE':d=filename
    else:d=dirname+'\\';d=repr(d);
    return d
        
def pathBlender(arg=''):
    dirname,filename = os.path.split(os.path.abspath(sys.argv[0])) 
    if arg.upper()=='FILE':d=filename
    else:d=dirname+'\\';d=repr(d);
    return d

def pathBl(a=''):pathBlender(a)
   

def fileMe():
    f=inspect.stack()[1][1];fp=bpy.data.texts[f[1:]].filepath;
    return fp
    
def pathMe(arg=''):
    f=inspect.stack()[1][1];fp=bpy.data.texts[f[1:]].filepath;
    dirname,filename = os.path.split(fp) 
    if arg.upper()=='FILE':d=filename
    else:d=dirname+'\\';d=repr(d);d=d[1:len(d)-1]
    return d


disk="D:"
pathCC=disk+"\\mybpy\\tx\\"
pathHDR=pathCC;fileHDR="default.hdr"

#===========Varible===============================
#------------------------------------------------
def Vector(ls):
    return mathutils.Vector(ls)

#------------------------------------------------
def radians(angle):
    return math.radians(angle)

def rd(angle):return radians(angle)
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


#---------last (return last object)---------------------------
def last(Type='OBJECT'):
  
    if Type.upper()=='OBJECT': i=len(bpy.data.objects)-1;return bpy.data.objects[i]
    if Type.upper()=='MESH':obj=bpy.context.object;i=len(obj.data)-1;return bpy.data.objects.data[i]
    if Type.upper()=='DRIVER':obj=bpy.context.object;d=obj.animation_data.drivers;i=len(d)-1;return d[i].driver
    if Type.upper() in ('MATERIAL','MT'):m=bpy.data.materials; i=len(m)-1;return m[i]
    if Type.upper()=='VI':obj=bpy.context.object;mx=len(obj.data.vertices);LastVertIndex=mx;return mx;
    
#============Mode=================================
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
    except:return None
        

def modeI():return modeIndex()

#--------get collectionIndex() use for m() move to coll, Note:index is +1 than collections list index --- 
def collectionIndex(Name=''):
    i=0; #--0 is default master scene
    for ii,c in enumerate(bpy.data.collections) :
        if c.name.upper()==Name.upper():
            i=ii+1
    return i

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
    if bpy.context.object.mode!='OBJECT':mode('OBJECT')

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

def m(i=''):    #<--when i=int is mode select ; i=str is collection move shotkey,default m(''),move to master scene 
    if str(type(i))=="<class 'int'>":
        if i==0: m0() #OBJECT MODE
        if i==1: m1() #EDIT-VERT
        if i==2: m2() #EDIT-EDGE
        if i==3: m3() #EDIT-FACE
        
    if str(type(i))=="<class 'str'>":  #--Move to Collection (or Add New Coll)--
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
def o(s=1,f=1):pMode(s,f)


#================Vert Convert==================================
#----------Vector 2 tuple-------------------------------------------------
def vector2tuple(v):
    return (v.x,v.y,v.z)
    
    
def v2t(v):return vector2tuple(v)

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
def n(Name='OBJ'): return name(Name)
def f2(Name='OBJ'):return name(Name)

#----------------return list of object select vert or edge or face (in edit mode) ---------------
def listSelect(v='V'):
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
def lsV(): return listSelect('V')
def lsE(): return listSelect('E')
def lsF(): return listSelect('F')
#-------------vertInRange---------------------------------------
def vertInRang(x=[],y=[],z=[]):
    obj=bpy.context.edit_object;me=obj.data
    bm=bmesh.from_edit_mesh(me)
    
def vRng(x=[],y=[],z=[]):vertInRange(x,y,z)
#-----------select all----------------------------------------
def selectAll():
    try:
        if mode('name')=='EDIT':bpy.ops.mesh.select_all(action='SELECT')
        else:bpy.ops.object.select_all(action='SELECT');
    except:pass
    
def a():selectAll()

#----------deselect all---------------------------------------
def deselectAll():
    bpy.ops.object.select_all(action='DESELECT');

def alt_a():deselectAll()
def altA():alt_a()
def aa(): alt_a()


#----------selectVertInSimpleTerm----------------------
def selectVertInSimpleTerm(s=''):   # 'x>0 & x<10 & y>=0 & y<10 & z>0 & z<1'  &=and |=or  ,=and
    obj=bpy.context.object
    bm=bmesh.from_edit_mesh(obj.data)
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
    
    bmesh.update_edit_mesh(obj.data, True)


#-----------selectEditMesh---------------------

def selectEditMesh(Mode='V',ls=[]):

    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    #bm.faces.active = None
    
    md=Mode.upper()
    if isType(ls,'s'):selectVertInSimpleTerm(ls);return
    
    if ls!=[]:
        if md=='V': bmV=bm.verts
        if md=='E': bmV=bm.edges
        if md=='F': bmV=bm.faces
        
        cnt=len(bmV)
        for v in bmV:v.select=False
        
        for i in ls:
            if i<cnt:
                for v in bmV[i:i+1]:v.select=True
                
        bmesh.update_edit_mesh(obj.data, True)
    else:
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
#-----------select vert------------------------
def selectVert(ls=[]):m1();selectEditMesh('V',ls)
def selV(ls=[]):selectVert(ls)
def sV(ls=[]):selV(ls)
#-----------select edge------------------------
def selectEdge(ls=[]):m2();selectEditMesh('E',ls)
def selE(ls=[]):selectEdge(ls)
def sE(ls=[]):selectEdge(ls)
def sE_(ls=[]):selE(v2e(ls))  #<--note: use verts list  as Argument

#-----------select face------------------------
def selectFace(ls=[]):m3();selectEditMesh('F',ls)
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
        bpy.context.collection.objects[ObjName].select_set(True)
        bpy.context.view_layer.objects.active=bpy.data.objects[ObjName]
    #-------------------------------------------------------

def selectObj(ls=''):
    if isTp(ls,'s'):selectObject(ls)
    if isTp(ls,'[','('):
        for n in ls: selectObject(n)

def sO(listOrstrName=''):selectObj(listOrstrName)
def so(n):selectObj(n)
    
#----------select_linked_pick----------------------------------
def selectLink(v=''):
    if v=='':v=lsV();v=v[0]
    #---------------Version Different------------------------
    if vs()<2.9:
        bpy.ops.mesh.select_linked_pick(deselect=False, delimit={'SEAM'}, index=v)
    else:
        bpy.ops.mesh.select_linked_pick(deselect=False, delimit={'SEAM'}, object_index=0, index=v)
        
def l(v=''):selectLink(v)

#----------loop_mul_select (only surpot edge)-------------------------------------
def selectLoop(Ring=False):
    bpy.ops.mesh.loop_multi_select(Ring)  #return edge, ring=False is horizontal
    
        
def alt_clk(r=False):selectLoop(r)
def alt(r):alt_clk(r)
def shft_alt_clk(r=False):selectLoop(r)

#---------loopCircle---------------------------------------------------------------
def loopCircle(ls=[]): #----not useful (not finish yet)
    obj=bpy.context.edit_object
    bm=bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:pass
    
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
def cO():c0()


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



#---------mesh rebuild after vertices re-ordered by x,z,y (in order to keep same in different bl versions)-------------------
def meshVertSort(Round=4):  
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

def remesh(Round=4): meshVertSort(Round)
def re(Round=4):remesh(Round)


#-----------------only new verts reindex------------
def meshVertSortNew(Round=4):
    msg(LastVertIndex)
    



#--------------------xxxxxx---- (aybe not useful, Later can delete this codes)---xxxxxxx---------------------------------
def meshReBuild_old_notUseful():#--------not use now (to write  ) Later can delete this codes
    md0=mode("EDIT");obj=bpy.context.object;bm=bmesh.from_edit_mesh(obj.data); #@Name=obj.name
    vi=[];v=[];e=[];f=[];v0=[];e0=[];f0=[];
    for V in bm.verts: v0.append([V.index,V.co.x,V.co.y,V.co.z])
    #for E in bm.edges: e0.append([E.verts[0].index,E.verts[1].index])
    #for F in bm.faces: f0.append([F.verts[0].index,F.verts[1].index,F.verts[2].index,F.verts[3].index])
    #--------sort----------
    v0.sort(key = operator.itemgetter(1,2,3))
    for VV in v0:vi.append(VV[0]);#v.append(VV[1:])
    #for EE in e0:e.append(lsI(vi,EE))
    #for FF in f0:f.append(lsI(vi,FF))

    #--------update-------
    i=0;
    for V in bm.verts:V.index=vi[i];i+=1
    bm.verts.sort()
    #i=0;
   # for E in bm.edges:E.verts[0].index=e[i][0];E.verts[1].index=e[i][1];i+=1
    #i=0;
   # for F in bm.faces:F.verts[0].index=f[i][0];F.verts[1].index=f[i][1];F.verts[2].index=f[i][2];F.verts[3].index=f[i][3];i+=1
    #bmesh.update_edit_mesh(obj.data, True)
    if md0!='EDIT':mode(md0)
    
def meshUpdate_not_useful(bm): #---- Later can delete this codes-----(aim to meshReBuild can self update no need to make new), but not useful, not finish yet.
    #--------update-------
    i=0;
    for V in bm.verts:V.co.x=v[i][0];V.co.y=v[i][1];V.co.z=v[i][2];i+=1
    i=0;
    for E in bm.edges:E.verts[0].index=e[i][0];E.verts[1].index=e[i][1];i+=1
    i=0;
    for F in bm.faces:F.verts[0].index=f[i][0];F.verts[1].index=f[i][1];F.verts[2].index=f[i][2];F.verts[3].index=f[i][3];i+=1
    bmesh.update_edit_mesh(obj.data, True)
#----------------xxxxxxxxxxxxxxx--end--xxxxxxxxxxxxxxxxxxxxxx--------------------------------------------------------------------------


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

#----------vert slide (shft_v)----------------------------------------
def vertSlide(v=0.5):
    u=ui()
    bpy.ops.transform.vert_slide(value=v, mirror=True, correct_uv=True)
    ui(u)
    
def shft_v():vertSlide(v=0.5)
def V():vertSlide(v=0.5)

#-----------rotate----------------------------------------------------
def rotate(Angle=90,Axis='X'):
    v=math.radians(Angle)

    #----------Version Different------------------------
    if vs()<2.8:
        if Axis.upper()=='X':A=(1,0,0);Con_Axis=(True,False,False)
        if Axis.upper()=='Y':A=(0,1,0);Con_Axis=(False,True,False)
        if Axis.upper()=='Z':A=(0,0,1);Con_Axis=(False,False,True)
        bpy.ops.transform.rotate(value=v, axis=A, constraint_axis=Con_Axis, constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    else:
        if vs()==2.92:v=-v
        bpy.ops.transform.rotate(value=v, orient_axis=Axis.upper(), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    #---------------------------------------------------

def r(j=90,z='Y'):rotate(j,z)    
def ry(j=90):rotate(j,'Y')
def rz(j=90):rotate(j,'Z')
def rx(j=90):rotate(j,'X')


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
        

def s(v): resize(v,v,v)
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


#-----------face add (fill)-------------------------------------------------
def faceAdd():
    bpy.ops.mesh.edge_face_add()

def fill():faceAdd()
def f():faceAdd()

#-----------duplicate------------------------------------------------
def duplicate(Link=False):
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":Link, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0,0,0)})

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

#--------------loopcut-----------------------------------------------
def loopCut(Axis='X',Slide=0):
    obj=bpy.context.object; Co=obj.location
    if mode('name')=='EDIT':a()
    else:m3()
    bisect(Axis,Co)
    if Slide!=0:
        ax=Axis
        if str(type(ax))=="<class 'str'>":ax=Axis.upper()
        if ax=='X' or ax==0:gx(Slide)
        if ax=='Y' or ax==1:gy(Slide)
        if ax=='Z' or ax==2:gz(Slide)


def ctrl_r(a='X',s=0):loopCut(a,s)
def ctrR(a='X',s=0):ctrl_r(a,s)

#-------------------FaceCut-----------------------------------------
def faceCut():
    exec('subdive()')
#-------------------EdgeClear---------------------------------------
def edgeClear():
    bpy.ops.mesh.dissolve_edges(use_verts=False)

#--------------knife cut--------------------------------------------
def knifeCut():
    bpy.ops.mesh.knife_tool(use_occlude_geometry=True, only_selected=False)

def k():knifeCut()

#---------------rip move-(not function yet, if run flash exit app)-------------------------------------------
def ripMove():
    u=ui('VIEW_3D')
    if mode('name')!='EDIT':m1()
    #----------------Version Different------------------------------
    if vs()<2.8:bpy.ops.mesh.rip_move(MESH_OT_rip={"mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "release_confirm":False, "use_accurate":False, "use_fill":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
    else:bpy.ops.mesh.rip_move(MESH_OT_rip={"mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "release_confirm":False, "use_accurate":False, "use_fill":False}, TRANSFORM_OT_translate={"value":(-0.713697, -0.606782, 0.818662), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
    #---------------------------------------------------------------
    ui(u)
    
#def v():ripMove()

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

def ctr1(v=1):ctrl_1(v)
def ctr2(v=2):ctrl_2(v)
def ctr3(v=3):ctrl_3(v)
def ctr4(v=4):ctrl_4(v)
def ctr5(v=5):ctrl_5(v)

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

#=================Outliner===============================================

#------------New Collection-------------------------------------------
def newCollection(Name='Collection'):
    m(Name)


#-----------------shft_s---------------------------------------------------
def shft_s(i=1):
    if i==1:cs0()
    if i==2:bpy.ops.view3d.snap_cursor_to_selected()
    if i==3:bpy.ops.view3d.snap_cursor_to_active()
    if i==4:bpy.ops.view3d.snap_cursor_to_grid()
    
    if i==6:bpy.ops.view3d.snap_selected_to_grid()
    if i==7:bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
    if i==8:bSpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    if i==9:bpy.ops.view3d.snap_selected_to_active()

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
    
def cube(v=0):
    cubeCreate();
    if v>0:subSurf(v);smooth()

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
    bpy.ops.mesh.primitive_monkey_add(size=Size, enter_editmode=False, location=(0, 0, 0))

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
        halfCube(zh);remesh()
        mirror(Axis,True)

    if isTp(Axis,'1'):
        cube(Axis);ap();clearX('-',-0.01);
        remesh()
        mirror('X',True)

        
def mirCube(a='X'): mirrorCube(a)
def mCube(a='X'):mirrorCube(a)
def mCu(a='X'):mirrorCube(a)

#---------------backWall---------------------------------------
def wall(Type='wallOnly',Name='wall'):
    plane();rx(90);gy(10);s(30);sx(5);n(Name)
    if Type.upper()=='withGround':gz(30);m2();sN();selE([1]);ey(-50);selE([1]);ctrB(0.2,10);sm();



#===================Bone Armature==============================
def parentSet(Type='ARMATURE_AUTO'):
    bpy.ops.object.parent_set(type=Type)

def ctrl_p(Type='ARMATURE_AUTO'):parentSet(Type)
def ctrP(Type='ARMATURE_AUTO'):parentSet(Type)

#===================Plug Function================================
#----------getClipBoard (need import ctypes)---------------------
def getClipBoard():
    CF_TEXT = 1;
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    user32.OpenClipboard(0)
    if user32.IsClipboardFormatAvailable(CF_TEXT):
        data = user32.GetClipboardData(CF_TEXT)
        data_locked = kernel32.GlobalLock(data)
        text = ctypes.c_char_p(data_locked)
        print(text.value)
        kernel32.GlobalUnlock(data_locked)
    else:
        print('no text in clipboard')
    user32.CloseClipboard()


#-----------------File Drop Operator----------------------------------------
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
    if mode('name')!='EDIT':mO=True;m3();
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
        for l in f.loops:
            luv = l[uv_layer]
            #if luv.select:
                #luv.uv = l.vert.co.xy # apply the location of the vertex as a UV
            if f.select:
                luv.uv=(x/div,y/div) # apply the location as x,y
                
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

    else:bpy.ops.object.load_reference_image(filepath=FilePath);rx(90)

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
        if Path=='' and File=='': bpy.ops.image.open(filepath=pathCC+"cc.png", directory=pathCC, files=[{"name":"cc.png", "name":"cc.png"}], relative_path=True, show_multiview=False)
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



#-----------------Color Card (cc) Material & Texture  ---------------
def colorCardTexture():
    if txExist('cc')==False:
        bpy.ops.texture.new();n=len(bpy.data.textures)-1;bpy.data.textures[n].name='cc'
        if imgExist('cc.png')==False:imgOpen()
        bpy.data.textures['cc'].image= bpy.data.images["cc.png"]
        #imgPack('cc.png')
        

def ccTx():colorCardTexture()

def ccMake():
    bpy.ops.material.new();n=len(bpy.data.materials)-1; mt=bpy.data.materials[n];mt.name="cc";ccTx()
    
    #-----------Version Different-----------------------------------------------------------------------
    if vs()<2.8:mt.texture_slots.add();mt.texture_slots[0].texture=bpy.data.textures['cc'];mt.use_textures[0] = True
    #---------------------------------------------------------------------------------------------------


def materialColorCard(x='',y=''): 
    if mtExist('cc')==False:ccMake()
    mtAsgnObj('cc')
    #-----------Version Different-----------------------------------------------------------------------
    if vs()>=2.8: #use_nodes
        obj=bpy.context.object;i=len(obj.material_slots)-1;mt=obj.material_slots[i].material;mt=bpy.data.materials['cc']
        mt.use_nodes=True;mt.node_tree.nodes.new(type="ShaderNodeTexImage");n=mt.node_tree.nodes;i=len(n)-1;[i];n[i].image=bpy.data.images['cc.png']
        I=n[0].inputs[0];O=n[2].outputs[0]; mt.node_tree.links.new(I,O);
    #----------------------------------------------------------------------------------------------------
    if isNum(x) and isNum(y):u(x,y)
    
def cc(x='',y=50):materialColorCard(x,y)






#================World=================================================
def hasWorld(Name=''):
    if Name=='':
        if len(bpy.data.worlds)<1: bpy.ops.world.new();return bpy.context.scene.world;
    else: return bpy.data.worlds[Name]


#=================Nodes================================================
    
#--------------Node Dictionary-----------------------------------------
nodeDict0={'out':'ShaderNodeOutputMaterial','img':'ShaderialTexImage','bs':'ShaderNodeBsdfPrincipled','mix':'ShaderNodeMixShader','geo':'ShaderNodeNewGeometry','mt':'ShaderNodeMaterial'
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
    

#---------------------HDR---(can be PathFile one Argument)--------------------------------------
def hdr(Path='',File=''):
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
    camera(l,r);sun();light();
    if vs()<2.8:render()


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
        objClear();mtClear();txClear();imgClear();wldClear()
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



#=============常用特色中文命令定义(也可看出对应英文快捷命s令,可直接控制台输入对应英文命令,中文则需要写外面文本编辑器粘进Blender)===========================

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

#----------模式----------------------------
def 物体模式():m0()
def 点编辑模式():m1()
def 线编辑模式():m2()
def 面编辑模式():m3()

#=============以下区域可自定义(可自己用def语句类似上面的设定 )====================================================































