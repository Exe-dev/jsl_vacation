import unicodedata


# numが数字か判定する漢数字やローマ数字も数字扱いになる
def check_word(num):
    result = num.isnumeric
    if(result == 'true'):
        return result
    # else:
