from urllib import request, parse
from typing import Any, Dict


def postRequest(url: str, postData: Dict[str, Any]) -> bytes:
    '''
    Requests-free method of posting to url
    '''
    headers = {
    'User-Agent': '',
}
    data = parse.urlencode(postData).encode()
    req = request.Request(url, data=data, headers=headers)
    return request.urlopen(req).read()
