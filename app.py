import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image

# 페이지 설정
st.set_page_config(
    page_title="홍길동의 연구 포트폴리오",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 메뉴 설정
st.sidebar.title("메뉴")
menu = st.sidebar.radio(
    "페이지 선택:",
    ["홈", "연구 실적", "관심 연구 분야", "프로젝트", "연락처"]
)

# CSS 스타일 적용
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #1E88E5;
    text-align: center;
    margin-bottom: 1rem;
}
.sub-header {
    font-size: 1.8rem;
    color: #0D47A1;
    margin-top: 2rem;
    margin-bottom: 1rem;
}
.text-content {
    font-size: 1.1rem;
    text-align: justify;
    margin-bottom: 1.5rem;
}
.highlight {
    background-color: #E3F2FD;
    padding: 1rem;
    border-radius: 5px;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# 함수: 전자기학 시뮬레이션 플롯 생성 (데모용)
def plot_em_field():
    # 2D 공간에서의 전자기장 시뮬레이션 데이터 생성
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # 간단한 전자기장 패턴 생성 (데모용)
    source_x, source_y = 0, 0
    R = np.sqrt((X - source_x)**2 + (Y - source_y)**2)
    Z = np.cos(R) / (R + 0.1)
    
    # 플롯 생성
    fig = px.imshow(
        Z,
        color_continuous_scale='RdBu',
        labels=dict(x="X 위치", y="Y 위치", color="필드 강도"),
        title="전자기장 시뮬레이션 (데모)"
    )
    
    return fig

# 홈 페이지
def home():
    # 헤더 및 소개
    st.markdown('<div class="main-header">Computational Electromagnetics 연구자 포트폴리오</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 실제 이미지 파일 경로로 교체 필요
        try:
            image = Image.open("profile_picture.jpg")
            st.image(image, width=250, caption="홍길동")
        except:
            st.info("프로필 사진을 추가하려면 'profile_picture.jpg' 파일을 프로젝트 폴더에 저장하세요.")
    
    with col2:
        st.markdown('<div class="text-content">', unsafe_allow_html=True)
        st.write("""
        안녕하세요! 저는 서울대학교 전기정보공학부에서 Computational Electromagnetics를 연구하고 있는 
        홍길동입니다. 제 연구는 고주파 전자기장 해석, 안테나 설계, 전자파 산란 문제 등에 집중하고 있습니다.
        
        현재 XYZ 연구실에서 박사과정으로 연구하고 있으며, 전자기 시뮬레이션 알고리즘 개발 및 
        최적화에 관심을 가지고 있습니다.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">전문 분야</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.subheader("📡 전자기 해석")
        st.write("FDTD, FEM, MoM 등의 수치해석 방법을 활용한 전자기장 시뮬레이션")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.subheader("💻 최적화 알고리즘")
        st.write("머신러닝과 딥러닝을 활용한 전자기 문제 해결 방법론 연구")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.subheader("🔍 안테나 설계")
        st.write("차세대 무선 통신을 위한 고효율/소형 안테나 설계 및 최적화")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 간단한 시뮬레이션 데모
    st.markdown('<div class="sub-header">전자기장 시뮬레이션 데모</div>', unsafe_allow_html=True)
    em_plot = plot_em_field()
    st.plotly_chart(em_plot, use_container_width=True)

# 연구 실적 페이지
def research_achievements():
    st.markdown('<div class="main-header">연구 실적</div>', unsafe_allow_html=True)
    
    # 학술 논문
    st.markdown('<div class="sub-header">학술 논문</div>', unsafe_allow_html=True)
    
    papers = pd.DataFrame({
        "제목": [
            "Novel FDTD Approach for Metamaterial Simulation",
            "Machine Learning Optimization for Antenna Design",
            "Efficient Electromagnetic Scattering Analysis in Complex Media"
        ],
        "저널/학회": [
            "IEEE Transactions on Antennas and Propagation",
            "Journal of Computational Physics",
            "International Conference on Electromagnetics (ICEM)"
        ],
        "연도": ["2024", "2023", "2022"],
        "링크": ["https://example.com/paper1", "https://example.com/paper2", "https://example.com/paper3"]
    })
    
    # 논문 목록 렌더링
    for i, paper in papers.iterrows():
        with st.expander(f"{paper['제목']} ({paper['연도']})"):
            st.write(f"**저널/학회:** {paper['저널/학회']}")
            st.write(f"**연도:** {paper['연도']}")
            st.write(f"**링크:** [{paper['제목']}]({paper['링크']})")
            
            # 논문 초록 (예시)
            st.markdown("""
            **초록:**  
            본 연구에서는 전자기학 분야의 새로운 수치해석 방법을 제안하였습니다. 
            제안된 방법은 기존 방법 대비 계산 효율성이 약 30% 향상되었으며, 
            복잡한 구조에서도 안정적인 해석이 가능함을 확인하였습니다.
            """)
    
    # 인용 지표
    st.markdown('<div class="sub-header">인용 지표</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 연도별 논문 수 차트
        years = ["2020", "2021", "2022", "2023", "2024"]
        paper_counts = [1, 0, 1, 1, 1]
        
        fig_papers = px.bar(
            x=years, 
            y=paper_counts,
            labels={"x": "연도", "y": "논문 수"},
            title="연도별 발표 논문 수"
        )
        st.plotly_chart(fig_papers, use_container_width=True)
    
    with col2:
        # 인용 수 차트
        citation_years = ["2021", "2022", "2023", "2024"]
        citations = [2, 5, 10, 15]
        
        fig_citations = px.line(
            x=citation_years, 
            y=citations,
            markers=True,
            labels={"x": "연도", "y": "인용 수"},
            title="누적 인용 수"
        )
        st.plotly_chart(fig_citations, use_container_width=True)
    
    # 수상 실적
    st.markdown('<div class="sub-header">수상 실적</div>', unsafe_allow_html=True)
    
    awards = [
        {"상명": "우수 논문상", "수여기관": "대한전자공학회", "연도": "2023"},
        {"상명": "Young Scientist Award", "수여기관": "International EM Conference", "연도": "2022"}
    ]
    
    for award in awards:
        st.markdown(f"- **{award['상명']}** ({award['연도']}) - {award['수여기관']}")

# 관심 연구 분야 페이지
def research_interests():
    st.markdown('<div class="main-header">관심 연구 분야</div>', unsafe_allow_html=True)
    
    # 주요 관심 분야 설명
    st.markdown('<div class="sub-header">주요 연구 분야</div>', unsafe_allow_html=True)
    
    interests = [
        {
            "title": "계산 전자기학 알고리즘 개발",
            "description": """
            전자기장 문제를 효율적으로 해석하기 위한 새로운 알고리즘 개발에 관심을 가지고 있습니다.
            특히 FDTD(Finite-Difference Time-Domain), FEM(Finite Element Method), 
            MoM(Method of Moments) 등의 수치해석 방법을 개선하는 연구를 진행하고 있습니다.
            """,
            "image": "algorithm.jpg"
        },
        {
            "title": "머신러닝 기반 전자기 문제 최적화",
            "description": """
            딥러닝과 강화학습 기술을 활용하여 전자기 설계 및 시뮬레이션 과정을 최적화하는 연구를 
            수행하고 있습니다. 이를 통해 복잡한 전자기 구조에 대한 설계 시간을 단축하고 
            성능을 향상시키는 방법을 탐구하고 있습니다.
            """,
            "image": "ml_optimization.jpg"
        },
        {
            "title": "메타표면 및 메타물질 설계",
            "description": """
            특수한 전자기적 특성을 가진 메타표면과 메타물질 설계에 집중하고 있습니다.
            이러한 구조체는 전통적인 물질에서는 관찰되지 않는 특성을 나타내며, 
            다양한 응용 분야에 활용될 수 있습니다.
            """,
            "image": "metamaterial.jpg"
        }
    ]
    
    for i, interest in enumerate(interests):
        with st.expander(f"{interest['title']}"):
            cols = st.columns([2, 1])
            with cols[0]:
                st.markdown(f"<div class='text-content'>{interest['description']}</div>", unsafe_allow_html=True)
            with cols[1]:
                try:
                    image = Image.open(interest['image'])
                    st.image(image, caption=interest['title'])
                except:
                    st.info(f"이미지를 추가하려면 '{interest['image']}' 파일을 프로젝트 폴더에 저장하세요.")
    
    # 키워드 클라우드 (시각적 요소로 추가)
    st.markdown('<div class="sub-header">연구 키워드</div>', unsafe_allow_html=True)
    
    keywords = {
        "Computational Electromagnetics": 100,
        "FDTD": 85,
        "FEM": 80,
        "Antenna Design": 75,
        "Machine Learning": 70,
        "Deep Learning": 65,
        "Metamaterials": 60,
        "RF Engineering": 55,
        "EM Wave Propagation": 50,
        "Wireless Communication": 45,
        "Numerical Methods": 40,
        "GPU Computing": 35
    }
    
    fig = go.Figure(data=[go.Bar(
        x=list(keywords.keys()),
        y=list(keywords.values()),
        marker_color='royalblue'
    )])
    
    fig.update_layout(
        title='연구 키워드 관심도',
        xaxis_tickangle=-45,
        yaxis_title='관심도',
        autosize=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

# 프로젝트 페이지
def projects():
    st.markdown('<div class="main-header">프로젝트</div>', unsafe_allow_html=True)
    
    projects_list = [
        {
            "title": "고성능 안테나 설계 자동화 시스템",
            "period": "2023.03 - 현재",
            "description": """
            딥러닝과 유전 알고리즘을 활용하여 안테나 설계를 자동화하는 시스템을 개발하고 있습니다.
            이 시스템은 설계 요구 사항을 입력받아 최적의 안테나 형상을 제안하고, 성능을 시뮬레이션합니다.
            현재까지 기존 수동 설계 대비 설계 시간을 90% 단축하는 성과를 달성했습니다.
            """,
            "image": "antenna_project.jpg"
        },
        {
            "title": "5G 통신을 위한 메타표면 필터 개발",
            "period": "2022.01 - 2022.12",
            "description": """
            5G 통신 환경에서 발생하는 간섭 신호를 효과적으로 차단하기 위한 메타표면 기반
            주파수 선택적 필터를 개발했습니다. FDTD 시뮬레이션과 실험을 통해 성능을 검증하였으며,
            원하는 주파수 대역에서 20dB 이상의 간섭 신호 저감 효과를 확인했습니다.
            """,
            "image": "metasurface_project.jpg"
        },
        {
            "title": "고속 전자기 시뮬레이션 라이브러리 개발",
            "period": "2021.06 - 2022.05",
            "description": """
            CUDA 기반 GPU 가속을 활용한 전자기 시뮬레이션 라이브러리를 개발했습니다.
            이 라이브러리는 기존 CPU 기반 시뮬레이션 대비 최대 100배 빠른 계산 속도를 제공하며,
            복잡한 3D 구조에서도 효율적인 해석이 가능합니다. Python 및 MATLAB 인터페이스를 제공하여
            다양한 연구 환경에서 활용 가능합니다.
            """,
            "image": "simulation_library.jpg"
        }
    ]
    
    for i, project in enumerate(projects_list):
        with st.expander(f"{project['title']} ({project['period']})"):
            cols = st.columns([2, 1])
            
            with cols[0]:
                st.markdown(f"<div class='text-content'>{project['description']}</div>", unsafe_allow_html=True)
            
            with cols[1]:
                try:
                    image = Image.open(project['image'])
                    st.image(image, caption=project['title'])
                except:
                    st.info(f"이미지를 추가하려면 '{project['image']}' 파일을 프로젝트 폴더에 저장하세요.")

# 연락처 페이지
def contact():
    st.markdown('<div class="main-header">연락처</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="sub-header">연락처 정보</div>', unsafe_allow_html=True)
        
        contact_info = {
            "이메일": "example@snu.ac.kr",
            "연구실 전화": "02-1234-5678",
            "연구실 위치": "서울대학교 공과대학 301동 1234호",
            "GitHub": "https://github.com/yourusername",
            "ResearchGate": "https://www.researchgate.net/profile/YourProfile",
            "Google Scholar": "https://scholar.google.com/citations?user=YourID"
        }
        
        for key, value in contact_info.items():
            if "https://" in value:
                st.markdown(f"**{key}**: [{value}]({value})")
            else:
                st.markdown(f"**{key}**: {value}")
    
    with col2:
        st.markdown('<div class="sub-header">메시지 보내기</div>', unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("이름")
            email = st.text_input("이메일")
            subject = st.text_input("제목")
            message = st.text_area("메시지")
            submit = st.form_submit_button("보내기")
            
            if submit:
                st.success("메시지가 전송되었습니다. 곧 답변 드리겠습니다!")
                # 실제로는 여기에 이메일 전송 코드를 추가해야 합니다.

# 메인 함수
def main():
    # 선택된 메뉴에 따라 페이지 표시
    if menu == "홈":
        home()
    elif menu == "연구 실적":
        research_achievements()
    elif menu == "관심 연구 분야":
        research_interests()
    elif menu == "프로젝트":
        projects()
    elif menu == "연락처":
        contact()

# 앱 실행
if __name__ == "__main__":
    main()