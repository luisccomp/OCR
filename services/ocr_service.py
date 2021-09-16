import os
import re

from easyocr import Reader

from core.utils import string_utils

DELETE = [
    'VALIDA EM TODO O TERRITORIO NACIONAL',
    'DATA DE',
    'REGISTRO',
    'GERAL',
    'EXPEDICAO',
    'DOC ORIGEM NASC',
    'NASC',
    'DATA DE NASCIMENTO'
]


def extract_document_info(filename: str, delete: bool = True) -> dict:
    reader = Reader(lang_list=['pt', 'en', 'la'], gpu=False, verbose=False)
    
    result = reader.readtext(filename, width_ths=0.8, height_ths=1.0, detail=0)
    result = list(map(lambda x: string_utils.remove_accents(x).upper().strip(), result))

    for string in DELETE:
        index = string_utils.find_index(result, string)

        if index != -1:
            result.pop(index)

    data = {}

    fields = {
        'rg': r'(\d{1,2})\.?(\d{3})\.?(\d{3})-?(\d{1}|X|x$)',
        'cpf': r'(\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$)',
        'data_expedicao': r'\d?\d\/\d?\d\/\d{4}',
        'data_nascimento': r'\d?\d\/\d?\d\/\d{4}'
    }

    funcs = {
        'rg': lambda x: re.sub(r'[^\d]', '', x),
        'cpf': lambda x: re.sub(r'[^\d]', '', x)
    }

    for field, regexpr in fields.items():
        index = string_utils.find_regexpr_index(result, regexpr, funcs.get(field))

        if index != -1:
            data[field] = funcs.get(field, lambda x: x)(result[index])
            result.pop(index)
        else:
            data[field] = None

    index = string_utils.find_index(result, 'NOME')

    if index != -1:
        data['nome'] = result[index + 1]
    else:
        data['nome'] = None

    index = string_utils.find_index(result, 'FILIACAO')

    if index != -1:
        index += 1
        data['filiacao'] = []

        while not string_utils.match(result[index], 'NATURALIDADE'):
            data['filiacao'].append(result[index])
            index += 1
    else:
        data['filiacao'] = None

    index = string_utils.find_index(result, 'NATURALIDADE')

    if index != -1:
        index += 1
        data['naturalidade'] = result[index]
    else:
        data['naturalidade'] = None

    if delete:
        os.remove(filename)

    return data


def extract_driver_license_info(filename: str, delete: bool = True) -> dict:
    # TODO: implement a better OCR strategy to read a driver license data and convert it into a JSON object...
    reader = Reader(['pt', 'en', 'la'], gpu=False)

    result = reader.readtext(filename, width_ths=0.8, height_ths=1.0, slope_ths=1.0)
    result = map(lambda detection: detection[1].upper(), result)
    result = list(map(lambda detection: string_utils.remove_accents(detection).upper().strip(), result))

    ignore_list = []

    for string in ignore_list:
        index = string_utils.find_index(result, string)

        if index != -1:
            result.pop(index)

    index = string_utils.find_index(result, 'DOC IDENTIDADE / ORG EMISSOR UF') \
            or string_utils.find_index(result, 'DOC IDENTIDADE') \
            or string_utils.find_index(result, 'ORG EMISSOR UF')

    data = {}

    fields = {
        'rg': r'(\d{1,2})\.?(\d{3})\.?(\d{3})-?(\d{1}|X|x$)'
    }

    funcs = {
        'rg': lambda x: re.sub(r'[^\d]', '', x),
    }

    validations = {}

    if index != -1:
        index += 1

        data['rg'] = result[index]
        data['orgao_emissor'] = result[index + 1]
        data['uf'] = result[index + 2]
    else:
        data['rg'] = data['orgao_emissor'] = data['uf'] = None

    if delete:
        os.remove(filename)

    return data
