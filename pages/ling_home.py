from PIL import Image
import streamlit as st
import pandas as pd

page = st.sidebar.radio('我的首页', ['兴趣推荐', '音乐室', '图片处理工具','小说网站大全', '留言区'])

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

# 我的首页
def page1():
    pass

# 兴趣推荐
def page2():
    st.write(':blossom:*Best wishes to you !!*:blossom:')
    st.write(':white_flower: 欢迎来到不糟糕工作室 :white_flower:')
    st.write(':hourglass:希望你能在这里度过美好的时刻:hourglass:')

# 音乐室
def page3():
        st.write('播放一首音乐吧')

    st.write(':wind_blowing_face:')
    st.write('*黄昏之时*')
    with open("黄昏之时.mp3", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format("audio/mp3"), start_time = 0)

    st.write(':four_leaf_clover:')
    st.write('*Call Of Silence*')
    with open("Call Of Silence.mp3", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format("audio/mp3"), start_time = 0)

    st.write(':ear_of_rice:')
    st.write('*Insomnia*')
    with open("Insomnia.mp3", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format("audio/mp3"), start_time = 0)
    
    st.write(':maple_leaf:')
    st.write('*城南花已开*')
    with open("城南花已开.mp3", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format("audio/mp3"), start_time = 0)
    
    st.write(':tulip:')
    st.write('*everything i wanted*')
    with open("everything i wanted.mp3", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format("audio/mp3"), start_time = 0)
    
    st.write(':cherry_blossom:')
    st.write('*bad guy*')
    with open("bad guy.mp3", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format("audio/mp3"), start_time = 0)

# 图片处理工具
def page3():
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传照片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

# 小说网站大全
def page5():
    st.write('Royal Road')
    st.write('*http://royalroad.com*')
    st.write('Web Fiction Guide')
    st.write('*http://webfictionguide.com*')
    st.write('Wattpad')
    st.write('*http://wattpad.com*')
    st.write('Gravity Tales')
    st.write('*http://gravitytales.com*')
    st.write('Wuxia World')
    st.write('*http://wuxiaworld.com*')
    st.write('Web Novel')
    st.write('*http://webnovel.com*')
    st.write('Flying-lines')
    st.write('*http://Flying-lines.com*')
    st.write('novelupdates')
    st.write('*https://www.novelupdates.com*')
    st.write('lnmtl')
    st.write('*https://lnmtl.com*')
    st.write('babelnovel')
    st.write('*https://babelnovel.com*')
    st.write('Obooko')
    st.write('*https://www.obooko.com*')

# 留言区
def page6():
    pass
    
if page == '我的首页':
    page1()

elif page == '兴趣推荐':
    page2()

elif page == '音乐室':
    page3()

elif page == '图片处理工具':
    page4()

elif page == '小说网站大全':
    page5()


elif page == '留言区':
    page6()
