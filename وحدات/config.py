import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID  =  int ( getenv ( "API_ID" ، "19223176" ))
API_HASH  =  getenv ( "API_HASH" ، "501458c547877e2fb2e3907b83f8d00f" )
BOT_TOKEN  =  getenv ( "BOT_TOKEN" ، "5536881929:AAEaP1pS92V337fbVS90IhFj4bNaiQngNUc" )
DURATION_LIMIT  =  int ( getenv ( "DURATION_LIMIT" ، "300" ))
STRING_SESSION   =   getenv ( "STRING_SESSION"  ،  "AgBtfbl-o2Lmc5ejna60ArJa_r06NtVXQz5pV_OU9ug-gX10aqsMzPfnzEeOhAdIDH6t4PV4IeDC6s45dCDyi6qfehR1_G2cIacfKFRuMRKx5WWPk_c-qCJU2gxZ25AMgkRT5ql-V4o2s1ZCoAZowQelaljMcxGSZkpj4UNerBKWuxWvzNpLBUtmroSM7Ycpzbl_SkvrK_p5GLEeoeLS6103Rs2RANMCdFPACaR9U3NPRPCZIN96cO1ZW8camXWSLzdYrUynWHp9p7WKS0Od9dp1XM2RtTJp7MUsz1lxjeeCSnenC_Tk_OobyOWcW1eru_F3tQlOfsj4yAijn5_rpk_bAAAAATwwHfUA" )
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5313375615")
