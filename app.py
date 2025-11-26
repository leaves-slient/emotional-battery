import streamlit as st
import random

# --- 1. 页面基础配置 ---
st.set_page_config(
    page_title="情绪充电站",
    page_icon="🔋",
    layout="centered"
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 2. 核心逻辑区 (模拟 LLM) ---
# 既然你是大模型专家，之后可以在这里接入 DeepSeek/OpenAI API
# 目前我们先用一个简单的列表代替，保证项目能跑通
def get_ai_encouragement():
    prompt_list = [
        "别担心，你今天的努力，即使微不足道，也在为未来积蓄力量。",
        "允许自己暂停一下，哪怕是超级英雄也需要充电。",
        "那些杀不死你的bug，终将让你成为更厉害的架构师。",
        "你比你想象中更强大，喝口水，深呼吸。",
        "代码可以重构，人生也是，随时都可以重新开始。",
        "今天的焦虑就留给今天，明天的太阳会照亮新的路。",
        "你做的已经很好了，真的。",
    ]
    return random.choice(prompt_list)

# 获取一句随机的鼓励
quote = get_ai_encouragement()

# --- 3. 界面样式区 (CSS魔法) ---
# Streamlit 原生不支持"鼠标悬停显示气泡"，所以我们嵌入一点 CSS
# 这是一个非常实用的技巧，能让你的 Python 网页瞬间变高级
css_code = f"""
<style>
    /* 容器居中 */
    .container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        flex-direction: column;
    }}
    
    /* 小人样式 (Emoji) */
    .avatar {{
        font-size: 100px;
        cursor: pointer;
        transition: transform 0.3s;
        position: relative;
        z-index: 2;
    }}
    
    /* 鼠标移上去小人放大 */
    .avatar:hover {{
        transform: scale(1.2);
    }}
    
    /* 对话气泡样式 */
    .bubble {{
        position: absolute;
        /* 以前是 top: -80px (头顶) */
        /* 现在改成 top: 110px (脚下) -> 因为机器人高100px，稍微留点缝隙 */
        top: 130px; 
        
        background-color: #FFEFD5;
        color: #333;
        padding: 15px 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        font-size: 18px;
        font-weight: bold;
        width: 350px; /*稍微把宽度加宽一点，容纳更多字*/
        text-align: center;
        
        opacity: 0; 
        transition: opacity 0.5s, top 0.5s; /* 增加 top 的过渡动画 */
        pointer-events: none;
        z-index: 10; /* 保证气泡在最上层 */
    }}
    
    /* 核心交互：鼠标悬停时 */
    .container:hover .bubble {{
        opacity: 1;
        top: 120px; /* 悬停时稍微往上浮动一点点，有个动态感 */
    }}
    
    /* --- 修改部分 2：气泡的小尾巴 (三角形) --- */
    .bubble::after {{
        content: '';
        position: absolute;
        /* 以前是 bottom: -10px (下面) */
        /* 现在改成 top: -20px (放到气泡顶端) */
        top: -20px; 
        
        left: 50%;
        margin-left: -10px;
        border-width: 10px;
        border-style: solid;
        
        /* 以前是上色下透，现在改成：下色上透 (指向上方) */
        border-color: transparent transparent #FFEFD5 transparent;
    }}
</style>

<div class="container">
    <div class="bubble">{quote}</div>
    <div class="avatar">🤖</div> 
    <p style="color: grey; margin-top: 20px;">(试着把鼠标移到机器人头上)</p>
</div>
"""

# --- 4. 渲染网页 ---
st.title("🔋 程序员的情绪充电站")
st.caption("Made by an Indie Hacker with Python")

# 渲染包含 HTML/CSS 的组件
st.markdown(css_code, unsafe_allow_html=True)

# 增加一个刷新按钮，模拟"重新生成"
if st.button("换一句鼓励"):
    st.rerun()