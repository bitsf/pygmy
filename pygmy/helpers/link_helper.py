from pygmy.core.hashdigest import HashDigest
from pygmy.model import LinkManager
from random import randint


def next_short_code():
    """Pass a long link and it returns the next available
    base62 short code.
    :return: str
    """
    link_manager = LinkManager()
    link = link_manager.latest_default_link()
    # set base id to random int for a 5 digit hash code
    base_id = randint(14776336, 916132831)
    base_str = HashDigest().shorten(base_id)
    while link_manager.find(short_code=base_str):
        base_id += 1
        base_str = HashDigest().shorten(base_id)
    return base_str


def long_url_exists(long_url):
    """Pass a long link, check and return if link exists or not.

    :param long_url: str
    :return: bool
    """
    link_manager = LinkManager()
    link = link_manager.find(long_url=long_url)
    if link is None:
        return False
    if link.is_disabled:
        return False
    return True
