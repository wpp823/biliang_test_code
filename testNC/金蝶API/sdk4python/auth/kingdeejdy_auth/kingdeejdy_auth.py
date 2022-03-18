# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time
from typing import List, Any

from Tea.core import TeaCore
from Tea.exceptions import TeaException, UnretryableException
from Tea.model import TeaModel
from Tea.request import TeaRequest
from alibabacloud_tea_util.client import Client as UtilClient

from auth.kingdeejdy_auth import models as sdkauth_models


class KingdeejdyAuth:
    _server_host: str = None

    def __init__(self):
        _server_host = 'api.kingdee.com'

    def get_token(self, query: TeaModel, ) -> sdkauth_models.AccountGroupRequest:
        """
        the api use to deal with get request
        @param pathname: pathname of the get api
        @param query: the model of query params
        @return: result result of the server
        """
        query.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'GET'
                _request.protocol = 'https'
                _request.pathname = '/auth/user/access_token'
                _request.headers = {
                    'host': 'api.kingdee.com'
                }
                _request.query = UtilClient.stringify_map_value(UtilClient.to_map(query))
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f'{_response.status_code}'
                    })
                result = UtilClient.assert_as_map(UtilClient.read_as_json(_response.body))
                if not UtilClient.equal_number(UtilClient.assert_as_number(result.get('errcode')), 0):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f"{result.get('description')}"
                    })
                data = UtilClient.assert_as_map(result.get('data'))
                access_token = UtilClient.assert_as_string(data.get('access_token'))
                # access_token = "1645428126aa1b3fbdaeeba9d2e1ddca"
                account_group_request = sdkauth_models.AccountGroupRequest(
                    access_token=access_token
                )
                return account_group_request
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_token_async(self, query: TeaModel,) -> sdkauth_models.AccountGroupRequest:
        """
        the api use to deal with get request
        @param pathname: pathname of the get api
        @param query: the model of query params
        @return: result result of the server
        """
        query.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'GET'
                _request.protocol = 'https'
                _request.pathname = '/auth/user/access_token'
                _request.headers = {
                    'host': 'api.kingdee.com'
                }
                _request.query = UtilClient.stringify_map_value(UtilClient.to_map(query))
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f'{_response.status_code}'
                    })
                result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(_response.body))
                if not UtilClient.equal_number(UtilClient.assert_as_number(result.get('errcode')), 0):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f"{result.get('description')}"
                    })
                data = UtilClient.assert_as_map(result.get('data'))
                access_token = UtilClient.assert_as_string(data.get('access_token'))
                account_group_request = sdkauth_models.AccountGroupRequest(
                    access_token=access_token
                )
                return account_group_request
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_account(self,query: TeaModel,) -> List[Any]:
        """
        the api use to deal with post request
        @param pathname: pathname of the post api
        @param query: the model of body params
        @param body: the model of body body
        @return: result result of the server
        """
        query.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'POST'
                _request.protocol = 'https'
                _request.pathname = '/jdy/sys/accountGroup'
                _request.headers = {
                    'host': 'api.kingdee.com',
                    'content-type': 'application/json; charset=utf-8'
                }
                _request.query = UtilClient.stringify_map_value(UtilClient.to_map(query))
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                print(_response.body.decode())
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f'{_response.status_code}'
                    })
                result = UtilClient.assert_as_map(UtilClient.read_as_json(_response.body))
                if not UtilClient.assert_as_boolean(result.get('success')):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f"{result.get('description')}"
                    })
                return UtilClient.assert_as_array(result.get('data'))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def get_account_async(self, query: TeaModel, ) -> List[Any]:
        """
        the api use to deal with post request
        @param pathname: pathname of the post api
        @param query: the model of body params
        @param body: the model of body body
        @return: result result of the server
        """
        query.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'POST'
                _request.protocol = 'https'
                _request.pathname = '/jdy/sys/accountGroup'
                _request.headers = {
                    'host': 'api.kingdee.com',
                    'content-type': 'application/json; charset=utf-8'
                }
                _request.query = UtilClient.stringify_map_value(UtilClient.to_map(query))
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                if not UtilClient.equal_number(_response.status_code, 200):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f'{_response.status_code}'
                    })
                result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(_response.body))
                if not UtilClient.assert_as_boolean(result.get('success')):
                    raise TeaException({
                        'message': f'Reqeust Failed!',
                        'code': f"{result.get('description')}"
                    })
                return UtilClient.assert_as_array(result.get('data'))
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)
