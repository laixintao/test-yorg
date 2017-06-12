# -*- coding: utf-8 -*-
# pylint: disable=R0201
from __future__ import unicode_literals

import unittest
from tests.utils import read_bytes
from mock import patch
from yorg.contrib.court.{package} import do_parse_detail_page, MONGO_NAME
from yorg.utils import mongo


class {testname}CourtTestCase(unittest.TestCase):

    @patch('yorg.utils.get_html_body')
    def test_parse_list_page_success(self, mock_get_html_body):
        rel_path = {html_path}
        case_detail = mongo[MONGO_NAME]['case_detail']
        mock_get_html_body.return_value = read_bytes(rel_path).decode('utf-8')
        old_case_detail_num = case_detail.count()
        do_parse_detail_page('{url}')
        new_case_detail_num = old_case_detail_num + {data_num}
        assert case_detail.count() == new_case_detail_num
        case_detail.drop()
