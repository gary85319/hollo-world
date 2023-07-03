from flask import Flask, url_for, redirect,  render_template, request,send_file
import time

import csv
import os
way=os.getcwd() 
print('運行路徑:',way)

aapp=Flask(__name__)
@aapp.route('/',)
def index():

    
    
    
    return render_template(r'8.html',oo='y')

@aapp.route('/han')
def han():
    from ans import ans
    r=ans()
    return render_template('word.html',u=r)
@aapp.route('/order',methods=['post','get'])
def order():
    itmm=request.form.getlist('item')
    user_name=request.form.get('use')
    with open('itemlist.txt','a',encoding='utf-8',errors='ignore',newline='') as f:
        w=csv.writer(f)
        w.writerow(['商品',user_name])
        for tv in itmm:
            w.writerow([tv])

    return render_template('l.html',item=itmm,ll='謝謝惠顧?')
@aapp.route('/shop')
def shop():
    return render_template('shop.html')
@aapp.route('/favion.ico')
def favionico():
    favion_way=os.path.join(way,'web','src','templates','favicon.ico')
    return send_file(favion_way)
@aapp.route('/ans',methods=['post','get'])
def ans():
    from ans import ans
    t=ans
    
    return render_template('ans1.html',u=t)
@aapp.route('/the_word_of_cmp')
def the_word_of_cmp():
    return render_template('ans.html')
@aapp.route('/test')
def test():
    with open('test.txt','a',encoding='utf-8',errors='ignore',newline='') as f:
        f.write('成功!!!!!!!')
        return 'HI!!!!!!!'
    
way=os.getcwd()       

@aapp.route('/t')
def t():
    pasexe_way=os.path.join(way,'web','src','pas.exe')
    
    return send_file(pasexe_way)
@aapp.route('/paspy')
def paspy():
      paspy_way=os.path.join(way,'web','src','pas.py')
      return send_file(paspy_way)

@aapp.route('/testu')
def test_u():
    return render_template('school.html')
@aapp.route('/testu/img')
def testu_img():
    return send_file(r'C:\Users\Lucas\OneDrive\桌面\詹晉瑜\env\web\src\templates\download.jpg')
@aapp.route('/youtube_csv')
def youtube_csv(): 
    return send_file(r'C:\Users\Lucas\OneDrive\桌面\詹晉瑜\env\youtube.csv')
@aapp.route('/background')
def background():
    return send_file(r'C:\Users\Lucas\OneDrive\桌面\詹晉瑜\env\background.jpg')

    
@aapp.route('/ggyy',methods=['get','post'])
def ggyy():
    dat=request.form.get('t')
    with open('st.txt','a',encoding='utf-8',errors='ignore',newline='') as f:
        f.write(dat+'\n')
    with open('st.txt','r',encoding='utf-8',errors='ignore',newline='')as o:
        o.seek(0)
        s=o.readlines()
    return render_template('a.html',talk=s)

@aapp.route('/留言板',methods=['get','post'])
def 留言板():
   
    
    return render_template('e.html')
if __name__=='__main__':
    
    aapp.run('0.0.0.0','80',debug=True)
