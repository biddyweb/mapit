import json
import zlib


def get_content(response):
    if getattr(response, 'streaming', None):
        content = b''.join(response.streaming_content)
    else:
        content = response.content

    # Just in case the response is gzipped
    try:
        content = zlib.decompress(content, 16+zlib.MAX_WBITS)
    except zlib.error:
        pass

    content = json.loads(content.decode('utf-8'))
    return content
