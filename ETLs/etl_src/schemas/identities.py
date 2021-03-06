from collections import OrderedDict
from functools import partial

from etl_src.schemas.conversion_functions import convert_bool, skip_empty_string

identities_schema = OrderedDict({
    "TransactionID": partial(skip_empty_string, conversion_func=int),
    "id_01": partial(skip_empty_string, conversion_func=float),
    "id_02": partial(skip_empty_string, conversion_func=float),
    "id_03": partial(skip_empty_string, conversion_func=float),
    "id_04": partial(skip_empty_string, conversion_func=float),
    "id_05": partial(skip_empty_string, conversion_func=float),
    "id_06": partial(skip_empty_string, conversion_func=float),
    "id_07": partial(skip_empty_string, conversion_func=float),
    "id_08": partial(skip_empty_string, conversion_func=float),
    "id_09": partial(skip_empty_string, conversion_func=float),
    "id_10": partial(skip_empty_string, conversion_func=float),
    "id_11": partial(skip_empty_string, conversion_func=float),
    "id_12": partial(skip_empty_string, conversion_func=str),
    "id_13": partial(skip_empty_string, conversion_func=float),
    "id_14": partial(skip_empty_string, conversion_func=float),
    "id_15": partial(skip_empty_string, conversion_func=str),
    "id_16": partial(skip_empty_string, conversion_func=str),
    "id_17": partial(skip_empty_string, conversion_func=float),
    "id_18": partial(skip_empty_string, conversion_func=float),
    "id_19": partial(skip_empty_string, conversion_func=float),
    "id_20": partial(skip_empty_string, conversion_func=float),
    "id_21": partial(skip_empty_string, conversion_func=float),
    "id_22": partial(skip_empty_string, conversion_func=float),
    "id_23": partial(skip_empty_string, conversion_func=str),
    "id_24": partial(skip_empty_string, conversion_func=float),
    "id_25": partial(skip_empty_string, conversion_func=float),
    "id_26": partial(skip_empty_string, conversion_func=float),
    "id_27": partial(skip_empty_string, conversion_func=str),
    "id_28": partial(skip_empty_string, conversion_func=str),
    "id_29": partial(skip_empty_string, conversion_func=str),
    "id_30": partial(skip_empty_string, conversion_func=str),
    "id_31": partial(skip_empty_string, conversion_func=str),
    "id_32": partial(skip_empty_string, conversion_func=float),
    "id_33": partial(skip_empty_string, conversion_func=str),
    "id_34": partial(skip_empty_string, conversion_func=str),
    "id_35": partial(skip_empty_string, conversion_func=convert_bool),
    "id_36": partial(skip_empty_string, conversion_func=convert_bool),
    "id_37": partial(skip_empty_string, conversion_func=convert_bool),
    "id_38": partial(skip_empty_string, conversion_func=convert_bool),
    "DeviceType": partial(skip_empty_string, conversion_func=str),
    "DeviceInfo": partial(skip_empty_string, conversion_func=str)
})

primary_key = "TransactionID"