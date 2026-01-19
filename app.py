from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# タイトル
st.title("🤖 AI専門家アドバイザー")

# アプリの概要
st.markdown("""
### 📖 アプリの概要
このアプリは、LangChainを使用して様々な分野の専門家AIと対話できるWebアプリケーションです。
専門家の種類を選択し、質問を入力することで、その分野に特化したアドバイスを受け取ることができます。

### 📝 使い方
1. 下のラジオボタンから相談したい専門家を選択してください
2. テキスト入力フォームに質問や相談内容を入力してください
3. 「実行」ボタンをクリックすると、AIが回答を生成します
""")

st.divider()

# ラジオボタンで専門家を選択
selected_expert = st.radio(
    "相談したい専門家を選択してください",
    ["健康・栄養アドバイザー", "キャリアカウンセラー", "旅行プランナー"],
    help="選択した専門家の知識に基づいた回答が提供されます"
)

# 入力フォーム
user_input = st.text_area(
    "質問や相談内容を入力してください",
    placeholder="例: バランスの良い食事について教えてください",
    height=100
)


def get_llm_response(user_text: str, expert_type: str) -> str:
    """
    LLMからの回答を取得する関数
    
    Args:
        user_text (str): ユーザーからの入力テキスト
        expert_type (str): 選択された専門家の種類
    
    Returns:
        str: LLMからの回答テキスト
    """
    # 専門家の種類に応じてシステムメッセージを設定
    system_messages = {
        "健康・栄養アドバイザー": "あなたは健康と栄養に関する専門家です。科学的根拠に基づいた、わかりやすく実践的なアドバイスを提供してください。医療行為ではないことを前提に、一般的な健康増進のための情報を提供してください。",
        "キャリアカウンセラー": "あなたはキャリア開発とキャリアプランニングの専門家です。職業選択、スキル開発、キャリアアップに関する具体的で建設的なアドバイスを提供してください。",
        "旅行プランナー": "あなたは旅行計画の専門家です。目的地の情報、観光スポット、予算管理、旅程作成など、楽しく充実した旅行を実現するための具体的なアドバイスを提供してください。"
    }
    
    # システムメッセージを取得
    system_message = system_messages.get(expert_type, "あなたは親切で知識豊富なアシスタントです。")
    
    # ChatOpenAIモデルのインスタンスを作成
    chat = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7
    )
    
    # メッセージを作成
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_text)
    ]
    
    # LLMに問い合わせ
    response = chat.invoke(messages)
    
    return response.content


# 実行ボタン
if st.button("🚀 実行", type="primary", use_container_width=True):
    if user_input.strip():
        with st.spinner("AIが回答を生成中..."):
            try:
                # LLMから回答を取得
                answer = get_llm_response(user_input, selected_expert)
                
                st.divider()
                st.success(f"**{selected_expert}からの回答:**")
                st.write(answer)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {str(e)}")
                st.info("OpenAI APIキーが正しく設定されているか確認してください。")
    else:
        st.warning("⚠️ 質問や相談内容を入力してください。")
