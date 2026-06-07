"""
このファイルは、固定の文字列や数値などのデータを変数として一括管理するファイルです。
"""

############################################################
# ライブラリの読み込み
############################################################
from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader, TextLoader


############################################################
# 共通変数の定義
############################################################

# ==========================================
# 画面表示系
# ==========================================
APP_NAME = "問い合わせ対応自動化AIエージェント"
CHAT_INPUT_HELPER_TEXT = "こちらからメッセージを送信してください。"
APP_BOOT_MESSAGE = "アプリが起動されました。"
USER_ICON_FILE_PATH = "user"
AI_ICON_FILE_PATH = "assistant"
WARNING_ICON = ":material/warning:"
ERROR_ICON = ":material/error:"
SPINNER_TEXT = "回答生成中..."


# ==========================================
# ユーザーフィードバック関連
# ==========================================
FEEDBACK_YES = "はい"
FEEDBACK_NO = "いいえ"

SATISFIED = "回答に満足した"
DISSATISFIED = "回答に満足しなかった"

FEEDBACK_REQUIRE_MESSAGE = "この回答はお役に立ちましたか？フィードバックをいただくことで、生成AIの回答の質が向上します。"
FEEDBACK_BUTTON_LABEL = "送信"
FEEDBACK_YES_MESSAGE = "ご満足いただけて良かったです！他にもご質問があれば、お気軽にお尋ねください！"
FEEDBACK_NO_MESSAGE = "ご期待に添えず申し訳ございません。今後の改善のために、差し支えない範囲でご満足いただけなかった理由を教えていただけますと幸いです。"
FEEDBACK_THANKS_MESSAGE = "ご回答いただき誠にありがとうございます。"


# ==========================================
# ログ出力系
# ==========================================
LOG_DIR_PATH = "./logs"
LOGGER_NAME = "ApplicationLog"
LOG_FILE = "application.log"


# ==========================================
# LLM設定系
# ==========================================
MODEL = "gpt-4o-mini"
TEMPERATURE = 0.0
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 5


# ==========================================
# トークン関連
# ==========================================
MAX_ALLOWED_TOKENS = 1000
ENCODING_KIND = "cl100k_base"


# ==========================================
# RAG参照用のデータソース系
# ==========================================
RAG_TOP_FOLDER_PATH = "./data"

SUPPORTED_EXTENSIONS = {
    ".pdf": PyMuPDFLoader,
    ".docx": Docx2txtLoader,
    ".txt": lambda path: TextLoader(path, encoding="utf-8")
}

DB_ALL_PATH = "./.db_all"
DB_COMPANY_PATH = "./.db_company"


# ==========================================
# AIエージェント関連
# ==========================================
AI_AGENT_MAX_ITERATIONS = 5

DB_SERVICE_PATH = "./.db_service"
DB_CUSTOMER_PATH = "./.db_customer"

DB_NAMES = {
    DB_COMPANY_PATH: f"{RAG_TOP_FOLDER_PATH}/company",
    DB_SERVICE_PATH: f"{RAG_TOP_FOLDER_PATH}/service",
    DB_CUSTOMER_PATH: f"{RAG_TOP_FOLDER_PATH}/customer"
}

AI_AGENT_MODE_ON = "利用する"
AI_AGENT_MODE_OFF = "利用しない"

SEARCH_ALL_INFO_TOOL_NAME = "search_all_info_tool"
SEARCH_ALL_INFO_TOOL_DESCRIPTION = "自社に関する質問全般で、どの文書を参照すべきか迷う場合に最初に使う"
SEARCH_COMPANY_INFO_TOOL_NAME = "search_company_info_tool"
SEARCH_COMPANY_INFO_TOOL_DESCRIPTION = "自社「株式会社EcoTee」に関する情報を参照したい時に使う"
SEARCH_SERVICE_INFO_TOOL_NAME = "search_service_info_tool"
SEARCH_SERVICE_INFO_TOOL_DESCRIPTION = "自社サービス「EcoTee」に関する情報を参照したい時に使う"
SEARCH_CUSTOMER_COMMUNICATION_INFO_TOOL_NAME = "search_customer_communication_tool"
SEARCH_CUSTOMER_COMMUNICATION_INFO_TOOL_DESCRIPTION = "顧客とのやりとりに関する情報を参照したい時に使う"
SEARCH_WEB_INFO_TOOL_NAME = "search_web_tool"
SEARCH_WEB_INFO_TOOL_DESCRIPTION = "自社サービス「EcoTee」に関する質問で、Web検索が必要と判断した場合に使う"


# ==========================================
# プロンプトテンプレート
# ==========================================
SYSTEM_PROMPT_CREATE_INDEPENDENT_TEXT = "会話履歴と最新の入力をもとに、会話履歴なしでも理解できる独立した入力テキストを生成してください。"

NO_DOC_MATCH_MESSAGE = "回答に必要な情報が見つかりませんでした。弊社に関する質問・要望を、入力内容を変えて送信してください。"

SYSTEM_PROMPT_INQUIRY = """
    あなたは株式会社EcoTeeの社内文書を基に、顧客からの問い合わせに答えるアシスタントです。
    以下の文脈に1件でも情報がある場合は、その内容を使って必ず具体的に日本語で回答してください。
    文脈にある情報を要約・言い換えしてよく、推測や一般論で補完しないでください。
    文脈が空、または本当に関係する情報が見当たらない場合のみ、
    「回答に必要な情報が見つかりませんでした。弊社に関する質問・要望を、入力内容を変えて送信してください。」と回答してください。

    文脈に情報がある場合は、必ず以下のMarkdown形式で回答してください。
    見出しはh3を使い、箇条書きは「- 」で統一してください。

    ### 概要
    - 企業やサービスの要点を2〜4項目で記載

    ### 主な特徴
    - 特徴を3〜6項目で記載

    ### 補足
    - 問い合わせに関連する補足事項を1〜3項目で記載

    文脈に存在しない固有情報は書かないでください。
    {context}
"""


# ==========================================
# エラー・警告メッセージ
# ==========================================
COMMON_ERROR_MESSAGE = "このエラーが繰り返し発生する場合は、管理者にお問い合わせください。"
INITIALIZE_ERROR_MESSAGE = "初期化処理に失敗しました。"
CONVERSATION_LOG_ERROR_MESSAGE = "過去の会話履歴の表示に失敗しました。"
GET_LLM_RESPONSE_ERROR_MESSAGE = "回答生成に失敗しました。"
DISP_ANSWER_ERROR_MESSAGE = "回答表示に失敗しました。"
INPUT_TEXT_LIMIT_ERROR_MESSAGE = f"入力されたテキストの文字数が受付上限値（{MAX_ALLOWED_TOKENS}）を超えています。受付上限値を超えないよう、再度入力してください。"


# ==========================================
# スタイリング
# ==========================================
STYLE = """
<style>
    .stHorizontalBlock {
        margin-top: -14px;
    }
    .stChatMessage + .stHorizontalBlock {
        margin-left: 56px;
    }
    .stChatMessage + .stHorizontalBlock .stColumn:nth-of-type(2) {
        margin-left: -24px;
    }
    @media screen and (max-width: 480px) {
        .stChatMessage + .stHorizontalBlock {
            flex-wrap: nowrap;
            margin-left: 56px;
        }
        .stChatMessage + .stHorizontalBlock .stColumn:nth-of-type(2) {
            margin-left: -206px;
        }
    }
</style>
"""