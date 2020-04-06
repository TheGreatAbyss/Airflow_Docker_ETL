from collections import OrderedDict
from functools import partial

from etl_src.schemas.conversion_functions import convert_bool, skip_empty_string

transactions_schema = OrderedDict({
    "TransactionID": partial(skip_empty_string, conversion_func=int),
    "isFraud": partial(skip_empty_string, conversion_func=convert_bool),
    "TransactionDT": partial(skip_empty_string, conversion_func=int),
    "TransactionAmt": partial(skip_empty_string, conversion_func=float),
    "ProductCD": partial(skip_empty_string, conversion_func=str),
    "card1": partial(skip_empty_string, conversion_func=int),
    "card2": partial(skip_empty_string, conversion_func=float),
    "card3": partial(skip_empty_string, conversion_func=float),
    "card4": partial(skip_empty_string, conversion_func=str),
    "card5": partial(skip_empty_string, conversion_func=float),
    "card6": partial(skip_empty_string, conversion_func=str),
    "addr1": partial(skip_empty_string, conversion_func=float),
    "addr2": partial(skip_empty_string, conversion_func=float),
    "dist1": partial(skip_empty_string, conversion_func=float),
    "dist2": partial(skip_empty_string, conversion_func=float),
    "P_emaildomain": partial(skip_empty_string, conversion_func=str),
    "R_emaildomain": partial(skip_empty_string, conversion_func=str),
    "C1": partial(skip_empty_string, conversion_func=float),
    "C2": partial(skip_empty_string, conversion_func=float),
    "C3": partial(skip_empty_string, conversion_func=float),
    "C4": partial(skip_empty_string, conversion_func=float),
    "C5": partial(skip_empty_string, conversion_func=float),
    "C6": partial(skip_empty_string, conversion_func=float),
    "C7": partial(skip_empty_string, conversion_func=float),
    "C8": partial(skip_empty_string, conversion_func=float),
    "C9": partial(skip_empty_string, conversion_func=float),
    "C10": partial(skip_empty_string, conversion_func=float),
    "C11": partial(skip_empty_string, conversion_func=float),
    "C12": partial(skip_empty_string, conversion_func=float),
    "C13": partial(skip_empty_string, conversion_func=float),
    "C14": partial(skip_empty_string, conversion_func=float),
    "D1": partial(skip_empty_string, conversion_func=float),
    "D2": partial(skip_empty_string, conversion_func=float),
    "D3": partial(skip_empty_string, conversion_func=float),
    "D4": partial(skip_empty_string, conversion_func=float),
    "D5": partial(skip_empty_string, conversion_func=float),
    "D6": partial(skip_empty_string, conversion_func=float),
    "D7": partial(skip_empty_string, conversion_func=float),
    "D8": partial(skip_empty_string, conversion_func=float),
    "D9": partial(skip_empty_string, conversion_func=float),
    "D10": partial(skip_empty_string, conversion_func=float),
    "D11": partial(skip_empty_string, conversion_func=float),
    "D12": partial(skip_empty_string, conversion_func=float),
    "D13": partial(skip_empty_string, conversion_func=float),
    "D14": partial(skip_empty_string, conversion_func=float),
    "D15": partial(skip_empty_string, conversion_func=float),
    "M1": partial(skip_empty_string, conversion_func=convert_bool),
    "M2": partial(skip_empty_string, conversion_func=convert_bool),
    "M3": partial(skip_empty_string, conversion_func=convert_bool),
    "M4": partial(skip_empty_string, conversion_func=str),
    "M5": partial(skip_empty_string, conversion_func=convert_bool),
    "M6": partial(skip_empty_string, conversion_func=convert_bool),
    "M7": partial(skip_empty_string, conversion_func=convert_bool),
    "M8": partial(skip_empty_string, conversion_func=convert_bool),
    "M9": partial(skip_empty_string, conversion_func=convert_bool),
    "V1": partial(skip_empty_string, conversion_func=convert_bool),
    "V2": partial(skip_empty_string, conversion_func=float),
    "V3": partial(skip_empty_string, conversion_func=float),
    "V4": partial(skip_empty_string, conversion_func=float),
    "V5": partial(skip_empty_string, conversion_func=float),
    "V6": partial(skip_empty_string, conversion_func=float),
    "V7": partial(skip_empty_string, conversion_func=float),
    "V8": partial(skip_empty_string, conversion_func=float),
    "V9": partial(skip_empty_string, conversion_func=float),
    "V10": partial(skip_empty_string, conversion_func=float),
    "V11": partial(skip_empty_string, conversion_func=float),
    "V12": partial(skip_empty_string, conversion_func=float),
    "V13": partial(skip_empty_string, conversion_func=float),
    "V14": partial(skip_empty_string, conversion_func=convert_bool),
    "V15": partial(skip_empty_string, conversion_func=float),
    "V16": partial(skip_empty_string, conversion_func=float),
    "V17": partial(skip_empty_string, conversion_func=float),
    "V18": partial(skip_empty_string, conversion_func=float),
    "V19": partial(skip_empty_string, conversion_func=float),
    "V20": partial(skip_empty_string, conversion_func=float),
    "V21": partial(skip_empty_string, conversion_func=float),
    "V22": partial(skip_empty_string, conversion_func=float),
    "V23": partial(skip_empty_string, conversion_func=float),
    "V24": partial(skip_empty_string, conversion_func=float),
    "V25": partial(skip_empty_string, conversion_func=float),
    "V26": partial(skip_empty_string, conversion_func=float),
    "V27": partial(skip_empty_string, conversion_func=float),
    "V28": partial(skip_empty_string, conversion_func=float),
    "V29": partial(skip_empty_string, conversion_func=float),
    "V30": partial(skip_empty_string, conversion_func=float),
    "V31": partial(skip_empty_string, conversion_func=float),
    "V32": partial(skip_empty_string, conversion_func=float),
    "V33": partial(skip_empty_string, conversion_func=float),
    "V34": partial(skip_empty_string, conversion_func=float),
    "V35": partial(skip_empty_string, conversion_func=float),
    "V36": partial(skip_empty_string, conversion_func=float),
    "V37": partial(skip_empty_string, conversion_func=float),
    "V38": partial(skip_empty_string, conversion_func=float),
    "V39": partial(skip_empty_string, conversion_func=float),
    "V40": partial(skip_empty_string, conversion_func=float),
    "V41": partial(skip_empty_string, conversion_func=convert_bool),
    "V42": partial(skip_empty_string, conversion_func=float),
    "V43": partial(skip_empty_string, conversion_func=float),
    "V44": partial(skip_empty_string, conversion_func=float),
    "V45": partial(skip_empty_string, conversion_func=float),
    "V46": partial(skip_empty_string, conversion_func=float),
    "V47": partial(skip_empty_string, conversion_func=float),
    "V48": partial(skip_empty_string, conversion_func=float),
    "V49": partial(skip_empty_string, conversion_func=float),
    "V50": partial(skip_empty_string, conversion_func=float),
    "V51": partial(skip_empty_string, conversion_func=float),
    "V52": partial(skip_empty_string, conversion_func=float),
    "V53": partial(skip_empty_string, conversion_func=float),
    "V54": partial(skip_empty_string, conversion_func=float),
    "V55": partial(skip_empty_string, conversion_func=float),
    "V56": partial(skip_empty_string, conversion_func=float),
    "V57": partial(skip_empty_string, conversion_func=float),
    "V58": partial(skip_empty_string, conversion_func=float),
    "V59": partial(skip_empty_string, conversion_func=float),
    "V60": partial(skip_empty_string, conversion_func=float),
    "V61": partial(skip_empty_string, conversion_func=float),
    "V62": partial(skip_empty_string, conversion_func=float),
    "V63": partial(skip_empty_string, conversion_func=float),
    "V64": partial(skip_empty_string, conversion_func=float),
    "V65": partial(skip_empty_string, conversion_func=convert_bool),
    "V66": partial(skip_empty_string, conversion_func=float),
    "V67": partial(skip_empty_string, conversion_func=float),
    "V68": partial(skip_empty_string, conversion_func=float),
    "V69": partial(skip_empty_string, conversion_func=float),
    "V70": partial(skip_empty_string, conversion_func=float),
    "V71": partial(skip_empty_string, conversion_func=float),
    "V72": partial(skip_empty_string, conversion_func=float),
    "V73": partial(skip_empty_string, conversion_func=float),
    "V74": partial(skip_empty_string, conversion_func=float),
    "V75": partial(skip_empty_string, conversion_func=float),
    "V76": partial(skip_empty_string, conversion_func=float),
    "V77": partial(skip_empty_string, conversion_func=float),
    "V78": partial(skip_empty_string, conversion_func=float),
    "V79": partial(skip_empty_string, conversion_func=float),
    "V80": partial(skip_empty_string, conversion_func=float),
    "V81": partial(skip_empty_string, conversion_func=float),
    "V82": partial(skip_empty_string, conversion_func=float),
    "V83": partial(skip_empty_string, conversion_func=float),
    "V84": partial(skip_empty_string, conversion_func=float),
    "V85": partial(skip_empty_string, conversion_func=float),
    "V86": partial(skip_empty_string, conversion_func=float),
    "V87": partial(skip_empty_string, conversion_func=float),
    "V88": partial(skip_empty_string, conversion_func=convert_bool),
    "V89": partial(skip_empty_string, conversion_func=float),
    "V90": partial(skip_empty_string, conversion_func=float),
    "V91": partial(skip_empty_string, conversion_func=float),
    "V92": partial(skip_empty_string, conversion_func=float),
    "V93": partial(skip_empty_string, conversion_func=float),
    "V94": partial(skip_empty_string, conversion_func=float),
    "V95": partial(skip_empty_string, conversion_func=float),
    "V96": partial(skip_empty_string, conversion_func=float),
    "V97": partial(skip_empty_string, conversion_func=float),
    "V98": partial(skip_empty_string, conversion_func=float),
    "V99": partial(skip_empty_string, conversion_func=float),
    "V100": partial(skip_empty_string, conversion_func=float),
    "V101": partial(skip_empty_string, conversion_func=float),
    "V102": partial(skip_empty_string, conversion_func=float),
    "V103": partial(skip_empty_string, conversion_func=float),
    "V104": partial(skip_empty_string, conversion_func=float),
    "V105": partial(skip_empty_string, conversion_func=float),
    "V106": partial(skip_empty_string, conversion_func=float),
    "V107": partial(skip_empty_string, conversion_func=convert_bool),
    "V108": partial(skip_empty_string, conversion_func=float),
    "V109": partial(skip_empty_string, conversion_func=float),
    "V110": partial(skip_empty_string, conversion_func=float),
    "V111": partial(skip_empty_string, conversion_func=float),
    "V112": partial(skip_empty_string, conversion_func=float),
    "V113": partial(skip_empty_string, conversion_func=float),
    "V114": partial(skip_empty_string, conversion_func=float),
    "V115": partial(skip_empty_string, conversion_func=float),
    "V116": partial(skip_empty_string, conversion_func=float),
    "V117": partial(skip_empty_string, conversion_func=float),
    "V118": partial(skip_empty_string, conversion_func=float),
    "V119": partial(skip_empty_string, conversion_func=float),
    "V120": partial(skip_empty_string, conversion_func=float),
    "V121": partial(skip_empty_string, conversion_func=float),
    "V122": partial(skip_empty_string, conversion_func=float),
    "V123": partial(skip_empty_string, conversion_func=float),
    "V124": partial(skip_empty_string, conversion_func=float),
    "V125": partial(skip_empty_string, conversion_func=float),
    "V126": partial(skip_empty_string, conversion_func=float),
    "V127": partial(skip_empty_string, conversion_func=float),
    "V128": partial(skip_empty_string, conversion_func=float),
    "V129": partial(skip_empty_string, conversion_func=float),
    "V130": partial(skip_empty_string, conversion_func=float),
    "V131": partial(skip_empty_string, conversion_func=float),
    "V132": partial(skip_empty_string, conversion_func=float),
    "V133": partial(skip_empty_string, conversion_func=float),
    "V134": partial(skip_empty_string, conversion_func=float),
    "V135": partial(skip_empty_string, conversion_func=float),
    "V136": partial(skip_empty_string, conversion_func=float),
    "V137": partial(skip_empty_string, conversion_func=float),
    "V138": partial(skip_empty_string, conversion_func=float),
    "V139": partial(skip_empty_string, conversion_func=float),
    "V140": partial(skip_empty_string, conversion_func=float),
    "V141": partial(skip_empty_string, conversion_func=float),
    "V142": partial(skip_empty_string, conversion_func=float),
    "V143": partial(skip_empty_string, conversion_func=float),
    "V144": partial(skip_empty_string, conversion_func=float),
    "V145": partial(skip_empty_string, conversion_func=float),
    "V146": partial(skip_empty_string, conversion_func=float),
    "V147": partial(skip_empty_string, conversion_func=float),
    "V148": partial(skip_empty_string, conversion_func=float),
    "V149": partial(skip_empty_string, conversion_func=float),
    "V150": partial(skip_empty_string, conversion_func=float),
    "V151": partial(skip_empty_string, conversion_func=float),
    "V152": partial(skip_empty_string, conversion_func=float),
    "V153": partial(skip_empty_string, conversion_func=float),
    "V154": partial(skip_empty_string, conversion_func=float),
    "V155": partial(skip_empty_string, conversion_func=float),
    "V156": partial(skip_empty_string, conversion_func=float),
    "V157": partial(skip_empty_string, conversion_func=float),
    "V158": partial(skip_empty_string, conversion_func=float),
    "V159": partial(skip_empty_string, conversion_func=float),
    "V160": partial(skip_empty_string, conversion_func=float),
    "V161": partial(skip_empty_string, conversion_func=float),
    "V162": partial(skip_empty_string, conversion_func=float),
    "V163": partial(skip_empty_string, conversion_func=float),
    "V164": partial(skip_empty_string, conversion_func=float),
    "V165": partial(skip_empty_string, conversion_func=float),
    "V166": partial(skip_empty_string, conversion_func=float),
    "V167": partial(skip_empty_string, conversion_func=float),
    "V168": partial(skip_empty_string, conversion_func=float),
    "V169": partial(skip_empty_string, conversion_func=float),
    "V170": partial(skip_empty_string, conversion_func=float),
    "V171": partial(skip_empty_string, conversion_func=float),
    "V172": partial(skip_empty_string, conversion_func=float),
    "V173": partial(skip_empty_string, conversion_func=float),
    "V174": partial(skip_empty_string, conversion_func=float),
    "V175": partial(skip_empty_string, conversion_func=float),
    "V176": partial(skip_empty_string, conversion_func=float),
    "V177": partial(skip_empty_string, conversion_func=float),
    "V178": partial(skip_empty_string, conversion_func=float),
    "V179": partial(skip_empty_string, conversion_func=float),
    "V180": partial(skip_empty_string, conversion_func=float),
    "V181": partial(skip_empty_string, conversion_func=float),
    "V182": partial(skip_empty_string, conversion_func=float),
    "V183": partial(skip_empty_string, conversion_func=float),
    "V184": partial(skip_empty_string, conversion_func=float),
    "V185": partial(skip_empty_string, conversion_func=float),
    "V186": partial(skip_empty_string, conversion_func=float),
    "V187": partial(skip_empty_string, conversion_func=float),
    "V188": partial(skip_empty_string, conversion_func=float),
    "V189": partial(skip_empty_string, conversion_func=float),
    "V190": partial(skip_empty_string, conversion_func=float),
    "V191": partial(skip_empty_string, conversion_func=float),
    "V192": partial(skip_empty_string, conversion_func=float),
    "V193": partial(skip_empty_string, conversion_func=float),
    "V194": partial(skip_empty_string, conversion_func=float),
    "V195": partial(skip_empty_string, conversion_func=float),
    "V196": partial(skip_empty_string, conversion_func=float),
    "V197": partial(skip_empty_string, conversion_func=float),
    "V198": partial(skip_empty_string, conversion_func=float),
    "V199": partial(skip_empty_string, conversion_func=float),
    "V200": partial(skip_empty_string, conversion_func=float),
    "V201": partial(skip_empty_string, conversion_func=float),
    "V202": partial(skip_empty_string, conversion_func=float),
    "V203": partial(skip_empty_string, conversion_func=float),
    "V204": partial(skip_empty_string, conversion_func=float),
    "V205": partial(skip_empty_string, conversion_func=float),
    "V206": partial(skip_empty_string, conversion_func=float),
    "V207": partial(skip_empty_string, conversion_func=float),
    "V208": partial(skip_empty_string, conversion_func=float),
    "V209": partial(skip_empty_string, conversion_func=float),
    "V210": partial(skip_empty_string, conversion_func=float),
    "V211": partial(skip_empty_string, conversion_func=float),
    "V212": partial(skip_empty_string, conversion_func=float),
    "V213": partial(skip_empty_string, conversion_func=float),
    "V214": partial(skip_empty_string, conversion_func=float),
    "V215": partial(skip_empty_string, conversion_func=float),
    "V216": partial(skip_empty_string, conversion_func=float),
    "V217": partial(skip_empty_string, conversion_func=float),
    "V218": partial(skip_empty_string, conversion_func=float),
    "V219": partial(skip_empty_string, conversion_func=float),
    "V220": partial(skip_empty_string, conversion_func=float),
    "V221": partial(skip_empty_string, conversion_func=float),
    "V222": partial(skip_empty_string, conversion_func=float),
    "V223": partial(skip_empty_string, conversion_func=float),
    "V224": partial(skip_empty_string, conversion_func=float),
    "V225": partial(skip_empty_string, conversion_func=float),
    "V226": partial(skip_empty_string, conversion_func=float),
    "V227": partial(skip_empty_string, conversion_func=float),
    "V228": partial(skip_empty_string, conversion_func=float),
    "V229": partial(skip_empty_string, conversion_func=float),
    "V230": partial(skip_empty_string, conversion_func=float),
    "V231": partial(skip_empty_string, conversion_func=float),
    "V232": partial(skip_empty_string, conversion_func=float),
    "V233": partial(skip_empty_string, conversion_func=float),
    "V234": partial(skip_empty_string, conversion_func=float),
    "V235": partial(skip_empty_string, conversion_func=float),
    "V236": partial(skip_empty_string, conversion_func=float),
    "V237": partial(skip_empty_string, conversion_func=float),
    "V238": partial(skip_empty_string, conversion_func=float),
    "V239": partial(skip_empty_string, conversion_func=float),
    "V240": partial(skip_empty_string, conversion_func=float),
    "V241": partial(skip_empty_string, conversion_func=float),
    "V242": partial(skip_empty_string, conversion_func=float),
    "V243": partial(skip_empty_string, conversion_func=float),
    "V244": partial(skip_empty_string, conversion_func=float),
    "V245": partial(skip_empty_string, conversion_func=float),
    "V246": partial(skip_empty_string, conversion_func=float),
    "V247": partial(skip_empty_string, conversion_func=float),
    "V248": partial(skip_empty_string, conversion_func=float),
    "V249": partial(skip_empty_string, conversion_func=float),
    "V250": partial(skip_empty_string, conversion_func=float),
    "V251": partial(skip_empty_string, conversion_func=float),
    "V252": partial(skip_empty_string, conversion_func=float),
    "V253": partial(skip_empty_string, conversion_func=float),
    "V254": partial(skip_empty_string, conversion_func=float),
    "V255": partial(skip_empty_string, conversion_func=float),
    "V256": partial(skip_empty_string, conversion_func=float),
    "V257": partial(skip_empty_string, conversion_func=float),
    "V258": partial(skip_empty_string, conversion_func=float),
    "V259": partial(skip_empty_string, conversion_func=float),
    "V260": partial(skip_empty_string, conversion_func=float),
    "V261": partial(skip_empty_string, conversion_func=float),
    "V262": partial(skip_empty_string, conversion_func=float),
    "V263": partial(skip_empty_string, conversion_func=float),
    "V264": partial(skip_empty_string, conversion_func=float),
    "V265": partial(skip_empty_string, conversion_func=float),
    "V266": partial(skip_empty_string, conversion_func=float),
    "V267": partial(skip_empty_string, conversion_func=float),
    "V268": partial(skip_empty_string, conversion_func=float),
    "V269": partial(skip_empty_string, conversion_func=float),
    "V270": partial(skip_empty_string, conversion_func=float),
    "V271": partial(skip_empty_string, conversion_func=float),
    "V272": partial(skip_empty_string, conversion_func=float),
    "V273": partial(skip_empty_string, conversion_func=float),
    "V274": partial(skip_empty_string, conversion_func=float),
    "V275": partial(skip_empty_string, conversion_func=float),
    "V276": partial(skip_empty_string, conversion_func=float),
    "V277": partial(skip_empty_string, conversion_func=float),
    "V278": partial(skip_empty_string, conversion_func=float),
    "V279": partial(skip_empty_string, conversion_func=float),
    "V280": partial(skip_empty_string, conversion_func=float),
    "V281": partial(skip_empty_string, conversion_func=float),
    "V282": partial(skip_empty_string, conversion_func=float),
    "V283": partial(skip_empty_string, conversion_func=float),
    "V284": partial(skip_empty_string, conversion_func=float),
    "V285": partial(skip_empty_string, conversion_func=float),
    "V286": partial(skip_empty_string, conversion_func=float),
    "V287": partial(skip_empty_string, conversion_func=float),
    "V288": partial(skip_empty_string, conversion_func=float),
    "V289": partial(skip_empty_string, conversion_func=float),
    "V290": partial(skip_empty_string, conversion_func=float),
    "V291": partial(skip_empty_string, conversion_func=float),
    "V292": partial(skip_empty_string, conversion_func=float),
    "V293": partial(skip_empty_string, conversion_func=float),
    "V294": partial(skip_empty_string, conversion_func=float),
    "V295": partial(skip_empty_string, conversion_func=float),
    "V296": partial(skip_empty_string, conversion_func=float),
    "V297": partial(skip_empty_string, conversion_func=float),
    "V298": partial(skip_empty_string, conversion_func=float),
    "V299": partial(skip_empty_string, conversion_func=float),
    "V300": partial(skip_empty_string, conversion_func=float),
    "V301": partial(skip_empty_string, conversion_func=float),
    "V302": partial(skip_empty_string, conversion_func=float),
    "V303": partial(skip_empty_string, conversion_func=float),
    "V304": partial(skip_empty_string, conversion_func=float),
    "V305": partial(skip_empty_string, conversion_func=float),
    "V306": partial(skip_empty_string, conversion_func=float),
    "V307": partial(skip_empty_string, conversion_func=float),
    "V308": partial(skip_empty_string, conversion_func=float),
    "V309": partial(skip_empty_string, conversion_func=float),
    "V310": partial(skip_empty_string, conversion_func=float),
    "V311": partial(skip_empty_string, conversion_func=float),
    "V312": partial(skip_empty_string, conversion_func=float),
    "V313": partial(skip_empty_string, conversion_func=float),
    "V314": partial(skip_empty_string, conversion_func=float),
    "V315": partial(skip_empty_string, conversion_func=float),
    "V316": partial(skip_empty_string, conversion_func=float),
    "V317": partial(skip_empty_string, conversion_func=float),
    "V318": partial(skip_empty_string, conversion_func=float),
    "V319": partial(skip_empty_string, conversion_func=float),
    "V320": partial(skip_empty_string, conversion_func=float),
    "V321": partial(skip_empty_string, conversion_func=float),
    "V322": partial(skip_empty_string, conversion_func=float),
    "V323": partial(skip_empty_string, conversion_func=float),
    "V324": partial(skip_empty_string, conversion_func=float),
    "V325": partial(skip_empty_string, conversion_func=float),
    "V326": partial(skip_empty_string, conversion_func=float),
    "V327": partial(skip_empty_string, conversion_func=float),
    "V328": partial(skip_empty_string, conversion_func=float),
    "V329": partial(skip_empty_string, conversion_func=float),
    "V330": partial(skip_empty_string, conversion_func=float),
    "V331": partial(skip_empty_string, conversion_func=float),
    "V332": partial(skip_empty_string, conversion_func=float),
    "V333": partial(skip_empty_string, conversion_func=float),
    "V334": partial(skip_empty_string, conversion_func=float),
    "V335": partial(skip_empty_string, conversion_func=float),
    "V336": partial(skip_empty_string, conversion_func=float),
    "V337": partial(skip_empty_string, conversion_func=float),
    "V338": partial(skip_empty_string, conversion_func=float),
    "V339": partial(skip_empty_string, conversion_func=float)
})

primary_key = "TransactionID"