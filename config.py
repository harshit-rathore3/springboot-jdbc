import os
from flask_caching import Cache
from dotenv import load_dotenv

try:
    ENV = os.environ["ENV"]
except Exception as e:
    print("Using local ENVs:", e)
    load_dotenv('config_local.env')

####### Cache Config ######
cache = Cache()

# ############################ GLOBAL VARIABLE ############################
glossary_dict = {}
code_profi_dict = {}
word_dict = {}

######### MONGODB #########
MONGODB_CLIENT = os.environ["MONGODB_CLIENT"]
MONGODB_SUMMARY_CLIENT = os.environ["MONGODB_SUMMARY_CLIENT"]
MONGO_COLLECTION = os.environ["MONGO_COLLECTION"]
MONGO_SUMMARY_COLLECTION = os.environ["MONGO_SUMMARY_COLLECTION"]

AUTOAI_URL = os.environ["AUTOAI_URL"]
COPILOT_URL = os.environ["COPILOT_URL"]
RLEF_TOKEN = os.environ["RLEF_TOKEN"]
RLEF_COPILOT_ID = os.environ["RLEF_COPILOT_ID"]

######### AZURE #########
AZURE_API_TYPE = os.environ["AZURE_API_TYPE"]
AZURE_API_BASE = os.environ["AZURE_API_BASE"]
AZURE_API_VERSION = os.environ["AZURE_API_VERSION"]
AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
AZURE_OPENAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
MODEL = os.environ["MODEL"]
MAX_TOKENS = int(os.environ["MAX_TOKENS"])
TEMPERATURE = int(os.environ["TEMPERATURE"])

UNIT_TEST_SCORE = os.environ["UNIT_TEST_SCORE"]
LUMBAR_BACKEND_URL = os.environ["LUMBAR_BACKEND_URL"]

URL_PROMPT_UPLOAD = os.environ["URL_PROMPT_UPLOAD"]
URL_RLEF = os.environ["URL_RLEF"]
URL_GLOSSARY=os.environ["URL_GLOSSARY"]
URL_GLOSSARY_TOKEN= os.environ["URL_GLOSSARY_TOKEN"]
CREDS_FOR_GLOSSARY= os.environ["CREDS_FOR_GLOSSARY"]
FEEDBACK_MODEL = os.environ["FEEDBACK_MODEL"]
GITHUB_RAG_PINECONE_KEY=os.environ["GITHUB_RAG_PINECONE_KEY"]
GITHUB_RAG_PINECONE_INDEX=os.environ["GITHUB_RAG_PINECONE_INDEX"]
EMBADDED_AZURE_KEY=os.environ["EMBADDED_AZURE_KEY"]
EMBADDED_AZURE_API=os.environ["EMBADDED_AZURE_API"]
URL_RLEF_COLLECTION=os.environ["URL_RLEF_COLLECTION"]

AUTH_TOKEN=os.environ["RLEF_TOKEN"]

SONAR_TOKEN=os.environ["SONAR_TOKEN"]

REDIS_HOST=os.environ["REDIS_HOST"]
REDIS_DB=os.environ["REDIS_DB"]
REDIS_URL=os.environ["REDIS_URL"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]

PREDICT_API = os.environ["PREDICT_API"]

C_11_VM_NAME = os.environ["C_11_VM_NAME"]
C_4_VM_NAME = os.environ["C_4_VM_NAME"]

CS_LANG = [
    "abap", "bat", "bibtex", "clojure", "coffeescript", "c", "cpp", "csharp",
    "dockercompose", "css", "cuda-cpp", "d", "pascal", "diff", "dockerfile",
    "erlang", "fsharp", "git-commit", "git-rebase", "go", "groovy", "handlebars",
    "haml", "haskell", "html", "ini", "java", "javascript", "javascriptreact",
    "json", "jsonc", "julia", "latex", "less", "lua", "makefile", "markdown",
    "objective-c", "objective-cpp", "ocaml", "pascal", "perl", "perl6", "php",
    "plaintext", "powershell", "jade", "pug", "python", "r", "razor", "ruby",
    "rust", "scss", "sass", "shaderlab", "shellscript", "slim", "sql", "stylus",
    "svelte", "swift", "typescript", "typescriptreact", "tex", "vb", "vue",
    "vue-html", "xml", "xsl", "yaml"
]

# ADMIN_EMAILS = [
#     "vibhav.singh@techolution.com",
#     "udit.dave@techolution.com",
#     "humant.sattabhayya@techolution.com",
#     "yogin.patil@techolution.com",
#     "ritik.dubey@techolution.com",
#     "saptyadeep.bhattacharjee@techolution.com",
#     "suraj.saxena@techolution.com",
#     "akash.singh@techolution.com",
#     "bhawani.bharti@techolution.com",
#     "soutik.bera@techolution.com",
# ]

ALLOYDB_NAME = os.environ["ALLOYDB_NAME"]

APPLICATION_CONVERSION_DB = os.environ["APPLICATION_CONVERSION_DB"]

LLM_PROJECT_ID = os.environ["LLM_PROJECT_ID"]


############ COMPILER ONBOARDING APIs ############
COMPILER_RUN_API = os.environ["COMPILER_RUN_API"]
COMPILER_UPLOAD_API = os.environ["COMPILER_UPLOAD_API"]
COMPILE_C_CODE_API = os.environ["COMPILE_C_CODE_API"]

EGPT_NODE_MONGO_CLIENT=os.environ["EGPT_NODE_MONGO_CLIENT"]
EGPT_NODE_MONGO_DB=os.environ["EGPT_NODE_MONGO_DB"]

EGPT_ALLOY_DB_NAME=os.environ["EGPT_ALLOY_DB_NAME"]
EGPT_ALLOY_DB_USER=os.environ["EGPT_ALLOY_DB_USER"]
EGPT_ALLOY_DB_PASS=os.environ["EGPT_ALLOY_DB_PASS"]
EGPT_ALLOY_DB_HOST=os.environ["EGPT_ALLOY_DB_HOST"]
EGPT_ALLOY_DB_PORT=os.environ["EGPT_ALLOY_DB_PORT"]

######### EMAIL #########
EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
APPMOD_DOMAIN = os.environ["APPMOD_DOMAIN"]
GIT_PAT_TOKEN = os.environ["GIT_PAT_TOKEN"]