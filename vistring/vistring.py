# -*- coding: utf-8 -*-

"""Main module."""

notones = {
    u'đ': u'd',

    u'à': u'a',
    u'á': u'a',
    u'ả': u'a',
    u'ã': u'a',
    u'ạ': u'a',

    u'ă': u'a',
    u'ằ': u'a',
    u'ắ': u'a',
    u'ẳ': u'a',
    u'ẵ': u'a',
    u'ặ': u'a',

    u'â': u'a',
    u'ầ': u'a',
    u'ấ': u'a',
    u'ẩ': u'a',
    u'ẫ': u'a',
    u'ậ': u'a',

    u'è': u'e',
    u'é': u'e',
    u'ẻ': u'e',
    u'ẽ': u'e',
    u'ẹ': u'e',

    u'ê': u'e',
    u'ề': u'e',
    u'ễ': u'e',
    u'ể': u'e',
    u'ễ': u'e',
    u'ệ': u'e',

    u'ì': u'i',
    u'í': u'i',
    u'ỉ': u'i',
    u'ĩ': u'i',
    u'ị': u'i',

    u'ò': u'o',
    u'ó': u'o',
    u'ỏ': u'o',
    u'õ': u'o',
    u'ọ': u'o',

    u'ô': u'o',
    u'ồ': u'o',
    u'ố': u'o',
    u'ổ': u'o',
    u'ỗ': u'o',
    u'ộ': u'o',

    u'ơ': u'o',
    u'ờ': u'o',
    u'ớ': u'o',
    u'ở': u'o',
    u'ỡ': u'o',
    u'ợ': u'o',

    u'ù': u'u',
    u'ú': u'u',
    u'ủ': u'u',
    u'ũ': u'u',
    u'ụ': u'u',

    u'ư': u'u',
    u'ừ': u'u',
    u'ứ': u'u',
    u'ử': u'u',
    u'ữ': u'u',
    u'ự': u'u',

    u'ỳ': u'y',
    u'ý': u'y',
    u'ỷ': u'y',
    u'ỹ': u'y',
    u'ỵ': u'y',
}


def remove_tones(vietnamese_string):
    out = []
    # to do use transformation here
    for c in vietnamese_string:
        if c in notones:
            out.append(notones[c])
        else:
            out.append(c)
    return ''.join(out)
