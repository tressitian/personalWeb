# pip install streamlit
import streamlit as st
import os

# 设置页面标题和布局
st.set_page_config(page_title="Tressi's Portfolio", layout="wide")

# 设置深色底，并用SVG生成蓝色几何线条作为背景装饰
st.markdown(
    """
    <style>
    .stApp {
        background: #6947CC;
        color: #fff !important;
    }
    .stApp * {
        color: #fff !important;
        text-shadow: 0 1px 6px rgba(0,0,0,0.5);
    }
    /* 增大导航栏tab文字尺寸 */
    .stTabs [data-baseweb="tab"] button {
        font-size: 1.25rem !important;
        font-weight: 600;
        padding: 0.75rem 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 顶部右上角语言切换
col1, col2 = st.columns([8, 1])
with col1:
    st.title("Tressi's Portfolio Website")
with col2:
    lang_icon = "🌐"  # 地球图标
    if 'lang' not in st.session_state:
        st.session_state['lang'] = 'English'
    if st.button(lang_icon + (" English" if st.session_state['lang'] == '中文' else " 中文")):
        st.session_state['lang'] = '中文' if st.session_state['lang'] == 'English' else 'English'
    lang = st.session_state['lang']

# 页面导航标签
if lang == "中文":
    nav_options = ["主页", "简历", "技能", "项目", "联系方式"]
else:
    nav_options = ["Home", "Resume", "Skills", "Projects", "Contact"]

# 顶部导航栏（标签页）
tabs = st.tabs(nav_options)

# 主页/Home
tab_idx = 0
if (lang == "中文"):
    home_idx, resume_idx, skills_idx, projects_idx, contact_idx = 0, 1, 2, 3, 4
else:
    home_idx, resume_idx, skills_idx, projects_idx, contact_idx = 0, 1, 2, 3, 4

with tabs[home_idx]:
    # 直接用本地图片替换头像，如assets/Slide1.jpg
    profile_path = "assets/Slide1.jpg"
    if os.path.exists(profile_path):
        st.image(profile_path, caption="Product Manager", use_column_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1519125323398-675f0ddb6308", caption="Product Manager", use_column_width=True)
    # 居中容器，宽度为50%，文字左对齐
    with st.container():
        if lang == "中文":
            st.markdown(
                """
                <div style='width:90%; margin:0 auto; text-align:left;'>
                <p>欢迎来到我的作品集网站！我是Tressi，一名热爱创新的产品设计师。请通过上方导航栏浏览我的简历、技能、项目和联系方式。</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style='width:90%; margin:0 auto; text-align:left;'>
                <p>I focus on building meaningful digital experiences at the intersection of AI, design, and user behavior. With hands-on experience as an AI Product Manager at Bytedance, I've worked on global-facing products like Hypic and Dreamina, where I drove AI feature optimization, user growth strategy, and market positioning for the U.S. audience.</p>
                <p>My background in visual communication and human-computer interaction allows me to approach product challenges with both creative intuition and technical insight. I've led cross-functional collaboration across product, design, and engineering teams, contributed to commercialization roadmaps, and shipped features that directly impacted user engagement.</p>
                <p>Beyond industry, I've also organized AI-driven design workshops and led international cultural-tech exhibitions, bridging storytelling and emerging tech in public spaces.</p>
                <p>Currently based between Beijing and Seattle, I'm looking for new opportunities where I can keep shaping products that are human-centered, globally relevant, and powered by smart systems.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

with tabs[resume_idx]:
    st.header("个人简历" if lang == "中文" else "Resume")
    if lang == "中文":
        st.subheader("教育背景")
        st.write("- 清华大学 – 华盛顿大学双硕士，GIX智慧互联（AIoT与HCI），2023.09 - 至今")
        st.write("- 芝加哥艺术学院，视觉传达设计BFA，2016.08 - 2020.05")
        st.subheader("工作经历")
        with st.expander("AI产品经理实习生，字节跳动（2023年12月-2024年3月）"):
            st.write("**图像编辑工具 - Hypic（海外版）**")
            st.write("聚焦美国市场 | AI功能商业化")
            st.write("- 参与AI图像工具的商业化策略，负责市场需求分析、用户增长策略及商业模式设计。")
            st.write("- 主导高清图像增强等AI功能开发，利用A/B测试优化工具入口，提升产品多场景适配能力。")
            st.write("\n**AIGC工具 - Dreamina（网页版）**")
            st.write("聚焦AI产品优化与用户增长")
            st.write("- 优化灵感库入口，降低用户使用门槛，提升模板使用率。制定用户增长系统的产品策略与需求文档。")
        with st.expander("空间与媒体实验室研究员，清华大学未来实验室（2021年9月-2022年11月）"):
            st.write("**展览：'未来城市：双城记'（北京-哥本哈根）**")
            st.write("项目负责人 | 获北京市副市长表扬，并获北京城市规划设计院及丹麦大使馆认可")
            st.write("- 负责与北京城市规划设计院、北京规划展览馆及丹麦大使馆的中英文双语沟通。")
            st.write("- 协调策展团队，确保设计输出进度，主导视觉物料制作，提出算法驱动创意流程，显著提升团队效率。")
            st.write("- 管理施工团队沟通，监督现场执行，解决突发问题。")
            st.write("- 组织并主持AI/AIGC主题工作坊及学术会议。")
        with st.expander("品牌设计师、UI/UX设计师，西安欧亚学院（2021年4月-2021年8月）"):
            st.write("- 负责毕业纪念册、招生手册、主视觉等平面设计项目，统筹印刷品交付及周边物料执行。")
            st.write("- 参与网站及小程序的UI/UX设计与迭代。")
        with st.expander("IFC讲师&助教，中央美术学院（2020年10月-2021年4月）"):
            st.write("- 协助中英文授课，提供翻译与教学支持。")
            st.write("- 一对一作品集辅导，85%学生获得知名院校奖学金。")
            st.write("- 负责约60人班级的Adobe软件课程教学。")
        with st.expander("平面设计实习生，Keyconcept（2020年2月-2020年7月）"):
            st.write("- 参与网页、海报、视觉系统及Logo设计，独立完成4个项目并获得留用offer。")
        st.subheader("论文发表")
        with st.expander("对话与艺术的协同：多模态AI聊天机器人在情感支持中的潜力探索（CSCW Companion '24）"):
            st.write("设计了ArtTheraCat多模态心理健康聊天机器人，将支持性对话与艺术图像生成结合。用户研究显示，互动后情绪显著改善，图像在情绪释放和自我洞察中发挥重要作用。")
            st.markdown("[查看论文](https://dl.acm.org/doi/10.1145/3678884.3681843)")
        with st.expander("Dreamory：AI驱动的睡前故事系统用于情绪重构与记忆巩固（CHI 2025）"):
            st.write("提出Dreamory，基于AI的睡前故事系统，通过LLM生成个性化故事，促进积极情绪重构。试点研究显示其有助于情绪调节和睡眠质量提升。")
            st.markdown("[查看论文](https://dl.acm.org/doi/10.1145/3706599.3719850)")
    else:
        st.subheader("Education")
        st.write("- Dual Master's (AIoT & HCI), Tsinghua University & University of Washington, 2023.09 - Present")
        st.write("- BFA in Visual Communication Design, School of the Art Institute of Chicago, 2016.08 - 2020.05")
        st.subheader("Experience")
        with st.expander("AI Product Manager Intern, ByteDance (Dec 2023 - Mar 2024)"):
            st.write("**Image Editing Tool - Hypic (Overseas Version)**")
            st.write("Focus: U.S. Market | AI Features Commercialization")
            st.write("- Contributed to the commercialization strategy for AI-powered image tools, focusing on the U.S. market. Responsible for market demand analysis, user growth strategy, and business model design.")
            st.write("- Led AI feature development such as high-definition image enhancement. Used A/B testing to optimize tool placements and leveraged HD model diffusion capabilities.")
            st.write("\n**AIGC Tool - Dreamina (Web Version)**")
            st.write("Focus: AI Product Optimization & User Growth")
            st.write("- Refined the entry point of the inspiration library to encourage template use and reduce user friction. Developed product strategies and requirement docs for user growth system.")
        with st.expander("Space & Media Lab Researcher, The Future Lab, Tsinghua University (Sep 2021 - Nov 2022)"):
            st.write("**Exhibition: 'A Tale of Two Cities' (Beijing & Copenhagen)**")
            st.write("Project Lead | Commended by Vice Mayor of Beijing and Recognized by Beijing Institute of Urban Planning & Danish Embassy")
            st.write("- Led bilingual communication with Beijing Institute of Urban Planning, Beijing Planning Exhibition Hall, and Danish Embassy.")
            st.write("- Coordinated planning team for timely design output. Directed visual production and proposed algorithm-driven creative process to improve efficiency.")
            st.write("- Managed construction communication, supervised on-site execution, and resolved unexpected issues.")
            st.write("- Organized and hosted AI/AIGC themed workshops and academic conferences.")
        with st.expander("Brand Designer, UI/UX Designer, Xi'an Eurasia University (Apr 2021 - Aug 2021)"):
            st.write("- Led graphic design projects: graduation yearbooks, brochures, admissions booklets, main visuals for exhibitions, and promotional materials.")
            st.write("- Coordinated with printing companies for product delivery. Involved in UI/UX design for website and mini-program development.")
        with st.expander("IFC Lecturer & Assistant Instructor, Central Academy of Fine Arts (Oct 2020 - Apr 2021)"):
            st.write("- Assisted English-speaking instructors in online/offline classes, providing translation and teaching support.")
            st.write("- Provided one-on-one portfolio guidance; 85% of students received scholarships from prestigious institutions.")
            st.write("- Taught Adobe Creative Suite to ~60 students.")
        with st.expander("Graphic Design Intern, Keyconcept (Feb 2020 - Jul 2020)"):
            st.write("- Worked on web, poster, visual system, and logo design. Sold four independent projects and received a return offer.")
        st.subheader("Publications")
        with st.expander("The Synergy of Dialogue and Art: Exploring the Potential of Multimodal AI Chatbots in Emotional Support (CSCW Companion '24)"):
            st.write("Designed ArtTheraCat, a multimodal chatbot for mental health, integrating supportive dialogue with artistic image generation. User study showed significant emotional improvement and highlighted the value of images in emotional release and self-insight.")
            st.markdown("[Show publication](https://dl.acm.org/doi/10.1145/3678884.3681843)")
        with st.expander("Dreamory: AI-Powered Bedtime Storytelling for Emotional Reframing Before In-Sleep Memory Consolidation (CHI 2025)"):
            st.write("Presents Dreamory, an AI storytelling system for emotional memory consolidation during sleep. Uses LLM to generate personalized bedtime stories for positive reframing. Pilot study showed improved emotional regulation and sleep quality.")
            st.markdown("[Show publication](https://dl.acm.org/doi/10.1145/3706599.3719850)")

with tabs[skills_idx]:
    st.header("我的技能" if lang == "中文" else "My Skills")
    if lang == "中文":
        st.subheader("设计工具")
        st.write("- Adobe全家桶, Figma, Blender, Fusion 360, KiCad, Midjourney")
        st.subheader("编程与技术")
        st.write("- Python, Arduino, Matlab, SQL, Signal Processing")
        st.subheader("语言能力")
        st.write("- 英语（TOEFL 104）, 日语（N2）, 法语")
    else:
        st.subheader("Design Tools")
        st.write("- Adobe Suite, Figma, Blender, Fusion 360, KiCad, Midjourney")
        st.subheader("Programming & Tech")
        st.write("- Python, Arduino, Matlab, SQL, Signal Processing")
        st.subheader("Languages")
        st.write("- English (TOEFL 104), Japanese (N2), French")

with tabs[projects_idx]:
    st.header("参与项目" if lang == "中文" else "Projects")
    projects = [
        {
            "name_zh": "Dreamory – AI睡前故事系统",
            "name_en": "Dreamory – AI-Powered Bedtime Storytelling",
            "desc_zh": "结合LLM与情绪调节理论，生成个性化的睡前故事，促进情绪重构与记忆巩固。已发表于CHI EA 2025。",
            "desc_en": "Combines LLM and emotional reframing theory to generate personalized bedtime stories for memory consolidation. Published at CHI EA 2025.",
            "link": "https://doi.org/10.1145/3706599.3719850"
        },
        {
            "name_zh": "Co-Performer – 可穿戴驱动的电吉他效果器系统",
            "name_en": "Co-Performer – Wearable-Driven Interactive Guitar FX System",
            "desc_zh": "将观众生理数据（如心率/动作）通过可穿戴设备实时输入电吉他效果器，让听众变成'共演者'。",
            "desc_en": "Uses audience biophysical signals (e.g., heart rate, motion) via wearables to modulate guitar effects in real-time, turning listeners into co-performers.",
            "link": ""
        },
        {
            "name_zh": "智慧蜡烛 – 多层结构与色彩控制交互装置",
            "name_en": "Digital Candle – Ambient Light with Multilayer Structure & Color Control",
            "desc_zh": "一款模拟蜡烛火焰晃动效果的智能灯具，支持滚轮调节亮度与色温，并具有物理反馈体验。",
            "desc_en": "A smart light simulating candle flame movement, with scroll-based brightness and hue control, designed for tactile interaction.",
            "link": ""
        },
        {
            "name_zh": "未来城市：双城记展览设计",
            "name_en": "Future Cities: Beijing-Copenhagen Twin Cities Exhibition",
            "desc_zh": "清华大学未来实验室主要项目负责人，展览获得北京市副市长表扬，涵盖城市规划与算法生成创作。",
            "desc_en": "Led the visual and spatial design for an international urban planning exhibition, praised by Beijing's vice mayor and covered by city planning and algorithmic creativity.",
            "link": ""
        },
        {
            "name_zh": "Hypic – 海外图像编辑工具AI功能策略",
            "name_en": "Hypic – Global Photo Editor AI Strategy",
            "desc_zh": "在字节跳动AI产品实习中，负责AI画质增强策略、商业化入口设计与用户增长。",
            "desc_en": "Worked on AI-based image enhancement strategy, monetization design, and user growth during TikTok (Bytedance) internship.",
            "link": ""
        }
    ]
    for p in projects:
        name = p["name_zh"] if lang == "中文" else p["name_en"]
        desc = p["desc_zh"] if lang == "中文" else p["desc_en"]
        link_text = "项目链接" if lang == "中文" else "Project Link"
        with st.expander(name):
            st.write(desc)
            if p["link"]:
                st.markdown(f"[{link_text}]({p['link']})")

with tabs[contact_idx]:
    st.header("联系我" if lang == "中文" else "Contact Me")
    if lang == "中文":
        st.write("欢迎通过以下方式联系我：")
        st.write("- 邮箱：tiantressi@gmail.com")
        st.write("- 微信：tressitian")
        st.write("- LinkedIn：[Tressi's LinkedIn](https://www.linkedin.com/in/runyan-tian-52889032b/)")
        st.write("- Behance：[Tressi's Behance](https://www.behance.net/tiantressi)")
        st.write("\n你也可以在下方留言：")
        name = st.text_input("你的名字")
        message = st.text_area("留言内容")
        if st.button("提交"):
            if name and message:
                st.success(f"感谢你的留言，{name}！我会尽快回复你。")
            else:
                st.warning("请填写完整信息后再提交。")
    else:
        st.write("Feel free to contact me via:")
        st.write("- Email: tiantressi@gmail.com")
        st.write("- WeChat: tressitian")
        st.write("- LinkedIn: [Tressi's LinkedIn](https://www.linkedin.com/in/runyan-tian-52889032b/)")
        st.write("- Behance: [Tressi's Behance](https://www.behance.net/tiantressi)")
        st.write("\nYou can also leave a message below:")
        name = st.text_input("Your Name")
        message = st.text_area("Message")
        if st.button("Submit"):
            if name and message:
                st.success(f"Thank you for your message, {name}! I will get back to you soon.")
            else:
                st.warning("Please fill in all information before submitting.")
