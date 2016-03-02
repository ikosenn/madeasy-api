from django.test import TestCase
from django.core.management import call_command
from django.conf import settings

from emrapp.data_bootstrap.bootstrap import DataAlreadyExistsException

import os

import pytest

slow = pytest.mark.skipif(
    not os.getenv('CI_ENVIRON'),
    reason="""need a PostgreSQL database to run these \
tests, which makes them very slow"""
)


@slow
class TestFullDataLoad(TestCase):

    def test_default_load(self):
        # The first data load should succeed
        data_files = settings.BASE_DIR + '/data/*/*.json'
        call_command('bootstrap', data_files)

        # The second data load should fail
        with pytest.raises(DataAlreadyExistsException):
            call_command('bootstrap', data_files)

        # Now try loading a single file, should still fail
        test_file = settings.BASE_DIR + \
            '/data/001_common/001_administrative-gender.json'
        with pytest.raises(DataAlreadyExistsException):
            call_command('bootstrap', test_file)


class TestDataLoad(TestCase):

    def test_default_load(self):
        # The first data load should succeed
        data_files = settings.BASE_DIR + '/data/001_common/*.json'
        call_command('bootstrap', data_files)

        # The second data load should fail
        with pytest.raises(DataAlreadyExistsException):
            call_command('bootstrap', data_files)

        # Now try loading a single file, should still fail
        test_file = settings.BASE_DIR + \
            '/data/001_common/001_administrative-gender.json'
        with pytest.raises(DataAlreadyExistsException):
            call_command('bootstrap', test_file)
