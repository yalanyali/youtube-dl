# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import get_element_by_class

class kk1990IE(InfoExtractor):
    _VALID_URL = r'(?:https?://)?(?:www\.)?1990kk\.com/(?P<id>.+)'
    _TESTS = [{
        'url': 'https://1990kk.com/kaybedenler-kulubu-kent-fm-1-nusha',
        'md5': '9c84e100f721cbfee4a97720afef5383',
        'info_dict': {
            'id': 'kaybedenler-kulubu-kent-fm-1-nusha',
            'ext': 'm4a',
            'title': 'kentfm/1nusha',
        }
    }]

    def _real_extract(self, url):
        url_path = self._match_id(url)
        webpage = self._download_webpage(url, url_path)
        video_id = self._html_search_regex(
            r'var video=\"(.+?)\"',
            webpage, 'title')
        title = get_element_by_class('card-title', webpage).strip()
        print(title)
        video_url_params = self._search_regex(
            r'var dogrula=\"(.+?)\"',
            webpage, 'video URL params', default=None)
        url_path_part = self._search_regex(
            r'\"(tga\d+?)\"',
            webpage, 'video URL path part', default="tga120")  # Seems to be constant but may change
        formats = (self._extract_mpd_formats(
            'https://cdn-video.yayin.com.tr/%s/_definst_/mp4:%s.mov/manifest.mpd?%s' % (url_path_part, video_id, video_url_params),
            video_id, mpd_id='dash'))
        print('title', title)
        print('video_id', video_id)
        return {
            'id': video_id,
            'title': title,
            'formats': formats
        }
